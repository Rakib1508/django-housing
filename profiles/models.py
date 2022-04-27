from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Profile(models.Model):
    name = models.CharField(_('name to display'), max_length=300)
    last_name_first = models.BooleanField(_('show last name first'), default=False)
    nicknames = ArrayField(
        models.CharField(max_length=50), blank=True, size=5,
        help_text=_('add up to 5 nicknames'),
    )
    birthday = models.DateField(blank=True, null=True)
    short_bio = models.CharField(
        _('add a short introduction'),
        max_length=1000, blank=True, null=True
    )
    profile_tags = ArrayField(
        models.CharField(max_length=50), blank=True, size=10,
        help_text=_('add important tags so that others can find you easily'),
    )
    social_links = models.JSONField(
        null=True, blank=True,
        help_text=_('link your social world'),
    )
    places = models.JSONField(
        null=True, blank=True,
        help_text=_('places you have lived in'),
    )
    educations = models.JSONField(
        null=True, blank=True,
        help_text=_('educational institutes you have studied at'),
    )
    workplaces = models.JSONField(
        null=True, blank=True,
        help_text=_('companies you have worked at'),
    )
