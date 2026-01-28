from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    ValidationError,
)
from apps.restaurant.models import Menu, Category, Dish, Order, Restaurant


class DishSerializer(ModelSerializer):

    class Meta:
        model = Dish
        fields = ["id", "name", "price", "category"]


class CategorySerializer(ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ["id", "description", "dishes"]


class MenuSerializer(ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ["id", "restaurant", "categories"]


class OrderSerializer(ModelSerializer):
    dishes = PrimaryKeyRelatedField(
        queryset=Dish.objects.all(), many=True
    )
    restaurant = PrimaryKeyRelatedField(
        queryset=Restaurant.objects.all(), write_only=True
    )

    class Meta:
        model = Order
        fields = [
            "id",
            "table",
            "dishes",
            "is_active",
            "create_date",
            "update_date",
            "restaurant",
        ]
        read_only_fields = ["id", "is_active"]

    def validate(self, data):
        table = data.get("table")
        restaurant = data.get("restaurant")
        if table.restaurant != restaurant:
            raise ValidationError("Нет такого стола в ресторане")
        return data

    def create(self, validated_data):
        dishes = validated_data.pop("dishes")
        validated_data.pop("restaurant")
        print(validated_data)
        order = Order.objects.create(**validated_data)
        order.dishes.set(dishes)

        return order