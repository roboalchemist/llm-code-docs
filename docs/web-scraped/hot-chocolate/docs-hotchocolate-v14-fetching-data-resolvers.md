# Source: https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers

Title: Resolvers - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers

Published Time: Tue, 17 Feb 2026 16:19:11 GMT

Markdown Content:
When it comes to fetching data in a GraphQL server, it will always come down to a resolver.

**A resolver is a generic function that fetches data from an arbitrary data source for a particular field.**

We can think of each field in our query as a method of the previous type which returns the next type.

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#resolver-tree)Resolver Tree
----------------------------------------------------------------------------------------------------

A resolver tree is a projection of a GraphQL operation that is prepared for execution.

For better understanding, let's imagine we have a simple GraphQL query like the following, where we select some fields of the currently logged-in user.

GraphQL

query {

me {

name

company {

id

name

}

}

}

In Hot Chocolate, this query results in the following resolver tree.

This tree will be traversed by the execution engine, starting with one or more root resolvers. In the above example the `me` field represents the only root resolver.

Field resolvers that are sub-selections of a field, can only be executed after a value has been resolved for their _parent_ field. In the case of the above example this means that the `name` and `company` resolvers can only run, after the `me` resolver has finished. Resolvers of field sub-selections can and will be executed in parallel.

**Because of this it is important that resolvers, with the exception of top level mutation field resolvers, do not contain side-effects, since their execution order may vary.**

The execution of a request finishes, once each resolver of the selected fields has produced a result.

_This is of course an oversimplification that differs from the actual implementation._

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#defining-a-resolver)Defining a Resolver
----------------------------------------------------------------------------------------------------------------

Resolvers can be defined in a way that should feel very familiar to C# developers, especially in the implementation-first approach.

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#properties)Properties
----------------------------------------------------------------------------------------------

Hot Chocolate automatically converts properties with a public get accessor to a resolver that simply returns its value.

Properties are also covered in detail by the [object type documentation](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types).

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#regular-resolver)Regular Resolver
----------------------------------------------------------------------------------------------------------

A regular resolver is just a simple method, which returns a value.

C#

public class Query

{

public string Foo() => "Bar";

}

C#

builder.Services

.AddGraphQLServer()

.AddQueryType<Query>();

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#async-resolver)Async Resolver
------------------------------------------------------------------------------------------------------

Most data fetching operations, like calling a service or communicating with a database, will be asynchronous.

In Hot Chocolate, we can simply mark our resolver methods and delegates as `async` or return a `Task<T>` and it becomes an async-capable resolver.

We can also add a `CancellationToken` argument to our resolver. Hot Chocolate will automatically cancel this token if the request has been aborted.

C#

public class Query

{

public async Task<string> Foo(CancellationToken ct)

{

}

}

When using a delegate resolver, the `CancellationToken` is passed as second argument to the delegate.

C#

descriptor

.Field("foo")

.Resolve((context, ct) =>

{

});

The `CancellationToken` can also be accessed through the `IResolverContext`.

C#

descriptor

.Field("foo")

.Resolve(context =>

{

CancellationToken ct = context.RequestAborted;

});

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#resolvewith)ResolveWith
------------------------------------------------------------------------------------------------

Thus far we have looked at two ways to specify resolvers in code-first:

*   Add new methods to the CLR type, e.g. the `T` type of `ObjectType<T>`

*   Add new fields to the schema type in the form of delegates

C#

descriptor.Field("foo").Resolve(context => ) 

But there's a third way. We can describe our field using the `descriptor`, but instead of a resolver delegate, we can point to a method on another class, responsible for resolving this field.

C#

public class FooResolvers

{

public string GetFoo(string arg, FooService service)

{

}

}

public class QueryType : ObjectType

{

protected override void Configure(IObjectTypeDescriptor descriptor)

{

descriptor

.Field("foo")

.Argument("arg", a => a.Type<NonNullType<StringType>>())

.ResolveWith<FooResolvers>(r => r.GetFoo(default, default));

}

}

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#arguments)Arguments
--------------------------------------------------------------------------------------------

We can access arguments we defined for our resolver like regular arguments of a function.

There are also specific arguments that will be automatically populated by Hot Chocolate when the resolver is executed. These include [Dependency injection services](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#injecting-services), [DataLoaders](https://chillicream.com/docs/hotchocolate/v14/fetching-data/dataloader), state, or even context like a [_parent_](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#accessing-parent-values) value.

[Learn more about arguments](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/arguments)

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#injecting-services)Injecting Services
--------------------------------------------------------------------------------------------------------------

Let's assume we have created a `UserService` and registered it as a service.

C#

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddSingleton<UserService>()

builder.Services

.AddGraphQLServer()

.AddQueryType<Query>();

We can now access it like the following in our resolvers.

C#

public class Query

{

public List<User> GetUsers(UserService userService)

=> userService.GetUsers();

}

[Learn more about dependency injection](https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection)

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#accessing-the-httpcontext)Accessing the HttpContext
----------------------------------------------------------------------------------------------------------------------------

The [IHttpContextAccessor](https://docs.microsoft.com/dotnet/api/microsoft.aspnetcore.http.ihttpcontextaccessor) allows us to access the [HttpContext](https://docs.microsoft.com/dotnet/api/microsoft.aspnetcore.http.httpcontext) of the current request from within our resolvers. This is useful, if we for example need to set a header or cookie.

First we need to add the `IHttpContextAccessor` as a service.

C#

builder.Services.AddHttpContextAccessor();

After this we can inject it into our resolvers and make use of the the `HttpContext` property.

C#

public string Foo(string id, IHttpContextAccessor httpContextAccessor)

{

if (httpContextAccessor.HttpContext is not null)

{

}

}

[](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers#accessing-parent-values)Accessing parent values
------------------------------------------------------------------------------------------------------------------------

The resolver of each field on a type has access to the value that was resolved for said type.

Let's look at an example. We have the following schema.

SDL

type Query {

me: User!;

}

type User {

id: ID!;

friends: [User!]!;

}

The `User` schema type is represented by an `User` CLR type. The `id` field is an actual property on this CLR type.

C#

public class User

{

public string Id { get; set; }

}

`friends` on the other hand is a resolver i.e. method we defined. It depends on the user's `Id` property to compute its result. From the point of view of this `friends` resolver, the `User` CLR type is its _parent_.

We can access this so called _parent_ value like the following.

In the implementation-first approach we can just access the properties using the `this` keyword.

C#

public class User

{

public string Id { get; set; }

public List<User> GetFriends()

{

var currentUserId = this.Id;

}

}

There's also a `[Parent]` attribute that injects the parent into the resolver.

C#

public class User

{

public string Id { get; set; }

public List<User> GetFriends([Parent] User parent)

{

}

}

This is especially useful when using [type extensions](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types).

Last updated on **2026-02-17** by**Tobias Tengler**
