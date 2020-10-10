from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    def __str__(self):
        return self.code

    code = models.CharField(max_length=30)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name="Account"
    )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
