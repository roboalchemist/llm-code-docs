# Source: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/overview?view=aspnetcore-10.0

Title: Web server implementations in ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/overview?view=aspnetcore-10.0

Markdown Content:
By [Tom Dykstra](https://github.com/tdykstra), [Steve Smith](https://ardalis.com/), [Stephen Halter](https://twitter.com/halter73), and [Chris Ross](https://github.com/Tratcher)

An ASP.NET Core app runs with an in-process HTTP server implementation. The server implementation listens for HTTP requests and surfaces them to the app as a set of [request features](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/request-features?view=aspnetcore-10.0) composed into an [HttpContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext).

*   [Windows](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/overview?view=aspnetcore-10.0#tabpanel_1_windows)
*   [macOS](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/overview?view=aspnetcore-10.0#tabpanel_1_macos)
*   [Linux](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/overview?view=aspnetcore-10.0#tabpanel_1_linux)

ASP.NET Core ships with [Kestrel server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0), which is the default, cross-platform HTTP server.

[Kestrel server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) is the default, cross-platform HTTP server implementation. Kestrel provides the best performance and memory utilization, but it doesn't have some of the advanced features in HTTP.sys. For more information, see [Kestrel vs. HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/overview?view=aspnetcore-10.0#korh) in this document.

Use Kestrel:

*   By itself as an edge server processing requests directly from a network, including the Internet.

![Image 1: Kestrel communicates directly with the Internet without a reverse proxy server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/_static/kestrel-to-internet2.png?view=aspnetcore-10.0)

*   With a _reverse proxy server_, such as [Internet Information Services (IIS)](https://www.iis.net/), [Nginx](https://nginx.org/), or [Apache](https://httpd.apache.org/). A reverse proxy server receives HTTP requests from the Internet and forwards them to Kestrel.

![Image 2: Kestrel communicates indirectly with the Internet through a reverse proxy server, such as IIS, Nginx, or Apache](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/_static/kestrel-to-internet.png?view=aspnetcore-10.0)

Either hosting configuration—with or without a reverse proxy server—is supported.

For Kestrel configuration guidance and information on when to use Kestrel in a reverse proxy configuration, see [Kestrel web server in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).

*   [Windows](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/overview?view=aspnetcore-10.0#tabpanel_2_windows)
*   [macOS](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/overview?view=aspnetcore-10.0#tabpanel_2_macos)
*   [Linux](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/overview?view=aspnetcore-10.0#tabpanel_2_linux)

ASP.NET Core ships with [Kestrel server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0), which is the default, cross-platform HTTP server.

For information on how to use Nginx on Linux as a reverse proxy server for Kestrel, see [Host ASP.NET Core on Linux with Nginx](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0).

If ASP.NET Core apps are run on Windows, HTTP.sys is an alternative to Kestrel. Kestrel is recommended over HTTP.sys unless the app requires features not available in Kestrel. For more information, see [HTTP.sys web server implementation in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0).

![Image 3: HTTP.sys communicates directly with the Internet](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/httpsys-to-internet.png?view=aspnetcore-10.0)

HTTP.sys can also be used for apps that are only exposed to an internal network.

![Image 4: HTTP.sys communicates directly with the internal network](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/httpsys-to-internal.png?view=aspnetcore-10.0)

For HTTP.sys configuration guidance, see [HTTP.sys web server implementation in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0).

The [IApplicationBuilder](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.iapplicationbuilder) available in the `Startup.Configure` method exposes the [ServerFeatures](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.iapplicationbuilder.serverfeatures#microsoft-aspnetcore-builder-iapplicationbuilder-serverfeatures) property of type [IFeatureCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.features.ifeaturecollection). Kestrel and HTTP.sys only expose a single feature each, [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature), but different server implementations may expose additional functionality.

`IServerAddressesFeature` can be used to find out which port the server implementation has bound at runtime.

If the built-in servers don't meet the app's requirements, a custom server implementation can be created. The [Open Web Interface for .NET (OWIN) guide](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/owin?view=aspnetcore-10.0) demonstrates how to write a [Nowin](https://github.com/Bobris/Nowin)-based [IServer](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.iserver) implementation. Only the feature interfaces that the app uses require implementation, though at a minimum [IHttpRequestFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.features.ihttprequestfeature) and [IHttpResponseFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.features.ihttpresponsefeature) must be supported.

The server is launched when the Integrated Development Environment (IDE) or editor starts the app:

*   [Visual Studio](https://visualstudio.microsoft.com/): Launch profiles can be used to start the app and server with either [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview)/[ASP.NET Core Module](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/aspnet-core-module?view=aspnetcore-10.0) or the console.
*   [Visual Studio Code](https://code.visualstudio.com/): The app and server are started by [Omnisharp](https://github.com/OmniSharp/omnisharp-vscode), which activates the CoreCLR debugger.

When launching the app from a command prompt in the project's folder, [dotnet run](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-run) launches the app and server (Kestrel and HTTP.sys only). The configuration is specified by the `-c|--configuration` option, which is set to either `Debug` (default) or `Release`.

A `launchSettings.json` file provides configuration when launching an app with `dotnet run` or with a debugger built into tooling, such as Visual Studio. If launch profiles are present in a `launchSettings.json` file, use the `--launch-profile {PROFILE NAME}` option with the `dotnet run` command or select the profile in Visual Studio. For more information, see [dotnet run](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-run) and [.NET distribution packaging](https://learn.microsoft.com/en-us/dotnet/core/build/distribution-packaging).

[HTTP/2](https://httpwg.org/specs/rfc7540.html) is supported with ASP.NET Core in the following deployment scenarios:

*   [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/http2?view=aspnetcore-10.0)
    *   Operating system 
        *   Windows Server 2016/Windows 10 or later†
        *   Linux with OpenSSL 1.0.2 or later (for example, Ubuntu 16.04 or later)
        *   macOS 10.15 or later

    *   Target framework: .NET Core 2.2 or later

*   [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later
    *   Target framework: Not applicable to HTTP.sys deployments.

*   [IIS (in-process)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later; IIS 10 or later
    *   Target framework: .NET Core 2.2 or later

*   [IIS (out-of-process)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later; IIS 10 or later
    *   Public-facing edge server connections use HTTP/2, but the reverse proxy connection to Kestrel uses HTTP/1.1.
    *   Target framework: Not applicable to IIS out-of-process deployments.

†Kestrel has limited support for HTTP/2 on Windows Server 2012 R2 and Windows 8.1. Support is limited because the list of supported TLS cipher suites available on these operating systems is limited. A certificate generated using an Elliptic Curve Digital Signature Algorithm (ECDSA) may be required to secure TLS connections.

*   [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/http2?view=aspnetcore-10.0)
    *   Operating system 
        *   Windows Server 2016/Windows 10 or later†
        *   Linux with OpenSSL 1.0.2 or later (for example, Ubuntu 16.04 or later)
        *   HTTP/2 will be supported on macOS in a future release.

    *   Target framework: .NET Core 2.2 or later

*   [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later
    *   Target framework: Not applicable to HTTP.sys deployments.

*   [IIS (in-process)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later; IIS 10 or later
    *   Target framework: .NET Core 2.2 or later

*   [IIS (out-of-process)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later; IIS 10 or later
    *   Public-facing edge server connections use HTTP/2, but the reverse proxy connection to Kestrel uses HTTP/1.1.
    *   Target framework: Not applicable to IIS out-of-process deployments.

†Kestrel has limited support for HTTP/2 on Windows Server 2012 R2 and Windows 8.1. Support is limited because the list of supported TLS cipher suites available on these operating systems is limited. A certificate generated using an Elliptic Curve Digital Signature Algorithm (ECDSA) may be required to secure TLS connections.

*   [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0#http2-support)
    *   Operating system 
        *   Windows Server 2016/Windows 10 or later†
        *   Linux with OpenSSL 1.0.2 or later (for example, Ubuntu 16.04 or later)
        *   HTTP/2 will be supported on macOS in a future release.

    *   Target framework: .NET Core 2.2 or later

*   [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later
    *   Target framework: Not applicable to HTTP.sys deployments.

*   [IIS (in-process)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later; IIS 10 or later
    *   Target framework: .NET Core 2.2 or later

*   [IIS (out-of-process)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later; IIS 10 or later
    *   Public-facing edge server connections use HTTP/2, but the reverse proxy connection to Kestrel uses HTTP/1.1.
    *   Target framework: Not applicable to IIS out-of-process deployments.

†Kestrel has limited support for HTTP/2 on Windows Server 2012 R2 and Windows 8.1. Support is limited because the list of supported TLS cipher suites available on these operating systems is limited. A certificate generated using an Elliptic Curve Digital Signature Algorithm (ECDSA) may be required to secure TLS connections.

*   [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later
    *   Target framework: Not applicable to HTTP.sys deployments.

*   [IIS (out-of-process)](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0#http2-support)
    *   Windows Server 2016/Windows 10 or later; IIS 10 or later
    *   Public-facing edge server connections use HTTP/2, but the reverse proxy connection to Kestrel uses HTTP/1.1.
    *   Target framework: Not applicable to IIS out-of-process deployments.

An HTTP/2 connection must use [Application-Layer Protocol Negotiation (ALPN)](https://tools.ietf.org/html/rfc7301#section-3) and TLS 1.2 or later. For more information, see the topics that pertain to your server deployment scenarios.

For guidance on creating a reliable, secure, performant, testable, and scalable ASP.NET Core app, see [Enterprise web app patterns](https://learn.microsoft.com/en-us/azure/architecture/web-apps/guides/enterprise-app-patterns/overview). A complete production-quality sample web app that implements the patterns is available.

*   [Kestrel web server in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0)
*   [ASP.NET Core Module (ANCM) for IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/aspnet-core-module?view=aspnetcore-10.0)
*   [Host ASP.NET Core on Windows with IIS](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/?view=aspnetcore-10.0)
*   [Deploy ASP.NET Core apps to Azure App Service](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/azure-apps/?view=aspnetcore-10.0)
*   [Host ASP.NET Core on Linux with Nginx](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0)
*   [HTTP.sys web server implementation in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0)
