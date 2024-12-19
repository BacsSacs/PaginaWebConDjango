from django.apps import AppConfig


class PortafolioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portafolio'
    #El verbose_name permite renombrar el metadato o el titulo del proyecto
    verbose_name = 'portafolio'
