from django.shortcuts import render
from rest_framework import viewsets
from .models import ThatsAppUser
from .serializers import ThatsAppUserSerializer
from rest_framework.views import exception_handler


def index(request):
    return render(request, 'index.html')


def api_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        response.data['status_code'] = response.status_code
        response.data['error'] = True
    return response


class ThatsAppUserViewset(viewsets.ModelViewSet):
    queryset = ThatsAppUser.objects.all()
    serializer_class = ThatsAppUserSerializer
