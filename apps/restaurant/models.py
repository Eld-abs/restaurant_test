from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    owners = models.ManyToManyField(User, related_name="restaurants")
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Table(models.Model):
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, related_name="tables"
    )
    number = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.restaurant}"


class Menu(models.Model):
    restaurant = models.OneToOneField(
        Restaurant, on_delete=models.CASCADE, related_name="menu"
    )
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.restaurant}"


class Category(models.Model):
    menu = models.ManyToManyField(Menu, related_name="categories")
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.description}"


class Dish(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="dishes",
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"Корзина пользователя: {self.user}"


class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    dishes = models.ManyToManyField(Dish, related_name="orders")
    is_active = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"Стул:{self.table}, Время: {self.create_date}, Активный:{self.is_active}"
        )
