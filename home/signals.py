from django.core.signals import request_finished
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import SimpleModel

# @receiver(request_finished, sender= [])
# def callback(sender, **kwargs):
#     print(sender)


# @receiver(post_save)
def call(**kwargs):
    print('_____________________________________')
    print(kwargs)