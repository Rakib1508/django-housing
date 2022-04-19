from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    email = models.EmailField(
        _("email address"),
        error_messages = {
            'required': _('Must provide a valid email address.'),
            'invalid': _('Must provide a valid email address.'),
        },
    )
    first_name = models.CharField(
        _('first name'), max_length=150,
        error_messages = {
            'required': _('Must provide a first name.'),
            'max_length': _('First name can be at most 150 characters.'),
        },
    )
    last_name = models.CharField(
        _('last name'), max_length=150,
        error_messages = {
            'required': _('Must provide a last name.'),
            'max_length': _('Last name can be at most 150 characters.'),
        }
    )
    preferred_name = models.CharField(
        _('preferred name'), max_length=150, blank=True,
        help_text=_(
            'Name to be used for calling you by. '
            'If empty, first name will be used by default.'
        ),
    )
    phone_number = PhoneNumberField(
        _('phone number'), unique=True, blank=True, null=True,
        help_text=_('Required if two factor authentication is enabled.'),
        error_messages={
            'unique': _('A user with that phone number already exists.'),
        },
    )
    
    def __str__(self):
        return self.username
    
    def save(self, **kwargs):
        # preferred name will be set to first name if blank
        if self.preferred_name is None:
            self.preferred_name = self.first_name
        
        super().save(**kwargs)
