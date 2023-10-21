from django.db import models
from django.contrib.auth.models import User
from back.sheets.models import SheetsModel
class CommentsModel(models.Model):
    id = models.AutoField(primary_key=True)
    star = models.IntegerField(default=0)
    comment = models.TextField()
    sheet = models.ForeignKey(SheetsModel, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User,on_delete=models.PROTECT, related_name='comments')
    commented_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment