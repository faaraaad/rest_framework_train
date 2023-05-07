from django.apps import AppConfig
from django.db.models.signals import post_save
from django.core.signals import request_started
from .training import test_send

class HomeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'

    def ready(self):
        from . import signals
        post_save.connect(signals.call)
        test_send.connect(signals.call)
