from django.shortcuts import render
from rest_framework import viewsets
from .models import ThatsAppUser
from .serializers import ThatsAppUserSerializer
from rest_framework.views import exception_handler


def index(request):
    return render(request, 'index.html')


class ThatsAppUserViewset(viewsets.ModelViewSet):
    queryset = ThatsAppUser.objects.all()
    serializer_class = ThatsAppUserSerializer
