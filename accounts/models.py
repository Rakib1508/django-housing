from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class Account(AbstractUser):
    """Keep only the fields that are crucial for authentication and authorization
    in this model as this will be kept on a separate database.
    """
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    
    # preferred name will be set to first name if blank
    # TODO: handle this during saving the data to database
    preferred_name = models.CharField(max_length=128, blank=True)
    # Groups will be handled from the admin panel as it is not user accessible
    role = models.ForeignKey(Group, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
