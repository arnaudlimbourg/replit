from django.db import models
from model_utils.models import TimeStampedModel
from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import UserManager


class UserManagerAugmented(UserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email, and password.
        """

        email = self.normalize_email(email)
        # Lookup the real model class from the global app registry so this
        # manager method can be used in migrations. This is fine because
        # managers are by definition working on the real model.
        GlobalUserModel = apps.get_model(self.model._meta.app_label,
                                         self.model._meta.object_name)

        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(TimeStampedModel, AbstractUser):
    """A user instance is used mostly for authentication and authorization purposes."""

    email = models.EmailField(unique=True, blank=False)

    pseudo = models.CharField(max_length=100, blank=True, unique=True)
    is_email_valid = models.BooleanField(default=False)
    account = models.ForeignKey("accounts.Account",
                                null=True,
                                related_name="users",
                                on_delete=models.SET_NULL)

    objects = UserManagerAugmented()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
