from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileModel(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self) -> str:
        return f'{self.user}'