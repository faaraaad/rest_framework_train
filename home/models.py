from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CommentModel(models.Model):
    user= models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    body= models.CharField(max_length=300)
    created_date= models.DateTimeField(auto_now_add=True)
    modified_date= models.DateTimeField(auto_now=True)
    is_reply= models.BooleanField(default=False)
    from_comment= models.ForeignKey('self', related_name='subcomment', on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return f'{self.user} - {self.body} - {self.created_date}'
