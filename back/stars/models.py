from django.db import models
from django.contrib.auth.models import User
from back.sheets.models import SheetsModel

def get_default_author():
    user = User.objects.get_or_create(username='admin')[0]
    return user.id

class StarsModel(models.Model):
    id = models.AutoField(primary_key=True)
    count = models.IntegerField(default=0)
    sheet = models.ForeignKey(SheetsModel, on_delete=models.CASCADE, related_name='stars')
    #giving default value to author to allow anonymous stars
    author = models.ForeignKey(User,on_delete=models.PROTECT, related_name='stars', default=get_default_author)
    starred_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sheet.title + ' - ' + str(self.count)
