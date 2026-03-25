# Source: https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection

Title: Dependency injection - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection

Markdown Content:
If you are unfamiliar with the term "dependency injection", we recommend the following articles to get you started:

*   [Dependency injection in .NET](https://docs.microsoft.com/dotnet/core/extensions/dependency-injection)
*   [Dependency injection in ASP.NET Core](https://docs.microsoft.com/aspnet/core/fundamentals/dependency-injection)

Dependency injection with Hot Chocolate works almost the same as with a regular ASP.NET Core application. For instance, nothing changes about how you add services to the dependency injection container.

C#

var builder = WebApplication.CreateBuilder(args);

builder.Services

.AddSingleton<MySingletonService>()

.AddScoped<MyScopedService>()

.AddTransient<MyTransientService>();

Injecting these services into Hot Chocolate resolvers works in a similar way to [Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/parameter-binding), in that the parameters are bound implicitly when the type is configured as a service, without the need to apply an attribute.

[](https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection#resolver-injection)Resolver injection
------------------------------------------------------------------------------------------------------------------

The correct way to inject dependencies into your resolvers is by injecting them into your resolver method as an argument.

[Learn more about why constructor injection into GraphQL types is a bad idea](https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection#constructor-injection)

Injecting dependencies at the method-level has a couple of benefits:

*   The resolver can be optimized and the execution strategy can be adjusted depending on the needs of a specific service.
*   Refactoring, i.e. moving the resolver method between classes, becomes easier, since the resolver does not have any dependencies on its outer class.

In the following example, `BookService` will be injected automatically when registered as a service in the DI container.

C#

[QueryType]

public static class Query

{

public static async Task<Book?> GetBookByIdAsync(

Guid id,

BookService bookService)

{

return await bookService.GetBookAsync(id);

}

}

[](https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection#default-scope)Default scope
--------------------------------------------------------------------------------------------------------

By default, scoped services are scoped to the resolver for queries and DataLoaders, and to the current request for mutations. This means that each execution of a query or DataLoader that accepts a scoped service will receive a **separate** instance, avoiding threading issues with services that do not support multi-threading (f.e. Entity Framework DbContexts). Since mutations are executed sequentially, they receive the **same** request-scoped instance.

These defaults can be changed globally as follows:

C#

builder.Services

.AddGraphQLServer()

.ModifyOptions(o =>

{

o.DefaultQueryDependencyInjectionScope =

DependencyInjectionScope.Resolver;

o.DefaultMutationDependencyInjectionScope =

DependencyInjectionScope.Request;

});

They can also be overridden on a per-resolver basis:

C#

[QueryType]

public static class Query

{

[UseRequestScope]

public static async Task<Book?> GetBookByIdAsync(

Guid id,

BookService bookService) =>

}

[](https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection#constructor-injection)Constructor injection
------------------------------------------------------------------------------------------------------------------------

When starting out with Hot Chocolate you might be inclined to inject dependencies into your GraphQL type definitions using the constructor.

You should **avoid** doing this, because:

*   GraphQL type definitions are singleton and your injected dependency will therefore also become a singleton.
*   Access to this dependency can not be synchronized by Hot Chocolate during the execution of a request.

Of course this does not apply within your own dependencies. Your `ServiceA` class can still inject `ServiceB` through the constructor.

When you need to access dependency injection services in your resolvers, try to stick to the [method-level dependency injection approach](https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection#resolver-injection) outlined above.

[](https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection#keyed-services)Keyed services
----------------------------------------------------------------------------------------------------------

A keyed service registered like this:

C#

builder.Services.AddKeyedScoped<BookService>("bookService");

... can be accessed in your resolver with the following code:

C#

[QueryType]

public static class Query

{

public static async Task<Book?> GetBookByIdAsync(

Guid id,

[Service("bookService")] BookService bookService)

{

return await bookService.GetBookAsync(id);

}

}

[](https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection#switching-the-service-provider)Switching the service provider
------------------------------------------------------------------------------------------------------------------------------------------

While Hot Chocolate's internals rely heavily on Microsoft's dependency injection container, you are not required to manage your own dependencies using this container. By default Hot Chocolate uses the request-scoped [`HttpContext.RequestServices`](https://docs.microsoft.com/dotnet/api/microsoft.aspnetcore.http.httpcontext.requestservices)`IServiceProvider` to provide services to your resolvers.

You can switch out the service provider used for GraphQL requests, as long as your dependency injection container implements the [`IServiceProvider`](https://docs.microsoft.com/dotnet/api/system.iserviceprovider) interface.

To switch out the service provider you need to call [`SetServices`](https://chillicream.com/docs/hotchocolate/v14/server/interceptors#setservices) on the [`OperationRequestBuilder`](https://chillicream.com/docs/hotchocolate/v14/server/interceptors#operationrequestbuilder) in both the [`IHttpRequestInterceptor`](https://chillicream.com/docs/hotchocolate/v14/server/interceptors#ihttprequestinterceptor) and the [`ISocketSessionInterceptor`](https://chillicream.com/docs/hotchocolate/v14/server/interceptors#isocketsessioninterceptor).

C#

public sealed class HttpRequestInterceptor

: DefaultHttpRequestInterceptor

{

public override async ValueTask OnCreateAsync(

HttpContext context,

IRequestExecutor requestExecutor,

OperationRequestBuilder requestBuilder,

CancellationToken cancellationToken)

{

await base.OnCreateAsync(

context,

requestExecutor,

requestBuilder,

cancellationToken);

requestBuilder.SetServices(YOUR_SERVICE_PROVIDER);

}

}

public sealed class SocketSessionInterceptor

: DefaultSocketSessionInterceptor

{

public override async ValueTask OnRequestAsync(

ISocketConnection connection,

OperationRequestBuilder requestBuilder,

CancellationToken cancellationToken)

{

await base.OnRequestAsync(

connection,

requestBuilder,

cancellationToken);

requestBuilder.SetServices(YOUR_SERVICE_PROVIDER);

}

}

You also need to register these interceptors for them to take effect.

C#

builder.Services

.AddGraphQLServer()

.AddHttpRequestInterceptor<HttpRequestInterceptor>()

.AddSocketSessionInterceptor<SocketSessionInterceptor>();

[Learn more about interceptors](https://chillicream.com/docs/hotchocolate/v14/server/interceptors)

Last updated on **2026-02-17** by**Tobias Tengler**
