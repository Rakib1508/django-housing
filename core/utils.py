from django.utils.translation import gettext_lazy as _
from django.db import models


class GenderChoices(models.TextChoices):
    MALE = 'm', _('Male')
    FEMALE = 'f', _('Female')
