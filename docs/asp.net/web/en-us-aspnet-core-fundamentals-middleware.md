# Source: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0

Title: ASP.NET Core Middleware

URL Source: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0

Markdown Content:
Middleware is software that's assembled into an app pipeline to handle requests and responses. Each middleware:

*   Chooses whether to pass the request to the next middleware in the pipeline.
*   Can perform work before and after the next middleware in the pipeline.

Request delegates are used to build the request pipeline. The request delegates handle each HTTP request.

Request delegates are configured using [Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.runextensions.run), [Map](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.mapextensions.map), and [Use](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.useextensions.use) extension methods. An individual request delegate can be specified inline as an anonymous method (called inline middleware) or defined in a reusable class. These inline anonymous methods or reusable classes are called _middleware_ or _middleware components_. Each middleware in the request pipeline is responsible for invoking the next middleware in the pipeline or short-circuiting the pipeline. When a middleware short-circuits, it's called a _terminal middleware_ because it prevents further middleware from processing the request.

For more information on the difference between request pipelines in ASP.NET Core and ASP.NET 4.x with additional middleware samples, see [Migrate HTTP modules to ASP.NET Core middleware](https://learn.microsoft.com/en-us/aspnet/core/migration/fx-to-core/areas/http-modules?view=aspnetcore-10.0).

Server-side Blazor, Razor Pages, and MVC process browser requests on the server with middleware. The guidance in this article applies to these types of apps.

Standalone Blazor WebAssembly apps run entirely on the client and don't process requests with a middleware pipeline. The guidance in this article doesn't apply to standalone Blazor WebAssembly apps.

For more information on ASP.NET Core's compiler platform analyzers that inspect app code for quality, see [Code analysis in ASP.NET Core apps](https://learn.microsoft.com/en-us/aspnet/core/diagnostics/code-analysis?view=aspnetcore-10.0).

The ASP.NET Core request pipeline consists of a sequence of request delegates, called one after the other. The following diagram demonstrates the concept. The thread of execution follows the black arrows.

![Image 1: Request processing pattern showing a request arriving, processing through three middlewares, and the response leaving the app. Each middleware runs its logic and hands off the request to the next middleware at the next() statement. After the third middleware processes the request, the request passes back through the prior two middlewares in reverse order for additional processing after their next() statements before leaving the app as a response to the client.](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/index/_static/request-delegate-pipeline.png?view=aspnetcore-10.0)

Each delegate can perform operations before and after the next delegate. Exception-handling delegates should be called early in the pipeline, so they can catch exceptions that occur in later stages of the pipeline.

Note

To experiment locally with the code examples in this section, create an ASP.NET Core app using the **ASP.NET Core Empty** project template. If using the .NET CLI, the template short name is `web` (`dotnet new web`).

The simplest ASP.NET Core app calls [Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.runextensions.run) to set up a single terminal middleware as an anonymous function request delegate to handle requests without a request pipeline.

In the following example:

*   The call to [RunExtensions.Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.runextensions.run) is invoked on every request and writes "Hello world!" to the response.
*   The call to [WebApplication.Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication.run) at the end of the code block runs the app and blocks the calling thread until host shutdown.

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.Run(async context =>
{
    await context.Response.WriteAsync("Hello world!");
});

app.Run();
```

Response when accessing the app in a browser at its launch URL:

> Hello world!

Chain multiple request delegates together with [Use](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.useextensions.use). The `next` parameter represents the next delegate in the pipeline. You can typically perform actions both before and after the `next` delegate.

The following example demonstrates:

*   Two [Use](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.useextensions.use) calls, each writing to the console: 
    *   Where work can be performed that can write to the response (`context.Response`, [HttpResponse](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpresponse)).
    *   Where work can be performed that doesn't write to the response after the `next` parameter is invoked.

*   A terminal request delegate with a call to [RunExtensions.Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.runextensions.run) that writes "Hello world!" to the response.
*   A final [Use](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.useextensions.use) call, which never executes because it follows the [Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.runextensions.run) terminal request delegate.
*   A call to [WebApplication.Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplication.run) at the end of the code block to run the app and block the calling thread until host shutdown.

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.Use(async (context, next) =>
{
    Console.WriteLine("Work that can write to the response. (1)");
    await next.Invoke(context);
    Console.WriteLine("Work that doesn't write to the response. (1)");
});

app.Use(async (context, next) =>
{
    Console.WriteLine("Work that can write to the response. (2)");
    await next.Invoke(context);
    Console.WriteLine("Work that doesn't write to the response. (2)");
});

app.Run(async context =>
{
    await context.Response.WriteAsync("Hello world!");
});

app.Use(async (context, next) =>
{
    Console.WriteLine("This statement isn't reached. (3)");
    await next.Invoke(context);
    Console.WriteLine("This statement isn't reached. (3)");
});

app.Run();
```

In the app's console window when the app is run:

> Work that can write to the response. (1)
> 
> Work that can write to the response. (2)
> 
> Work that doesn't write to the response. (2)
> 
> Work that doesn't write to the response. (1)

_Short-circuiting_ the request pipeline is often desirable because it avoids unnecessary work. For example, [Static File Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0) can act as a _terminal middleware_ by processing a request for a static file and short-circuiting the rest of the pipeline. Middleware added to the pipeline before the terminal middleware still processes code after their `next.Invoke` statements. If you don't plan to call `next.Invoke` because your goal is to terminate the pipeline, use a [`Run` delegate](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0#run-delegate) instead of calling the [Use](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.useextensions.use) extension method.

Don't call `next.Invoke` during or after the response is sent to the client. After an [HttpResponse](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpresponse) is started, changes result in an exception. For example, [setting headers or a response status code throw an exception](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices?view=aspnetcore-10.0#do-not-modify-the-status-code-or-headers-after-the-response-body-has-started) after the response starts. Writing to the response body after calling `next` may:

*   Cause a protocol violation, such as writing more bytes to the response than the stated response's content length (`Content-Length` header value).
*   Corrupt the body format, such as writing an HTML footer to a CSS file.

To determine if the response has started, check the value of [HasStarted](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpresponse.hasstarted).

For more information, see [Short-circuit middleware after routing](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing?view=aspnetcore-10.0#short-circuit-middleware-after-routing).

A [Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.runextensions.run) delegate doesn't receive a `next` parameter. The first `Run` delegate always terminates the pipeline. `Run` is also a convention, and some middleware may expose `Run` methods that execute at the end of the pipeline.

Any [Use](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.useextensions.use) or [Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.runextensions.run) delegates after the first [Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.runextensions.run) delegate aren't called.

[Map](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.mapextensions.map) extensions are used as a convention to branch the request processing pipeline. [Map](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.mapextensions.map) branches the request pipeline based on matches of the given request path. If the request path starts with the given path, the branch is executed.

In the following example, `HandleMap1` is called for requests to `/map1`, and `HandleMap2` is called for requests to `/map2`:

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.Map("/map1", HandleMap1);
app.Map("/map2", HandleMap2);

app.Run(async context =>
{
    await context.Response.WriteAsync("Hello from the non-Map delegate!");
});

app.Run();

private static void HandleMap1(IApplicationBuilder app)
{
    app.Run(async context =>
    {
        await context.Response.WriteAsync("Map 1");
    });
}

private static void HandleMap2(IApplicationBuilder app)
{
    app.Run(async context =>
    {
        await context.Response.WriteAsync("Map 2");
    });
}
```

The following table shows the requests and responses using the preceding code.

| Request | Response |
| --- | --- |
| `/` | Hello from the non-Map delegate. |
| `/map1` | Map 1 |
| `/map2` | Map 2 |
| `/map3` | Hello from the non-Map delegate. |

When [Map](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.mapextensions.map) is used, the matched path segments are removed from [HttpRequest.Path](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httprequest.path) and appended to [HttpRequest.PathBase](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httprequest.pathbase) for each request.

[Map](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.mapextensions.map) can match multiple segments at once:

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.Map("/map1/segment1", HandleMultipleSegments);

app.Run(async context =>
{
    await context.Response.WriteAsync("Hello from the non-Map delegate.");
});

app.Run();

private static void HandleMultipleSegments(IApplicationBuilder app)
{
    app.Run(async context =>
    {
        await context.Response.WriteAsync("Processing '/map1/segment1'");
    });
}
```

The following table shows the requests and responses using the preceding code.

| Request | Response |
| --- | --- |
| `/` | Hello from the non-Map delegate. |
| `/map1/segment1` | Processing '/map1/segment1' |

[Map](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.mapextensions.map) supports nesting:

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.Map("/level1", level1App => {
    level1App.Map("/level2a", level2AApp => {
        app.Run(async context =>
        {
            await context.Response.WriteAsync("Processing '/level1/level2a'");
        });
    });
    level1App.Map("/level2b", level2BApp => {
        app.Run(async context =>
        {
            await context.Response.WriteAsync("Processing '/level1/level2b'");
        });
    });
});

app.Run(async context =>
{
    await context.Response.WriteAsync("Hello from the non-Map delegate!");
});

app.Run();
```

The following table shows the requests and responses using the preceding code.

| Request | Response |
| --- | --- |
| `/` | Hello from the non-Map delegate. |
| `/level1/level2a` | Processing '/level1/level2a' |
| `/level1/level2b` | Processing '/level1/level2b' |

[MapWhen](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.mapwhenextensions.mapwhen) branches the request pipeline based on the result of the given predicate. Any predicate of type `Func<HttpContext, bool>` can be used to map requests to a new branch of the pipeline. In the following example, a predicate is used to detect the presence of a query string variable named "`branch`":

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapWhen(context => context.Request.Query.ContainsKey("branch"), HandleBranch);

app.Run(async context =>
{
    await context.Response.WriteAsync("Hello from the non-Map delegate.");
});

app.Run();

private static void HandleBranch(IApplicationBuilder app)
{
    app.Run(async context =>
    {
        var branchVer = context.Request.Query["branch"];
        await context.Response.WriteAsync($"Branch used = '{branchVer}'");
    });
}
```

The following table shows the requests and responses using the preceding code.

| Request | Response |
| --- | --- |
| `/` | Hello from the non-Map delegate. |
| `/?branch=main` | Branch used = 'main' |

[UseWhen](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.usewhenextensions.usewhen) can branch the request pipeline based on the result of the given predicate. Unlike [MapWhen](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.mapwhenextensions.mapwhen), the branch is rejoined to the main pipeline if it doesn't contain a terminal middleware:

```
var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.UseWhen(context => context.Request.Query.ContainsKey("branch"),
    appBuilder => HandleBranchAndRejoin(appBuilder));

app.Run(async context =>
{
    await context.Response.WriteAsync("Hello from the non-Map delegate.");
});

app.Run();

void HandleBranchAndRejoin(IApplicationBuilder app)
{
    var logger = app.ApplicationServices.GetRequiredService<ILogger<Program>>(); 

    app.Use(async (context, next) =>
    {
        var branchVer = context.Request.Query["branch"];
        logger.LogInformation("Branch used = {branchVer}", branchVer.ToString());

        Console.WriteLine("Work that can write to the response.");
        await next.Invoke(context);
        Console.WriteLine("Work that doesn't write to the response.");
    });
}
```

In the preceding example, a response of "Hello from the non-Map delegate." is written for all requests. If the request includes a query string variable named "`branch`," its value is logged before the main pipeline is rejoined.

The ASP.NET Core request pipeline consists of a sequence of request delegates, called one after the other. The following diagram demonstrates the concept. The thread of execution follows the black arrows.

![Image 2: Request processing pattern showing a request arriving, processing through three middlewares, and the response leaving the app. Each middleware runs its logic and hands off the request to the next middleware at the next() statement. After the third middleware processes the request, the request passes back through the prior two middlewares in reverse order for additional processing after their next() statements before leaving the app as a response to the client.](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/index/_static/request-delegate-pipeline.png?view=aspnetcore-10.0)

Each delegate can perform operations before and after the next delegate. Exception-handling delegates should be called early in the pipeline, so they can catch exceptions that occur in later stages of the pipeline.

The simplest possible ASP.NET Core app sets up a single request delegate that handles all requests. This case doesn't include an actual request pipeline. Instead, a single anonymous function is called in response to every HTTP request.

```
public class Startup
{
    public void Configure(IApplicationBuilder app)
    {
        app.Run(async context =>
        {
            await context.Response.WriteAsync("Hello, World!");
        });
    }
}
```

Chain multiple request delegates together with [Use](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.useextensions.use). The `next` parameter represents the next delegate in the pipeline. You can short-circuit the pipeline by _not_ calling the _next_ parameter. You can typically perform actions both before and after the next delegate, as the following example demonstrates:

```
app.Use(async (context, next) =>
{
    // Do work that doesn't write to the Response.
    await next.Invoke();
    // Do logging or other work that doesn't write to the Response.
});
```

When a delegate doesn't pass a request to the next delegate, it's called _short-circuiting the request pipeline_. Short-circuiting is often desirable because it avoids unnecessary work. For example, [Static File Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0) can act as a _terminal middleware_ by processing a request for a static file and short-circuiting the rest of the pipeline. Middleware added to the pipeline before the middleware that terminates further processing still processes code after their `next.Invoke` statements. However, see the following warning about attempting to write to a response that has already been sent.

Warning

Don't call `next.Invoke` after the response has been sent to the client. Changes to [HttpResponse](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpresponse) after the response has started throw an exception. For example, [setting headers and a status code throw an exception](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/best-practices?view=aspnetcore-10.0#do-not-modify-the-status-code-or-headers-after-the-response-body-has-started). Writing to the response body after calling `next`:

*   May cause a protocol violation. For example, writing more than the stated `Content-Length`.
*   May corrupt the body format. For example, writing an HTML footer to a CSS file.

[HasStarted](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpresponse.hasstarted) is a useful hint to indicate if headers have been sent or the body has been written to.

[Run](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.runextensions.run) delegates don't receive a `next` parameter. The first `Run` delegate is always terminal and terminates the pipeline. `Run` is a convention. Some middleware components may expose `Run[Middleware]` methods that run at the end of the pipeline:

```
app.Run(async context =>
{
    await context.Response.WriteAsync("Hello from 2nd delegate.");
});
```

In the preceding example, the `Run` delegate writes `"Hello from 2nd delegate."` to the response and then terminates the pipeline. If another `Use` or `Run` delegate is added after the `Run` delegate, it's not called.

[Map](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.mapextensions.map) extensions are used as a convention for branching the pipeline. `Map` branches the request pipeline based on matches of the given request path. If the request path starts with the given path, the branch is executed.

```
public class Startup
{
    private static void HandleMapTest1(IApplicationBuilder app)
    {
        app.Run(async context =>
        {
            await context.Response.WriteAsync("Map Test 1");
        });
    }

    private static void HandleMapTest2(IApplicationBuilder app)
    {
        app.Run(async context =>
        {
            await context.Response.WriteAsync("Map Test 2");
        });
    }

    public void Configure(IApplicationBuilder app)
    {
        app.Map("/map1", HandleMapTest1);

        app.Map("/map2", HandleMapTest2);

        app.Run(async context =>
        {
            await context.Response.WriteAsync("Hello from non-Map delegate.");
        });
    }
}
```

The following table shows the requests and responses from `http://localhost:1234` using the previous code.

| Request | Response |
| --- | --- |
| localhost:1234 | Hello from non-Map delegate. |
| localhost:1234/map1 | Map Test 1 |
| localhost:1234/map2 | Map Test 2 |
| localhost:1234/map3 | Hello from non-Map delegate. |

When `Map` is used, the matched path segments are removed from `HttpRequest.Path` and appended to `HttpRequest.PathBase` for each request.

`Map` supports nesting, for example:

```
app.Map("/level1", level1App => {
    level1App.Map("/level2a", level2AApp => {
        // "/level1/level2a" processing
    });
    level1App.Map("/level2b", level2BApp => {
        // "/level1/level2b" processing
    });
});
```

`Map` can also match multiple segments at once:

```
public class Startup
{
    private static void HandleMultiSeg(IApplicationBuilder app)
    {
        app.Run(async context =>
        {
            await context.Response.WriteAsync("Map multiple segments.");
        });
    }

    public void Configure(IApplicationBuilder app)
    {
        app.Map("/map1/seg1", HandleMultiSeg);

        app.Run(async context =>
        {
            await context.Response.WriteAsync("Hello from non-Map delegate.");
        });
    }
}
```

[MapWhen](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.mapwhenextensions.mapwhen) branches the request pipeline based on the result of the given predicate. Any predicate of type `Func<HttpContext, bool>` can be used to map requests to a new branch of the pipeline. In the following example, a predicate is used to detect the presence of a query string variable `branch`:

```
public class Startup
{
    private static void HandleBranch(IApplicationBuilder app)
    {
        app.Run(async context =>
        {
            var branchVer = context.Request.Query["branch"];
            await context.Response.WriteAsync($"Branch used = {branchVer}");
        });
    }

    public void Configure(IApplicationBuilder app)
    {
        app.MapWhen(context => context.Request.Query.ContainsKey("branch"),
                               HandleBranch);

        app.Run(async context =>
        {
            await context.Response.WriteAsync("Hello from non-Map delegate.");
        });
    }
}
```

The following table shows the requests and responses from `http://localhost:1234` using the previous code:

| Request | Response |
| --- | --- |
| localhost:1234 | Hello from non-Map delegate. |
| localhost:1234/?branch=main | Branch used = main |

[UseWhen](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.usewhenextensions.usewhen) also branches the request pipeline based on the result of the given predicate. Unlike with `MapWhen`, this branch is rejoined to the main pipeline if it doesn't short-circuit or contain a terminal middleware:

```
public class Startup
{
    private void HandleBranchAndRejoin(IApplicationBuilder app, ILogger<Startup> logger)
    {
        app.Use(async (context, next) =>
        {
            var branchVer = context.Request.Query["branch"];
            logger.LogInformation("Branch used = {branchVer}", branchVer.ToString());

            // Do work that doesn't write to the Response.
            await next();
            // Do other work that doesn't write to the Response.
        });
    }

    public void Configure(IApplicationBuilder app, ILogger<Startup> logger)
    {
        app.UseWhen(context => context.Request.Query.ContainsKey("branch"),
                               appBuilder => HandleBranchAndRejoin(appBuilder, logger));

        app.Run(async context =>
        {
            await context.Response.WriteAsync("Hello from main pipeline.");
        });
    }
}
```

In the preceding example, a response of "Hello from main pipeline." is written for all requests. If the request includes a query string variable `branch`, its value is logged before the main pipeline is rejoined.

The order that middleware appears in the app's `Program` file defines the order in which middleware are invoked on a request with the reverse order for the response.

You have full control over the order of middleware and the ability to add custom middleware for request processing scenarios, keeping in mind that the order of middleware can be critical for security, performance, and functionality.

The following examples demonstrate middleware order for common app scenarios. Each middleware extension method is exposed on [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder) through the [Microsoft.AspNetCore.Builder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder) namespace:

1.   Exception/error handling 
    *   When the app runs in the `Development` environment: 
        *   Developer Exception Page Middleware ([UseDeveloperExceptionPage](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.developerexceptionpageextensions.usedeveloperexceptionpage)) reports app runtime errors.
        *   Database Error Page Middleware ([UseDatabaseErrorPage](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.databaseerrorpageextensions.usedatabaseerrorpage)) reports database runtime errors.

    *   When the app runs in the `Production` environment: 
        *   Exception Handler Middleware ([UseExceptionHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.exceptionhandlerextensions.useexceptionhandler)) catches exceptions thrown in the following middlewares.
        *   HTTP Strict Transport Security Protocol (HSTS) Middleware ([UseHsts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.hstsbuilderextensions.usehsts)) adds the `Strict-Transport-Security` header.

2.   HTTPS Redirection Middleware ([UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection)) redirects HTTP requests to HTTPS.
3.   Static File Middleware (if required, [UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles)) returns static files and short-circuits further request processing.
4.   Cookie Policy Middleware ([UseCookiePolicy](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.cookiepolicyappbuilderextensions.usecookiepolicy)) conforms the app to the EU General Data Protection Regulation (GDPR).
5.   Routing Middleware ([UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting)) to route requests.
6.   Authentication Middleware ([UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication)) attempts to authenticate the user before they're allowed access to secure resources.
7.   Authorization Middleware ([UseAuthorization](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authorizationappbuilderextensions.useauthorization)) authorizes a user to access secure resources.
8.   Antiforgery Middleware ([UseAntiforgery](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.antiforgeryapplicationbuilderextensions.useantiforgery)) adds antiforgery middleware to the pipeline [UseAntiforgery](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.antiforgeryapplicationbuilderextensions.useantiforgery) must be placed after calls to [UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication) and [UseAuthorization](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authorizationappbuilderextensions.useauthorization).
9.   Session Middleware (Razor Pages and MVC only, [UseSession](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.sessionmiddlewareextensions.usesession)) establishes and maintains session state. If the app uses session state, call Session Middleware after Cookie Policy Middleware and before Razor Pages/MVC Middleware.
10.   Endpoint Routing Middleware

*   [MapRazorComponents](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.razorcomponentsendpointroutebuilderextensions.maprazorcomponents) to add Razor component endpoints to the request pipeline.
*   [MapRazorPages](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.razorpagesendpointroutebuilderextensions.maprazorpages) to add Razor Pages endpoints to the request pipeline.
*   [MapControllerRoute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.controllerendpointroutebuilderextensions.mapcontrollerroute) to add controller endpoints to the request pipeline.

Typical Blazor Web App middleware pipeline:

```
app.UseWebAssemblyDebugging(); // Development environment with client-side rendering
app.UseMigrationsEndPoint(); // Development environment with ASP.NET Core Identity

app.UseExceptionHandler("/Error", createScopeForErrors: true); // Non-Development environment
app.UseHsts(); // Non-Development environment with HTTPS protocol

app.UseStatusCodePagesWithReExecute("/not-found", createScopeForStatusCodePages: true);

app.UseHttpsRedirection(); // With HTTPS protocol

app.UseAntiforgery();

app.MapStaticAssets();

app.MapRazorComponents<App>(); // With additional extension methods for render modes

app.MapAdditionalIdentityEndpoints(); // With ASP.NET Core Identity

app.Run();
```

Typical Razor Pages/MVC middleware pipeline:

```
app.UseMigrationsEndPoint(); // Development environment with ASP.NET Core Identity

app.UseExceptionHandler("/Error"); // Non-Development environment
app.UseHsts(); // Non-Development environment with HTTPS protocol

app.UseHttpsRedirection(); // With HTTPS protocol

// app.UseCookiePolicy();
app.UseRouting(); // If not called, runs at the beginning of the pipeline by default
// app.UseRateLimiter();
// app.UseRequestLocalization();
// app.UseCors();

// app.UseAuthentication(); // Called internally for ASP.NET Core Identity
app.UseAuthorization();
// app.UseSession();
// app.UseResponseCompression();
// app.UseResponseCaching();

app.MapStaticAssets();

app.MapControllerRoute(...); // For MVC controllers

app.MapRazorPages(); // For Razor Pages pages

app.MapControllers(); // With authentication in a Razor Pages app

app.Run();
```

In the preceding code:

*   CORS Middleware ([UseCors](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.corsmiddlewareextensions.usecors)), Authentication Middleware ([UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication)), and Authorization Middleware ([UseAuthorization](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authorizationappbuilderextensions.useauthorization)) must appear in the order shown.
*   CORS Middleware ([UseCors](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.corsmiddlewareextensions.usecors)) must appear before Response Caching Middleware ([UseResponseCaching](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.responsecachingextensions.useresponsecaching)) to add CORS headers on every request, including cached responses. For more information, see [It is not clear that UseCORS must come before UseResponseCaching (`dotnet/aspnetcore` #23218](https://github.com/dotnet/aspnetcore/issues/23218).
*   Request Localization Middleware ([UseRequestLocalization](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.applicationbuilderextensions.userequestlocalization)) must appear before any middleware that might check the request culture, for example, Static File Middleware ([UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles)).
*   Rate Limiting Middleware ([UseRateLimiter](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.ratelimiterapplicationbuilderextensions.useratelimiter)) must be called after Routing Middleware ([UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting)) when rate limiting endpoint-specific APIs are used. For example, if the [`[EnableRateLimiting]` attribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.ratelimiting.enableratelimitingattribute) is used, Rate Limiting Middleware must be called after Routing Middleware. When calling only global limiters, Rate Limiting Middleware can be called before Routing Middleware.

In some scenarios, middleware has different ordering. For example, caching and compression ordering depends on the app's specification. In the following order, CPU usage might be reduced by caching the compressed response, but the app might end up caching multiple representations of a resource using different compression algorithms, such as Gzip or Brotli:

```
app.UseResponseCaching();
app.UseResponseCompression();
```

Static assets are typically served early in the pipeline so that the app can short-circuit request processing to improve performance.

Authentication doesn't short-circuit unauthenticated requests. Although Authentication Middleware authenticates requests, authorization occurs after the framework selects a Razor component in a Blazor Web App, a page in a Razor Pages app, or a controller and action in an MVC app.

The following diagram shows the complete request processing pipeline for ASP.NET Core MVC and Razor Pages apps. You can see how, in a typical app, existing middlewares are ordered and where custom middlewares are added. You have full control over how to reorder existing middlewares or inject new custom middlewares as necessary for your scenarios.

![Image 3: ASP.NET Core middleware pipeline](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/index/_static/middleware-pipeline.svg?view=aspnetcore-10.0)

The **Endpoint** middleware in the preceding diagram executes the filter pipeline for the corresponding app type—MVC or Razor Pages.

The **Routing** middleware in the preceding diagram is shown following **Static Files**. This is the order that the project templates implement by explicitly calling [app.UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting). If you don't call `app.UseRouting`, the **Routing** middleware runs at the beginning of the pipeline by default. For more information, see [Routing](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing?view=aspnetcore-10.0).

The order that middleware components are added in the `Program.cs` file defines the order in which the middleware components are invoked on requests and the reverse order for the response. The order is **critical** for security, performance, and functionality.

The following highlighted code in `Program.cs` adds security-related middleware components in the typical recommended order:

```
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;
using WebMiddleware.Data;

var builder = WebApplication.CreateBuilder(args);

var connectionString = builder.Configuration.GetConnectionString("DefaultConnection")
    ?? throw new InvalidOperationException("Connection string 'DefaultConnection' not found.");
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(connectionString));
builder.Services.AddDatabaseDeveloperPageExceptionFilter();

builder.Services.AddDefaultIdentity<IdentityUser>(options => options.SignIn.RequireConfirmedAccount = true)
    .AddEntityFrameworkStores<ApplicationDbContext>();
builder.Services.AddRazorPages();
builder.Services.AddControllersWithViews();

var app = builder.Build();

if (app.Environment.IsDevelopment())
{
    app.UseMigrationsEndPoint();
}
else
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
// app.UseCookiePolicy();

app.UseRouting();
// app.UseRateLimiter();
// app.UseRequestLocalization();
// app.UseCors();

app.UseAuthentication();
app.UseAuthorization();
// app.UseSession();
// app.UseResponseCompression();
// app.UseResponseCaching();

app.MapRazorPages();
app.MapDefaultControllerRoute();

app.Run();
```

In the preceding code:

*   Middleware that is not added when creating a new web app with [individual users accounts](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-10.0) is commented out.
*   Not every middleware appears in this exact order, but many do. For example: 
    *   `UseCors`, `UseAuthentication`, and `UseAuthorization` must appear in the order shown.
    *   `UseCors` currently must appear before `UseResponseCaching`. This requirement is explained in [GitHub issue dotnet/aspnetcore #23218](https://github.com/dotnet/aspnetcore/issues/23218).
    *   `UseRequestLocalization` must appear before any middleware that might check the request culture, for example, `app.UseStaticFiles()`.
    *   [UseRateLimiter](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.ratelimiterapplicationbuilderextensions.useratelimiter) must be called after `UseRouting` when rate limiting endpoint specific APIs are used. For example, if the [`[EnableRateLimiting]`](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.ratelimiting.enableratelimitingattribute) attribute is used, `UseRateLimiter` must be called after `UseRouting`. When calling only global limiters, `UseRateLimiter` can be called before `UseRouting`.

In some scenarios, middleware has different ordering. For example, caching and compression ordering is scenario specific, and there are multiple valid orderings. For example:

```
app.UseResponseCaching();
app.UseResponseCompression();
```

With the preceding code, CPU usage could be reduced by caching the compressed response, but you might end up caching multiple representations of a resource using different compression algorithms such as Gzip or Brotli.

The following ordering combines static files to allow caching compressed static files:

```
app.UseResponseCaching();
app.UseResponseCompression();
app.UseStaticFiles();
```

The following `Program.cs` code adds middleware components for common app scenarios:

1.   Exception/error handling 
    *   When the app runs in the `Development` environment: 
        *   Developer Exception Page Middleware ([UseDeveloperExceptionPage](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.developerexceptionpageextensions.usedeveloperexceptionpage)) reports app runtime errors.
        *   Database Error Page Middleware ([UseDatabaseErrorPage](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.databaseerrorpageextensions.usedatabaseerrorpage)) reports database runtime errors.

    *   When the app runs in the `Production` environment: 
        *   Exception Handler Middleware ([UseExceptionHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.exceptionhandlerextensions.useexceptionhandler)) catches exceptions thrown in the following middlewares.
        *   HTTP Strict Transport Security Protocol (HSTS) Middleware ([UseHsts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.hstsbuilderextensions.usehsts)) adds the `Strict-Transport-Security` header.

2.   HTTPS Redirection Middleware ([UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection)) redirects HTTP requests to HTTPS.
3.   Static File Middleware ([UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles)) returns static files and short-circuits further request processing.
4.   Cookie Policy Middleware ([UseCookiePolicy](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.cookiepolicyappbuilderextensions.usecookiepolicy)) conforms the app to the EU General Data Protection Regulation (GDPR) regulations.
5.   Routing Middleware ([UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting)) to route requests.
6.   Authentication Middleware ([UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication)) attempts to authenticate the user before they're allowed access to secure resources.
7.   Authorization Middleware ([UseAuthorization](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authorizationappbuilderextensions.useauthorization)) authorizes a user to access secure resources.
8.   Session Middleware ([UseSession](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.sessionmiddlewareextensions.usesession)) establishes and maintains session state. If the app uses session state, call Session Middleware after Cookie Policy Middleware and before MVC Middleware.
9.   Endpoint Routing Middleware ([UseEndpoints](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.useendpoints) with [MapRazorPages](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.razorpagesendpointroutebuilderextensions.maprazorpages)) to add Razor Pages endpoints to the request pipeline.

```
if (env.IsDevelopment())
{
    app.UseDeveloperExceptionPage();
    app.UseDatabaseErrorPage();
}
else
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}
app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseCookiePolicy();
app.UseRouting();
app.UseAuthentication();
app.UseAuthorization();
app.UseSession();
app.MapRazorPages();
```

In the preceding example code, each middleware extension method is exposed on [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder) through the [Microsoft.AspNetCore.Builder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder) namespace.

[UseExceptionHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.exceptionhandlerextensions.useexceptionhandler) is the first middleware component added to the pipeline. Therefore, the Exception Handler Middleware catches any exceptions that occur in later calls.

Static File Middleware is called early in the pipeline so that it can handle requests and short-circuit without going through the remaining components. The Static File Middleware provides **no** authorization checks. Any files served by Static File Middleware, including those under _wwwroot_, are publicly available. For an approach to secure static files, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).

If the request isn't handled by the Static File Middleware, it's passed on to the Authentication Middleware ([UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication)), which performs authentication. Authentication doesn't short-circuit unauthenticated requests. Although Authentication Middleware authenticates requests, authorization (and rejection) occurs only after MVC selects a specific Razor Page or MVC controller and action.

The following example demonstrates a middleware order where requests for static files are handled by Static File Middleware before Response Compression Middleware. Static files aren't compressed with this middleware order. The Razor Pages responses can be compressed.

```
// Static files aren't compressed by Static File Middleware.
app.UseStaticFiles();

app.UseRouting();

app.UseResponseCompression();

app.MapRazorPages();
```

The following diagram shows the complete request processing pipeline for ASP.NET Core MVC and Razor Pages apps. You can see how, in a typical app, existing middlewares are ordered and where custom middlewares are added. You have full control over how to reorder existing middlewares or inject new custom middlewares as necessary for your scenarios.

![Image 4: ASP.NET Core middleware pipeline](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/index/_static/middleware-pipeline.svg?view=aspnetcore-10.0)

The **Endpoint** middleware in the preceding diagram executes the filter pipeline for the corresponding app type—MVC or Razor Pages.

The **Routing** middleware in the preceding diagram is shown following **Static Files**. This is the order that the project templates implement by explicitly calling [app.UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting). If you don't call `app.UseRouting`, the **Routing** middleware runs at the beginning of the pipeline by default. For more information, see [Routing](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing?view=aspnetcore-10.0).

The order that middleware components are added in the `Program.cs` file defines the order in which the middleware components are invoked on requests and the reverse order for the response. The order is **critical** for security, performance, and functionality.

The following highlighted code in `Program.cs` adds security-related middleware components in the typical recommended order:

```
using IndividualAccountsExample.Data;
using Microsoft.AspNetCore.Identity;
using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.
var connectionString = builder.Configuration.GetConnectionString("DefaultConnection");
builder.Services.AddDbContext<ApplicationDbContext>(options =>
    options.UseSqlServer(connectionString));
builder.Services.AddDatabaseDeveloperPageExceptionFilter();

builder.Services.AddDefaultIdentity<IdentityUser>(options => options.SignIn.RequireConfirmedAccount = true)
    .AddEntityFrameworkStores<ApplicationDbContext>();
builder.Services.AddRazorPages();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseMigrationsEndPoint();
}
else
{
    app.UseExceptionHandler("/Error");
    // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();
// app.UseCookiePolicy();

app.UseRouting();
// app.UseRequestLocalization();
// app.UseCors();

app.UseAuthentication();
app.UseAuthorization();
// app.UseSession();
// app.UseResponseCompression();
// app.UseResponseCaching();

app.MapRazorPages();
app.MapControllerRoute(
    name: "default",
    pattern: "{controller=Home}/{action=Index}/{id?}");

app.Run();
```

In the preceding code:

*   Middleware that is not added when creating a new web app with [individual users accounts](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-10.0) is commented out.
*   Not every middleware appears in this exact order, but many do. For example: 
    *   `UseCors`, `UseAuthentication`, and `UseAuthorization` must appear in the order shown.
    *   `UseCors` currently must appear before `UseResponseCaching`. This requirement is explained in [GitHub issue dotnet/aspnetcore #23218](https://github.com/dotnet/aspnetcore/issues/23218).
    *   `UseRequestLocalization` must appear before any middleware that might check the request culture (for example, `app.UseMvcWithDefaultRoute()`).

In some scenarios, middleware has different ordering. For example, caching and compression ordering is scenario specific, and there are multiple valid orderings. For example:

```
app.UseResponseCaching();
app.UseResponseCompression();
```

With the preceding code, CPU usage could be reduced by caching the compressed response, but you might end up caching multiple representations of a resource using different compression algorithms such as Gzip or Brotli.

The following ordering combines static files to allow caching compressed static files:

```
app.UseResponseCaching();
app.UseResponseCompression();
app.UseStaticFiles();
```

The following `Program.cs` code adds middleware components for common app scenarios:

1.   Exception/error handling 
    *   When the app runs in the `Development` environment: 
        *   Developer Exception Page Middleware ([UseDeveloperExceptionPage](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.developerexceptionpageextensions.usedeveloperexceptionpage)) reports app runtime errors.
        *   Database Error Page Middleware ([UseDatabaseErrorPage](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.databaseerrorpageextensions.usedatabaseerrorpage)) reports database runtime errors.

    *   When the app runs in the `Production` environment: 
        *   Exception Handler Middleware ([UseExceptionHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.exceptionhandlerextensions.useexceptionhandler)) catches exceptions thrown in the following middlewares.
        *   HTTP Strict Transport Security Protocol (HSTS) Middleware ([UseHsts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.hstsbuilderextensions.usehsts)) adds the `Strict-Transport-Security` header.

2.   HTTPS Redirection Middleware ([UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection)) redirects HTTP requests to HTTPS.
3.   Static File Middleware ([UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles)) returns static files and short-circuits further request processing.
4.   Cookie Policy Middleware ([UseCookiePolicy](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.cookiepolicyappbuilderextensions.usecookiepolicy)) conforms the app to the EU General Data Protection Regulation (GDPR) regulations.
5.   Routing Middleware ([UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting)) to route requests.
6.   Authentication Middleware ([UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication)) attempts to authenticate the user before they're allowed access to secure resources.
7.   Authorization Middleware ([UseAuthorization](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authorizationappbuilderextensions.useauthorization)) authorizes a user to access secure resources.
8.   Session Middleware ([UseSession](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.sessionmiddlewareextensions.usesession)) establishes and maintains session state. If the app uses session state, call Session Middleware after Cookie Policy Middleware and before MVC Middleware.
9.   Endpoint Routing Middleware ([UseEndpoints](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.useendpoints) with [MapRazorPages](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.razorpagesendpointroutebuilderextensions.maprazorpages)) to add Razor Pages endpoints to the request pipeline.

```
if (env.IsDevelopment())
{
    app.UseDeveloperExceptionPage();
    app.UseDatabaseErrorPage();
}
else
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}
app.UseHttpsRedirection();
app.UseStaticFiles();
app.UseCookiePolicy();
app.UseRouting();
app.UseAuthentication();
app.UseAuthorization();
app.UseSession();
app.MapRazorPages();
```

In the preceding example code, each middleware extension method is exposed on [WebApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.webapplicationbuilder) through the [Microsoft.AspNetCore.Builder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder) namespace.

[UseExceptionHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.exceptionhandlerextensions.useexceptionhandler) is the first middleware component added to the pipeline. Therefore, the Exception Handler Middleware catches any exceptions that occur in later calls.

Static File Middleware is called early in the pipeline so that it can handle requests and short-circuit without going through the remaining components. The Static File Middleware provides **no** authorization checks. Any files served by Static File Middleware, including those under _wwwroot_, are publicly available. For an approach to secure static files, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).

If the request isn't handled by the Static File Middleware, it's passed on to the Authentication Middleware ([UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication)), which performs authentication. Authentication doesn't short-circuit unauthenticated requests. Although Authentication Middleware authenticates requests, authorization (and rejection) occurs only after MVC selects a specific Razor Page or MVC controller and action.

The following example demonstrates a middleware order where requests for static files are handled by Static File Middleware before Response Compression Middleware. Static files aren't compressed with this middleware order. The Razor Pages responses can be compressed.

```
// Static files aren't compressed by Static File Middleware.
app.UseStaticFiles();

app.UseRouting();

app.UseResponseCompression();

app.MapRazorPages();
```

The following diagram shows the complete request processing pipeline for ASP.NET Core MVC and Razor Pages apps. You can see how, in a typical app, existing middlewares are ordered and where custom middlewares are added. You have full control over how to reorder existing middlewares or inject new custom middlewares as necessary for your scenarios.

![Image 5: ASP.NET Core middleware pipeline](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/index/_static/middleware-pipeline.svg?view=aspnetcore-10.0)

The **Endpoint** middleware in the preceding diagram executes the filter pipeline for the corresponding app type—MVC or Razor Pages.

The order that middleware components are added in the `Startup.Configure` method defines the order in which the middleware components are invoked on requests and the reverse order for the response. The order is **critical** for security, performance, and functionality.

The following `Startup.Configure` method adds security-related middleware components in the typical recommended order:

```
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
        app.UseDatabaseErrorPage();
    }
    else
    {
        app.UseExceptionHandler("/Error");
        app.UseHsts();
    }

    app.UseHttpsRedirection();
    app.UseStaticFiles();
    // app.UseCookiePolicy();

    app.UseRouting();
    // app.UseRequestLocalization();
    // app.UseCors();

    app.UseAuthentication();
    app.UseAuthorization();
    // app.UseSession();
    // app.UseResponseCompression();
    // app.UseResponseCaching();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapRazorPages();
        endpoints.MapControllerRoute(
            name: "default",
            pattern: "{controller=Home}/{action=Index}/{id?}");
    });
}
```

In the preceding code:

*   Middleware that is not added when creating a new web app with [individual users accounts](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-10.0) is commented out.
*   Not every middleware appears in this exact order, but many do. For example: 
    *   `UseCors`, `UseAuthentication`, and `UseAuthorization` must appear in the order shown.
    *   `UseCors` currently must appear before `UseResponseCaching` due to [this bug](https://github.com/dotnet/aspnetcore/issues/23218).
    *   `UseRequestLocalization` must appear before any middleware that might check the request culture (for example, `app.UseMvcWithDefaultRoute()`).

In some scenarios, middleware has different ordering. For example, caching and compression ordering is scenario specific, and there's multiple valid orderings. For example:

```
app.UseResponseCaching();
app.UseResponseCompression();
```

With the preceding code, CPU could be saved by caching the compressed response, but you might end up caching multiple representations of a resource using different compression algorithms such as Gzip or Brotli.

The following ordering combines static files to allow caching compressed static files:

```
app.UseResponseCaching();
app.UseResponseCompression();
app.UseStaticFiles();
```

The following `Startup.Configure` method adds middleware components for common app scenarios:

1.   Exception/error handling 
    *   When the app runs in the `Development` environment: 
        *   Developer Exception Page Middleware ([UseDeveloperExceptionPage](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.developerexceptionpageextensions.usedeveloperexceptionpage)) reports app runtime errors.
        *   Database Error Page Middleware reports database runtime errors.

    *   When the app runs in the `Production` environment: 
        *   Exception Handler Middleware ([UseExceptionHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.exceptionhandlerextensions.useexceptionhandler)) catches exceptions thrown in the following middlewares.
        *   HTTP Strict Transport Security Protocol (HSTS) Middleware ([UseHsts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.hstsbuilderextensions.usehsts)) adds the `Strict-Transport-Security` header.

2.   HTTPS Redirection Middleware ([UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection)) redirects HTTP requests to HTTPS.
3.   Static File Middleware ([UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles)) returns static files and short-circuits further request processing.
4.   Cookie Policy Middleware ([UseCookiePolicy](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.cookiepolicyappbuilderextensions.usecookiepolicy)) conforms the app to the EU General Data Protection Regulation (GDPR) regulations.
5.   Routing Middleware ([UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting)) to route requests.
6.   Authentication Middleware ([UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication)) attempts to authenticate the user before they're allowed access to secure resources.
7.   Authorization Middleware ([UseAuthorization](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authorizationappbuilderextensions.useauthorization)) authorizes a user to access secure resources.
8.   Session Middleware ([UseSession](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.sessionmiddlewareextensions.usesession)) establishes and maintains session state. If the app uses session state, call Session Middleware after Cookie Policy Middleware and before MVC Middleware.
9.   Endpoint Routing Middleware ([UseEndpoints](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.useendpoints) with [MapRazorPages](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.razorpagesendpointroutebuilderextensions.maprazorpages)) to add Razor Pages endpoints to the request pipeline.

```
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
        app.UseDatabaseErrorPage();
    }
    else
    {
        app.UseExceptionHandler("/Error");
        app.UseHsts();
    }

    app.UseHttpsRedirection();
    app.UseStaticFiles();
    app.UseCookiePolicy();
    app.UseRouting();
    app.UseAuthentication();
    app.UseAuthorization();
    app.UseSession();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapRazorPages();
    });
}
```

In the preceding example code, each middleware extension method is exposed on [IApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.iapplicationbuilder) through the [Microsoft.AspNetCore.Builder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder) namespace.

[UseExceptionHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.exceptionhandlerextensions.useexceptionhandler) is the first middleware component added to the pipeline. Therefore, the Exception Handler Middleware catches any exceptions that occur in later calls.

Static File Middleware is called early in the pipeline so that it can handle requests and short-circuit without going through the remaining components. The Static File Middleware provides **no** authorization checks. Any files served by Static File Middleware, including those under _wwwroot_, are publicly available. For an approach to secure static files, see [Static files in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0).

If the request isn't handled by the Static File Middleware, it's passed on to the Authentication Middleware ([UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication)), which performs authentication. Authentication doesn't short-circuit unauthenticated requests. Although Authentication Middleware authenticates requests, authorization (and rejection) occurs only after MVC selects a specific Razor Page or MVC controller and action.

The following example demonstrates a middleware order where requests for static files are handled by Static File Middleware before Response Compression Middleware. Static files aren't compressed with this middleware order. The Razor Pages responses can be compressed.

```
public void Configure(IApplicationBuilder app)
{
    // Static files aren't compressed by Static File Middleware.
    app.UseStaticFiles();

    app.UseRouting();

    app.UseResponseCompression();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapRazorPages();
    });
}
```

For Single Page Applications (SPAs), the SPA middleware [UseSpaStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.spastaticfilesextensions.usespastaticfiles) usually comes last in the middleware pipeline. The SPA middleware comes last:

*   To allow all other middlewares to respond to matching requests first.
*   To allow SPAs with client-side routing to run for all routes that are unrecognized by the server app.

For more details on SPAs, see the guides for the [React](https://learn.microsoft.com/en-us/aspnet/core/client-side/spa/react?view=aspnetcore-10.0) and [Angular](https://learn.microsoft.com/en-us/aspnet/core/client-side/spa/angular?view=aspnetcore-10.0) project templates.

For information about Single Page Applications, see the guides for the [React](https://learn.microsoft.com/en-us/aspnet/core/client-side/spa/react?view=aspnetcore-10.0) and [Angular](https://learn.microsoft.com/en-us/aspnet/core/client-side/spa/angular?view=aspnetcore-10.0) project templates.

For more information on ordering [UseCors](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.corsmiddlewareextensions.usecors) and [UseStaticFiles](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.staticfileextensions.usestaticfiles), see [Enable Cross-Origin Requests (CORS) in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/cors?view=aspnetcore-10.0#usecors-and-usestaticfiles-order).

Run Forwarded Headers Middleware before other middleware to ensure that the middleware relying on forwarded headers information can consume the header values for processing. To run Forwarded Headers Middleware after Diagnostics and Error Handling Middleware, see [Forwarded Headers Middleware order](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0#forwarded-headers-middleware-order).

The latest release of ASP.NET Core ships with the following middleware. The _UI stack_ column indicates the typical UI stack where the middleware is used [All, Blazor Web App (BWA), Razor Pages and MVC (RP/MVC)]. The _Order_ column provides notes on middleware placement in the request processing pipeline and under what conditions the middleware may terminate request processing. When a middleware short-circuits the request processing pipeline and prevents further downstream middleware from processing a request, it's called a _terminal middleware_. For more information on short-circuiting, see the [Create a middleware pipeline with `WebApplication`](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0#create-a-middleware-pipeline-with-webapplication) section.

| Middleware | Description | UI stack | Order |
| --- | --- | --- | --- |
| [Antiforgery](https://learn.microsoft.com/en-us/aspnet/core/security/anti-request-forgery?view=aspnetcore-10.0) | Provides anti-request-forgery support. | All | After authentication and authorization, before endpoints. |
| [Authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-10.0) | Provides authentication support. | All | Before `HttpContext.User` is required. Terminal for OAuth callbacks. |
| [Authorization](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authorizationappbuilderextensions.useauthorization) | Provides authorization support. | All | Immediately after the Authentication Middleware. |
| [Cookie Policy](https://learn.microsoft.com/en-us/aspnet/core/security/gdpr?view=aspnetcore-10.0) | Tracks consent from users for storing personal information and enforces minimum standards for cookie fields, such as `secure` and `SameSite`. | All | Before middleware that issues cookies. Examples: Authentication, Session, MVC (TempData). |
| [CORS](https://learn.microsoft.com/en-us/aspnet/core/security/cors?view=aspnetcore-10.0) | Configures Cross-Origin Resource Sharing. | All | Before middleware that use CORS. [UseCors](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.corsmiddlewareextensions.usecors) must go before [UseResponseCaching](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.responsecachingextensions.useresponsecaching). For more information, see [It is not clear that UseCORS must come before UseResponseCaching (`dotnet/aspnetcore` #23218](https://github.com/dotnet/aspnetcore/issues/23218). |
| [Developer Exception Page](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.diagnostics.developerexceptionpagemiddleware) | Generates a page with error information that is intended for use only in the `Development` environment. | All | Before middleware that generate errors. The project templates automatically register this middleware as the first middleware in the pipeline when the environment is `Development`. |
| [Diagnostics](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-10.0) | Several separate middlewares that provide a developer exception page, exception handling, status code pages, and the default web page for new apps. | All | Before middleware that generate errors. Terminal for exceptions or serving the default web page for new apps. |
| [Forwarded Headers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0) | Forwards proxied headers onto the current request. | All | Before middleware that consume the updated fields. Examples: scheme, host, client IP, method. |
| [Health Check](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/health-checks?view=aspnetcore-10.0) | Checks the health of an ASP.NET Core app and its dependencies, such as checking database availability. | All | Terminal if a request matches a health check endpoint. |
| [Header Propagation](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/http-requests?view=aspnetcore-10.0#header-propagation-middleware) | Propagates HTTP headers from the incoming request to the outgoing HTTP Client requests. |  |  |
| All |  |  |  |
| [HTTP Logging](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/http-logging/?view=aspnetcore-10.0) | Logs HTTP Requests and Responses. | All | At the beginning of the middleware pipeline. |
| [HTTP Method Override](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpmethodoverrideextensions) | Allows an incoming POST request to override the method. | All | Before middleware that consume the updated method. |
| [HTTPS Redirection](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#require-https) | Redirect all HTTP requests to HTTPS. | All | Before middleware that consume the URL. |
| [HTTP Strict Transport Security (HSTS)](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) | Security enhancement middleware that adds a special response header. | All | Before responses are sent and after middleware that modify requests. Examples: Forwarded Headers, URL Rewriting. |
| [MVC](https://learn.microsoft.com/en-us/aspnet/core/mvc/overview?view=aspnetcore-10.0) | Processes requests with MVC/Razor Pages. | RP/MVC | Terminal if a request matches a route. |
| [OWIN](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/owin?view=aspnetcore-10.0) | Interop with OWIN-based apps, servers, and middleware. | RP/MVC | Terminal if the OWIN Middleware fully processes the request. |
| [Output Caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/output?view=aspnetcore-10.0) | Provides support for caching responses based on configuration. | RP/MVC | Before middleware that require caching. [UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting) and [UseCors](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.corsmiddlewareextensions.usecors) must come before [UseOutputCache](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.outputcacheapplicationbuilderextensions.useoutputcache). |
| [Response Caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/middleware?view=aspnetcore-10.0) | Provides support for caching responses. This requires client participation to work. Use output caching for complete server control. | RP/MVC | Before middleware that require caching. [UseCors](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.corsmiddlewareextensions.usecors) must come before [UseResponseCaching](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.responsecachingextensions.useresponsecaching). Response caching isn't typically beneficial for UI apps, such as Razor Pages, because browsers generally set request headers that prevent caching. [Output caching](https://learn.microsoft.com/en-us/aspnet/core/performance/caching/output?view=aspnetcore-10.0) benefits UI apps. |
| [Request Decompression](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/request-decompression?view=aspnetcore-10.0) | Provides support for decompressing requests. | All | Before middleware that read the request body. |
| [Response Compression](https://learn.microsoft.com/en-us/aspnet/core/performance/response-compression?view=aspnetcore-10.0) | Provides support for compressing responses. | All | Before middleware that require compression. |
| [Request Localization](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/localization?view=aspnetcore-10.0) | Provides localization support. | All | Before localization sensitive middleware. Must appear after Routing Middleware when using [RouteDataRequestCultureProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.localization.routing.routedatarequestcultureprovider). |
| [Request Timeouts](https://learn.microsoft.com/en-us/aspnet/core/performance/timeouts?view=aspnetcore-10.0) | Provides support for configuring request timeouts, global and per endpoint. | All | [UseRequestTimeouts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.requesttimeoutsiapplicationbuilderextensions.userequesttimeouts) must come after [UseExceptionHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.exceptionhandlerextensions.useexceptionhandler), [UseDeveloperExceptionPage](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.developerexceptionpageextensions.usedeveloperexceptionpage), and [UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting). |
| [Endpoint Routing](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/routing?view=aspnetcore-10.0). | Defines and constrains request routes. | All | Terminal for matching routes. |
| [SPA](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.spaapplicationbuilderextensions.usespa) | Handles all requests from this point in the middleware chain by returning the default page for the Single Page Application (SPA). | All | Appears late in the pipeline, so other middleware for serving static files, such as MVC actions, take precedence. |
| [Session](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/app-state?view=aspnetcore-10.0) | Provides support for managing user sessions. | RP/MVC | Before middleware that require Session. |
| [Static File](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/static-files?view=aspnetcore-10.0) | Provides support for serving static files and directory browsing. | All | Terminal if a request matches a file. |
| [URL Rewrite](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting?view=aspnetcore-10.0) | Provides support for rewriting URLs and redirecting requests. | All | Before middleware that consume the URL. |
| [W3C Logging](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/w3c-logger/?view=aspnetcore-10.0) | Generates server access logs in the [W3C Extended Log File Format](https://www.w3.org/TR/WD-logfile.html). | All | At the beginning of the middleware pipeline. |
| [Blazor WebAssembly Debugging](https://learn.microsoft.com/en-us/aspnet/core/blazor/debug?view=aspnetcore-10.0) | Debugging Blazor Web Apps that adopt client-side rendering (CSR) inside Chromium developer tools. | BWA | At the beginning of the middleware pipeline. |
| [WebSockets](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/websockets?view=aspnetcore-10.0) | Enables the WebSockets protocol. | All | Before middleware that are required to accept WebSocket requests. |

*   [Lifetime and registration options (includes middleware sample)](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection?view=aspnetcore-10.0#lifetime-and-registration-options)
*   [Write custom ASP.NET Core middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/write?view=aspnetcore-10.0)
*   [Test ASP.NET Core middleware](https://learn.microsoft.com/en-us/aspnet/core/test/middleware?view=aspnetcore-10.0)
*   [Configure gRPC-Web in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/grpc/browser?view=aspnetcore-10.0#configure-grpc-web-in-aspnet-core)
*   [Migrate HTTP modules to ASP.NET Core middleware](https://learn.microsoft.com/en-us/aspnet/core/migration/fx-to-core/areas/http-modules?view=aspnetcore-10.0)
*   [App startup in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0)
*   [Request Features in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/request-features?view=aspnetcore-10.0)
*   [Factory-based middleware activation in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/extensibility?view=aspnetcore-10.0)
*   [Middleware activation with a third-party container in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/extensibility-third-party-container?view=aspnetcore-10.0)
