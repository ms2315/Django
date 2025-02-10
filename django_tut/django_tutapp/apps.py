from django.apps import AppConfig


class DjangoTutappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'django_tutapp'

    def ready(self):
        """
        This ready() function s for importing signals
        """
        import django_tutapp.signals 