from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account
from profiles.models import Profile


@receiver(post_save, sender=Account)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(
            username=instance.username,
            email=instance.email,
            first_name=instance.first_name,
            last_name=instance.last_name,
            gender=instance.gender,
            mail_accounts={'primary': instance.email},
        )
