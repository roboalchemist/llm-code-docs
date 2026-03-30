# Source: https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html

Title: Delegating Handlers — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html

Markdown Content:
Ocelot allows the user to add [delegating handlers](https://learn.microsoft.com/en-us/dotnet/api/system.net.http.delegatinghandler) to the `HttpClient` transport. [[1]](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html#f1)

Configuration[¶](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html#configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

In order to utilize the [Delegating Handlers](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html#) feature, you need to do the following three steps of configuration.

1.   Create a class that can be used as a _delegating handler_: it must inherit from the `DelegatingHandler` class. We are going to register these handlers in the ASP.NET Core DI container, so you can inject any other services you have registered into the constructor of your handler.

public class MyHandler : DelegatingHandler
{
 protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken token)
 {
 // Do stuff before sending request, and optionally call the base handler...
 var response = await base.SendAsync(request, token);
 // Do post-processing of the response...
 return response;
 }
} 
2.   You must add the handlers to the DI container in your [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs), as shown below:

builder.Services
 .AddOcelot(builder.Configuration)
 .AddDelegatingHandler<MyHandler>()
 .AddDelegatingHandler<MyHandlerTwo>(); 
Both of these `AddDelegatingHandler{T}` methods have an optional parameter called `global`, which is set to `false`. If it is `false`, then the intent of the _delegating handler_ is to be applied to specific routes via [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json) (see step 3). If it is set to `true`, then it becomes a global handler and will be applied to all routes, as shown below:

builder.Services
 .AddOcelot(builder.Configuration)
 .AddDelegatingHandler<MyGlobalHandler>(true); // it's global! 

> **Note 1**: The generic `AddDelegatingHandler<T>(bool)` method has another overloaded non-generic one with the `Type` parameter: `AddDelegatingHandler(Type, bool)`. Thus, here is an alternative to set it up:
> 
> 
> 
> builder.Services
>  .AddOcelot(builder.Configuration)
>  .AddDelegatingHandler(typeof(MyHandler)) // for selected routes only
>  .AddDelegatingHandler(typeof(MyGlobalHandler), true); // it's global!
> 
> 
> **Note 2**: Both versions of the methods add transient services to the DI container. It is recommended to utilize the generic version.

1.   If you want route-specific _delegating handlers_ or to order your specific and/or global _delegating handlers_ (more on this in the [Execution Order](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html#dh-execution-order) section), then you must add the following to the specific route in [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json). The names in the array must match the class names of your _delegating handlers_ for Ocelot to match them together:

"DelegatingHandlers": [ "MyHandlerTwo", "MyHandler" ] 

Execution Order[¶](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html#execution-order "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

You can have as many _delegating handlers_ as you want, and they are run in the following order:

1.   Any globals that are left in the order they were added to services and are not in the `DelegatingHandlers` option array from [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json).

2.   Any non-global _delegating handlers_ plus any globals that were in the `DelegatingHandlers` option array from [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json), ordered as they are in the `DelegatingHandlers` array.

3.   Tracing _delegating handler_, if enabled (refer to the [Tracing](https://ocelot.readthedocs.io/en/latest/features/tracing.html) chapter).

4.   Quality of Service _delegating handler_, if enabled (refer to the [Quality of Service](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html) chapter).

5.   The `HttpClient` sends the `HttpRequestMessage`.

Hopefully, other people will find this feature useful!

* * *
