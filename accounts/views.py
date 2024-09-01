# Import the render and redirect functions from django.shortcuts to handle rendering templates and redirecting URLs
from django.shortcuts import render, redirect
# Import the login function from django.contrib.auth to handle user login
from django.contrib.auth import login
# Import the UserCreationForm from django.contrib.auth.forms to handle user registration
from django.contrib.auth.forms import UserCreationForm

# Define the register view function to handle user registration
def register(request):
    """Register a new user."""
    # Check if the request method is not POST
    if request.method != 'POST':
        # Display a blank registration form
        form = UserCreationForm()
    else:
        # Process the completed registration form
        form = UserCreationForm(data=request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the new user to the database
            new_user = form.save()
            # Log the user in and then redirect to the home page
            login(request, new_user)
            return redirect('learning_logs:index')

    # Display a blank or invalid form
    context = {'form': form}
    # Render the registration template with the form context
    return render(request, 'registration/register.html', context)
