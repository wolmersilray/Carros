from django.apps import AppConfig


class CarsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cars'

    def ready(self) -> None: #Para carragear aplicação signails criado 
        import cars.signals
