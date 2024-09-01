"""Define URL patterns for accounts."""

# Import the path and include functions from django.urls to define URL patterns
from django.urls import path, include

# Import views from the current package
from . import views

# Set the application namespace
app_name = 'accounts'

# Define the URL patterns for the accounts app
urlpatterns = [
    # Include default authentication URLs provided by Django
    path('', include('django.contrib.auth.urls')),
    # URL pattern for the user registration view
    path('register/', views.register, name='register'),
]