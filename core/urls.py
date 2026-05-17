from django.urls import path #Used to create website URLs/routes.
from .views import home, about #Means:import the home function from views.py & The dot . means:current app (core)

urlpatterns = [ #This is a list of all URLs for this app.
    path('', home, name='home'),
    path('about/', about, name='about'),
]

#'' : homepage/root URL
#home : run home view
#name='home' : internal URL name

