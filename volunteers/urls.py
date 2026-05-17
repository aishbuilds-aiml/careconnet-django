from django.urls import path
from .views import (
    volunteer_register,
    ngo_register,
    volunteer_login,
    volunteer_logout,
    volunteer_dashboard,
    apply_opportunity,
    opportunities
)

urlpatterns = [

    path(
        'volunteer/register/',
        volunteer_register,
        name='volunteer_register'
    ),

    path(
        'ngo/register/',
        ngo_register,
        name='ngo_register'
    ),

    path(
        'volunteer/login/',
        volunteer_login,
        name='volunteer_login'
    ),

    path(
        'volunteer/logout/',
        volunteer_logout,
        name='volunteer_logout'
    ),

    path(
        'volunteer/dashboard/',
        volunteer_dashboard,
        name='volunteer_dashboard'
    ),

    path(
        'apply/<int:opportunity_id>/',
        apply_opportunity,
        name='apply_opportunity'
    ),
    
    path(
        'opportunities/',
        opportunities,
        name='opportunities'
    ),

]