# Source: https://chillicream.com/docs/hotchocolate/v14/server/introspection

Title: Introspection - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/server/introspection

Markdown Content:
This is documentation for **v14**, which is no longer actively maintained.

For up-to-date documentation, see the

[latest stable version](https://chillicream.com/docs/hotchocolate/v15/server/introspection).

Introspection is what enables GraphQL's rich tooling ecosystem as well powerful IDEs like [Nitro](https://chillicream.com/products/nitro) or GraphiQL.

Every GraphQL server exposes a `__schema` and `__type` field on the query type as well as an `__typename` field on each type. These fields are used to gain insights into the schema of our GraphQL server.

Using the `__schema` field, we could for example list the names of all types our GraphQL server contains:

GraphQL

{

__schema {

types {

name

}

}

}

We could also request the fields plus their arguments of a specific type using the `__type` field:

GraphQL

{

__type(name: "Book") {

fields {

name

args {

name

type {

name

}

}

}

}

}

The `__typename` field will most likely be the introspection feature we as regular developers will be using the most. When working with [unions](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/unions) for example it can tell us the name of the type that's being returned, allowing us to handle the result accordingly.

GraphQL

{

posts {

__typename

... on VideoPost {

videoUrl

}

... on TextPost {

text

}

}

}

While these fields can be useful to us, they are mainly intended for use in developer tooling and as regular developers we are unlikely required to write our own introspection queries on a daily basis.

[Learn more about introspection](https://graphql.org/learn/introspection)

[](https://chillicream.com/docs/hotchocolate/v14/server/introspection#disabling-introspection)Disabling introspection
---------------------------------------------------------------------------------------------------------------------

While introspection is a powerful feature that can tremendously improve our development workflow, it can also be used as an attack vector. A malicious user could for example request all details about all the types of our GraphQL server. Depending on the number of types this can degrade the performance of our GraphQL server. If our API should not be browsed by other developers we have the option to disable the introspection feature.

We can disable introspection by calling `AllowIntrospection()` with a `false` argument on the `IRequestExecutorBuilder`.

C#

builder.Services

.AddGraphQLServer()

.AllowIntrospection(false);

While clients can still issue introspection queries, Hot Chocolate will now return an error response.

But we most likely do not want to disable introspection while developing, so we can toggle it based on the current hosting environment.

C#

builder.Services

.AddGraphQLServer()

.AllowIntrospection(builder.Environment.IsDevelopment());

[](https://chillicream.com/docs/hotchocolate/v14/server/introspection#allowlisting-requests)Allowlisting requests
-----------------------------------------------------------------------------------------------------------------

We can allow introspection on a per-request basis, while keeping it disabled for the majority of requests. In order to do this we need to create a request interceptor and determine based on the request, i.e. the `HttpContext`, whether we want to allow introspection or not.

C#

public class IntrospectionInterceptor : DefaultHttpRequestInterceptor

{

public override ValueTask OnCreateAsync(HttpContext context,

IRequestExecutor requestExecutor, OperationRequestBuilder requestBuilder,

CancellationToken cancellationToken)

{

if (context.Request.Headers.ContainsKey("X-Allow-Introspection"))

{

requestBuilder.AllowIntrospection();

}

return base.OnCreateAsync(context, requestExecutor, requestBuilder,

cancellationToken);

}

}

C#

builder.Services

.AddGraphQLServer()

.AllowIntrospection(false)

.AddHttpRequestInterceptor<IntrospectionInterceptor>();

[Learn more about interceptors](https://chillicream.com/docs/hotchocolate/v14/server/interceptors)

[](https://chillicream.com/docs/hotchocolate/v14/server/introspection#custom-error-message)Custom error message
---------------------------------------------------------------------------------------------------------------

If a client tries to execute an introspection query whilst introspection is not allowed, he will receive an error message similar to the following:

JSON

{

"errors": [

{

"message": "Introspection is not allowed for the current request.",

"locations": [

{

"line": 2,

"column": 3

}

],

"extensions": {

"field": "__schema",

"code": "HC0046"

}

}

]

}

If we need to customize the error message, we can do so in our request interceptor as well.

C#

public class IntrospectionInterceptor : DefaultHttpRequestInterceptor

{

public override ValueTask OnCreateAsync(HttpContext context,

IRequestExecutor requestExecutor, OperationRequestBuilder requestBuilder,

CancellationToken cancellationToken)

{

if (context.Request.Headers.ContainsKey("X-Allow-Introspection"))

{

requestBuilder.AllowIntrospection();

}

else

{

requestBuilder.SetIntrospectionNotAllowedMessage(

"Missing `X-Allow-Introspection` header");

}

return base.OnCreateAsync(context, requestExecutor, requestBuilder,

cancellationToken);

}

}

Last updated on **2026-02-17** by**Tobias Tengler**
