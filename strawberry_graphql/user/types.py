import strawberry
import strawberry_django
from django.contrib.auth import get_user_model
from strawberry.django import auto
from typing import List


@strawberry_django.type(get_user_model())
class Users:
    pk: strawberry.ID
    id: auto
    username: auto
    email: auto
    first_name: auto
    last_name: auto


# input types

@strawberry_django.input(get_user_model())
class UserInput:
    username: auto
    first_name: auto
    last_name: auto
