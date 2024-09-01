# Import the admin module from django.contrib to manage the admin interface
from django.contrib import admin

# Register your models here.

# Import the Topic and Entry models from the current package's models module
from .models import Topic, Entry

# Register the Topic model with the admin site to manage it through the admin interface
admin.site.register(Topic)
# Register the Entry model with the admin site to manage it through the admin interface
admin.site.register(Entry)
