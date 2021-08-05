# Query / Mutation Example


#### Create Category
```graphql
mutation{
  createCategory(data: {name: "Fruits"}){
    id
    name
  }
}
```

#### Delete shopping list
```graphql
mutation{
  deleteShoppingLists(filters: {id:{exact:4}}){
    name
  }
}
```

#### Create shopping list
```graphql
mutation{
  createShoppingList(data: {name:"brush", category:{set:2}}){
    name
    id
  }
}
```

#### Query shopping lists
```graphql
query{
  shoppingLists{
    id
    name
    category{
      id
      name
    }
  }
}
```

#### Filter shopping list
```graphql
query{
  shoppingLists(filters: {name: {contains:"br"} } ){
    name
  }
}
```



```graphql
# Welcome to GraphiQL
#
# GraphiQL is an in-browser tool for writing, validating, and
# testing GraphQL queries.
#
# Type queries into this side of the screen, and you will see intelligent
# typeaheads aware of the current GraphQL type schema and live syntax and
# validation errors highlighted within the text.
#
# GraphQL queries typically start with a "{" character. Lines that starts
# with a # are ignored.
#
# An example GraphQL query might look like:
#
#     {
#       field(arg: "value") {
#         subField
#       }
#     }
#
# Keyboard shortcuts:
#
#  Prettify Query:  Shift-Ctrl-P (or press the prettify button above)
#
#     Merge Query:  Shift-Ctrl-M (or press the merge button above)
#
#       Run Query:  Ctrl-Enter (or press the play button above)
#
#   Auto Complete:  Ctrl-Space (or just start typing)
#

```
