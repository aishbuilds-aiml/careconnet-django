from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import VolunteerApplication, NGOApplication


class VolunteerApplicationForm(forms.ModelForm):

    class Meta:

        model = VolunteerApplication

        fields = [
            'full_name',
            'email',
            'phone',
            'skills',
            'motivation'
        ]

        widgets = {

            'skills': forms.Textarea(
                attrs={'rows': 3}
            ),

            'motivation': forms.Textarea(
                attrs={'rows': 4}
            ),

        }

class NGOApplicationForm(forms.ModelForm):

    class Meta:

        model = NGOApplication

        fields = [

            'organization_name',

            'email',

            'phone',

            'mission',

            'website'

        ]

        widgets = {

            'mission': forms.Textarea(
                attrs={'rows': 4}
            ),

        }