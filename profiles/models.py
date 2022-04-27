from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Profile(models.Model):
    name = models.CharField(
        _('name to display'), max_length=300,
        blank=True, null=True
    )
    nicknames = ArrayField(
        models.CharField(max_length=50), blank=True, size=5,
        help_text=_('add up to 5 nicknames'),
    )
    birthday = models.DateField(blank=True, null=True)
    short_bio = models.CharField(
        _('add a short introduction'),
        max_length=1000, blank=True, null=True
    )
