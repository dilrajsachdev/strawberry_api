from django.contrib import admin

from shopping.models import Category, ShoppingList


@admin.register(Category)
class CodesInviteStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(ShoppingList)
class CodesInviteStatusAdmin(admin.ModelAdmin):
    pass
