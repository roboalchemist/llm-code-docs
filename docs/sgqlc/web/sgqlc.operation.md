# sgqlc.operation module

## Generate Operations (Query and Mutations) using Python

Note

This module could be called “query”, however it should also generate
mutations and a class `Query` could lead to mistakes, since the
users should define their own root `Query` class with the
top-level queries in their GraphQL schema.