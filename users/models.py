from django.db import models
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser


class User(TimeStampedModel, AbstractUser):
    """A user instance is used mostly for authentication and authorization purposes."""

    email = models.EmailField(unique=True, blank=False)

    pseudo = models.CharField(max_length=100, blank=True, unique=True)
    is_email_valid = models.BooleanField(default=False)
    account = models.ForeignKey("accounts.Account",
                                null=True,
                                related_name="users",
                                on_delete=models.SET_NULL)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []