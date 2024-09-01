"""
URL configuration for ll_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Import the admin module from django.contrib to manage the admin interface
from django.contrib import admin
# Import the path and include functions from django.urls to define URL patterns
from django.urls import path, include

# Define the urlpatterns list to route URLs to views
urlpatterns = [
    # Route for the admin interface
    path('admin/', admin.site.urls),
    # Route for the accounts app, including its URL configurations
    path('accounts/', include('accounts.urls')),
    # Route for the learning_logs app, including its URL configurations
    path('', include('learning_logs.urls')),
]
