# Source: https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13

Title: Migrate Hot Chocolate from 12 to 13 - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13

Markdown Content:
This guide will walk you through the manual migration steps to update your Hot Chocolate GraphQL server to version 13.

Start by installing the latest `13.x.x` version of **all** of the `HotChocolate.*` packages referenced by your project.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#breaking-changes)Breaking changes
------------------------------------------------------------------------------------------------------------------

Things that have been removed or had a change in behavior that may cause your code not to compile or lead to unexpected behavior at runtime if not addressed.

If you previously annotated a type with `@authorize`, either directly in the schema or via `[Authorize]` or `descriptor.Authorize()`, the authorization rule was copied to each field of this type. This meant the authorization rule would be evaluated for each selected field beneath the annotated type in a request. This is inefficient, so we switched to evaluating the authorization rule **once** on the field that returns the "authorized" type instead.

Let's imagine you currently have the following GraphQL schema:

GraphQL

type Query {

user: User

}

type User @authorize {

field1: String

field2: Int

}

This is how the authorization rule would be evaluated previously and now:

**Before**

GraphQL

{

user {

field1

field2

}

}

**After**

GraphQL

{

user {

field1

field2

}

}

We observed a common pattern to put a '@authorize' directive on the root types and secure all their fields.

With the new default behavior of authorization, this would now fail since annotating the type will ensure that all fields returning instances of this type will be validated. Since there is no field returning the root types in most cases, these authorization rules will have no effect.

With the Authorization overhaul, we also introduced a way to more efficiently implement such a pattern by moving parts of the authorization into the validation.

GraphQL

type Query @authorize(apply: VALIDATION) {

user: User

}

type User {

field1: String

field2: Int

}

The ‘apply‘ argument defines when an authorization rule is applied. In the above case, the validation ensures that the GraphQL request documents authorization rules are fulfilled. We do that by collecting all authorization directives with ‘apply‘ set to ‘Validation‘ and running them before we start the execution.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#registerdbcontext)RegisterDbContext
--------------------------------------------------------------------------------------------------------------------

We changed the default [DbContextKind](https://chillicream.com/docs/hotchocolate/v13/integrations/entity-framework#dbcontextkind) from [DbContextKind.Synchronized](https://chillicream.com/docs/hotchocolate/v13/integrations/entity-framework#dbcontextkindsynchronized) to [DbContextKind.Resolver](https://chillicream.com/docs/hotchocolate/v13/integrations/entity-framework#dbcontextkindresolver). If the instance of your `DbContext` doesn't need to be the same for each executed resolver during a request, this should lead to a performance improvement.

To restore the v12 default behavior, pass the [DbContextKind.Synchronized](https://chillicream.com/docs/hotchocolate/v13/integrations/entity-framework#dbcontextkindsynchronized) to the `RegisterDbContext<T>` call.

**Before**

C#

services.AddGraphQLServer()

.RegisterDbContext<DbContext>()

**After**

C#

services.AddGraphQLServer()

.RegisterDbContext<DbContext>(DbContextKind.Synchronized)

> Note: Only add this if your application requires it. You're better off with the new default otherwise.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#batching)Batching
--------------------------------------------------------------------------------------------------

As an added security measure, batching has been disabled per default in this release. If you require batching, you now need to explicitly enable it.

C#

app.MapGraphQL().WithOptions(new GraphQLServerOptions

{

EnableBatching = true

});

Previously you might have also configured the ([now replaced](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#ihttpresultserializer)) `IHttpResultSerializer` to produce a `JsonArray` for your batches:

C#

services.AddHttpResultSerializer(batchSerialization: HttpResultSerialization.JsonArray)

This option has been removed in this release and batch results are now always being delivered through `multipart/mixed` responses. This allows us to send the batch results back to the client as soon as they are ready, without having to hold on to the result and performing a JSON array aggregation on the server. If you need an aggregated batch result, you should do the aggregation on the client instead.

[Learn more about the batching](https://chillicream.com/docs/hotchocolate/v13/server/batching)

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#nodes-batch-size)Nodes batch size
------------------------------------------------------------------------------------------------------------------

The number of nodes that can be requested through the `nodes` field is limited to 10 by default. See [Nodes batch size](https://chillicream.com/docs/hotchocolate/v13/security#nodes-batch-size) for the details.

You can change this default to suite the needs of your application as shown below:

C#

builder.Services.AddGraphQLServer()

.ModifyOptions(o => o.MaxAllowedNodeBatchSize = 1);

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#useoffsetpaging)UseOffsetPaging
----------------------------------------------------------------------------------------------------------------

In this release we aligned the naming of types generated by `UseOffsetPaging` with the behavior of `UsePaging`.

C#

[UseOffsetPaging]

public IQueryable<Order> GetUserOrders() => ...

The above resolver would previously generated a schema like this:

GraphQL

type Query {

userOrders(skip: Int, take: Int): OrderCollectionSegment

}

type OrderCollectionSegment {

items: [Order!]

pageInfo: CollectionSegmentInfo!

}

Notice how the CollectionSegment is named after the type being returned and not the name of the field. If you were to create a second resolver returning the same type also annotated with `UseOffsetPaging`, the previous CollectionSegment would be re-used. This could lead to issues, if you wanted to add additional information to only one of the CollectionSegments.

Given the same resolver from above, we now generate the following schema in v13, where the CollectionSegment is named after the field it's being returned from and not the field's return type:

GraphQL

type Query {

userOrders(skip: Int, take: Int): UserOrdersCollectionSegment

}

type UserOrdersCollectionSegment {

items: [Order!]

pageInfo: CollectionSegmentInfo!

}

If you want to retain the old behavior, you can disable the inferring from the field name either on a per-field basis

C#

[UseOffsetPaging(InferCollectionSegmentNameFromField = false)]

or change the global default

C#

builder.Services

.AddGraphQLServer()

.SetPagingOptions(new PagingOptions

{

InferCollectionSegmentNameFromField = false

});

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#field-naming)Field naming
----------------------------------------------------------------------------------------------------------

Previously only the first character in a property or method name was lowercased in the schema. This worked fine in most cases, but if a name started with multiple uppercase characters or was all uppercase, the resulting field name was pretty weird. In this release we therefore changed how those field names are being inferred.

**Before**

FooBar --> fooBar

IPAddress --> iPAddress

PLZ --> pLZ

**After**

FooBar --> fooBar

IPAddress --> ipAddress

PLZ --> plz

If you need to retain the old naming behavior or the inferred field name doesn't match your expectation, you can still [explicitly override the name of the fields in question](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/object-types#naming).

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#ihttpresultserializer)IHttpResultSerializer
----------------------------------------------------------------------------------------------------------------------------

In this release we have replaced the `IHttpResultSerializer`, and consequently the `DefaultHttpResultSerializer`, with the `IHttpResponseFormatter` and `DefaultHttpResponseFormatter`.

Below you can see how you can port your custom HTTP status code generation logic to the new contract:

**Before**

C#

builder.Services.AddHttpResultSerializer<CustomHttpResultSerializer>();

public class CustomHttpResultSerializer : DefaultHttpResultSerializer

{

public override HttpStatusCode GetStatusCode(IExecutionResult result)

{

if (result is IQueryResult queryResult &&

queryResult.Errors?.Count > 0 &&

queryResult.Errors.Any(error => error.Code == "SOME_AUTH_ISSUE"))

{

return HttpStatusCode.Forbidden;

}

return base.GetStatusCode(result);

}

}

**After**

C#

builder.Services.AddHttpResponseFormatter<CustomHttpResponseFormatter>();

public class CustomHttpResponseFormatter : DefaultHttpResponseFormatter

{

protected override HttpStatusCode OnDetermineStatusCode(

IQueryResult result, FormatInfo format,

HttpStatusCode? proposedStatusCode)

{

if (result.Errors?.Count > 0 &&

result.Errors.Any(error => error.Code == "SOME_AUTH_ISSUE"))

{

return HttpStatusCode.Forbidden;

}

return base.OnDetermineStatusCode(result, format, proposedStatusCode);

}

}

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#http-transport)HTTP transport
--------------------------------------------------------------------------------------------------------------

With this release we adopted the latest [GraphQL over HTTP](https://github.com/graphql/graphql-over-http/blob/a1e6d8ca248c9a19eb59a2eedd988c204909ee3f/spec/GraphQLOverHTTP.md) specification changes.

Most notably the server now returns the `Content-Type: application/graphql-response+json;charset=utf-8` response header for requests without an `Accept: application/json` request header. This might break expectations of existing clients. Apollo Federation Gateway (`@apollo/gateway`) for example still expects responses from subgraphs to contain the `Content-Type: application/json` header.

If you need to support legacy clients that do not yet support the [GraphQL over HTTP](https://github.com/graphql/graphql-over-http/blob/a1e6d8ca248c9a19eb59a2eedd988c204909ee3f/spec/GraphQLOverHTTP.md) specification, you can

1.   Send the `Accept: application/json` header in requests from the legacy client
2.   Infer `application/json` as the `Accept` header value for requests with a missing `Accept` header or `Accept: */*`, by setting the `HttpTransportVersion` to `Legacy`:

C#

builder.Services.AddHttpResponseFormatter(new HttpResponseFormatterOptions {

HttpTransportVersion = HttpTransportVersion.Legacy

});

An `Accept` header with the value `application/json` will opt you out of the [GraphQL over HTTP](https://github.com/graphql/graphql-over-http/blob/a1e6d8ca248c9a19eb59a2eedd988c204909ee3f/spec/GraphQLOverHTTP.md) specification. The response `Content-Type` will now be `application/json` and a status code of 200 will be returned for every request, even if it had validation errors or a valid response could not be produced.

[Learn more about the HTTP transport](https://chillicream.com/docs/hotchocolate/v13/server/http-transport)

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#dataloaderattribute)DataLoaderAttribute
------------------------------------------------------------------------------------------------------------------------

Previously you might have annotated [DataLoaders](https://chillicream.com/docs/hotchocolate/v13/fetching-data/dataloader) in your resolver method signature with the `[DataLoader]` attribute. This attribute has been removed in v13 and can be safely removed from your code.

**Before**

C#

public async Task<User> GetUserByIdAsync(string id, [DataLoader] UserDataLoader loader)

=> await loader.LoadAsync(id);

**After**

C#

public async Task<User> GetUserByIdAsync(string id, UserDataLoader loader)

=> await loader.LoadAsync(id);

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#itopiceventreceiver--itopiceventsender)ITopicEventReceiver / ITopicEventSender
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Previously you could use any type as the topic for an event stream. In this release we are requiring the topic to be a `string`.

**Before**

C#

ITopicEventReceiver.SubscribeAsync<TTopic, TMessage>(TTopic topic,

CancellationToken cancellationToken);

ITopicEventSender.SendAsync<TTopic, TMessage>(TTopic topic, TMessage message,

CancellationToken cancellationToken)

**After**

C#

ITopicEventReceiver.SubscribeAsync<TMessage>(string topicName,

CancellationToken cancellationToken);

ITopicEventSender.SendAsync<TMessage>(string topicName, TMessage message,

CancellationToken cancellationToken)

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#topicattribute)TopicAttribute
--------------------------------------------------------------------------------------------------------------

Previously you might have annotated the `[Topic]` attribute on a method argument, to designate its runtime value as a dynamic topic. Now we no longer allow the attribute on arguments, but only on the method itself.

**Before**

C#

public class Subscription

{

[Subscribe]

public Book BookPublished([Topic] string author, [EventMessage] Book book)

=> book;

}

**After**

C#

public class Subscription

{

[Subscribe]

[Topic("{author}")]

public Book BookPublished(string author, [EventMessage] Book book)

=> book;

}

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#addinmemorysubscriptions--addredissubscriptions)AddInMemorySubscriptions / AddRedisSubscriptions
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We moved the extension methods from the `IServiceCollection` to our `IRequestExecutorBuilder`.

**Before**

C#

builder.Services.AddInMemorySubscriptions();

builder.Services.AddRedisSubscriptions();

**After**

C#

builder.Services

.AddGraphQLServer()

.AddInMemorySubscriptions()

.AddRedisSubscriptions();

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#defer--stream)@defer / @stream
---------------------------------------------------------------------------------------------------------------

`@defer` and `@stream` have now been disabled per default. If you want to continue using them, you have to opt-in now:

C#

services.AddGraphQLServer()

.ModifyOptions(o =>

{

o.EnableDefer = true;

o.EnableStream = true;

});

If your client is setting an `Accept` header value that doesn't include `multipart/mixed` or `text/event-stream`, the server will no longer produce a response, because the client is signaling that it can't handle a streamed response. In order for the server to produce a streamed response, you now need to either

1.   Omit the `Accept` header
2.   Send an `Accept` header with the value `*/*`, signaling that your client can handle any format
3.   Send an `Accept` header which includes `multipart/mixed` and/or `text/event-stream`

There have also been changes to the response format of streamed responses. You can checkout the currently proposed format [here](https://github.com/graphql/graphql-spec/blob/94363c9d5d8e53e91240ea3eabd32ff522f27a6b/spec/Section%207%20--%20Response.md).

Warning

The spec of these features is still evolving, so expect more changes on how the incremental payloads are being delivered.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#namestring)NameString
------------------------------------------------------------------------------------------------------

In this release we have abandoned the `NameString` in favor of simple `string`s. Most commonly you would encounter the `NameString` when defining names for fields or types. Since `string` was already implicitly converted to `NameString`, there shouldn't be any issues unless you were instantiating a `NameString` yourself.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#iresolvercontext--imiddlewarecontext)IResolverContext / IMiddlewareContext
-----------------------------------------------------------------------------------------------------------------------------------------------------------

Previously you could access properties like `Document` and `RootType` directly on the `IResolverContext` or the `IMiddlewareContext`. In this release we have moved these properties and they can now be accessed through the `Operation` property on the contexts. We have also removed the deprecated properties `Field` and `FieldSelection`.

`context.Document` -->`context.Operation.Document``context.RootType` -->`context.Operation.RootType``context.Field` -->`context.Selection.Field``context.FieldSelection` -->`context.Selection.SyntaxNode`

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#deprecations)Deprecations
----------------------------------------------------------------------------------------------------------

Things that will continue to function this release, but we encourage you to move away from.

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#scopedserviceattribute)ScopedServiceAttribute
------------------------------------------------------------------------------------------------------------------------------

In this release, we are deprecating the `[ScopedService]` attribute and encourage you to use `RegisterDbContext<T>(DbContextKind.Pooled)` instead.

Checkout [this part of our Entity Framework documentation](https://chillicream.com/docs/hotchocolate/v13/integrations/entity-framework#registerdbcontext) to learn how to register your `DbContext` with `DbContextKind.Pooled`.

Afterward you just need to update your resolvers:

**Before**

C#

[UseDbContext]

public IQueryable<User> GetUsers([ScopedService] MyDbContext dbContext)

=> dbContext.Users;

**After**

C#

public IQueryable<User> GetUsers(MyDbContext dbContext)

=> dbContext.Users;

If you've been using `[ScopedService]` without a pooled `DbContext`, you can recreate its behavior by switching it out for `[LocalState("FullName")]` (where `FullName` is the [full name](https://learn.microsoft.com/dotnet/api/system.type.fullname) of the method argument type).

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#subscribeandresolve)SubscribeAndResolve
------------------------------------------------------------------------------------------------------------------------

**Before**

C#

public class Subscription

{

[SubscribeAndResolve]

public ValueTask<ISourceStream<Book>> BookPublished(string author,

[Service] ITopicEventReceiver receiver)

{

var topic = $"{author}_PublishedBook";

return receiver.SubscribeAsync<string, Book>(topic);

}

}

**After**

C#

public class Subscription

{

public ValueTask<ISourceStream<Book>> SubscribeToPublishedBooks(

string author, ITopicEventReceiver receiver)

{

var topic = $"{author}_PublishedBook";

return receiver.SubscribeAsync<Book>(topic);

}

[Subscribe(With = nameof(SubscribeToPublishedBooks))]

public Book BookPublished(string author, [EventMessage] Book book)

=> book;

}

[](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#localvalue--scopedvalue--globalvalue)LocalValue / ScopedValue / GlobalValue
------------------------------------------------------------------------------------------------------------------------------------------------------------

We aligned the naming of state related APIs:

### [](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#iresolvercontext)IResolverContext

*   `IResolverContext.GetGlobalValue` -->`IResolverContext.GetGlobalStateOrDefault`
*   `IResolverContext.GetOrAddGlobalValue` -->`IResolverContext.GetOrSetGlobalState`
*   `IResolverContext.SetGlobalValue` -->`IResolverContext.SetGlobalState`
*   `IResolverContext.RemoveGlobalValue` -->_Removed_
*   `IResolverContext.GetScopedValue` -->`IResolverContext.GetScopedStateOrDefault`
*   `IResolverContext.GetOrAddScopedValue` -->`IResolverContext.GetOrSetScopedState`
*   `IResolverContext.SetScopedValue` -->`IResolverContext.SetScopedState`
*   `IResolverContext.RemoveScopedValue` -->`IResolverContext.RemoveScopedState`
*   `IResolverContext.GetLocalValue` -->`IResolverContext.GetLocalStateOrDefault`
*   `IResolverContext.GetOrAddLocalValue` -->`IResolverContext.GetOrSetLocalState`
*   `IResolverContext.SetLocalValue` -->`IResolverContext.SetLocalState`
*   `IResolverContext.RemoveLocalValue` -->`IResolverContext.RemoveLocalState`

### [](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13#operationrequestbuilder)OperationRequestBuilder

*   `OperationRequestBuilder.SetProperties` -->`OperationRequestBuilder.InitializeGlobalState`
*   `OperationRequestBuilder.SetProperty` -->`OperationRequestBuilder.SetGlobalState`
*   `OperationRequestBuilder.AddProperty` -->`OperationRequestBuilder.AddGlobalState`
*   `OperationRequestBuilder.TryAddProperty` -->`OperationRequestBuilder.TryAddGlobalState`
*   `OperationRequestBuilder.TryRemoveProperty` -->`OperationRequestBuilder.RemoveGlobalState`

Last updated on **2026-02-17** by**Tobias Tengler**
