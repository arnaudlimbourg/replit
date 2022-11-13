from django.db import models

from model_utils.models import TimeStampedModel


class Media(TimeStampedModel):
    """Users post media to our platform, images or videos, could also be audio"""
    media_file = models.FileField(upload_to="user_uploads/%Y/%m/%d/",
                                  max_length=300,
                                  null=True)
    account = models.ForeignKey("accounts.Account",
                                models.CASCADE,
                                related_name="medias")

    post = models.ForeignKey("posts.Post",
                             on_delete=models.CASCADE,
                             related_named="medias",
                             null=True)

    def __str__(self):
        return f"{self.account.name} uploaded {self.media_file}"
