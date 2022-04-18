from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class Account(AbstractUser):
    first_name = models.CharField(_('First Name'))
    last_name = models.CharField(_('Last Name'))
    preferred_name = models.CharField(_('Preferred Name'), max_length=150, blank=True)
    
    def __str__(self):
        return self.username
    
    def set_preferred_name(self):
        """preferred name will be set to first name if blank"""
        if self.preferred_name is None:
            self.preferred_name = self.first_name
