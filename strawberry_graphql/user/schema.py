from typing import List

import strawberry
import strawberry_django
from strawberry_django import mutations
from strawberry_django.auth import current_user

from user.types import Users, UserInput


@strawberry.type
class Query:
    users: List[Users] = strawberry_django.field()
    me: Users = current_user()


@strawberry.type
class Mutation:
    createUser: Users = mutations.create(UserInput)


# schema = strawberry.Schema(query=Query)
