from django.db.models.signals import post_save
from django.dispatch import receiver
from backend.settings.base import AUTH_USER_MODEL
from profiles.models import Profile


@receiver(post_save, sender = AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender = AUTH_USER_MODEL)
def safe_user_profile(sender, instance, created, **kwargs):
    instance.profile.save()