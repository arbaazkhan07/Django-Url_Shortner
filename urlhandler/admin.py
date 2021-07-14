from django.contrib import admin
from .models import Shorturl

@admin.register(Shorturl)
class AdminShortUrl(admin.ModelAdmin):
    list_display = ('id', 'user', 'original_url', 'short_query', 'visits')

