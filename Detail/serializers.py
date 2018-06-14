from rest_framework import serializers
from Account.models import Profile
from .models import Details


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'location', 'password', 'profile_pic', 'cover_pic')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('username', 'password')


class DetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Details
        fields = ('profile', 'score', 'complete_lessons')