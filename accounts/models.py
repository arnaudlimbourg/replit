from django.db import models

from model_utils.models import TimeStampedModel


class Account(TimeStampedModel):
    """Represents an account on our Instagram clone.
    
    Accounts are the keystone of our application.
    """
    name = models.CharField(max_length=150)
    description = models.TextField(default="")

    def __str__(self):
        return self.name