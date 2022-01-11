from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class HelloView(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, name):
        return Response({'Key': 'Hello {}'.format(name)})
