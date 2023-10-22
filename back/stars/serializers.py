from rest_framework import serializers
from .models import StarsModel

class StarsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StarsModel
        fields = ('id', 'count', 'author', 'sheet', 'starred_at')