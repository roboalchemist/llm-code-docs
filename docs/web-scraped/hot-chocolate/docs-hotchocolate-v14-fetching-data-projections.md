# Source: https://chillicream.com/docs/hotchocolate/v14/fetching-data/projections

Title: Projections - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/fetching-data/projections

Markdown Content:
Every GraphQL request specifies exactly what data should be returned. Over or under fetching can be reduced or even eliminated. Hot Chocolate projections leverage this concept and directly projects incoming queries to the database.

Projections operate on `IQueryable` by default, but it is possible to create custom providers for projections to support a specific database driver.

> ⚠️ **Note:** Projections currently need a public setter on fields they operate on in order to function correctly. Otherwise the default constructed value will be returned upon query.

GraphQL

{

users {

email

address {

street

}

}

}

SQL

SELECT "u"."Email", "a"."Id" IS NOT NULL, "a"."Street"

FROM "Users" AS "u"

LEFT JOIN "Address" AS "a" ON "u"."AddressId" = "a"."Id"

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/projections#getting-started)Getting Started
----------------------------------------------------------------------------------------------------------

Filtering is part of the `HotChocolate.Data` package.

Bash

dotnet add package HotChocolate.Data

Warning

All `HotChocolate.*` packages need to have the same version.

To use projections with your GraphQL endpoint you have to register projections on the schema:

C#

builder.Services

.AddGraphQLServer()

.AddProjections();

Projections can be registered on a field. A middleware will apply the selected fields on the result. Support for `IQueryable` comes out of the box. The projection middleware will create a projection for the whole subtree of its field. Only fields that are members of a type will be projected. Fields that define a custom resolver cannot be projected to the database. If the middleware encounters a field that specifies `UseProjection()` this field will be skipped.

C#

public class Query

{

[UseProjection]

public IQueryable<User> GetUsers(IUserRepository repository)

=> repository.GetUsers();

}

> ⚠️ **Note:** If you use more than one middleware, keep in mind that **ORDER MATTERS**. The correct order is UsePaging > UseProjection > UseFiltering > UseSorting

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/projections#firstordefault--singleordefault)FirstOrDefault / SingleOrDefault
-------------------------------------------------------------------------------------------------------------------------------------------

If you want to limit the response to a single result, you would have to declare a resolver. Without returning an `IQueryable<>` you lose the ability to use filtering.

There are two extensions you can use to leverage `collection.FirstOrDefault()` and `collection.SingleOrDefault()` to the GraphQL layer. The extensions will rewrite the response type to the element type of the collection apply the behavior.

C#

public class Query

{

[UseFirstOrDefault]

[UseProjection]

[UseFiltering]

public IQueryable<User> GetUsers([ScopedService] SomeDbContext someDbContext)

{

return someDbContext.Users;

}

}

SDL

type Query {

users(where: UserFilterInput): User

}

type User {

id: Int!

name: String!

email: String!

}

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/projections#sorting-filtering-and-paging)Sorting Filtering and Paging
------------------------------------------------------------------------------------------------------------------------------------

Projections can be used together with sorting, filtering and paging. The order of the middlewares must be correct. Make sure to have the following order: UsePaging > UseProjection > UseFiltering > UseSorting

Filtering and sorting can be projected over relations. Projections **cannot** project paging over relations.

C#

public class Query

{

[UsePaging]

[UseProjection]

[UseFiltering]

[UseSorting]

public IQueryable<User> GetUsers([ScopedService] SomeDbContext someDbContext)

{

return someDbContext.Users;

}

}

public class User

{

public int Id { get; set; }

public string Name { get; set; }

public string Email { get; set; }

[UseFiltering]

[UseSorting]

public ICollection<Address> Addresses { get; set; }

}

GraphQL

{

users(

where: { name: { eq: "ChilliCream" } }

order: [{ name: DESC }, { email: DESC }]

) {

nodes {

email

addresses(where: { street: { eq: "Sesame Street" } }) {

street

}

}

pageInfo {

endCursor

hasNextPage

hasPreviousPage

startCursor

}

}

}

SQL

SELECT "t"."Email", "t"."Id", "a"."Street", "a"."Id"

FROM (

SELECT "u"."Email", "u"."Id", "u"."Name"

FROM "Users" AS "u"

WHERE "u"."Name" = @__p_0

ORDER BY "u"."Name" DESC, "u"."Email" DESC

LIMIT @__p_1

) AS "t"

LEFT JOIN "Address" AS "a" ON "t"."Id" = "a"."UserId"

ORDER BY "t"."Name" DESC, "t"."Email" DESC, "t"."Id", "a"."Id"

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/projections#always-project-fields)Always Project Fields
----------------------------------------------------------------------------------------------------------------------

Resolvers on types often access data of the parent, e.g. uses the `Email` member of the parent to fetch some related data from another service. With projections, this resolver could only work when the user also queries for the `email` field. To ensure a field is always projected you have to use `IsProjected(true)`.

C#

public class User

{

public int Id { get; set; }

public string Name { get; set; }

[IsProjected(true)]

public string Email { get; set; }

public Address Address { get; set; }

}

GraphQL

{

users {

address {

street

}

}

}

SQL

SELECT "u"."Email", "a"."Id" IS NOT NULL, "a"."Street"

FROM "Users" AS "u"

LEFT JOIN "Address" AS "a" ON "u"."AddressId" = "a"."Id"

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/projections#exclude-fields)Exclude fields
--------------------------------------------------------------------------------------------------------

If a projected field is requested, the whole subtree is processed. Sometimes you want to opt out of projections. The projections middleware skips a field in two cases. Either the visitor encounters a field that is a `UseProjection` field itself, or it defines `IsProjected(false)`.

C#

public class User

{

public int Id { get; set; }

public string Name { get; set; }

[IsProjected(false)]

public string Email { get; set; }

public Address Address { get; set; }

}

GraphQL

{

users {

email

address {

street

}

}

}

SQL

SELECT "a"."Id" IS NOT NULL, "a"."Street"

FROM "Users" AS "u"

LEFT JOIN "Address" AS "a" ON "u"."AddressId" = "a"."Id"

Last updated on **2026-02-17** by**Tobias Tengler**
