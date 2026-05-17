from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.db.models import Q

from .forms import VolunteerApplicationForm, NGOApplicationForm
from .models import Opportunity,  OpportunityApplication

def volunteer_register(request):

    if request.method == 'POST':

        form = VolunteerApplicationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(

                request,

                'Application submitted successfully! Admin will review your application.'

            )

            return redirect('home')

    else:

        form = VolunteerApplicationForm()

    return render(

        request,

        'core/volunteer_form.html',

        {'form': form}

    )

def ngo_register(request):

    if request.method == 'POST':

        form = NGOApplicationForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(

                request,

                'NGO application submitted successfully! Admin will review your application.'

            )

            return redirect('home')

    else:

        form = NGOApplicationForm()

    return render(

        request,

        'core/ngo_form.html',

        {'form': form}

    )

def volunteer_login(request):
    if request.user.is_authenticated:

        return redirect('volunteer_dashboard')
    
    if request.method == 'POST':

        form = AuthenticationForm(
            request,
            data=request.POST
        )

        if form.is_valid():

            username = form.cleaned_data.get('username')

            password = form.cleaned_data.get('password')

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                messages.success(
                    request,
                    'Login successful!'
                )

                return redirect('volunteer_dashboard')

    else:

        form = AuthenticationForm()

    return render(

        request,

        'core/volunteer_login.html',

        {'form': form}

    )

@login_required(login_url='volunteer_login')
def volunteer_dashboard(request):

    try:

        profile = request.user.volunteerprofile

    except:

        messages.error(

            request,

            'You are not registered as a volunteer.'

        )

        return redirect('home')
    applications = OpportunityApplication.objects.filter(

        volunteer=profile

    ).order_by('-applied_at')
            
    return render(

        request,

        'core/volunteer_dashboard.html',

        {
            'profile': profile,

            'applications': applications
        }

    )

@login_required(login_url='volunteer_login')
def apply_opportunity(request, opportunity_id):

    try:

        profile = request.user.volunteerprofile

    except:

        messages.error(

            request,

            'You are not registered as a volunteer.'

        )

        return redirect('home')

    opportunity = Opportunity.objects.get(
        id=opportunity_id
    )

    if not opportunity.is_open:

        messages.warning(

            request,

            'This opportunity is already closed.'

        )

        return redirect('opportunities')

    already_applied = OpportunityApplication.objects.filter(

        volunteer=profile,

        opportunity=opportunity

    ).exists()

    if already_applied:

        messages.warning(

            request,

            'You already applied to this opportunity.'

        )

    else:

        OpportunityApplication.objects.create(

            volunteer=profile,

            opportunity=opportunity

        )

        messages.success(

            request,

            'Application submitted successfully!'

        )

    return redirect('opportunities')

def volunteer_logout(request):

    logout(request)

    messages.success(
        request,
        'Logged out successfully!'
    )

    return redirect('home')

def opportunities(request):

    query = request.GET.get('q')

    opportunities = Opportunity.objects.all().order_by('-created_at')

    if query:

        opportunities = opportunities.filter(

            Q(title__icontains=query) |
            Q(location__icontains=query) |
            Q(required_skills__icontains=query) |
            Q(ngo_name__icontains=query)

        )

    return render(request, 'core/opportunities.html', {
        'opportunities': opportunities,
        'query': query
    })