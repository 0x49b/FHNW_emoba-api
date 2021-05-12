from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings
import uuid


class ThatsAppUser(models.Model):
    class Meta:
        verbose_name = "ThatsAppUser"
        verbose_name_plural = "ThatsAppUsers"

    id = models.UUIDField(primary_key=True, blank=True, default=uuid.uuid4, editable=False)
    nickname = models.CharField(max_length=500, blank=False, null=False, verbose_name='nickname')
    mqtt_topic = models.CharField(max_length=1000, blank=True, null=False, verbose_name='topic')
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nickname

    def save(self, *args, **kwargs):

        if not self.id:
            self.id = uuid.uuid4()

        if not self.mqtt_topic:
            self.mqtt_topic = "%s/%s" % (settings.TOPIC, str(self.id))
        return super().save(*args, **kwargs)
