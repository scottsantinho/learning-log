"""Defines URL patterns for learning_logs."""

# Import the path function from django.urls to define URL patterns
from django.urls import path

# Import views from the current package
from . import views

# Set the application namespace
app_name = 'learning_logs'

# Define the URL patterns for the learning_logs app
urlpatterns = [
    # URL pattern for the home page
    path('', views.index, name='index'),
    # URL pattern for the page that shows all topics
    path('topics/', views.topics, name='topics'),
    # URL pattern for the detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # URL pattern for the page for adding a new topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # URL pattern for the page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # URL pattern for the page for editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]