from django.contrib import admin
from django.contrib.auth.models import User

from .models import (
    Opportunity,
    VolunteerProfile,
    VolunteerApplication,
     OpportunityApplication,
    NGOApplication,
    NGOProfile
)


@admin.register(VolunteerApplication)
class VolunteerApplicationAdmin(admin.ModelAdmin):

    list_display = (
        'full_name',
        'email',
        'status',
        'applied_at'
    )

    actions = ['approve_applications']


    def approve_applications(self, request, queryset):

        for application in queryset:

            try:

                if application.status != 'Approved':

                    if not User.objects.filter(
                        email=application.email
                    ).exists():

                        user = User.objects.create_user(

                            username=application.email,

                            email=application.email,

                            password='temp12345'

                        )

                        VolunteerProfile.objects.create(

                            user=user,

                            phone=application.phone,

                            skills=application.skills

                        )

                        application.status = 'Approved'

                        application.save()

            except Exception as e:

                self.message_user(
                    request,
                    f'ERROR: {str(e)}'
                )

        self.message_user(
            request,
            'Applications approved successfully.'
        )

    approve_applications.short_description = (
        'Approve applications'
    )

@admin.register(OpportunityApplication)
class OpportunityApplicationAdmin(admin.ModelAdmin):

    list_display = (

        'volunteer',

        'opportunity',

        'status',

        'applied_at'

    )

    actions = [

        'accept_applications',

        'reject_applications'

    ]


    def accept_applications(

        self,

        request,

        queryset

    ):

        for application in queryset:

            application.status = 'Accepted'

            application.save()

            opportunity = application.opportunity

            opportunity.is_open = False

            opportunity.save()

        self.message_user(

            request,

            'Applications accepted successfully.'

        )


    def reject_applications(

        self,

        request,

        queryset

    ):

        queryset.update(
            status='Rejected'
        )

        self.message_user(

            request,

            'Applications rejected successfully.'

        )


    accept_applications.short_description = (
        'Accept selected applications'
    )

    reject_applications.short_description = (
        'Reject selected applications'
    )

@admin.register(NGOApplication)
class NGOApplicationAdmin(admin.ModelAdmin):

    list_display = (

        'organization_name',

        'email',

        'status',

        'applied_at'

    )

    actions = ['approve_ngos']


    def approve_ngos(

        self,

        request,

        queryset

    ):

        for application in queryset:

            if application.status != 'Approved':

                if not User.objects.filter(
                    email=application.email
                ).exists():

                    user = User.objects.create_user(

                        username=application.email,

                        email=application.email,

                        password='temp12345'

                    )

                    NGOProfile.objects.create(

                        user=user,

                        organization_name=application.organization_name,

                        phone=application.phone,

                        mission=application.mission,

                        website=application.website

                    )

                    application.status = 'Approved'

                    application.save()

        self.message_user(

            request,

            'NGO applications approved successfully.'

        )

    approve_ngos.short_description = (
        'Approve selected NGOs'
    )

admin.site.register(Opportunity)
admin.site.register(VolunteerProfile)
admin.site.register(NGOProfile)