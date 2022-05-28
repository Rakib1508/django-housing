from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Account
from profiles.models import Profile


@receiver(post_save, sender=Account)
def create_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.using('default').create(
            username=instance.username,
            first_name=instance.first_name,
            last_name=instance.last_name,
            gender=instance.gender,
            mail_accounts={'primary': instance.email},
        )


@receiver(post_delete, sender=Account)
def delete_profile_signal(sender, instance, **kwargs):
    Profile.objects.using('default').delete(username=instance.username)
