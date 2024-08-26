from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    image = models.ImageField(upload_to="user/images", blank=True, null=True)
    phoneNumber = PhoneNumberField(region="UZ")
    type = models.CharField(max_length=4, choices=[("CAFE", 1), ("USER", 2)])
