from django import forms

from media_management.models import Media
from media_management.utils import validate_media, validate_media_size


class MediaForm(forms.ModelForm):
    def clean_media_file(self):
        media = self.cleaned_data.get("media_file", False)
        if not validate_media(media.file):
            raise forms.ValidationError(f"Media is not in the authorized list")

        if not validate_media_size(media.size):
            raise forms.ValidationError(f"Media is too big")
        return media

    class Meta:
        model = Media
        fields = ["media_file", "account"]
