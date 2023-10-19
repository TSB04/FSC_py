from django.contrib.auth.models import User, Group
from rest_framework import serializers
from back.sheets.serializers import SheetsSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    sheet = SheetsSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'sheet', 'password', 'first_name', 'last_name']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']