from rest_framework import serializers
from .models import ThatsAppUser


class ThatsAppUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThatsAppUser
        fields = ['id', 'nickname', 'mqtt_topic', 'added', 'url']
