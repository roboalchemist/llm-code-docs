# Source: https://chillicream.com/docs/hotchocolate/v14/integrations/mongodb

Title: MongoDB - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/integrations/mongodb

Markdown Content:
Hot Chocolate has a data integration for MongoDB. With this integration, you can translate paging, filtering, sorting, and projections, directly into native MongoDB queries.

You can find an example project in [Hot Chocolate Examples](https://github.com/ChilliCream/hotchocolate-examples/tree/master/misc/MongoDB)

[](https://chillicream.com/docs/hotchocolate/v14/integrations/mongodb#get-started)Get Started
---------------------------------------------------------------------------------------------

To use the MongoDB integration, you need to install the package `HotChocolate.Data.MongoDb`.

Bash

dotnet add package HotChocolate.Data.MongoDb

Warning

All `HotChocolate.*` packages need to have the same version.

[](https://chillicream.com/docs/hotchocolate/v14/integrations/mongodb#mongoexecutable)MongoExecutable
-----------------------------------------------------------------------------------------------------

The whole integration builds around `IExecutable<T>`. The integration provides you the extension method `AsExecutable` on `IMongoCollection<T>`, `IAggregateFluent<T>` and `IFindFluent<T>` The execution engine picks up the `IExecutable` and executes it efficiently. You are free to use any form of aggregation or find a pipeline before you execute `AsExecutable`

C#

[UsePaging]

[UseProjection]

[UseSorting]

[UseFiltering]

public IExecutable<Person> GetPersons(IMongoCollection<Person> collection)

{

return collection.AsExecutable();

}

[UseFirstOrDefault]

public IExecutable<Person> GetPersonById(IMongoCollection<Person> collection, Guid id)

{

return collection.Find(x => x.Id == id).AsExecutable();

}

[](https://chillicream.com/docs/hotchocolate/v14/integrations/mongodb#filtering)Filtering
-----------------------------------------------------------------------------------------

To use MongoDB filtering you need to register the convention on the schema builder:

C#

builder.Services

.AddGraphQLServer()

.AddQueryType<Query>()

.AddMongoDbFiltering();

> To use MongoDB filtering alongside with `IQueryable`/`IEnumerable`, you have to register the MongoDB convention under a different scope. You can specify the scope on the schema builder by executing `AddMongoDbFiltering("yourScope")`. You then have to specify this scope on each method you use MongoDb filtering: `[UseFiltering(Scope = "yourScope")]` or `UseFiltering(scope = "yourScope")`

Your filters are now converted to `BsonDocument`s and applied to the executable.

_GraphQL Query:_

GraphQL

query GetPersons {

persons(

where: {

name: { eq: "Yorker Shorton" }

addresses: { some: { street: { eq: "04 Leroy Trail" } } }

}

) {

name

addresses {

street

city

}

}

}

_Mongo Query_

JSON

{

"find": "person",

"filter": {

"Name": { "$eq": "Yorker Shorton" },

"Addresses": { "$elemMatch": { "Street": { "$eq": "04 Leroy Trail" } } }

}

}

[](https://chillicream.com/docs/hotchocolate/v14/integrations/mongodb#sorting)Sorting
-------------------------------------------------------------------------------------

To use MongoDB sorting you need to register the convention on the schema builder:

C#

builder.Services

.AddGraphQLServer()

.AddQueryType<Query>()

.AddMongoDbSorting();

> To use MongoDB Sorting alongside with `IQueryable`/`IEnumerable`, you have to register the MongoDB convention under a different scope. You can specify the scope on the schema builder by executing `AddMongoDbSorting("yourScope")`. You then have to specify this scope on each method you use MongoDb Sorting: `[UseSorting(Scope = "yourScope")]` or `UseSorting(scope = "yourScope")`

Your sorting is now converted to `BsonDocument`s and applied to the executable.

_GraphQL Query:_

GraphQL

query GetPersons {

persons(order: [{ name: ASC }, { mainAddress: { city: DESC } }]) {

name

addresses {

street

city

}

}

}

_Mongo Query_

JSON

{

"find": "person",

"filter": {},

"sort": { "Name": 1, "MainAddress.City": -1 }

}

[](https://chillicream.com/docs/hotchocolate/v14/integrations/mongodb#projections)Projections
---------------------------------------------------------------------------------------------

To use MongoDB projections you need to register the convention on the schema builder:

C#

builder.Services

.AddGraphQLServer()

.AddQueryType<Query>()

.AddMongoDbProjections();

> To use MongoDB Projections alongside with `IQueryable`/`IEnumerable`, you have to register the MongoDB convention under a different scope. You can specify the scope on the schema builder by executing `AddMongoDbProjections("yourScope")`. You then have to specify this scope on each method you use MongoDb Projections: `[UseProjections(Scope = "yourScope")]` or `UseProjections(scope = "yourScope")`

Projections do not always lead to a performance increase. Even though MongoDB processes and transfers less data, it more often than not harms query performance. This [Medium article by Tek Loon](https://betterprogramming.pub/improve-mongodb-performance-using-projection-c08c38334269) explains how and when to use projections well.

_GraphQL Query:_

GraphQL

query GetPersons {

persons {

name

addresses {

city

}

}

}

_Mongo Query_

JSON

{

"find": "person",

"filter": {},

"projection": { "Addresses.City": 1, "Name": 1 }

}

[](https://chillicream.com/docs/hotchocolate/v14/integrations/mongodb#paging)Paging
-----------------------------------------------------------------------------------

In order to use pagination with MongoDB, we have to register the MongoDB specific pagination providers.

C#

builder.Services

.AddGraphQLServer()

.AddMongoDbPagingProviders();

[Learn more about pagination providers](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#providers)

To use cursor based pagination annotate your resolver with `[UsePaging]` or `.UsePaging()`

C#

[UsePaging]

public IExecutable<Person> GetPersons(IMongoCollection<Person> collection)

{

return collection.AsExecutable();

}

You can then execute queries like the following one:

GraphQL

query GetPersons {

persons(first: 50, after: "OTk=") {

nodes {

name

addresses {

city

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

To use offset based pagination annotate your resolver with `[UseOffsetPaging]` or `.UseOffsetPaging()`

C#

[UseOffsetPaging]

public IExecutable<Person> GetPersons(IMongoCollection<Person> collection)

{

return collection.AsExecutable();

}

You can then execute queries like the following one:

GraphQL

query GetPersons {

persons(skip: 50, take: 50) {

items {

name

addresses {

city

}

}

pageInfo {

hasNextPage

hasPreviousPage

}

}

}

[](https://chillicream.com/docs/hotchocolate/v14/integrations/mongodb#firstordefault--singleordefault)FirstOrDefault / SingleOrDefault
--------------------------------------------------------------------------------------------------------------------------------------

Sometimes you may want to return only a single object of a collection. To limit the response to one element you can use the `UseFirstOrDefault` or `UseSingleOrDefault` middleware. Hot Chocolate will rewrite the type of the field from a list type to an object type.

C#

[UseFirstOrDefault]

public IExecutable<Person> GetPersonById(IMongoCollection<Person> collection, Guid id)

{

return collection.Find(x => x.Id == id).AsExecutable();

}

Last updated on **2026-02-17** by**Tobias Tengler**
