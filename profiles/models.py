from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from core.utils import GenderChoices
from django.db import models


class Profile(models.Model):
    username = models.CharField(
        _('profile owner username'), max_length=150, unique=True,
        help_text=_('username connecting profile owner with user account'),
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
    is_active = models.BooleanField(
        _('active status'), default=True,
        help_text=_('Designates whether this profile should be treated as active.'),
    )
    last_name_first = models.BooleanField(_('show last name first'), default=False)
    nicknames = ArrayField(
        models.CharField(_('add nicknames'), max_length=50, blank=True),
        default=list, size=5, help_text=_('add up to 5 nicknames'),
    )
    gender = models.CharField(
        _('gender'), max_length=1, blank=True, null=True,
        choices=GenderChoices.choices,
    )
    birthday = models.DateField(_('add birthday'), blank=True, null=True)
    short_bio = models.CharField(
        _('add a short introduction'),
        max_length=1000, blank=True, null=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_tags = ArrayField(
        models.CharField(_('add special tags to profile'), max_length=50, blank=True),
        size=10, default=list, help_text=_('add important tags so that others can find you easily'),
    )
    mail_accounts = models.JSONField(
        _('add emails'), null=True, blank=True,
        help_text=_('link your email addresses'),
    )
    phone_numbers = models.JSONField(
        _('add phone numbers'), null=True, blank=True,
        help_text=_('link your phone numbers'),
    )
    social_links = models.JSONField(
        _('add social accounts'), null=True, blank=True,
        help_text=_('link your social world'),
    )
    places = models.JSONField(
        _('add places'), null=True, blank=True,
        help_text=_('places you have lived in'),
    )
    educations = models.JSONField(
        _('add educations'), null=True, blank=True,
        help_text=_('educational institutes you have studied at'),
    )
    workplaces = models.JSONField(
        _('add workplaces'), null=True, blank=True,
        help_text=_('companies you have worked at'),
    )
    
    class Meta:
        indexes = [
            models.Index(fields=['username']),
            models.Index(fields=['first_name']),
            models.Index(fields=['last_name']),
            models.Index(fields=['gender']),
            models.Index(fields=['first_name', 'last_name']),
            models.Index(fields=['first_name', 'gender']),
            models.Index(fields=['last_name', 'gender']),
            models.Index(fields=['first_name', 'last_name', 'gender']),
        ]
    
    def __str__(self):
        return self.username
    
    def deactivate_profile(self):
        self.is_active = False
        self.save()
