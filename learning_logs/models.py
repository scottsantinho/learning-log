from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Define a Topic model that inherits from Django's base Model class
class Topic(models.Model):
    """A topic the user is learning about."""
    # Create a CharField to store the topic text, limiting it to 200 characters
    text = models.CharField(max_length=200)
    # Create a DateTimeField that automatically sets to the current date and time when a topic is created
    date_added = models.DateTimeField(auto_now_add=True)
    # Create a ForeignKey to establish a many-to-one relationship with the User model
    # The on_delete=models.CASCADE argument specifies that when a User is deleted, all their associated topics should also be deleted
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Define a string representation of the Topic model
    def __str__(self):
        """Return a string representation of the model."""
        # Return the text of the topic as its string representation
        return self.text

# Define an Entry model that also inherits from Django's base Model class
class Entry(models.Model):
    """Something specific learned about a topic."""
    # Create a ForeignKey to establish a many-to-one relationship with the Topic model
    # The on_delete=models.CASCADE argument specifies that when a Topic is deleted, all its associated entries should also be deleted
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # Create a TextField to store the entry's content without a character limit
    text = models.TextField()
    # Create another DateTimeField that automatically sets to the current date and time when an entry is created
    date_added = models.DateTimeField(auto_now_add=True)

    # Define metadata for the Entry model
    class Meta:
        # Set the plural name for the model in the admin interface
        verbose_name_plural = 'entries'
    
    # Define a string representation of the Entry model
    def __str__(self):
        """Return a string representation of the entry."""
        # Check if the entry's text is less than 50 characters
        if len(self.text) <= 50:
            # If it's 50 characters or less, return the entire text
            return self.text
        else:
            # If it's more than 50 characters, return the first 50 characters followed by an ellipsis
            return f"{self.text[:50]}..."