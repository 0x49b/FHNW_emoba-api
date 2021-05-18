from django.contrib import admin
from .models import ThatsAppUser


class ThatsAppUserAdmin(admin.ModelAdmin):
    list_display = ("id", "nickname", "mqtt_topic", "avatar", "added")


admin.site.register(ThatsAppUser, ThatsAppUserAdmin)
