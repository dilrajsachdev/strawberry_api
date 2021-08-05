import strawberry_django
from strawberry.django import auto
from typing import List
from shopping import models


# filters

@strawberry_django.filters.filter(models.ShoppingList, lookups=True)
class ShoppingListFilter:
    id: auto
    name: auto
    category: 'CategoryFilter'


@strawberry_django.filters.filter(models.Category, lookups=True)
class CategoryFilter:
    id: auto
    name: auto
    shoppinglist_set: ShoppingListFilter


# order

@strawberry_django.ordering.order(models.ShoppingList)
class ShoppingListOrder:
    name: auto
    category: 'CategoryOrder'


@strawberry_django.ordering.order(models.Category)
class CategoryOrder:
    name: auto
    shoppinglist_set: ShoppingListOrder


# types

@strawberry_django.type(models.ShoppingList, filters=ShoppingListFilter, order=ShoppingListOrder, pagination=True)
class ShoppingList:
    id: auto
    name: auto
    category: 'Category'


@strawberry_django.type(models.Category, filters=CategoryFilter, order=CategoryOrder, pagination=True)
class Category:
    id: auto
    name: auto
    shoppinglist_set: List[ShoppingList]  # reverse FK set


# input types

@strawberry_django.input(models.ShoppingList)
class ShoppingListInput:
    id: auto
    name: auto
    category: auto


@strawberry_django.input(models.Category)
class CategoryInput:
    id: auto
    name: auto
    shoppinglist_set: auto


# partial input types

@strawberry_django.input(models.ShoppingList, partial=True)
class ShoppingListPartialInput(ShoppingListInput):
    pass


@strawberry_django.input(models.Category, partial=True)
class CategoryPartialInput(CategoryInput):
    pass


