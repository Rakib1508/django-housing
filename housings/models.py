from django.utils.translation import gettext_lazy as _
from django.db import models


class Property(models.Model):
    property_number = models.IntegerField(
        _('property identification number'), unique=True,
        help_text=_('identifier of each property'),
    )
