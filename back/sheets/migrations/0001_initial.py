# Generated by Django 4.2.6 on 2023-10-19 09:50

import back.sheets.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SheetsModel',
            fields=[
                ('ine', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('published_date', models.DateField()),
                ('desc', models.TextField()),
                ('stock', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(default=back.sheets.models.get_default_owner, on_delete=django.db.models.deletion.CASCADE, related_name='sheets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
