# Import the AppConfig class from django.apps to configure the application
from django.apps import AppConfig

# Define the LearningLogsConfig class to configure the learning_logs application
class LearningLogsConfig(AppConfig):
    # Set the default type for primary keys to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    # Set the name of the application to 'learning_logs'
    name = 'learning_logs'
