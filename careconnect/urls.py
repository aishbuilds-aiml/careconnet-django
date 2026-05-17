from django.contrib import admin
from django.urls import path, include #include() means: connect another URL file.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')), #This means: For homepage/root URL, use URLs from core app
    path('', include('volunteers.urls')), 
]