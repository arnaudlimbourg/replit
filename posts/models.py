from django.db import models

from model_utils.models import TimeStampedModel


class Post(TimeStampedModel):
    description = models.TextField()
