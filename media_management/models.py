from django.db import models

from model_utils.models import TimeStampedModel


class Media(TimeStampedModel):
    """Users post media to our platform, images or videos, could also be audio"""
    full_path = models.FileField(upload_to="user_uploads/%Y/%m/%d/")
    account = models.ForeignKey("accounts.Account",
                                models.CASCADE,
                                related_name="medias")
