# Source: https://chillicream.com/docs/hotchocolate/v14/server/endpoints

Title: Endpoints - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/server/endpoints

Markdown Content:
Hot Chocolate comes with a set of ASP.NET Core middleware used for making the GraphQL server available via HTTP and WebSockets. There are also middleware for hosting our GraphQL IDE [Nitro](https://chillicream.com/products/nitro) as well as an endpoint used for downloading the schema in its SDL representation.

[](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#mapgraphql)MapGraphQL
---------------------------------------------------------------------------------------

We can call `MapGraphQL()` on the `IEndpointRouteBuilder` to register all of the middleware a standard GraphQL server requires.

C#

app.UseRouting();

app.UseEndpoints(endpoints =>

{

endpoints.MapGraphQL();

});

If you are using .NET 6 Minimal APIs, you can also call `MapGraphQL()` on the `app` builder directly, since it implements `IEndpointRouteBuilder`:

C#

var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.MapGraphQL();

app.Run();

The middleware registered by `MapGraphQL` makes the GraphQL server available at `/graphql` per default.

We can customize the endpoint at which the GraphQL server is hosted like the following.

C#

endpoints.MapGraphQL("/my/graphql/endpoint");

Calling `MapGraphQL()` will enable the following functionality on the specified endpoint:

*   HTTP GET and HTTP POST GraphQL requests are handled (Multipart included)
*   WebSocket GraphQL requests are handled (if the ASP.NET Core WebSocket Middleware has been registered)
*   Including the query string `?sdl` after the endpoint will download the GraphQL schema
*   Accessing the endpoint from a browser will load our GraphQL IDE [Nitro](https://chillicream.com/products/nitro)

We can customize the combined middleware using `GraphQLServerOptions` as shown below or we can only include the parts of the middleware we need and configure them explicitly.

The following middleware are available:

*   [MapNitroApp](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#mapnitroapp)
*   [MapGraphQLHttp](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#mapgraphqlhttp)
*   [MapGraphQLWebsocket](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#mapgraphqlwebsocket)
*   [MapGraphQLSchema](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#mapgraphqlschema)

[](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#graphqlserveroptions)GraphQLServerOptions
-----------------------------------------------------------------------------------------------------------

We can influence the behavior of the middleware registered by `MapGraphQL` using `GraphQLServerOptions`.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#enableschemarequests)EnableSchemaRequests

C#

endpoints.MapGraphQL().WithOptions(new GraphQLServerOptions

{

EnableSchemaRequests = false

});

This setting controls whether the schema of the GraphQL server can be downloaded by appending `?sdl` to the endpoint.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#enablegetrequests)EnableGetRequests

C#

endpoints.MapGraphQL().WithOptions(new GraphQLServerOptions

{

EnableGetRequests = false

});

This setting controls whether the GraphQL server is able to handle GraphQL operations sent via the query string in a HTTP GET request.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#allowedgetoperations)AllowedGetOperations

C#

endpoints.MapGraphQL().WithOptions(new GraphQLServerOptions

{

AllowedGetOperations = AllowedGetOperations.Query

});

If [EnableGetRequests](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#enablegetrequests) is `true` we can control the allowed operations for HTTP GET requests using the `AllowedGetOperations` setting.

Per default only queries are accepted via HTTP GET. We can also allow mutations by setting `AllowedGetOperations` to `AllowedGetOperations.QueryAndMutation`.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#enablemultipartrequests)EnableMultipartRequests

C#

endpoints.MapGraphQL().WithOptions(new GraphQLServerOptions

{

EnableMultipartRequests = false

});

This setting controls whether the GraphQL server is able to handle HTTP Multipart forms, i.e. file uploads.

[Learn more about uploading files](https://chillicream.com/docs/hotchocolate/v14/server/files#upload-scalar)

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#tool)Tool

We can specify options for the Nitro using the `Tool` property.

We could for example only enable Nitro during development.

C#

app.UseRouting();

app.UseEndpoints(endpoints =>

{

endpoints.MapGraphQL().WithOptions(new GraphQLServerOptions

{

Tool = {

Enable = env.IsDevelopment()

}

});

});

[Learn more about possible GraphQLToolOptions](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#graphqltooloptions)

[](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#mapnitroapp)MapNitroApp
-----------------------------------------------------------------------------------------

We can call `MapNitroApp()` on the `IEndpointRouteBuilder` to serve [Nitro](https://chillicream.com/products/nitro) on a different endpoint than the actual GraphQL endpoint.

C#

app.UseRouting();

app.UseEndpoints(endpoints =>

{

endpoints.MapNitroApp("/graphql/ui");

});

This would make Nitro accessible via a Web Browser at the `/graphql/ui` endpoint.

[](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#graphqltooloptions)GraphQLToolOptions
-------------------------------------------------------------------------------------------------------

We can configure Nitro using `GraphQLToolOptions`.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#enable)Enable

C#

endpoints.MapNitroApp("/ui").WithOptions(new GraphQLToolOptions

{

Enable = false

});

This setting controls whether Nitro should be served or not.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#graphqlendpoint)GraphQLEndpoint

C#

endpoints.MapNitroApp("/ui").WithOptions(new GraphQLToolOptions

{

GraphQLEndpoint = "/my/graphql/endpoint"

});

This setting sets the GraphQL endpoint to use when creating new documents within Nitro.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#usebrowserurlasgraphqlendpoint)UseBrowserUrlAsGraphQLEndpoint

C#

endpoints.MapNitroApp("/ui").WithOptions(new GraphQLToolOptions

{

UseBrowserUrlAsGraphQLEndpoint = true

});

If set to `true` the current Web Browser URL is treated as the GraphQL endpoint when creating new documents within Nitro.

Warning

[GraphQLEndpoint](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#graphqlendpoint) takes precedence over this setting.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#document)Document

C#

endpoints.MapNitroApp("/ui").WithOptions(new GraphQLToolOptions

{

Document = "{ __typename }"

});

This setting allows us to set a default GraphQL document that should be a placeholder for each new document created using Nitro.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#httpmethod)HttpMethod

C#

endpoints.MapNitroApp("/ui").WithOptions(new GraphQLToolOptions

{

HttpMethod = DefaultHttpMethod.Get

});

This setting controls the default HTTP method used to execute GraphQL operations when creating new documents within Nitro.

C#

endpoints.MapNitroApp("/ui").WithOptions(new GraphQLToolOptions

{

HttpHeaders = new HeaderDictionary

{

{ "Content-Type", "application/json" }

}

});

This setting allows us to specify default HTTP Headers that will be added to each new document created using Nitro.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#includecookies)IncludeCookies

C#

endpoints.MapNitroApp("/ui").WithOptions(new GraphQLToolOptions

{

IncludeCookies = true

});

This setting specifies the default for including cookies in cross-origin when creating new documents within Nitro.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#title)Title

C#

endpoints.MapNitroApp("/ui").WithOptions(new GraphQLToolOptions

{

Title = "My GraphQL explorer"

});

This setting controls the tab name, when Nitro is opened inside of a Web Browser.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#disabletelemetry)DisableTelemetry

C#

endpoints.MapNitroApp("/ui").WithOptions(new GraphQLToolOptions

{

DisableTelemetry = true

});

This setting allows us to disable telemetry events.

### [](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#gatrackingid)GaTrackingId

C#

endpoints.MapNitroApp("/ui").WithOptions(new GraphQLToolOptions

{

GaTrackingId = "google-analytics-id"

});

This setting allows us to set a custom Google Analytics Id, which in turn allows us to gain insights into the usage of Nitro hosted as part of our GraphQL server.

The following information is collected:

| Name | Description |
| --- | --- |
| `deviceId` | Random string generated on a per-device basis |
| `operatingSystem` | Name of the operating system: `Windows`, `macOS`, `Linux`&`Unknown` |
| `userAgent` | `User-Agent` header |
| `applicationType` | The type of application: `app` (Electron) or `middleware` |
| `applicationVersion` | Version of Nitro |

[](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#mapgraphqlhttp)MapGraphQLHttp
-----------------------------------------------------------------------------------------------

We can call `MapGraphQLHttp()` on the `IEndpointRouteBuilder` to make our GraphQL server available via HTTP at a specific endpoint.

C#

app.UseRouting();

app.UseEndpoints(endpoints =>

{

endpoints.MapGraphQLHttp("/graphql/http");

});

With the above configuration we could now issue HTTP GET / POST requests against the `/graphql/http` endpoint.

[](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#graphqlhttpoptions)GraphQLHttpOptions
-------------------------------------------------------------------------------------------------------

The HTTP endpoint can be configured using `GraphQLHttpOptions`.

C#

endpoints.MapGraphQLHttp("/graphql/http").WithOptions(new GraphQLHttpOptions

{

EnableGetRequests = false

});

The `GraphQLHttpOptions` are the same as the `GraphQLServerOptions` except that there are no `Tool` and `EnableSchemaRequests` properties.

[Learn more about GraphQLServerOptions](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#graphqlserveroptions)

[](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#mapgraphqlwebsocket)MapGraphQLWebsocket
---------------------------------------------------------------------------------------------------------

We can call `MapGraphQLWebSocket()` on the `IEndpointRouteBuilder` to make our GraphQL server available via WebSockets at a specific endpoint.

C#

app.UseRouting();

app.UseEndpoints(endpoints =>

{

endpoints.MapGraphQLWebSocket("/graphql/ws");

});

With the above configuration we could now issue GraphQL subscription requests via WebSocket against the `/graphql/ws` endpoint.

[](https://chillicream.com/docs/hotchocolate/v14/server/endpoints#mapgraphqlschema)MapGraphQLSchema
---------------------------------------------------------------------------------------------------

We can call `MapGraphQLSchema()` on the `IEndpointRouteBuilder` to make our GraphQL schema available at a specific endpoint.

C#

app.UseRouting();

app.UseEndpoints(endpoints =>

{

endpoints.MapGraphQLSchema("/graphql/schema");

});

With the above configuration we could now download our `schema.graphql` file from the `/graphql/schema` endpoint.

Last updated on **2026-02-17** by**Tobias Tengler**
