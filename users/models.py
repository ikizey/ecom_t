from django.contrib.auth.models import AbstractUser
from django.db import models


class ExtendedUser(AbstractUser):
    @property
    def manager(self):
        """wraps staff field into 'manager' (for admin view)"""
        return self.is_staff
