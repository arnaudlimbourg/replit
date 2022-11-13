from django.contrib import admin
from media_management.models import Media
from media_management.forms import MediaForm


class MediaAdmin(admin.ModelAdmin):

    form = MediaForm


admin.site.register(Media, MediaAdmin)
