from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.base_user import BaseUserManager


class CustomManager(BaseUserManager):

    def create_user(self, first_name, last_name, email, username, password,
                    **extra_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name,
                          last_name=last_name, username=username,
                          **extra_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractUser):
    phone_number = PhoneNumberField(null=True, unique=True, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to="static/users/images/", null=True)
    objects = CustomManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
