from django.db import models
from django.contrib.auth.models import User


def get_default_owner():
    user = User.objects.get_or_create(username='admin')[0]
    return user.id


class SheetsModel(models.Model):
    ine = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    desc = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sheets', default=get_default_owner)
    stock = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


