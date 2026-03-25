# Source: https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11

Title: Migrate Hot Chocolate from 10 to 11 - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11

Markdown Content:
This guide will walk you through the manual migration steps to get you Hot Chocolate GraphQL server to version 11.

As a general preparation, we recommend removing all HotChocolate.* package references from your project. Then start by adding the `HotChocolate.AspNetCore` package. The server package now contains most of the needed packages.

When do I need to add other Hot Chocolate packages explicitly?

We have now added the most common packages to the Hot Chocolate core. But there are certain areas where we still need to add some additional packages.

| Package | Topic |
| --- | --- |
| HotChocolate.AspNetCore.Authorization | The authorization package adds the authorization directive and integrates with Microsoft Authorization Policies |
| HotChocolate.Data | The new data package represents our integration with all kinds of data sources. This package provides the fundamentals for filtering, sorting, and projection logic. |
| HotChocolate.Types.Spatial | This package provides GeoJson spatial types. |
| HotChocolate.Data.Spatial | The package integrates the spatial types with the data package to allow for spatial filtering, sorting, and projections. |
| HotChocolate.Subscriptions.Redis | The in-memory subscription provider, is now integrated by default. To have an integration with Redis, you need to add this package. |
| HotChocolate.PersistedQueries.FileSystem | This package provides a persisted query storage for the file system. |
| HotChocolate.PersistedQueries.Redis | This package provides a persisted query storage for Redis. |

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#aspnet-core)ASP.NET Core
---------------------------------------------------------------------------------------------------------

One of the main focuses of version 11 was to create a new configuration API that brings all our builders together into one unified API. This also means that we had to introduce breaking changes to the way we configure schemas.

After you have cleaned up your packages, head over to the `Startup.cs` to start with the new configuration API migration.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#configureservices)ConfigureServices
--------------------------------------------------------------------------------------------------------------------

In your `Startup.cs` head over to the `ConfigureServices` methods. The configuration of a schema has slightly changed, and the new configuration API has replaced the `SchemaBuilder`.

We now start with `AddGraphQLServer` to define a new GraphQL server, `AddGraphQLServer`, returns the new `IRequestExecutorBuilder` that lets us apply all the configuration methods that used to be on the `SchemaBuilder`, `StitchingBuilder` and the `QueryExecutionBuilder`.

**Old:**

C#

services.AddGraphQL(sp =>

SchemaBuilder.New()

.AddServices(sp)

.AddQueryType<QueryType>()

.AddMutationType<MutationType>()

...

.Create());

**New:**

C#

services

.AddGraphQLServer()

.AddQueryType<QueryType>()

.AddMutationType<MutationType>()

...

If you were using the `OperationRequestBuilder` to configure request options or change the request pipeline, you need to add those things to the configuration chain of the ```IRequestExecutorBuilder`.

C#

services

.AddGraphQLServer()

.AddQueryType<QueryType>()

.AddMutationType<MutationType>()

...

.ModifyRequestOptions(o => o.ExecutionTimeout = TimeSpan.FromSeconds(180));

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#configure)Configure
----------------------------------------------------------------------------------------------------

After migrating the schema configuration, the next area that has fundamentally changed is the schema middleware.

Hot Chocolate server now embraces the new endpoint routing API from ASP.NET core and with that brings a lot of new features. Head over [here](https://chillicream.com/docs/hotchocolate/v11/api-reference/aspnetcore) to read more about the ASP.NET Core integration.

**Old:**

C#

app.UseGraphQL();

**New:**

C#

app.UseRouting();

app.UseEndpoints(x => x.MapGraphQL());

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#request-interceptor)Request Interceptor
------------------------------------------------------------------------------------------------------------------------

The query request interceptor was reworked and we renamed it to `IHttpRequestInterceptor`.

C#

public interface IHttpRequestInterceptor

{

ValueTask OnCreateAsync(

HttpContext context,

IRequestExecutor requestExecutor,

OperationRequestBuilder requestBuilder,

CancellationToken cancellationToken);

}

**Old:**

C#

services.AddQueryRequestInterceptor(

(context, builder, ct) =>

{

});

**New:**

C#

services.AddGraphQLServer()

...

.AddHttpRequestInterceptor(

(context, executor, builder, ct) =>

{

});

You can also extend `DefaultHttpRequestInterceptor` and inject it like the following.

C#

services.AddGraphQLServer()

...

.AddHttpRequestInterceptor<MyCustomExecutor>();

> A request interceptor is a service that is used by all hosted schemas.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#entity-framework-serial-execution)Entity Framework Serial Execution
----------------------------------------------------------------------------------------------------------------------------------------------------

The serial execution for Entity Framework compatibility is gone. If you use Entity Framework Core we recommend using version 5 and the new context factory in combination with context pooling. This allows the execution engine to execute in parallel and still be memory efficient since context objects are pooled.

Another variant here is to use our scoped service feature that scopes services for the resolver pipeline. This is explained in our GraphQL Workshop project.

[https://github.com/ChilliCream/graphql-workshop](https://github.com/ChilliCream/graphql-workshop)

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#schema--resolvers)Schema / Resolvers
---------------------------------------------------------------------------------------------------------------------

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#field-ordering)Field ordering
--------------------------------------------------------------------------------------------------------------

Hot Chocolate 11 follows the spec and returns the fields in the order they were defined. This feature makes migrations harder because the schema snapshot looks different compared to version 11. You can change this behavior with the following setting.

C#

builder.ModifyOptions(x => x.SortFieldsByName = true)

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#dataloaders)DataLoaders
--------------------------------------------------------------------------------------------------------

With Hot Chocolate server 11, we have embraced the new DataLoader spec version 2. With that, we have decoupled the scheduler from the DataLoader itself, meaning you now have to pass on the `IBatchScheduler` to the base implementation of the DataLoader. Apart from that, DataLoader now uses `ValueTask` instead of `Task` when doing async work.

If you were adding the `DataLoaderRegistry` to the services, remove that code since `service.AddDataLoaderRegistry` is no longer needed.

**Old:**

C#

public class FooDataLoader : DataLoaderBase<Guid, Foo>

{

private readonly IFooRepository _fooRepository;

public FooDataLoader(IFooRepository fooRepository)

{

_fooRepository = fooRepository;

}

protected override async Task<IReadOnlyList<Result<Foo>>> FetchAsync(

IReadOnlyList<Guid> keys,

CancellationToken cancellationToken)

{

....

}

}

**New:**

C#

public class FooDataLoader : DataLoaderBase<Guid, Foo>

{

private readonly IFooRepository _fooRepository;

public FooDataLoader(

IBatchScheduler scheduler,

IFooRepository fooRepository)

: base(scheduler)

{

_fooRepository = fooRepository;

}

protected override async ValueTask<IReadOnlyList<Result<Foo>>> FetchAsync(

IReadOnlyList<Guid> keys,

CancellationToken cancellationToken)

{

....

}

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#node-resolver)Node Resolver
------------------------------------------------------------------------------------------------------------

With version 11, we have reworked how Relay node types are defined. Furthermore, we added pure code-first (annotation-based) support.

**Old:**

C#

descriptor

.AsNode()

.IdField(d => d.Id)

.NodeResolver(async (ctx, id) => await ctx

.DataLoader<FooDataLoader>()

.LoadAsync(id, ctx.RequestAborted))

**New:**

The following example essentially aligns very closely to the old variant.

C#

descriptor

.ImplementsNode()

.IdField(d => d.Id)

.ResolveNode(async (ctx, id) => await ctx

.DataLoader<FooDataLoader>()

.LoadAsync(id, ctx.RequestAborted))

But, we can now also use an external resolver like with standard resolvers. This allows us to write better testable code that takes advantage of the method parameter injection we use in everyday resolvers.

C#

descriptor

.ImplementsNode()

.IdField(d => d.Id)

.ResolveNodeWith<NodeResolver>(t => t.GetNodeAsync(default, default));

But we can go even further now with pure code-first (annotation-based) support. By just annotating the entity with the `NodeAttribute`, we essentially told the schema builder that this is a node. The type initialization can then try to infer the node resolver directly from the type.

C#

[Node]

public class MyEntity

{

public string Id { get; set; }

public async Task<MyEntity> GetAsync(....)

{

....

}

}

Often, however, we want the repository logic decoupled from our domain object/entity. In this case, we can specify the entity resolver type.

C#

[Node(NodeResolverType = typeof(MyEntityResolver))]

public class MyEntity

{

public string Id { get; set; }

}

public class MyEntityResolver

{

public async Task<MyEntity> GetAsync(....)

{

....

}

}

There are more variants possible, but to give an impression of the new convenience and flexibility around nodes. As a side note, if you do not want the node attribute on the domain objects, you can also now add your very own attribute or interface to mark this and rewrite that in the schema building process to the `NodeAttribute`.

The first thing to note around pagination is that we listened to a lot of feedback and have removed the `PaginationAmountType`.

Moreover, we have introduced new PagingOptions, which can be set with the new configuration API on the schema level. With the new options, you can configure the `MaxPageSize`, `DefaultPageSize` and whether the total count shall be included `IncludeTotalCount`.

C#

builder.SetPagingOptions(

new PagingOptions()

{

MaxPageSize = searchOptions.PaginationAmount,

DefaultPageSize = searchOptions.PaginationAmount,

IncludeTotalCount = true

});

Further, you can override the paging option on the resolver level.

C#

[UsePaging(MaxPageSize = 100)]

C#

descriptor.Field(...).UsePaging(maxPageSize = 100)...

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#projections)Projections
--------------------------------------------------------------------------------------------------------

The selection middleware, that was available in `HotChocolate.Types.Selections` was replaced by the projection middleware from `HotChocolate.Data`.

**Old:**

C#

descriptor.Field(...).UseSelection()...

**New:**

C#

descriptor.Field(...).UseProjection()...

Similarly, the attribute `[UseSelection]` was replaced by `[UseProjection]`.

To use projections with your GraphQL endpoint you have to register it on the schema:

C#

services.AddGraphQLServer()

.AddProjections();

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#enum-type)Enum Type
----------------------------------------------------------------------------------------------------

Hot Chocolate server 11 now follows the spec recommendation with the new enum name conventions and formats the enum values by default as UPPER_SNAIL_CASE.

To avoid breaking changes to your schema, you will have to override the naming convention:

**Configuration:**

C#

builder

.AddConvention<INamingConventions>(new CompatibilityNamingConvention())

**Convention:**

C#

public class CompatibilityNamingConvention

: DefaultNamingConventions

{

public override NameString GetEnumValueName(object value)

{

if (value == null)

{

throw new ArgumentNullException(nameof(value));

}

return value.ToString().ToUpperInvariant();

}

}

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#iresolvercontextsource)IResolverContext.Source
-------------------------------------------------------------------------------------------------------------------------------

The source result stack was removed from the resolver context for performance reasons. If you need such a functionality, you can write a middleware that aggregates the resulting path on the scoped context.

**Old:**

C#

public class FooType : ObjectType<Foo>

{

private static readonly object _empty = new object();

protected override void Configure(IObjectTypeDescriptor<Foo> descriptor)

{

descriptor

.Field("bar")

.Type<NonNullType<BarType>>()

.Resolver(_empty);

}

}

public class BarType : ObjectType

{

protected override void Configure(IObjectTypeDescriptor descriptor)

{

descriptor

.Field("baz")

.Type<DateTimeType>()

.Resolve(ctx =>

{

Foo foo = (Foo)ctx.Source.Pop().Peek();

return foo.Baz;

});

}

}

**New:**

C#

public class FooType : ObjectType<Foo>

{

protected override void Configure(IObjectTypeDescriptor<Foo> descriptor)

{

descriptor

.Field("bar")

.Type<NonNullType<BarType>>()

.Resolve(

ctx =>

{

ctx.ScopedContextData =

ctx.ScopedContextData.SetItem(nameof(Foo), ctx.Parent<Foo>());

return new object();

});

}

}

public class BarType : ObjectType

{

protected override void Configure(IObjectTypeDescriptor descriptor)

{

descriptor

.Field("baz")

.Type<DateTimeType>()

.Resolve(

ctx =>

{

if (ctx.ScopedContextData.TryGetValue(nameof(Foo), out object? potentialFoo) &&

potentialFoo is Foo foo)

{

return foo.Baz;

}

throw new GraphQLException(

ErrorBuilder.New()

.AddLocation(ctx.Field.SyntaxNode)

.SetMessage("Foo was not pushed down.")

.SetPath(ctx.Path)

.Build());

});

}

}

If you use authorization, you need to add a package reference to `HotChocolate.AspNetCore.Authorization`.

**Old:**

C#

builder.AddAuthorizeDirectiveType()

**New:**

C#

builder.AddAuthorization()

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#typebinding)TypeBinding
--------------------------------------------------------------------------------------------------------

We have renamed the binding method from `BindClrType` to `BindRuntimeType` to make it more clear what it does.

**Old:**

C#

builder.BindClrType<DateTime, DateTimeType>()

**New:**

C#

builder.BindRuntimeType<DateTime, DateTimeType>()

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#fieldmiddleware)FieldMiddleware
----------------------------------------------------------------------------------------------------------------

Since all configuration APIs were integrated into one, we needed to make it more specific for what a middleware is defined. `UseField` defines a middleware that is applied to the resolver pipeline / field pipeline whereas `UseRequest` defines a middleware that is defined for the request processing.

**Old:**

C#

builder.Use<CustomMiddleware>()

**New:**

C#

builder.UseField<CustomMiddleware>()

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#stitching)Stitching
----------------------------------------------------------------------------------------------------

The schema stitching configuration API has been completely integrated into the new configuration API. This means that a Gateway is nothing more than a GraphQL schema, which will make it easier for new users. However, you will need to completely rewire your stitching configuration.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#configuration)Configuration
------------------------------------------------------------------------------------------------------------

The stitching builder no longer exists in version 11 and you need to use the new configuration API to configure your gateway.

**Old:**

C#

services.AddStitchedSchema(x => ....);

**New:**

C#

services.AddGraphQLServer()....

### [](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#addschemafromhttp)AddSchemaFromHttp

Registering a remote schema has slightly changed in version 11 to make it more clear that we are adding a remote schema into the local gateway schema. Removing, root types and importing a remote schema can be done in one go now.

**Old:**

C#

builder.AddSchemaFromHttp("SomeSchema").IgnoreRootTypes("SomeSchema");

**New:**

C#

builder.AddRemoteSchema("SomeSchema", ignoreRootTypes: true);

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#addschemaconfiguration)AddSchemaConfiguration
------------------------------------------------------------------------------------------------------------------------------

In version 11 it is now much easier to configure the gateway schema.

**Old:**

C#

services.AddStitchedSchema(x => x.AddSchemaConfiguration(y => y.RegisterType<FooType>()));

**New:**

C#

services

.AddGraphQLServer()

.AddType<FooType>();

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#ignorefield)IgnoreField
--------------------------------------------------------------------------------------------------------

The order of the parameters in ignore field and ignore type has changed since we moved optional parameters to the end.

**Old:**

C#

services.AddStitchedSchema(x => x.IgnoreField("SchemaName", "TypeName, "FieldName"));

**New:**

C#

services

.AddGraphQLServer()

.IgnoreField("TypeName, "FieldName", "SchemaName")

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#setexecutionoptions)SetExecutionOptions
------------------------------------------------------------------------------------------------------------------------

Execution options can now be configured on the root schema directly like for any other schema:

**Old:**

C#

services.AddStitchedSchema(

x => x.SetExecutionOptions(

new QueryExecutionOptions

{

TracingPreference = TracingPreference.OnDemand

}));

**New:**

C#

services

.AddGraphQLServer()

.ModifyRequestOptions(x => x.TracingPreference = TracingPreference.OnDemand);

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#configuring-a-downstream-schema)Configuring a downstream schema
------------------------------------------------------------------------------------------------------------------------------------------------

In case you want to configure a downstream schema, you can now just use the new configuration API since all downstream schemas have an in-memory representation.

C#

services

.AddGraphQLServer()

.AddRemoteSchema("SomeSchema");

services

.AddGraphQL("SomeSchema")

.AddType(new IntType("SpecialIntegerType"));

The `PaginationAmount` scalar was removed since it caused a lot of issues with clients and only provided limited benefit. The arguments `first` and `last` use now `Int` as a type. To avoid breaking schemas on a stitched schema, you can add a rewriter that rewrites all `first: Int` and `last: Int` on a connection to `first: PaginationAmount` and `last: PaginationAmount`. You also have to make sure that you register a new `IntType` on the root schema and rewrite all downstream schemas.

**Configuration:**

C#

services

.AddGraphQLServer()

.AddRemoteSchema("SomeSchema")

.ConfigureSchema(x =>

x.AddType(new IntType())

.AddType(new IntType("PaginationAmount")))

.AddMergedDocumentRewriter(

d => (DocumentNode)new PagingAmountRewriter().Rewrite(d, null));

services

.AddGraphQL("SomeSchema")

.ConfigureSchema(x =>

x.AddType(new IntType())

.AddType(new IntType("PaginationAmount")));

**PagingAmountRewriter:**

C#

internal class PagingAmountRewriter : SchemaSyntaxRewriter<object?>

{

protected override FieldDefinitionNode RewriteFieldDefinition(

FieldDefinitionNode node,

object? context)

{

if (node.Type.NamedType().Name.Value.EndsWith("Connection") &&

(node.Arguments.Any(

t => t.Name.Value.EqualsOrdinal("first") &&

t.Type.NamedType().Name.Value.EqualsOrdinal("Int"))

|| node.Arguments.Any(

t => t.Name.Value.EqualsOrdinal("last") &&

t.Type.NamedType().Name.Value.EqualsOrdinal("Int"))

))

{

var arguments = node.Arguments.ToList();

InputValueDefinitionNode first =

arguments.FirstOrDefault(t => t.Name.Value.EqualsOrdinal("first"));

InputValueDefinitionNode last =

arguments.FirstOrDefault(t => t.Name.Value.EqualsOrdinal("last"));

if (first != null) arguments[arguments.IndexOf(first)] = first.WithType(RewriteType(first.Type, "PaginationAmount"));

if (last != null) arguments[arguments.IndexOf(last)] = last.WithType(RewriteType(last.Type, "PaginationAmount"));

node = node.WithArguments(arguments);

}

return base.RewriteFieldDefinition(node, context);

}

private static ITypeNode RewriteType(ITypeNode type, NameString name)

{

if (type is NonNullTypeNode nonNullType)

{

return new NonNullTypeNode(

(INullableTypeNode)RewriteType(nonNullType.Type, name));

}

if (type is ListTypeNode listType)

{

return new ListTypeNode(RewriteType(listType.Type, name));

}

return new NamedTypeNode(name);

}

}

internal static class StringExtensions

{

public static bool EqualsOrdinal(this string value, string other) =>

string.Equals(value, other, StringComparison.Ordinal);

}

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#batch-responses)Batch responses
----------------------------------------------------------------------------------------------------------------

In v10, responses to batched operations were returned as a JsonArray. In v11 the default is to return MultiPartChunked responses. To switch back to JsonArray, configure the HttpResult serializer as follows:

C#

services.AddHttpResultSerializer(

batchSerialization: HttpResultSerialization.JsonArray

);

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#testing)Testing
------------------------------------------------------------------------------------------------

We have added a couple of test helpers to make the transition to the new configuration API easier.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#schema-snapshot-tests)Schema Snapshot Tests
----------------------------------------------------------------------------------------------------------------------------

**Old:**

C#

SchemaBuilder.New()

.AddQueryType<Query>()

.Create()

.ToString()

.MatchSnapshot();

**New:**

C#

ISchema schema =

await new ServiceCollection()

.AddGraphQL()

.AddQueryType<Query>()

.BuildSchemaAsync();

schema.Print().MatchSnapshot();

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#request-tests)Request Tests
------------------------------------------------------------------------------------------------------------

**Old:**

C#

IQueryExecutor executor =

SchemaBuilder.New()

.AddQueryType<Query>()

.Create()

.MakeExecutable();

**New:**

C#

IRequestExecutor executor =

await new ServiceCollection()

.AddGraphQL()

.AddQueryType<Query>()

.BuildRequestExecutorAsync();

IExecutionResult result =

await executor.ExecuteAsync("{ __typename }");

result.ToJson().MatchSnapshot();

Or you can directly build and execute:

C#

IExecutionResult result =

await new ServiceCollection()

.AddGraphQL()

.AddQueryType<Query>()

.ExecuteRequestAsync("{ __typename }");

result.ToJson().MatchSnapshot();

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11#dataloader-testing)DataLoader Testing
----------------------------------------------------------------------------------------------------------------------

Due to the changed constructor you now need to also create a scheduler for the dataloaders

Old

C#

FooDataLoader dataLoader = new FooDataLoader( fooRepoMock.Object);

New

C#

var scheduler = new BatchScheduler();

FooDataLoader dataLoader = new FooDataLoader(

scheduler,

fooRepoMock.Object);

// TODO : Type Converter

Last updated on **2026-02-17** by**Tobias Tengler**
