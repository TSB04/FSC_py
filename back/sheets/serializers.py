from rest_framework import serializers
from .models import SheetsModel
from back.comments.serializers import CommentsSerializer
from back.stars.serializers import StarsSerializer


class SheetsSerializer(serializers.HyperlinkedModelSerializer):

    # get sheet's comments
    comments = CommentsSerializer(many=True, read_only=True)

    # get sheet's stars
    stars = StarsSerializer(many=True, read_only=True)
    class Meta:
        model = SheetsModel
        fields = ('ine', 'title', 'desc', 'author', 'published_date', 'stock', 'owner', 'comments', 'stars')

