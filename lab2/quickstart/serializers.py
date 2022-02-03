import imp
from django.contrib.auth.models import User
from rest_framework import serializers
from affairs.models import Trainee


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainee
        fields = ['id', 'name', 'track','bdate','intake']