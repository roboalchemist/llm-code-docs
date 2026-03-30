# Source: https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination

Title: Pagination - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination

Markdown Content:
Pagination is one of the most common problems that we have to solve when implementing our backend. Often, sets of data are too large to pass them directly to the consumer of our service.

Pagination solves this problem by giving the consumer the ability to fetch a set in chunks.

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#connections)Connections
-------------------------------------------------------------------------------------------------

_Connections_ are a standardized way to expose pagination to clients.

Instead of returning a list of entries, we return a _Connection_.

SDL

type Query {

users(first: Int after: String last: Int before: String): UsersConnection

}

type UsersConnection {

pageInfo: PageInfo!

edges: [UsersEdge!]

nodes: [User!]

}

type UsersEdge {

cursor: String!

node: User!

}

type PageInfo {

hasNextPage: Boolean!

hasPreviousPage: Boolean!

startCursor: String

endCursor: String

}

You can learn more about this in the [GraphQL Cursor Connections Specification](https://relay.dev/graphql/connections.htm).

> Note: _Connections_ are often associated with _cursor-based_ pagination, due to the use of a _cursor_. Nonetheless, since the specification describes the _cursor_ as opaque, it can be used to facilitate an _offset_ as well.

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#definition)Definition
-----------------------------------------------------------------------------------------------

Adding pagination capabilities to our fields is a breeze. All we have to do is add the `UsePaging` middleware.

C#

public class Query

{

[UsePaging]

public IEnumerable<User> GetUsers(IUserRepository repository)

=> repository.GetUsers();

}

For the `UsePaging` middleware to work, our resolver needs to return an `IEnumerable<T>` or an `IQueryable<T>`. The middleware will then apply the pagination arguments to what we have returned. In the case of an `IQueryable<T>` this means that the pagination operations can be directly translated to native database queries.

We also offer pagination integrations for some database technologies that do not use `IQueryable`.

[Learn more about pagination providers](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#providers)

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#naming)Naming
---------------------------------------------------------------------------------------

The name of the _Connection_ and Edge type is automatically inferred from the field name. If our field is called `users`, a `UsersConnection` and `UsersEdge` type is automatically generated.

We can also specify a custom name for our _Connection_ like the following.

C#

public class Query

{

[UsePaging(ConnectionName = "CustomUsers")]

public IEnumerable<User> GetUsers(IUserRepository repository)

{

}

}

The strings `Connection` and `Edge` are automatically appended to this user specified value to form the names of the _Connection_ and Edge types.

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#options)Options
-----------------------------------------------------------------------------------------

We can define a number of options on a per-field basis.

In the implementation-first approach we can define these options using properties on the `[UsePaging]` attribute.

C#

[UsePaging(MaxPageSize = 100)]

[Learn more about the possible PagingOptions](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#pagingoptions)

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#changing-the-node-type)Changing the node type
-----------------------------------------------------------------------------------------------------------------------

Lets say we are returning a collection of `string` from our pagination resolver, but we want these `string` to be represented in the schema using the `ID` scalar.

For this we can specifically tell the `UsePaging` middleware, which type to use in the schema for representation of the returned CLR type.

C#

public class Query

{

[UsePaging(typeof(IdType))]

public IEnumerable<string> GetIds()

{

}

}

The same applies of course, if we are returning a collection of `User` from our pagination resolver, but we want to use the `UserType` for representation in the schema.

If we need more control over the pagination process we can do so, by returning a `Connection<T>`.

C#

public class Query

{

[UsePaging]

public Connection<User> GetUsers(string? after, int? first, string sortBy)

{

IEnumerable<User> users = null;

var edges = users.Select(user => new Edge<User>(user, user.Id))

.ToList();

var pageInfo = new ConnectionPageInfo(false, false, null, null);

var connection = new Connection<User>(edges, pageInfo,

ct => ValueTask.FromResult(0));

return connection;

}

}

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#adding-fields-to-an-edge)Adding fields to an Edge
---------------------------------------------------------------------------------------------------------------------------

We can add new fields to an Edge type, by creating a type extension that targets the Edge type by its name.

If our Edge is named `UsersEdge`, we can add a new field to it like the following.

C#

[ExtendObjectType("UsersEdge")]

public class UsersEdge

{

public string NewField([Parent] Edge<User> edge)

{

var cursor = edge.Cursor;

var user = edge.Node;

}

}

[Learn more about extending types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types)

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#adding-fields-to-a-connection)Adding fields to a Connection
-------------------------------------------------------------------------------------------------------------------------------------

We can add new fields to a _Connection_ type, by creating a type extension that targets the _Connection_ type by its name.

If our _Connection_ is named `UsersConnection`, we can add a new field to it like the following.

C#

[ExtendObjectType("UsersConnection")]

public class UsersConnectionExtension

{

public string NewField()

{

}

}

[Learn more about extending types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types)

These additional fields are great to perform aggregations either on the entire dataset, by for example issuing a second database call, or on top of the paginated result.

We can access the pagination result like the following:

C#

[ExtendObjectType("UsersConnection")]

public class UsersConnectionExtension

{

public string NewField([Parent] Connection<User> connection)

{

var result = connection.Edges.Sum(e => e.Node.SomeField);

}

}

> Note: If you are using [Projections](https://chillicream.com/docs/hotchocolate/v14/fetching-data/projections), be aware that some properties on your model might not be set, depending on what the user queried for.

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#total-count)Total count
-------------------------------------------------------------------------------------------------

Sometimes we might want to return the total number of pageable entries.

For this to work we need to enable the `IncludeTotalCount` flag on the `UsePaging` middleware.

C#

[UsePaging(IncludeTotalCount = true)]

This will add a new field called `totalCount` to our _Connection_.

SDL

type UsersConnection {

pageInfo: PageInfo!

edges: [UsersEdge!]

nodes: [User!]

totalCount: Int!

}

If our resolver returns an `IEnumerable<T>` or an `IQueryable<T>` the `totalCount` will be automatically computed, if it has been specified as a subfield in the query.

If we have customized our pagination and our resolver now returns a `Connection<T>`, we have to explicitly declare how the `totalCount` value is computed.

C#

var connection = new Connection<User>(

edges,

pageInfo,

getTotalCount: cancellationToken => ValueTask.FromResult(0));

> Note: While we support _offset-based_ pagination, we highly encourage the use of [_Connections_](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#connections) instead. _Connections_ provide an abstraction which makes it easier to switch to another pagination mechanism later on.

Besides _Connections_ we can also expose a more traditional _offset-based_ pagination.

SDL

type Query {

users(skip: Int take: Int): UserCollectionSegment

}

type UserCollectionSegment {

items: [User!]

pageInfo: CollectionSegmentInfo!

}

type CollectionSegmentInfo {

hasNextPage: Boolean!

hasPreviousPage: Boolean!

}

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#definition-1)Definition
-------------------------------------------------------------------------------------------------

To add _offset-based_ pagination capabilities to our fields we have to add the `UseOffsetPaging` middleware.

C#

public class Query

{

[UseOffsetPaging]

public IEnumerable<User> GetUsers(IUserRepository repository)

=> repository.GetUsers();

}

For the `UseOffsetPaging` middleware to work, our resolver needs to return an `IEnumerable<T>` or an `IQueryable<T>`. The middleware will then apply the pagination arguments to what we have returned. In the case of an `IQueryable<T>` this means that the pagination operations can be directly translated to native database queries.

We also offer pagination integrations for some database technologies that do not use `IQueryable`.

[Learn more about pagination providers](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#providers)

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#naming-1)Naming
-----------------------------------------------------------------------------------------

The name of the CollectionSegment type is inferred from the item type name. If our field returns a collection of `UserType` and the name of this type is `User`, the CollectionSegment will be called `UserCollectionSegment`.

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#options-1)Options
-------------------------------------------------------------------------------------------

We can define a number of options on a per-field basis.

In the implementation-first approach we can define these options using properties on the `[UseOffsetPaging]` attribute.

C#

[UseOffsetPaging(MaxPageSize = 100)]

[Learn more about the possible PagingOptions](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#pagingoptions)

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#changing-the-item-type)Changing the item type
-----------------------------------------------------------------------------------------------------------------------

Lets say we are returning a collection of `string` from our pagination resolver, but we want these `string` to be represented in the schema using the `ID` scalar.

For this we can specifically tell the `UseOffsetPaging` middleware, which type to use in the schema for representation of the returned CLR type.

C#

public class Query

{

[UseOffsetPaging(typeof(IdType))]

public IEnumerable<string> GetIds()

{

}

}

The same applies of course, if we are returning a collection of `User` from our pagination resolver, but we want to use the `UserType` for representation in the schema.

If we need more control over the pagination process we can do so, by returning a `CollectionSegment<T>`.

C#

public class Query

{

[UseOffsetPaging]

public CollectionSegment<User> GetUsers(int? skip, int? take, string sortBy)

{

IEnumerable<User> users = null;

var pageInfo = new CollectionSegmentInfo(false, false);

var collectionSegment = new CollectionSegment<User>(

users,

pageInfo,

ct => ValueTask.FromResult(0));

return collectionSegment;

}

}

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#adding-fields-to-a-collectionsegment)Adding fields to a CollectionSegment
---------------------------------------------------------------------------------------------------------------------------------------------------

We can add new fields to a CollectionSegment type, by creating a type extension that targets the CollectionSegment by its name.

If our CollectionSegment is named `UserCollectionSegment`, we can add a new field to it like the following.

C#

[ExtendObjectType("UserCollectionSegment")]

public class UserCollectionSegmentExtension

{

public string NewField()

{

}

}

[Learn more about extending types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types)

These additional fields are great to perform aggregations either on the entire dataset, by for example issuing a second database call, or on top of the paginated result.

We can access the pagination result like the following:

C#

[ExtendObjectType("UserCollectionSegment")]

public class UserCollectionSegmentExtension

{

public string NewField([Parent] CollectionSegment<User> collectionSegment)

{

var result = collectionSegment.Items.Sum(i => i.SomeField);

}

}

> Note: If you are using [Projections](https://chillicream.com/docs/hotchocolate/v14/fetching-data/projections), be aware that some properties on your model might not be set, depending on what the user queried for.

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#total-count-1)Total count
---------------------------------------------------------------------------------------------------

Sometimes we might want to return the total number of pageable entries.

For this to work we need to enable the `IncludeTotalCount` flag on the `UseOffsetPaging` middleware.

C#

[UseOffsetPaging(IncludeTotalCount = true)]

This will add a new field called `totalCount` to our _CollectionSegment_.

SDL

type UserCollectionSegment {

pageInfo: CollectionSegmentInfo!

items: [User!]

totalCount: Int!

}

If our resolver returns an `IEnumerable<T>` or an `IQueryable<T>` the `totalCount` will be automatically computed, if it has been specified as a subfield in the query.

If we have customized our pagination and our resolver now returns a `CollectionSegment<T>`, we have to explicitly declare how the `totalCount` value is computed.

C#

var collectionSegment = new CollectionSegment<User>(

items,

pageInfo,

getTotalCount: cancellationToken => ValueTask.FromResult(0));

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#providers)Providers
---------------------------------------------------------------------------------------------

The `UsePaging` and `UseOffsetPaging` middleware provide a unified way of applying pagination to our resolvers. Depending on the data source used within the resolver the pagination mechanism needs to be different though. Hot Chocolate includes so called paging providers that allow us to use the same API, e.g. `UsePaging`, but for different data sources, e.g. MongoDB and SQL.

Paging providers can be registered using various methods on the `IRequestExecutorBuilder`. For example the MongoDB paging provider can be registered like the following.

C#

builder.Services

.AddGraphQLServer()

.AddMongoDbPagingProviders();

[Consult the specific integration documentation for more details](https://chillicream.com/docs/hotchocolate/v14/integrations)

When registering paging providers we can name them to be able to explicitly reference them.

C#

builder.Services

.AddGraphQLServer()

.AddMongoDbPagingProviders(providerName: "MongoDB");

They can then be referenced like the following.

C#

[UsePaging(ProviderName = "MongoDB")]

public IEnumerable<User> GetUsers()

If no `ProviderName` is specified, the correct provider is selected based on the return type of the resolver. If the provider to use can't be inferred from the return type, the first (default) provider is used automatically. If needed we can mark a paging provider as the explicit default.

C#

builder.Services

.AddGraphQLServer()

.AddMongoDbPagingProviders(defaultProvider: true);

If no paging providers have been registered, a default paging provider capable of handling `IEnumerable<T>` and `IQueryable<T>` is used.

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#pagingoptions)PagingOptions
-----------------------------------------------------------------------------------------------------

`PagingOptions` can either be defined on a per-field basis or [globally](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#pagination-defaults).

The following options can be configured.

| Property | Default | Description |
| --- | --- | --- |
| `MaxPageSize` | `50` | Maximum number of items a client can request via `first`, `last` or `take`. |
| `DefaultPageSize` | `10` | The default number of items, if a client does not specify`first`, `last` or `take`. |
| `IncludeTotalCount` | `false` | Add a `totalCount` field for clients to request the total number of items. |
| `AllowBackwardPagination` | `true` | Include `before` and `last` arguments on the _Connection_. |
| `RequirePagingBoundaries` | `false` | Clients need to specify either `first`, `last` or `take`. |
| `InferConnectionNameFromField` | `true` | Infer the name of the _Connection_ from the field name rather than its type. |
| `ProviderName` | `null` | The name of the pagination provider to use. |

If we want to enforce consistent pagination defaults throughout our app, we can do so by modifying the global `PagingOptions`.

C#

builder.Services

.AddGraphQLServer()

.ModifyPagingOptions(opt => opt.MaxPageSize = 100);

[Learn more about possible PagingOptions](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#pagingoptions)

In this section we will look at the most common pagination approaches and their downsides. There are mainly two concepts we find today: _offset-based_ and _cursor-based_ pagination.

> Note: This section is intended as a brief overview and should not be treated as a definitive guide or recommendation.

_Offset-based_ pagination is found in many server implementations whether the backend is implemented in SOAP, REST or GraphQL.

It is so common, since it is the simplest form of pagination we can implement. All it requires is an `offset` (start index) and a `limit` (number of entries) argument.

SQL

SELECT * FROM Users

ORDER BY Id

LIMIT %limit OFFSET %offset

### [](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#problems)Problems

But whilst _offset-based_ pagination is simple to implement and works relatively well, there are also some problems:

*   Using `OFFSET` on the database-side does not scale well for large datasets. Most databases work with an index instead of numbered rows. This means the database always has to count _offset + limit_ rows, before discarding the _offset_ and only returning the requested number of rows.

*   If new entries are written to or removed from our database at high frequency, the _offset_ becomes unreliable, potentially skipping or returning duplicate entries.

Contrary to the _offset-based_ pagination, where we identify the position of an entry using an _offset_, _cursor-based_ pagination works by returning the pointer to the next entry in our pagination.

To understand this concept better, let's look at an example: We want to paginate over the users in our application.

First we execute the following to receive our first page:

SQL

SELECT * FROM Users

ORDER BY Id

LIMIT %limit

`%limit` is actually `limit + 1`. We are doing this to know wether there are more entries in our dataset and to receive the _cursor_ of the next entry (in this case its `Id`). This additional entry will not be returned to the consumer of our pagination.

To now receive the second page, we execute:

SQL

SELECT * FROM Users

WHERE Id >= %cursor

ORDER BY Id

LIMIT %limit

Using `WHERE` instead of `OFFSET` is great, since now we can leverage the index of the `Id` field and the database does not have to compute an _offset_.

For this to work though, our _cursor_ needs to be **unique** and **sequential**. Most of the time the _Id_ field will be the best fit.

But what if we need to sort by a field that does not have the aforementioned properties? We can simply combine the field with another field, which has the needed properties (like `Id`), to form a _cursor_.

Let's look at another example: We want to paginate over the users sorted by their birthday.

After receiving the first page, we create a combined _cursor_, like `"1435+2020-12-31"` (`Id` + `Birthday`), of the next entry. To receive the second page, we convert the _cursor_ to its original values (`Id` + `Birthday`) and use them in our query:

SQL

SELECT * FROM Users

WHERE (Birthday >= %cursorBirthday

OR (Birthday = %cursorBirthday AND Id >= %cursorId))

ORDER BY Birthday, Id

LIMIT %limit

### [](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination#problems-1)Problems

Even though _cursor-based_ pagination can be more performant than _offset-based_ pagination, it comes with some downsides as well:

*   When using `WHERE` and `ORDER BY` on a field without an index, it can be slower than using `ORDER BY` with `OFFSET`.

*   Since we now only know of the next entry, there is no more concept of pages. If we have a feed or only _Next_ and _Previous_ buttons, this works great, but if we depend on page numbers, we are in a tight spot.

Last updated on **2026-02-17** by**Tobias Tengler**
