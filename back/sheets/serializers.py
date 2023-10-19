from rest_framework import serializers
from .models import SheetsModel


class SheetsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SheetsModel
        fields = ('ine', 'title', 'desc', 'author', 'published_date', 'stock', 'owner')

