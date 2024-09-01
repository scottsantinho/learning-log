# Import the AppConfig class from django.apps to configure the application
from django.apps import AppConfig

# Define the AccountsConfig class to configure the accounts application
class AccountsConfig(AppConfig):
    # Set the default type for primary keys to BigAutoField
    default_auto_field = 'django.db.models.BigAutoField'
    # Set the name of the application to 'accounts'
    name = 'accounts'
