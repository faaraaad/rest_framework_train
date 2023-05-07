# Generated by Django 4.1.5 on 2023-02-22 17:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_profilemodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='user',
        ),
        migrations.AddField(
            model_name='profilemodel',
            name='user_profile',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userprofile', to=settings.AUTH_USER_MODEL),
        ),
    ]
