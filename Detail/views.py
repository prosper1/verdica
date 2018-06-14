from Account.models import Profile
from .models import Details
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Q
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, serializers
from django.shortcuts import render, redirect
from .serializers import DetailsSerializer, ProfileSerializer, LoginSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username',)

class LoginViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = LoginSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('username',)

class DetailsViewSet(viewsets.ModelViewSet):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('profile',)

def my(request):
    return render(request,'index.html')

