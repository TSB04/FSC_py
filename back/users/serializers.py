from django.contrib.auth.models import User, Group
from rest_framework import serializers
# from comments.serializers import CommentsSerializer
from back.sheets.serializers import SheetsSerializer
from back.comments.serializers import CommentsSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    # get user's sheets
    sheets = SheetsSerializer(many=True)

    # get user's comments
    comments = CommentsSerializer(many=True)

    # comments = CommentsSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'sheets', 'comments']
