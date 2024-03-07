from django.apps import AppConfig


class TeretanaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'teretana'

    def ready(self):
        # Register your signal here, so it will be imported once
        # when the app is ready
        from teretana import signals