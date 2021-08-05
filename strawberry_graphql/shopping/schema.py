from typing import List

import strawberry
import strawberry_django
from strawberry_django import mutations

from shopping.types import ShoppingList, Category, ShoppingListInput, ShoppingListPartialInput, CategoryInput, \
    CategoryPartialInput
from user.types import Users


@strawberry.type
class Query:
    shopping_list: ShoppingList = strawberry_django.field()
    shopping_lists: List[ShoppingList] = strawberry_django.field()

    category: Category = strawberry_django.field()
    categories: List[Category] = strawberry_django.field()

    # users: List[Users] = strawberry_django.field()


@strawberry.type
class Mutation:
    createShoppingList: ShoppingList = mutations.create(ShoppingListInput)
    createShoppingLists: List[ShoppingList] = mutations.create(ShoppingListInput)
    updateShoppingLists: List[ShoppingList] = mutations.update(ShoppingListPartialInput)
    deleteShoppingLists: List[ShoppingList] = mutations.delete()

    createCategory: Category = mutations.create(CategoryInput)
    createCategories: List[Category] = mutations.create(CategoryInput)
    updateCategories: List[Category] = mutations.update(CategoryPartialInput)
    deleteCategories: List[Category] = mutations.delete()


# schema = strawberry.Schema(query=Query, mutation=Mutation)
