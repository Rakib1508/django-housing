from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from profiles.models import Profile


@receiver(post_save, sender=Account)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        full_name = instance.first_name + ' ' + instance.last_name
        Profile.objects.create(name=full_name)
