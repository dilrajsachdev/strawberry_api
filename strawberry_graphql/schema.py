import strawberry

from shopping.schema import Query as ShoppingQuery
from user.schema import Query as UserQuery

from shopping.schema import Mutation as ShoppingMutation
from user.schema import Mutation as UserMutation


@strawberry.type
class Query(ShoppingQuery, UserQuery):
    pass


@strawberry.type
class Mutation(ShoppingMutation, UserMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
