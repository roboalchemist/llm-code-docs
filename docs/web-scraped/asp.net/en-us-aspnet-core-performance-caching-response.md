# Source: https://learn.microsoft.com/en-us/aspnet/core/performance/caching/response?view=aspnetcore-10.0

Title: Response caching in ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/performance/caching/response?view=aspnetcore-10.0

Markdown Content:
By [Rick Anderson](https://twitter.com/RickAndMSFT) and [Kirk Larkin](https://twitter.com/serpent5)

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/performance/caching/response/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

Response caching reduces the number of requests a client or proxy makes to a web server. Response caching also reduces the amount of work the web server performs to generate a response. Response caching is set in headers.

The [ResponseCache attribute](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/response?view=aspnetcore-10.0#responsecache-attribute) sets response caching headers. Clients and intermediate proxies should honor the headers for caching responses under [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111).

For server-side caching that follows the HTTP 1.1 Caching specification, use [Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0). The middleware can use the [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) properties to influence server-side caching behavior.

The Response caching middleware:

*   Enables caching server responses based on [HTTP cache headers](https://developer.mozilla.org/docs/Web/HTTP/Headers/Cache-Control). Implements the standard HTTP caching semantics. Caches based on HTTP cache headers like proxies do.
*   Is typically not beneficial for UI apps such as Razor Pages because browsers generally set request headers that prevent caching. [Output caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/output?view=aspnetcore-10.0), which is available in .NET 7 or later, benefits UI apps. With output caching, configuration decides what should be cached independently of HTTP headers.
*   May be beneficial for public GET or HEAD API requests from clients where the [Conditions for caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0#cfc) are met.

To test response caching, use [Fiddler](https://www.telerik.com/fiddler), or another tool that can explicitly set request headers. Setting headers explicitly is preferred for testing caching. For more information, see [Troubleshooting](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0#troubleshooting).

[RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) describes how Internet caches should behave. The primary HTTP header used for caching is [Cache-Control](https://www.rfc-editor.org/rfc/rfc9111#field.cache-control), which is used to specify cache directives. The directives control caching behavior as requests make their way from clients to servers and as responses make their way from servers back to clients. Requests and responses move through proxy servers, and proxy servers must also conform to the HTTP 1.1 Caching specification.

Common `Cache-Control` directives are shown in the following table.

| Directive | Action |
| --- | --- |
| [public](https://www.rfc-editor.org/rfc/rfc9111#cache-response-directive.public) | A cache may store the response. |
| [private](https://www.rfc-editor.org/rfc/rfc9111#cache-response-directive.private) | The response must not be stored by a shared cache. A private cache may store and reuse the response. |
| [max-age](https://www.rfc-editor.org/rfc/rfc9111#cache-response-directive.max-age) | The client doesn't accept a response whose age is greater than the specified number of seconds. Examples: `max-age=60` (60 seconds), `max-age=2592000` (1 month) |
| [no-cache](https://www.rfc-editor.org/rfc/rfc9111#cache-response-directive.no-cache) | **On requests**: A cache must not use a stored response to satisfy the request. The origin server regenerates the response for the client, and the middleware updates the stored response in its cache. **On responses**: The response must not be used for a subsequent request without validation on the origin server. |
| [no-store](https://www.rfc-editor.org/rfc/rfc9111#cache-response-directive.no-store) | **On requests**: A cache must not store the request. **On responses**: A cache must not store any part of the response. |

Other cache headers that play a role in caching are shown in the following table.

| Header | Function |
| --- | --- |
| [Age](https://www.rfc-editor.org/rfc/rfc9111#field.age) | An estimate of the amount of time in seconds since the response was generated or successfully validated at the origin server. |
| [Expires](https://www.rfc-editor.org/rfc/rfc9111#field.expires) | The time after which the response is considered stale. |
| [Pragma](https://www.rfc-editor.org/rfc/rfc9111#field.pragma) | Exists for backwards compatibility with HTTP/1.0 caches for setting `no-cache` behavior. If the `Cache-Control` header is present, the `Pragma` header is ignored. |
| [Vary](https://www.rfc-editor.org/rfc/rfc9110#field.vary) | Specifies that a cached response must not be sent unless all of the `Vary` header fields match in both the cached response's original request and the new request. |

[RFC 9111: HTTP Caching (Section 5.2. Cache-Control)](https://www.rfc-editor.org/rfc/rfc9111#field.cache-control) requires a cache to honor a valid `Cache-Control` header sent by the client. A client can make requests with a `no-cache` header value and force the server to generate a new response for every request.

Always honoring client `Cache-Control` request headers makes sense if you consider the goal of HTTP caching. Under the official specification, caching is meant to reduce the latency and network overhead of satisfying requests across a network of clients, proxies, and servers. It isn't necessarily a way to control the load on an origin server.

There's no developer control over this caching behavior when using the [Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0) because the middleware adheres to the official caching specification. Support for _output caching_ to better control server load was added in .NET 7. For more information, see [Output caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/overview?view=aspnetcore-10.0#output-caching).

The [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) specifies the parameters necessary for setting appropriate headers in response caching.

Warning

Disable caching for content that contains information for authenticated clients. Caching should only be enabled for content that doesn't change based on a user's identity or whether a user is signed in.

[VaryByQueryKeys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyquerykeys#microsoft-aspnetcore-mvc-cacheprofile-varybyquerykeys) varies the stored response by the values of the given list of query keys. When a single value of `*` is provided, the middleware varies responses by all request query string parameters.

[Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0) must be enabled to set the [VaryByQueryKeys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyquerykeys#microsoft-aspnetcore-mvc-cacheprofile-varybyquerykeys) property. Otherwise, a runtime exception is thrown. There isn't a corresponding HTTP header for the [VaryByQueryKeys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyquerykeys#microsoft-aspnetcore-mvc-cacheprofile-varybyquerykeys) property. The property is an HTTP feature handled by Response Caching Middleware. For the middleware to serve a cached response, the query string and query string value must match a previous request. For example, consider the sequence of requests and results shown in the following table:

| Request | Returned from |
| --- | --- |
| `http://example.com?key1=value1` | Server |
| `http://example.com?key1=value1` | Middleware |
| `http://example.com?key1=NewValue` | Server |

The first request is returned by the server and cached in middleware. The second request is returned by middleware because the query string matches the previous request. The third request isn't in the middleware cache because the query string value doesn't match a previous request.

The [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) is used to configure and create (via [IFilterFactory](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.filters.ifilterfactory)) a `Microsoft.AspNetCore.Mvc.Internal.ResponseCacheFilter`. The `ResponseCacheFilter` performs the work of updating the appropriate HTTP headers and features of the response. The filter:

*   Removes any existing headers for `Vary`, `Cache-Control`, and `Pragma`.
*   Writes out the appropriate headers based on the properties set in the [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute).
*   Updates the response caching HTTP feature if [VaryByQueryKeys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyquerykeys#microsoft-aspnetcore-mvc-cacheprofile-varybyquerykeys) is set.

This header is only written when the [VaryByHeader](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyheader#microsoft-aspnetcore-mvc-cacheprofile-varybyheader) property is set. The property set to the `Vary` property's value. The following sample uses the [VaryByHeader](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyheader#microsoft-aspnetcore-mvc-cacheprofile-varybyheader) property:

```
[ApiController]
public class TimeController : ControllerBase
{
    [Route("api/[controller]")]
    [HttpGet]
    [ResponseCache(VaryByHeader = "User-Agent", Duration = 30)]
    public ContentResult GetTime() => Content(
                      DateTime.Now.Millisecond.ToString());
```

View the response headers with Fiddler or another tool. The response headers include:

```
Cache-Control: public,max-age=30
Vary: User-Agent
```

The preceding code requires adding the Response Caching Middleware services [AddResponseCaching](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.responsecachingservicesextensions.addresponsecaching) to the service collection and configures the app to use the middleware with the [UseResponseCaching](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.responsecachingextensions.useresponsecaching) extension method.

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddControllers();
builder.Services.AddResponseCaching();

var app = builder.Build();

app.UseHttpsRedirection();

// UseCors must be called before UseResponseCaching
//app.UseCors();

app.UseResponseCaching();

app.UseAuthorization();

app.MapControllers();

app.Run();
```

[NoStore](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.nostore#microsoft-aspnetcore-mvc-cacheprofile-nostore) overrides most of the other properties. When this property is set to `true`, the `Cache-Control` header is set to `no-store`. If [Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location) is set to `None`:

*   `Cache-Control` is set to `no-store,no-cache`.
*   `Pragma` is set to `no-cache`.

If [NoStore](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.nostore#microsoft-aspnetcore-mvc-cacheprofile-nostore) is `false` and [Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location) is `None`, `Cache-Control`, and `Pragma` are set to `no-cache`.

[NoStore](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.nostore#microsoft-aspnetcore-mvc-cacheprofile-nostore) is typically set to `true` for error pages. The following produces response headers that instruct the client not to store the response.

```
[Route("api/[controller]/ticks")]
[HttpGet]
[ResponseCache(Location = ResponseCacheLocation.None, NoStore = true)]
public ContentResult GetTimeTicks() => Content(
                  DateTime.Now.Ticks.ToString());
```

The preceding code includes the following headers in the response:

```
Cache-Control: no-store,no-cache
Pragma: no-cache
```

To apply the [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) to all of the app's MVC controller or Razor Pages page responses, add it with an [MVC filter](https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/filters?view=aspnetcore-10.0) or [Razor Pages filter](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/filter?view=aspnetcore-10.0).

In an MVC app:

```
builder.Services.AddControllersWithViews().AddMvcOptions(options => 
    options.Filters.Add(
        new ResponseCacheAttribute
        {
            NoStore = true, 
            Location = ResponseCacheLocation.None
        }));
```

For an approach that applies to Razor Pages apps, see [Adding `ResponseCacheAttribute` to MVC global filter list does not apply to Razor Pages (dotnet/aspnetcore #18890)](https://github.com/dotnet/aspnetcore/issues/18890#issuecomment-584290537). The example provided in the issue comment was written for apps targeting ASP.NET Core prior to the release of [Minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis?view=aspnetcore-10.0) at 6.0. For 6.0 or later apps, change the service registration in the example to `builder.Services.AddSingleton...` for `Program.cs`.

To enable caching, [Duration](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.duration#microsoft-aspnetcore-mvc-cacheprofile-duration) must be set to a positive value and [Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location) must be either `Any` (the default) or `Client`. The framework sets the `Cache-Control` header to the location value followed by the `max-age` of the response.

[Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location)'s options of `Any` and `Client` translate into `Cache-Control` header values of `public` and `private`, respectively. As noted in the [NoStore and Location.None](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/response?view=aspnetcore-10.0#nostore-and-locationnone) section, setting [Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location) to `None` sets both `Cache-Control` and `Pragma` headers to `no-cache`.

`Location.Any` (`Cache-Control` set to `public`) indicates that the _client or any intermediate proxy_ may cache the value, including [Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0).

`Location.Client` (`Cache-Control` set to `private`) indicates that _only the client_ may cache the value. No intermediate cache should cache the value, including [Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0).

Cache control headers provide guidance to clients and intermediary proxies when and how to cache responses. There's no guarantee that clients and proxies will honor [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111). [Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0) always follows the caching rules laid out by the specification.

The following example shows the headers produced by setting [Duration](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.duration#microsoft-aspnetcore-mvc-cacheprofile-duration) and leaving the default [Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location) value:

```
[Route("api/[controller]/ms")]
[HttpGet]
[ResponseCache(Duration = 10, Location = ResponseCacheLocation.Any, NoStore = false)]
public ContentResult GetTimeMS() => Content(
                  DateTime.Now.Millisecond.ToString());
```

The preceding code includes the following headers in the response:

```
Cache-Control: public,max-age=10
```

Instead of duplicating response cache settings on many controller action attributes, cache profiles can be configured as options when setting up MVC/Razor Pages. Values found in a referenced cache profile are used as the defaults by the [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) and are overridden by any properties specified on the attribute.

The following example shows a 30 second cache profile:

```
using Microsoft.AspNetCore.Mvc;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddResponseCaching();
builder.Services.AddControllers(options =>
{
    options.CacheProfiles.Add("Default30",
        new CacheProfile()
        {
            Duration = 30
        });
});

var app = builder.Build();

app.UseHttpsRedirection();

// UseCors must be called before UseResponseCaching
//app.UseCors();

app.UseResponseCaching();

app.UseAuthorization();

app.MapControllers();

app.Run();
```

The following code references the `Default30` cache profile:

```
[ApiController]
[ResponseCache(CacheProfileName = "Default30")]
public class Time2Controller : ControllerBase
{
    [Route("api/[controller]")]
    [HttpGet]
    public ContentResult GetTime() => Content(
                      DateTime.Now.Millisecond.ToString());

    [Route("api/[controller]/ticks")]
    [HttpGet]
    public ContentResult GetTimeTicks() => Content(
                      DateTime.Now.Ticks.ToString());
}
```

The resulting header response by the `Default30` cache profile includes:

```
Cache-Control: public,max-age=30
```

The [`[ResponseCache]`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) attribute can be applied to:

*   Razor Pages: Attributes can't be applied to handler methods. Browsers used with UI apps prevent response caching.
*   MVC controllers.
*   MVC action methods: Method-level attributes override the settings specified in class-level attributes.

The following code applies the `[ResponseCache]` attribute at the controller level and method level:

```
[ApiController]
[ResponseCache(VaryByHeader = "User-Agent", Duration = 30)]
public class Time4Controller : ControllerBase
{
    [Route("api/[controller]")]
    [HttpGet]
    public ContentResult GetTime() => Content(
                      DateTime.Now.Millisecond.ToString());

    [Route("api/[controller]/ticks")]
    [HttpGet]
    public ContentResult GetTimeTicks() => Content(
                  DateTime.Now.Ticks.ToString());

    [Route("api/[controller]/ms")]
    [HttpGet]
    [ResponseCache(Duration = 10, Location = ResponseCacheLocation.Any, NoStore = false)]
    public ContentResult GetTimeMS() => Content(
                      DateTime.Now.Millisecond.ToString());
}
```

*   [Storing Responses in Caches](https://www.rfc-editor.org/rfc/rfc9111.html#name-storing-responses-in-caches)
*   [Cache-Control](https://www.rfc-editor.org/rfc/rfc9111.html#field.cache-control)
*   [Cache in-memory in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/memory?view=aspnetcore-10.0)
*   [Distributed caching in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/distributed?view=aspnetcore-10.0)
*   [Detect changes with change tokens in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/change-tokens?view=aspnetcore-10.0)
*   [Response Caching Middleware in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0)
*   [Cache Tag Helper in ASP.NET Core MVC](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/tag-helpers/built-in/cache-tag-helper?view=aspnetcore-10.0)
*   [Distributed Cache Tag Helper in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/tag-helpers/built-in/distributed-cache-tag-helper?view=aspnetcore-10.0)

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/performance/caching/response/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

Response caching reduces the number of requests a client or proxy makes to a web server. Response caching also reduces the amount of work the web server performs to generate a response. Response caching is controlled by headers that specify how you want client, proxy, and middleware to cache responses.

The [`[ResponseCache]`](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/response?view=aspnetcore-10.0#responsecache-attribute) participates in setting response caching headers. Clients and intermediate proxies should honor the headers for caching responses under [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111).

For server-side caching that follows the HTTP 1.1 Caching specification, use [Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0). The middleware can use the [`[ResponseCache]`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) properties to set server-side caching headers.

[RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111) describes how Internet caches should behave. The primary HTTP header used for caching is [Cache-Control](https://www.rfc-editor.org/rfc/rfc9111#field.cache-control), which is used to specify cache _directives_. The directives control caching behavior as requests make their way from clients to servers and as responses make their way from servers back to clients. Requests and responses move through proxy servers, and proxy servers must also conform to the HTTP 1.1 Caching specification.

Common `Cache-Control` directives are shown in the following table.

| Directive | Action |
| --- | --- |
| [public](https://www.rfc-editor.org/rfc/rfc9111#cache-response-directive.public) | A cache may store the response. |
| [private](https://www.rfc-editor.org/rfc/rfc9111#cache-response-directive.private) | The response must not be stored by a shared cache. A private cache may store and reuse the response. |
| [max-age](https://www.rfc-editor.org/rfc/rfc9111#cache-response-directive.max-age) | The client doesn't accept a response whose age is greater than the specified number of seconds. Examples: `max-age=60` (60 seconds), `max-age=2592000` (1 month) |
| [no-cache](https://www.rfc-editor.org/rfc/rfc9111#cache-response-directive.no-cache) | **On requests**: A cache must not use a stored response to satisfy the request. The origin server regenerates the response for the client, and the middleware updates the stored response in its cache. **On responses**: The response must not be used for a subsequent request without validation on the origin server. |
| [no-store](https://www.rfc-editor.org/rfc/rfc9111#cache-response-directive.no-store) | **On requests**: A cache must not store the request. **On responses**: A cache must not store any part of the response. |

Other cache headers that play a role in caching are shown in the following table.

| Header | Function |
| --- | --- |
| [Age](https://www.rfc-editor.org/rfc/rfc9111#field.age) | An estimate of the amount of time in seconds since the response was generated or successfully validated at the origin server. |
| [Expires](https://www.rfc-editor.org/rfc/rfc9111#field.expires) | The time after which the response is considered stale. |
| [Pragma](https://www.rfc-editor.org/rfc/rfc9111#field.pragma) | Exists for backwards compatibility with HTTP/1.0 caches for setting `no-cache` behavior. If the `Cache-Control` header is present, the `Pragma` header is ignored. |
| [Vary](https://www.rfc-editor.org/rfc/rfc9110#field.vary) | Specifies that a cached response must not be sent unless all of the `Vary` header fields match in both the cached response's original request and the new request. |

[RFC 9111: HTTP Caching (Section 5.2. Cache-Control)](https://www.rfc-editor.org/rfc/rfc9111#field.cache-control) requires a cache to honor a valid `Cache-Control` header sent by the client. A client can make requests with a `no-cache` header value and force the server to generate a new response for every request.

Always honoring client `Cache-Control` request headers makes sense if you consider the goal of HTTP caching. Under the official specification, caching is meant to reduce the latency and network overhead of satisfying requests across a network of clients, proxies, and servers. It isn't necessarily a way to control the load on an origin server.

There's no developer control over this caching behavior when using the [Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0) because the middleware adheres to the official caching specification. Support for _output caching_ to better control server load is a design proposal for a future release of ASP.NET Core. For more information, see [Add support for Output Caching (dotnet/aspnetcore #27387)](https://github.com/dotnet/aspnetcore/issues/27387).

In-memory caching uses server memory to store cached data. This type of caching is suitable for a single server or multiple servers using session affinity. Session affinity is also known as _sticky sessions_. Session affinity means that the requests from a client are always routed to the same server for processing.

For more information, see [Cache in-memory in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/memory?view=aspnetcore-10.0) and [Troubleshoot Azure Application Gateway session affinity issues](https://learn.microsoft.com/en-us/azure/application-gateway/how-to-troubleshoot-application-gateway-session-affinity-issues).

Use a distributed cache to store data in memory when the app is hosted in a cloud or server farm. The cache is shared across the servers that process requests. A client can submit a request that's handled by any server in the group if cached data for the client is available. ASP.NET Core works with SQL Server, [Redis](https://www.nuget.org/packages/Microsoft.Extensions.Caching.StackExchangeRedis), [Postgres](https://www.nuget.org/packages/Microsoft.Extensions.Caching.Postgres), and [NCache](https://www.nuget.org/packages/Alachisoft.NCache.OpenSource.SDK/) distributed caches.

For more information, see [Distributed caching in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/distributed?view=aspnetcore-10.0).

Cache the content from an MVC view or Razor Page with the Cache Tag Helper. The Cache Tag Helper uses in-memory caching to store data.

For more information, see [Cache Tag Helper in ASP.NET Core MVC](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/tag-helpers/built-in/cache-tag-helper?view=aspnetcore-10.0).

Cache the content from an MVC view or Razor Page in distributed cloud or web farm scenarios with the Distributed Cache Tag Helper. The Distributed Cache Tag Helper uses SQL Server, [Redis](https://www.nuget.org/packages/Microsoft.Extensions.Caching.StackExchangeRedis), or [NCache](https://www.nuget.org/packages/Alachisoft.NCache.OpenSource.SDK/) to store data.

For more information, see [Distributed Cache Tag Helper in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/tag-helpers/built-in/distributed-cache-tag-helper?view=aspnetcore-10.0).

The [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) specifies the parameters necessary for setting appropriate headers in response caching.

Warning

Disable caching for content that contains information for authenticated clients. Caching should only be enabled for content that doesn't change based on a user's identity or whether a user is signed in.

[VaryByQueryKeys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyquerykeys#microsoft-aspnetcore-mvc-cacheprofile-varybyquerykeys) varies the stored response by the values of the given list of query keys. When a single value of `*` is provided, the middleware varies responses by all request query string parameters.

[Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0) must be enabled to set the [VaryByQueryKeys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyquerykeys#microsoft-aspnetcore-mvc-cacheprofile-varybyquerykeys) property. Otherwise, a runtime exception is thrown. There isn't a corresponding HTTP header for the [VaryByQueryKeys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyquerykeys#microsoft-aspnetcore-mvc-cacheprofile-varybyquerykeys) property. The property is an HTTP feature handled by Response Caching Middleware. For the middleware to serve a cached response, the query string and query string value must match a previous request. For example, consider the sequence of requests and results shown in the following table.

| Request | Result |
| --- | --- |
| `http://example.com?key1=value1` | Returned from the server. |
| `http://example.com?key1=value1` | Returned from middleware. |
| `http://example.com?key1=value2` | Returned from the server. |

The first request is returned by the server and cached in middleware. The second request is returned by middleware because the query string matches the previous request. The third request isn't in the middleware cache because the query string value doesn't match a previous request.

The [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) is used to configure and create (via [IFilterFactory](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.filters.ifilterfactory)) a `Microsoft.AspNetCore.Mvc.Internal.ResponseCacheFilter`. The `ResponseCacheFilter` performs the work of updating the appropriate HTTP headers and features of the response. The filter:

*   Removes any existing headers for `Vary`, `Cache-Control`, and `Pragma`.
*   Writes out the appropriate headers based on the properties set in the [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute).
*   Updates the response caching HTTP feature if [VaryByQueryKeys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyquerykeys#microsoft-aspnetcore-mvc-cacheprofile-varybyquerykeys) is set.

This header is only written when the [VaryByHeader](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyheader#microsoft-aspnetcore-mvc-cacheprofile-varybyheader) property is set. The property set to the `Vary` property's value. The following sample uses the [VaryByHeader](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.varybyheader#microsoft-aspnetcore-mvc-cacheprofile-varybyheader) property:

```
[ResponseCache(VaryByHeader = "User-Agent", Duration = 30)]
public class Cache1Model : PageModel
{
```

Using the sample app, view the response headers with the browser's network tools. The following response headers are sent with the Cache1 page response:

```
Cache-Control: public,max-age=30
Vary: User-Agent
```

[NoStore](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.nostore#microsoft-aspnetcore-mvc-cacheprofile-nostore) overrides most of the other properties. When this property is set to `true`, the `Cache-Control` header is set to `no-store`. If [Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location) is set to `None`:

*   `Cache-Control` is set to `no-store,no-cache`.
*   `Pragma` is set to `no-cache`.

If [NoStore](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.nostore#microsoft-aspnetcore-mvc-cacheprofile-nostore) is `false` and [Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location) is `None`, `Cache-Control`, and `Pragma` are set to `no-cache`.

[NoStore](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.nostore#microsoft-aspnetcore-mvc-cacheprofile-nostore) is typically set to `true` for error pages. The Cache2 page in the sample app produces response headers that instruct the client not to store the response.

```
[ResponseCache(Duration = 0, Location = ResponseCacheLocation.None, NoStore = true)]
public class Cache2Model : PageModel
{
```

The sample app returns the Cache2 page with the following headers:

```
Cache-Control: no-store,no-cache
Pragma: no-cache
```

To apply the [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) to all of the app's MVC controller or Razor Pages page responses, add it with an [MVC filter](https://learn.microsoft.com/en-us/aspnet/core/mvc/controllers/filters?view=aspnetcore-10.0) or [Razor Pages filter](https://learn.microsoft.com/en-us/aspnet/core/razor-pages/filter?view=aspnetcore-10.0).

In an MVC app:

```
services.AddMvc().AddMvcOptions(options => 
    options.Filters.Add(
        new ResponseCacheAttribute
        {
            NoStore = true, 
            Location = ResponseCacheLocation.None
        }));
```

For an approach that applies to Razor Pages apps, see [Adding `ResponseCacheAttribute` to MVC global filter list does not apply to Razor Pages (dotnet/aspnetcore #18890)](https://github.com/dotnet/aspnetcore/issues/18890#issuecomment-584290537).

To enable caching, [Duration](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.duration#microsoft-aspnetcore-mvc-cacheprofile-duration) must be set to a positive value and [Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location) must be either `Any` (the default) or `Client`. The framework sets the `Cache-Control` header to the location value followed by the `max-age` of the response.

[Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location)'s options of `Any` and `Client` translate into `Cache-Control` header values of `public` and `private`, respectively. As noted in the [NoStore and Location.None](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/response?view=aspnetcore-10.0#nostore-and-locationnone) section, setting [Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location) to `None` sets both `Cache-Control` and `Pragma` headers to `no-cache`.

`Location.Any` (`Cache-Control` set to `public`) indicates that the _client or any intermediate proxy_ may cache the value, including [Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0).

`Location.Client` (`Cache-Control` set to `private`) indicates that _only the client_ may cache the value. No intermediate cache should cache the value, including [Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0).

Cache control headers merely provide guidance to clients and intermediary proxies when and how to cache responses. There's no guarantee that clients and proxies will honor [RFC 9111: HTTP Caching](https://www.rfc-editor.org/rfc/rfc9111). [Response Caching Middleware](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0) always follows the caching rules laid out by the specification.

The following example shows the Cache3 page model from the sample app and the headers produced by setting [Duration](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.duration#microsoft-aspnetcore-mvc-cacheprofile-duration) and leaving the default [Location](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.cacheprofile.location#microsoft-aspnetcore-mvc-cacheprofile-location) value:

```
[ResponseCache(Duration = 10, Location = ResponseCacheLocation.Any, NoStore = false)]
public class Cache3Model : PageModel
{
```

The sample app returns the Cache3 page with the following header:

```
Cache-Control: public,max-age=10
```

Instead of duplicating response cache settings on many controller action attributes, cache profiles can be configured as options when setting up MVC/Razor Pages in `Startup.ConfigureServices`. Values found in a referenced cache profile are used as the defaults by the [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) and are overridden by any properties specified on the attribute.

Set up a cache profile. The following example shows a 30 second cache profile in the sample app's `Startup.ConfigureServices`:

```
public void ConfigureServices(IServiceCollection services)
{
    services.AddRazorPages();
    services.AddMvc(options =>
    {
        options.CacheProfiles.Add("Default30",
            new CacheProfile()
            {
                Duration = 30
            });
    });
}
```

The sample app's Cache4 page model references the `Default30` cache profile:

```
[ResponseCache(CacheProfileName = "Default30")]
public class Cache4Model : PageModel
{
```

The [ResponseCacheAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.responsecacheattribute) can be applied to:

*   Razor Pages: Attributes can't be applied to handler methods.
*   MVC controllers.
*   MVC action methods: Method-level attributes override the settings specified in class-level attributes.

The resulting header applied to the Cache4 page response by the `Default30` cache profile:

```
Cache-Control: public,max-age=30
```

*   [Storing Responses in Caches](https://www.rfc-editor.org/rfc/rfc9111#name-storing-responses-in-caches)
*   [RFC 9111: HTTP Caching (Section 5.2. Cache-Control)](https://www.rfc-editor.org/rfc/rfc9111#field.cache-control)
*   [Cache in-memory in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/memory?view=aspnetcore-10.0)
*   [Distributed caching in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/distributed?view=aspnetcore-10.0)
*   [Detect changes with change tokens in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/change-tokens?view=aspnetcore-10.0)
*   [Response Caching Middleware in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0)
*   [Cache Tag Helper in ASP.NET Core MVC](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/tag-helpers/built-in/cache-tag-helper?view=aspnetcore-10.0)
*   [Distributed Cache Tag Helper in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/mvc/views/tag-helpers/built-in/distributed-cache-tag-helper?view=aspnetcore-10.0)
