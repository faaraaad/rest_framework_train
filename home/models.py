from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CommentModel(models.Model):
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    body = models.CharField(max_length=300)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_reply = models.BooleanField(default=False)
    from_comment = models.ForeignKey('self', related_name='subcomment', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.user} - {self.body} - {self.created_date}'


class SimpleModel(models.Model):
    name = models.CharField(max_length=200)
    family = models.CharField(default='barbar', max_length=200)
    is_ok = models.BooleanField()

    def __str__(self):
        return self.name + ' '+ self.family


class ProfileModel(models.Model):
    user_profile = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile',
                                        blank=True, null=True)
    address = models.TextField(max_length=500)
