# Source: https://ocelot.readthedocs.io/en/latest/features/websockets.html

Title: Websockets — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/websockets.html

Markdown Content:
> *   [WebSockets Standard](https://websockets.spec.whatwg.org/) by WHATWG organization
> 
> *   [The WebSocket Protocol](https://datatracker.ietf.org/doc/html/rfc6455) by Internet Engineering Task Force (IETF) organization

Ocelot supports proxying [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)[[1]](https://ocelot.readthedocs.io/en/latest/features/websockets.html#f1) with some extra bits.

Configuration[¶](https://ocelot.readthedocs.io/en/latest/features/websockets.html#configuration "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

To enable _WebSockets_ proxying with Ocelot, you need to do the following in your [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs):

var app = builder.Build();
app.UseWebSockets();await app.UseOcelot();
await app.RunAsync();

Then, in your [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json), add the following to proxy a route using _WebSockets_:

{
 "UpstreamPathTemplate": "/",
 "DownstreamPathTemplate": "/ws",
 "DownstreamScheme": "ws", "DownstreamHostAndPorts": [
 { "Host": "localhost", "Port": 5001 }
 ]
}

With this configuration, Ocelot will match any _WebSockets_ traffic that comes in on / and proxy it to `localhost:5001/ws`. For clarity, Ocelot will receive messages from the upstream client, proxy them to the downstream service, receive messages from the downstream service, and then proxy them back to the upstream client.

Handy Links[¶](https://ocelot.readthedocs.io/en/latest/features/websockets.html#handy-links "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

*   WHATWG: [WebSockets Standard](https://websockets.spec.whatwg.org/)

*   Mozilla Developer Network: [The WebSocket API (WebSockets)](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API)

*   Microsoft Learn: [WebSockets support in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/websockets)

*   Microsoft Learn: [WebSockets support in .NET](https://learn.microsoft.com/en-us/dotnet/fundamentals/networking/websockets)

SignalR [[2]](https://ocelot.readthedocs.io/en/latest/features/websockets.html#f2)[¶](https://ocelot.readthedocs.io/en/latest/features/websockets.html#signalr "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ocelot supports proxying _SignalR_. To enable this with Ocelot, you need to do the following:

First, install the [SignalR Client](https://www.nuget.org/packages/Microsoft.AspNetCore.SignalR.Client) NuGet package:

Install-Package Microsoft.AspNetCore.SignalR.Client

Second, you need to configure your application to use _SignalR_. A complete reference can be found here: [ASP.NET Core SignalR configuration](https://learn.microsoft.com/en-us/aspnet/core/signalr/configuration).

builder.Services.AddOcelot(builder.Configuration);
builder.Services.AddSignalR();

> **Note**: Make sure to pay attention to the transport-level configuration for _WebSockets_. Ensure that allowed transports are properly configured to enable _WebSockets_ connections: [ASP.NET Core SignalR configuration](https://learn.microsoft.com/en-us/aspnet/core/signalr/configuration).

Next, include the following in your [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json) file to proxy a route using _SignalR_. Note that standard Ocelot routing rules apply; the key aspect is that the scheme is set to `ws` (_WebSockets_).

{
 "UpstreamPathTemplate": "/gateway/{catchAll}",
 "DownstreamPathTemplate": "/{catchAll}",
 "DownstreamScheme": "ws", "DownstreamHostAndPorts": [
 { "Host": "localhost", "Port": 5001 }
 ]
}

WebSocket Secure[¶](https://ocelot.readthedocs.io/en/latest/features/websockets.html#websocket-secure "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

If you define a route with the _secured WebSockets_ protocol, use the `wss` scheme:

"DownstreamScheme": "wss",

Keep in mind that you can use WebSocket SSL for both [SignalR](https://ocelot.readthedocs.io/en/latest/features/websockets.html#ws-signalr) and [Websockets](https://ocelot.readthedocs.io/en/latest/features/websockets.html#).

If you want to ignore SSL warnings (errors) [[3]](https://ocelot.readthedocs.io/en/latest/features/websockets.html#f3), configure your route as follows:

"DownstreamScheme": "wss",
"DangerousAcceptAnyServerCertificateValidator": true,

_However, we strongly advise against this!_ Refer to the official notes regarding [SSL Errors](https://ocelot.readthedocs.io/en/latest/features/configuration.html#ssl-errors) in the [Configuration](https://ocelot.readthedocs.io/en/latest/features/configuration.html) documentation. There, you can also explore best practices tailored for your environments.

Supported[¶](https://ocelot.readthedocs.io/en/latest/features/websockets.html#supported "Link to this heading")
---------------------------------------------------------------------------------------------------------------

1.   [Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html)

2.   [Load Balancer](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html)

3.   [Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html)

This means you can configure your downstream services to run _WebSockets_ and either:

*   Include multiple `DownstreamHostAndPorts` in your route configuration.

*   Connect your route to a [Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html) provider. This allows you to load balance requests, which we think is pretty cool!

Not Supported[¶](https://ocelot.readthedocs.io/en/latest/features/websockets.html#not-supported "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Unfortunately, many Ocelot features are not specific to _WebSockets_, such as header handling and HTTP client functionalities. Below is a list of features that will not work:

1.   [Tracing](https://ocelot.readthedocs.io/en/latest/features/tracing.html)

2.   [Logging](https://ocelot.readthedocs.io/en/latest/features/logging.html)[Request ID](https://ocelot.readthedocs.io/en/latest/features/logging.html#lg-request-id)

3.   [Aggregation](https://ocelot.readthedocs.io/en/latest/features/aggregation.html)

4.   [Rate Limiting](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html)

5.   [Quality of Service](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html)

6.   [Middleware Injection](https://ocelot.readthedocs.io/en/latest/features/middlewareinjection.html)

7.   [Headers Transformation](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html)

8.   [Delegating Handlers](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html)

9.   [Claims Transformation](https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html)

10.   [Caching](https://ocelot.readthedocs.io/en/latest/features/caching.html)

11.   [Authentication](https://ocelot.readthedocs.io/en/latest/features/authentication.html)[[4]](https://ocelot.readthedocs.io/en/latest/features/websockets.html#f4)

12.   [Authorization](https://ocelot.readthedocs.io/en/latest/features/authorization.html)

We cannot be entirely sure how this feature will behave once it is widely used. Therefore, thorough testing is strongly recommended!

Roadmap[¶](https://ocelot.readthedocs.io/en/latest/features/websockets.html#roadmap "Link to this heading")
-----------------------------------------------------------------------------------------------------------

_WebSockets_ and _SignalR_ are being actively developed by the .NET community. It is important to stay updated with trends and regularly check for new releases in the official documentation:

*   [WebSockets docs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/websockets)

*   [SignalR docs](https://learn.microsoft.com/en-us/aspnet/core/signalr/introduction)

As a team, we are unable to provide direct development advice. However, feel free to ask questions or explore coding recipes in [Discussions](https://github.com/ThreeMammals/Ocelot/discussions) of the repository. Additionally, we welcome any bug reports, enhancement suggestions, or proposals related to this feature. [![Image 1: octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)](https://github.githubassets.com/images/icons/emoji/octocat.png)

Note

The Ocelot team considers the current implementation of the _WebSockets_ feature to be obsolete, as it is based on the [WebSocketsProxyMiddleware](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20WebSocketsProxyMiddleware&type=code) class. _WebSockets_ are a part of the ASP.NET Core framework, which includes the native [WebSocketMiddleware](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.websockets.websocketmiddleware) class. We have a strong intention to either migrate or redesign this feature. For more details, see issue [1707](https://github.com/ThreeMammals/Ocelot/issues/1707).

* * *
