from rest_framework import serializers
from .models import CommentsModel

class CommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CommentsModel
        fields = ('id', 'comment', 'author', 'sheet', 'commented_at')