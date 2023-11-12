from django.apps import AppConfig


class SheetsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'back.sheets'

    def ready(self):
        from back.sheets import handlers
