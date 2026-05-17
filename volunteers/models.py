from django.db import models
from django.contrib.auth.models import User
    
class Opportunity(models.Model):

    title = models.CharField(max_length=200)

    ngo_name = models.CharField(max_length=200)

    location = models.CharField(max_length=100)

    required_skills = models.CharField(max_length=200)

    description = models.TextField()

    is_open = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    from django.contrib.auth.models import User


class VolunteerProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    phone = models.CharField(max_length=15)

    skills = models.TextField()

    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
class VolunteerApplication(models.Model):

    STATUS_CHOICES = [

        ('Pending', 'Pending'),

        ('Approved', 'Approved'),

        ('Rejected', 'Rejected'),

    ]

    full_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    skills = models.TextField()

    motivation = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.full_name
    
class NGOApplication(models.Model):

    STATUS_CHOICES = [

        ('Pending', 'Pending'),

        ('Approved', 'Approved'),

        ('Rejected', 'Rejected'),

    ]

    organization_name = models.CharField(
        max_length=200
    )

    email = models.EmailField(
        unique=True
    )

    phone = models.CharField(
        max_length=15
    )

    mission = models.TextField()

    website = models.URLField(
        blank=True,
        null=True
    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='Pending'
    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.organization_name

class NGOProfile(models.Model):

    user = models.OneToOneField(

        User,

        on_delete=models.CASCADE

    )

    organization_name = models.CharField(
        max_length=200
    )

    phone = models.CharField(
        max_length=15
    )

    mission = models.TextField()

    website = models.URLField(
        blank=True,
        null=True
    )

    joined_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.organization_name

class OpportunityApplication(models.Model):

    STATUS_CHOICES = [

        ('Applied', 'Applied'),

        ('Accepted', 'Accepted'),

        ('Rejected', 'Rejected'),

    ]

    volunteer = models.ForeignKey(

        VolunteerProfile,

        on_delete=models.CASCADE

    )

    opportunity = models.ForeignKey(

        Opportunity,

        on_delete=models.CASCADE

    )

    status = models.CharField(

        max_length=20,

        choices=STATUS_CHOICES,

        default='Applied'

    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.volunteer.user.username} - {self.opportunity.title}"