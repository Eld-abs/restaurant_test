from django.apps import AppConfig
from django.db.models.signals import post_migrate



class RestaurantConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.restaurant"

    def ready(self):
        from apps.restaurant.signals import create_groups

        post_migrate.connect(create_groups, sender=self)