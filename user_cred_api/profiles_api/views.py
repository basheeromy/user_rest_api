from django.shortcuts import render
from rest_framework import viewsets

from profiles_api import models
from profiles_api import serializers


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()