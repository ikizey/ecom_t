from django.contrib.auth.models import AbstractUser
from django.db import models


class ExtendedUser(AbstractUser):
    is_manager = models.BooleanField(
        ('manager status'),
        default=False,
        help_text=('Designates whether the user is manager'),
    )

    USERNAME_FIELD = 'username'
