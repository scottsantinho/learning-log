# Import the render and redirect functions from django.shortcuts to handle rendering templates and redirecting URLs
from django.shortcuts import render, redirect
# Import the Topic and Entry models from the current package's models module
from .models import Topic, Entry
# Import the TopicForm and EntryForm from the current package's forms module
from .forms import TopicForm, EntryForm
# Import the login_required decorator from django.contrib.auth.decorators to restrict access to logged-in users
from django.contrib.auth.decorators import login_required
# Import the Http404 exception from django.http to handle 404 errors
from django.http import Http404

# Create your views here.

# Define a function to check if the topic owner matches the current user
def check_topic_owner(topic, user):
    """Check if the topic's owner matches the current user."""
    # Compare the topic's owner with the current user
    if topic.owner != user:
        # If they don't match, raise an Http404 exception
        raise Http404

# Define the index view function to render the home page
def index(request):
    """The home page for learning log."""
    # Render the index.html template
    return render(request, 'learning_logs/index.html')

# Define the topics view function to show all topics
@login_required
def topics(request):
    """Show all topics."""
    # Filter topics by the current user and order them by date_added
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # Create a context dictionary to pass to the template
    context = {'topics': topics}
    # Render the topics.html template with the context
    return render(request, 'learning_logs/topics.html', context)

# Define the topic view function to show a single topic and all its entries
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    # Get the topic by its ID
    topic = Topic.objects.get(id=topic_id)
    # Call the check_topic_owner function to ensure the user has permission
    check_topic_owner(topic, request.user)
    # Get all entries for the topic and order them by date_added in descending order
    entries = topic.entry_set.order_by('-date_added')
    # Create a context dictionary to pass to the template
    context = {'topic': topic, 'entries': entries}
    # Render the topic.html template with the context
    return render(request, 'learning_logs/topic.html', context)    

# Define the new_topic view function to add a new topic
@login_required
def new_topic(request):
    """Add a new topic."""
    # Check if the request method is not POST
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the new topic to the database without committing
            new_topic = form.save(commit=False)
            # Set the owner of the new topic to the current user
            new_topic.owner = request.user
            # Save the new topic to the database
            new_topic.save()
            # Redirect to the topics page
            return redirect('learning_logs:topics')
        
    # Display a blank or invalid form.
    # Create a context dictionary to pass to the template
    context = {'form': form}
    # Render the new_topic.html template with the context
    return render(request, 'learning_logs/new_topic.html', context)

# Define the new_entry view function to add a new entry for a particular topic
@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    # Get the topic by its ID
    topic = Topic.objects.get(id=topic_id)
    # Call the check_topic_owner function to ensure the user has permission
    check_topic_owner(topic, request.user)

    # Check if the request method is not POST
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = EntryForm()
    else:
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the new entry to the database without committing
            new_entry = form.save(commit=False)
            # Set the topic of the new entry to the current topic
            new_entry.topic = topic
            # Save the new entry to the database
            new_entry.save()
            # Redirect to the topic page
            return redirect('learning_logs:topic', topic_id=topic_id)
        
    # Display a blank or invalid form.
    # Create a context dictionary to pass to the template
    context = {'topic': topic, 'form': form}
    # Render the new_entry.html template with the context
    return render(request, 'learning_logs/new_entry.html', context)

# Define the edit_entry view function to edit an existing entry
@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    # Get the entry by its ID
    entry = Entry.objects.get(id=entry_id)
    # Get the topic of the entry
    topic = entry.topic
    # Call the check_topic_owner function to ensure the user has permission
    check_topic_owner(topic, request.user)

    # Check if the request method is not POST
    if request.method != 'POST':
        # Initial request; pre-fill form with the current entry.
        form = EntryForm(instance=entry)
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        # Check if the form is valid
        if form.is_valid():
            # Save the updated entry to the database
            form.save()
            # Redirect to the topic page
            return redirect('learning_logs:topic', topic_id=topic.id)
        
    # Create a context dictionary to pass to the template
    context = {'entry': entry, 'topic': topic, 'form': form}
    # Render the edit_entry.html template with the context
    return render(request, 'learning_logs/edit_entry.html', context)
