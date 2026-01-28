# from django.contrib import admin
# from django.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from apps.restaurant.views import MenuViewSet, OrderCreateViewSet

router = DefaultRouter()
router.register(r"menu", MenuViewSet, basename="menu")
router.register(r"order", OrderCreateViewSet, basename="order")

urlpatterns = router.urls