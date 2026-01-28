from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet

from apps.restaurant.models import Menu, Order
from apps.restaurant.serializers import MenuSerializer, OrderSerializer


class MenuViewSet(ReadOnlyModelViewSet):
    queryset = Menu.objects.prefetch_related("categories__dishes").all()
    serializer_class = MenuSerializer


class OrderCreateViewSet(GenericViewSet, CreateModelMixin, ListModelMixin):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer