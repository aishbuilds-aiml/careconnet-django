from django.shortcuts import render #render() helps Django: display HTML pages.
from django.db.models import Q  #Q helps perform: advanced searches like: title OR location OR skill
from volunteers.models import Opportunity

def home(request):

    opportunities = Opportunity.objects.all().order_by('-created_at')[:3] #fetch all opportunities from the database , orderby sort newest opportunities , - means descending order , [:3] means only first 3 records

    return render(request, 'core/home.html', {
        'opportunities': opportunities  # sends data to home.html . this is called context data
    })
def about(request):
    return render(request, 'core/about.html')

def opportunities(request): 

    query = request.GET.get('q') #Reads search input from URL.

    opportunities = Opportunity.objects.all().order_by('-created_at')  #Fetch all opportunities initially.

    if query:  #Only run search filter if user searched something.

        opportunities = opportunities.filter(

            Q(title__icontains=query) |  #icontains means its case-insensitive partial matchin
            Q(location__icontains=query) |  #(|) means or condition
            Q(required_skills__icontains=query) |
            Q(ngo_name__icontains=query)

        )

    return render(request, 'core/opportunities.html', {
        'opportunities': opportunities,
        'query': query
    })