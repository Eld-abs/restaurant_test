from django.contrib import admin
from django.apps import apps
from apps.restaurant.models import Restaurant, Table, Menu, Category, Dish, Cart, Order


admin.site.register(Restaurant)
admin.site.register(Table)
admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Cart)
admin.site.register(Order)

# models = apps.get_models()
# for model in models:
#     if model.__name__ in ["Restaurant", "Table", ""]:
#         admin.site.register(model)

