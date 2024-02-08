from django.apps import AppConfig


class ClassbasedAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'classbased_app'
