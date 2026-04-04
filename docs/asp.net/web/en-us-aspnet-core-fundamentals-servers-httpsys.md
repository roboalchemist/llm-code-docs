# Source: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0

Title: HTTP.sys web server implementation in ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0

Markdown Content:
By [Tom Dykstra](https://github.com/tdykstra) and [Chris Ross](https://github.com/Tratcher)

[HTTP.sys](https://learn.microsoft.com/en-us/iis/get-started/introduction-to-iis/introduction-to-iis-architecture#hypertext-transfer-protocol-stack-httpsys) is a [web server for ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0) that only runs on Windows. HTTP.sys is an alternative to [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server and offers some features that Kestrel doesn't provide.

Important

HTTP.sys isn't compatible with the [ASP.NET Core Module](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/aspnet-core-module?view=aspnetcore-10.0) and can't be used with IIS or IIS Express.

HTTP.sys supports the following features:

*   [Windows Authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-10.0)
*   Port sharing
*   HTTPS with SNI
*   HTTP/2 over TLS (Windows 10 or later)
*   HTTP/3 over TLS (Windows 11 or later)
*   Direct file transmission
*   Response caching
*   WebSockets (Windows 8 or later)
*   Customizable security descriptors
*   Automatic memory pool eviction

Supported Windows versions:

*   Windows 7 or later
*   Windows Server 2008 R2 or later

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/servers/httpsys/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

HTTP.sys is useful for deployments where:

*   There's a need to expose the server directly to the Internet without using IIS.

![Image 1: HTTP.sys communicates directly with the Internet](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/httpsys-to-internet.png?view=aspnetcore-10.0)

*   An internal deployment requires a feature not available in Kestrel. For more information, see [Kestrel vs. HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0#kestrel-vs-httpsys)

![Image 2: HTTP.sys communicates directly with the internal network](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/httpsys-to-internal.png?view=aspnetcore-10.0)

HTTP.sys is mature technology that protects against many types of attacks and provides the robustness, security, and scalability of a full-featured web server. IIS itself runs as an HTTP listener on top of HTTP.sys.

[HTTP/2](https://httpwg.org/specs/rfc7540.html) is enabled for ASP.NET Core apps when the following base requirements are met:

*   Windows Server 2016/Windows 10 or later
*   [Application-Layer Protocol Negotiation (ALPN)](https://tools.ietf.org/html/rfc7301#section-3) connection
*   TLS 1.2 or later connection

If an HTTP/2 connection is established, [HttpRequest.Protocol](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httprequest.protocol) reports `HTTP/2`.

HTTP/2 is enabled by default. If an HTTP/2 connection isn't established, the connection falls back to HTTP/1.1. In a future release of Windows, HTTP/2 configuration flags will be available, including the ability to disable HTTP/2 with HTTP.sys.

[HTTP/3](https://datatracker.ietf.org/doc/rfc9114/) is enabled for ASP.NET Core apps when the following base requirements are met:

*   Windows Server 2022/Windows 11 or later
*   An `https` url binding is used.
*   The [EnableHttp3 registry key](https://techcommunity.microsoft.com/t5/networking-blog/enabling-http-3-support-on-windows-server-2022/ba-p/2676880) is set.

The preceding Windows 11 Build versions may require the use of a [Windows Insider](https://www.microsoft.com/en-us/windowsinsider/) build.

HTTP/3 is discovered as an upgrade from HTTP/1.1 or HTTP/2 via the `alt-svc` header. That means the first request will normally use HTTP/1.1 or HTTP/2 before switching to HTTP/3. Http.Sys doesn't automatically add the `alt-svc` header, it must be added by the application. The following code is a middleware example that adds the `alt-svc` response header.

```
app.Use((context, next) =>
{
    context.Response.Headers.AltSvc = "h3=\":443\"";
    return next(context);
});
```

Place the preceding code early in the request pipeline.

Http.Sys also supports sending an AltSvc HTTP/2 protocol message rather than a response header to notify the client that HTTP/3 is available. See the [EnableAltSvc registry key](https://techcommunity.microsoft.com/t5/networking-blog/enabling-http-3-support-on-windows-server-2022/ba-p/2676880). This requires netsh sslcert bindings that use host names rather than IP addresses.

HTTP.sys delegates to kernel mode authentication with the Kerberos authentication protocol. User mode authentication isn't supported with Kerberos and HTTP.sys. The machine account must be used to decrypt the Kerberos token/ticket that's obtained from Active Directory and forwarded by the client to the server to authenticate the user. Register the Service Principal Name (SPN) for the host, not the user of the app.

In some scenarios, high volumes of small writes with high latency can cause significant performance impact to `HTTP.sys`. This impact is due to the lack of a [Pipe](https://learn.microsoft.com/en-us/dotnet/api/system.io.pipelines.pipe) buffer in the `HTTP.sys` implementation. To improve performance in these scenarios, support for response buffering is included in `HTTP.sys`. Enable buffering by setting [HttpSysOptions.EnableKernelResponseBuffering](https://github.com/dotnet/aspnetcore/blob/main/src/Servers/HttpSys/src/HttpSysOptions.cs#L120) to `true`. Response buffering should be enabled by an app that does synchronous I/O, or asynchronous I/O with no more than one outstanding write at a time. In these scenarios, response buffering can significantly improve throughput over high-latency connections.

Apps that use asynchronous I/O and that may have more than one write outstanding at a time should **_not_** use this flag. Enabling this flag can result in higher CPU and memory usage by HTTP.Sys.

Call the [UseHttpSys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.webhostbuilderhttpsysextensions.usehttpsys) extension method when building the host, specifying any required [HttpSysOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions). The following example sets options to their default values:

```
using Microsoft.AspNetCore.Hosting.Server;
using Microsoft.AspNetCore.Hosting.Server.Features;
using Microsoft.AspNetCore.Http.Features;
using Microsoft.AspNetCore.Server.HttpSys;

var builder = WebApplication.CreateBuilder(args);

builder.WebHost.UseHttpSys(options =>
{
    options.AllowSynchronousIO = false;
    options.Authentication.Schemes = AuthenticationSchemes.None;
    options.Authentication.AllowAnonymous = true;
    options.MaxConnections = null;
    options.MaxRequestBodySize = 30_000_000;
    options.UrlPrefixes.Add("http://localhost:5005");
});

builder.Services.AddRazorPages();

var app = builder.Build();
```

Additional HTTP.sys configuration is handled through [registry settings](https://support.microsoft.com/help/820129/http-sys-registry-settings-for-windows).

For more information about HTTP.sys options, see [HttpSysOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions).

A _request queue_ in HTTP.sys is a kernel-level structure that temporarily stores incoming HTTP requests until your application is ready to process them. Manage access to the request queue by using the [RequestQueueSecurityDescriptor](https://source.dot.net/#Microsoft.AspNetCore.Server.HttpSys/HttpSysOptions.cs,a556950881fd2d87) property on [HttpSysOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions). Set it to a [GenericSecurityDescriptor](https://learn.microsoft.com/en-us/dotnet/api/system.security.accesscontrol.genericsecuritydescriptor) instance when configuring your HTTP.sys server.

By customizing the security descriptor, you can allow or deny specific users or groups access to the request queue. This is useful in scenarios where you want to restrict or delegate HTTP.sys request handling at the operating system level.

For example, the following code allows all authenticated users but denies guests:

```
using System.Security.AccessControl;
using System.Security.Principal;
using Microsoft.AspNetCore.Server.HttpSys;

// Create a new security descriptor
var securityDescriptor = new CommonSecurityDescriptor(isContainer: false, isDS: false, sddlForm: string.Empty);

// Create a discretionary access control list (DACL)
var dacl = new DiscretionaryAcl(isContainer: false, isDS: false, capacity: 2);
dacl.AddAccess(
    AccessControlType.Allow,
    new SecurityIdentifier(WellKnownSidType.BuiltinUsersSid, null),
    -1,
    InheritanceFlags.None,
    PropagationFlags.None
);
dacl.AddAccess(
    AccessControlType.Deny,
    new SecurityIdentifier(WellKnownSidType.BuiltinGuestsSid, null),
    -1,
    InheritanceFlags.None,
    PropagationFlags.None
);

// Assign the DACL to the security descriptor
securityDescriptor.DiscretionaryAcl = dacl;

// Configure HTTP.sys options
var builder = WebApplication.CreateBuilder();
builder.WebHost.UseHttpSys(options =>
{
    options.RequestQueueSecurityDescriptor = securityDescriptor;
});
```

The `RequestQueueSecurityDescriptor` property applies only when creating a new request queue. The property doesn't affect existing request queues.

**MaxRequestBodySize**

The maximum allowed size of any request body in bytes. When set to `null`, the maximum request body size is unlimited. This limit has no effect on upgraded connections, which are always unlimited.

The recommended method to override the limit in an ASP.NET Core MVC app for a single `IActionResult` is to use the [RequestSizeLimitAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.requestsizelimitattribute) attribute on an action method:

```
[RequestSizeLimit(100000000)]
public IActionResult MyActionMethod()
```

An exception is thrown if the app attempts to configure the limit on a request after the app has started reading the request. An `IsReadOnly` property can be used to indicate if the `MaxRequestBodySize` property is in a read-only state, meaning it's too late to configure the limit.

If the app should override [MaxRequestBodySize](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.maxrequestbodysize#microsoft-aspnetcore-server-httpsys-httpsysoptions-maxrequestbodysize) per-request, use the [IHttpMaxRequestBodySizeFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.features.ihttpmaxrequestbodysizefeature):

```
app.Use((context, next) =>
{
    context.Features.GetRequiredFeature<IHttpMaxRequestBodySizeFeature>()
                                             .MaxRequestBodySize = 10 * 1024;

    var server = context.RequestServices
        .GetRequiredService<IServer>();
    var serverAddressesFeature = server.Features
                                 .GetRequiredFeature<IServerAddressesFeature>();

    var addresses = string.Join(", ", serverAddressesFeature.Addresses);

    var loggerFactory = context.RequestServices
        .GetRequiredService<ILoggerFactory>();
    var logger = loggerFactory.CreateLogger("Sample");

    logger.LogInformation("Addresses: {addresses}", addresses);

    return next(context);
});
```

If using Visual Studio, make sure the app isn't configured to run IIS or IIS Express.

In Visual Studio, the default launch profile is for IIS Express. To run the project as a console app, manually change the selected profile, as shown in the following screenshot:

![Image 3: Select console app profile](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/vs-choose-profile.png?view=aspnetcore-10.0)

1.   Determine the ports to open for the app and use [Windows Firewall](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/create-an-inbound-port-rule) or the [New-NetFirewallRule](https://learn.microsoft.com/en-us/powershell/module/netsecurity/new-netfirewallrule) PowerShell cmdlet to open firewall ports to allow traffic to reach HTTP.sys. In the following commands and app configuration, port 443 is used.

2.   When deploying to an Azure VM, open the ports in the [Network Security Group](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/nsg-quickstart-portal). In the following commands and app configuration, port 443 is used.

3.   Obtain and install X.509 certificates, if required.

On Windows, create self-signed certificates using the [New-SelfSignedCertificate PowerShell cmdlet](https://learn.microsoft.com/en-us/powershell/module/pki/new-selfsignedcertificate). For an unsupported example, see [UpdateIISExpressSSLForChrome.ps1](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/includes/make-x509-cert/UpdateIISExpressSSLForChrome.ps1).

Install either self-signed or CA-signed certificates in the server's **Local Machine**>**Personal** store.

4.   If the app is a [framework-dependent deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/#framework-dependent-deployments-fdd), install .NET, .NET Framework, or both (if the app is a .NET app targeting the .NET Framework).

    *   **.NET**: If the app requires .NET, obtain and run the **.NET Runtime** installer from [.NET Downloads](https://dotnet.microsoft.com/download). Don't install the full SDK on the server.
    *   **.NET Framework**: If the app requires .NET Framework, see the [.NET Framework installation guide](https://learn.microsoft.com/en-us/dotnet/framework/install/). Install the required .NET Framework. The installer for the latest .NET Framework is available from the [.NET Downloads](https://dotnet.microsoft.com/download) page.

If the app is a [self-contained deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/#self-contained-deployments-scd), the app includes the runtime in its deployment. No framework installation is required on the server.

5.   Configure URLs and ports in the app.

By default, ASP.NET Core binds to `http://localhost:5000`. To configure URL prefixes and ports, options include:

    *   [UseUrls](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.hostingabstractionswebhostbuilderextensions.useurls)
    *   `urls` command-line argument
    *   `ASPNETCORE_URLS` environment variable
    *   [UrlPrefixes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.urlprefixes#microsoft-aspnetcore-server-httpsys-httpsysoptions-urlprefixes)

The following code example shows how to use [UrlPrefixes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.urlprefixes#microsoft-aspnetcore-server-httpsys-httpsysoptions-urlprefixes) with the server's local IP address `10.0.0.4` on port 443:

```
var builder = WebApplication.CreateBuilder(args);

builder.WebHost.UseHttpSys(options =>
{
    options.UrlPrefixes.Add("https://10.0.0.4:443");
});

builder.Services.AddRazorPages();

var app = builder.Build();
```

An advantage of `UrlPrefixes` is that an error message is generated immediately for improperly formatted prefixes.

The settings in `UrlPrefixes` override `UseUrls`/`urls`/`ASPNETCORE_URLS` settings. Therefore, an advantage of `UseUrls`, `urls`, and the `ASPNETCORE_URLS` environment variable is that it's easier to switch between Kestrel and HTTP.sys.

HTTP.sys recognizes two types of wild cards in URL prefixes:

    *   `*` is a _weak binding_, also known as a _fallback binding_. If the URL prefix is `http://*:5000`, and something else is bound to port 5000, this binding won't be used.
    *   `+` is a _strong binding_. If the URL prefix is `http://+:5000`, this binding will be used before other port 5000 bindings.

For more information, see [UrlPrefix Strings](https://learn.microsoft.com/en-us/windows/win32/http/urlprefix-strings).

Warning

Top-level wildcard bindings (`http://*:80/` and `http://+:80`) should **not** be used. Top-level wildcard bindings create app security vulnerabilities. This applies to both strong and weak wildcards. Use explicit host names or IP addresses rather than wildcards. Subdomain wildcard binding (for example, `*.mysub.com`) isn't a security risk if you control the entire parent domain (as opposed to `*.com`, which is vulnerable). For more information, see [RFC 9110: Section 7.2: Host and :authority](https://www.rfc-editor.org/rfc/rfc9110#field.host).

Apps and containers are often given only a port to listen on, like port 80, without additional constraints like host or path. HTTP_PORTS and HTTPS_PORTS are config keys that specify the listening ports for the Kestrel and HTTP.sys servers. These keys may be specified as environment variables defined with the `DOTNET_` or `ASPNETCORE_` prefixes, or specified directly through any other config input, such as `appsettings.json`. Each is a semicolon-delimited list of port values, as shown in the following example:

```
ASPNETCORE_HTTP_PORTS=80;8080
ASPNETCORE_HTTPS_PORTS=443;8081
```

The preceding example is shorthand for the following configuration, which specifies the scheme (HTTP or HTTPS) and any host or IP.

```
ASPNETCORE_URLS=http://*:80/;http://*:8080/;https://*:443/;https://*:8081/
```

The HTTP_PORTS and HTTPS_PORTS configuration keys are lower priority and are overridden by URLS or values provided directly in code. Certificates still need to be configured separately via server-specific mechanics for HTTPS.

These configuration keys are equivalent to top-level wildcard bindings. They're convenient for development and container scenarios, but avoid wildcards when running on a machine that may also host other services.

6.   Preregister URL prefixes on the server.

The built-in tool for configuring HTTP.sys is _netsh.exe_. _netsh.exe_ is used to reserve URL prefixes and assign X.509 certificates. The tool requires administrator privileges.

Use the _netsh.exe_ tool to register URLs for the app:

```
netsh http add urlacl url=<URL> user=<USER>
```

    *   `<URL>`: The fully qualified Uniform Resource Locator (URL). Don't use a wildcard binding. Use a valid hostname or local IP address. _The URL must include a trailing slash._
    *   `<USER>`: Specifies the user or user-group name.

In the following example, the local IP address of the server is `10.0.0.4`:

```
netsh http add urlacl url=https://10.0.0.4:443/ user=Users
```

When a URL is registered, the tool responds with `URL reservation successfully added`.

To delete a registered URL, use the `delete urlacl` command:

```
netsh http delete urlacl url=<URL>
```
7.   Register X.509 certificates on the server.

Use the _netsh.exe_ tool to register certificates for the app:

```
netsh http add sslcert ipport=<IP>:<PORT> certhash=<THUMBPRINT> appid="{<GUID>}"
```

    *   `<IP>`: Specifies the local IP address for the binding. Don't use a wildcard binding. Use a valid IP address.
    *   `<PORT>`: Specifies the port for the binding.
    *   `<THUMBPRINT>`: The X.509 certificate thumbprint.
    *   `<GUID>`: A developer-generated GUID to represent the app for informational purposes.

For reference purposes, store the GUID in the app as a package tag:

    *   In Visual Studio: 
        *   Open the app's project properties by right-clicking on the app in **Solution Explorer** and selecting **Properties**.
        *   Select the **Package** tab.
        *   Enter the GUID that you created in the **Tags** field.

    *   When not using Visual Studio: 
        *   Open the app's project file.

        *   Add a `<PackageTags>` property to a new or existing `<PropertyGroup>` with the GUID that you created:

```
<PropertyGroup>
  <PackageTags>00001111-aaaa-2222-bbbb-3333cccc4444</PackageTags>
</PropertyGroup>
```

In the following example:

    *   The local IP address of the server is `10.0.0.4`.
    *   An online random GUID generator provides the `appid` value.

```
netsh http add sslcert 
    ipport=10.0.0.4:443 
    certhash=b66ee04419d4ee37464ab8785ff02449980eae10 
    appid="{00001111-aaaa-2222-bbbb-3333cccc4444}"
```

When a certificate is registered, the tool responds with `SSL Certificate successfully added`.

To delete a certificate registration, use the `delete sslcert` command:

```
netsh http delete sslcert ipport=<IP>:<PORT>
```

Reference documentation for _netsh.exe_:

    *   [Netsh Commands for Hypertext Transfer Protocol (HTTP)](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc725882(v=ws.10))
    *   [UrlPrefix Strings](https://learn.microsoft.com/en-us/windows/win32/http/urlprefix-strings)

8.   Run the app.

Administrator privileges aren't required to run the app when binding to localhost using HTTP (not HTTPS) with a port number greater than 1024. For other configurations (for example, using a local IP address or binding to port 443), run the app with administrator privileges.

The app responds at the server's public IP address. In this example, the server is reached from the Internet at its public IP address of `104.214.79.47`.

A development certificate is used in this example. The page loads securely after bypassing the browser's untrusted certificate warning.

![Image 4: Browser window showing the app's Index page loaded](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/browser.png?view=aspnetcore-10.0)

For apps hosted by HTTP.sys that interact with requests from the Internet or a corporate network, additional configuration might be required when hosting behind proxy servers and load balancers. For more information, see [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0).

[IHttpSysRequestTimingFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.ihttpsysrequesttimingfeature) provides detailed timing information for requests:

*   Timestamps are obtained using [QueryPerformanceCounter](https://learn.microsoft.com/en-us/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter).
*   The timestamp frequency can be obtained via [QueryPerformanceFrequency](https://learn.microsoft.com/en-us/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency).
*   The index of the timing can be cast to [HttpSysRequestTimingType](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysrequesttimingtype) to know what the timing represents.
*   The value may be 0 if the timing isn't available for the current request.
*   Requires Windows 10 version 2004, Windows Server 2022, or later.

```
using Microsoft.AspNetCore.Http.Features;
using Microsoft.AspNetCore.Server.HttpSys;

var builder = WebApplication.CreateBuilder(args);

builder.WebHost.UseHttpSys();

var app = builder.Build();

app.Use((context, next) =>
{
    var feature = context.Features.GetRequiredFeature<IHttpSysRequestTimingFeature>();
    
    var loggerFactory = context.RequestServices.GetRequiredService<ILoggerFactory>();
    var logger = loggerFactory.CreateLogger("Sample");

    var timestamps = feature.Timestamps;

    for (var i = 0; i < timestamps.Length; i++)
    {
        var timestamp = timestamps[i];
        var timingType = (HttpSysRequestTimingType)i;

        logger.LogInformation("Timestamp {timingType}: {timestamp}",
                                          timingType, timestamp);
    }

    return next(context);
});

app.MapGet("/", () => Results.Ok());

app.Run();
```

[IHttpSysRequestTimingFeature.TryGetTimestamp](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.ihttpsysrequesttimingfeature.trygettimestamp) retrieves the timestamp for the provided timing type:

```
using Microsoft.AspNetCore.Http.Features;
using Microsoft.AspNetCore.Server.HttpSys;
var builder = WebApplication.CreateBuilder(args);

builder.WebHost.UseHttpSys();

var app = builder.Build();

app.Use((context, next) =>
{
    var feature = context.Features.GetRequiredFeature<IHttpSysRequestTimingFeature>();

    var loggerFactory = context.RequestServices.GetRequiredService<ILoggerFactory>();
    var logger = loggerFactory.CreateLogger("Sample");

    var timingType = HttpSysRequestTimingType.RequestRoutingEnd;

    if (feature.TryGetTimestamp(timingType, out var timestamp))
    {
        logger.LogInformation("Timestamp {timingType}: {timestamp}",
                                          timingType, timestamp);
    }
    else
    {
        logger.LogInformation("Timestamp {timingType}: not available for the "
                                           + "current request",    timingType);
    }

    return next(context);
});

app.MapGet("/", () => Results.Ok());

app.Run();
```

[IHttpSysRequestTimingFeature.TryGetElapsedTime](/dotnet/api/microsoft.aspnetcore.server.httpsys.ihttpsysrequesttimingfeature.trygetelapsedtime yields the elapsed time between two specified timings:

```
using Microsoft.AspNetCore.Http.Features;
using Microsoft.AspNetCore.Server.HttpSys;

var builder = WebApplication.CreateBuilder(args);

builder.WebHost.UseHttpSys();

var app = builder.Build();

app.Use((context, next) =>
{
    var feature = context.Features.GetRequiredFeature<IHttpSysRequestTimingFeature>();

    var loggerFactory = context.RequestServices.GetRequiredService<ILoggerFactory>();
    var logger = loggerFactory.CreateLogger("Sample");

    var startingTimingType = HttpSysRequestTimingType.RequestRoutingStart;
    var endingTimingType = HttpSysRequestTimingType.RequestRoutingEnd;

    if (feature.TryGetElapsedTime(startingTimingType, endingTimingType, out var elapsed))
    {
        logger.LogInformation(
            "Elapsed time {startingTimingType} to {endingTimingType}: {elapsed}",
            startingTimingType,
            endingTimingType,
            elapsed);
    }
    else
    {
        logger.LogInformation(
            "Elapsed time {startingTimingType} to {endingTimingType}:"
            + " not available for the current request.",
            startingTimingType,
            endingTimingType);
    }

    return next(context);
});

app.MapGet("/", () => Results.Ok());

app.Run();
```

Additional HTTP/2 features in HTTP.sys support gRPC, including support for response trailers and sending reset frames.

Requirements to run gRPC with HTTP.sys:

*   Windows 11 Build 22000 or later, Windows Server 2022 Build 20348 or later.
*   TLS 1.2 or later connection.

HTTP Trailers are similar to HTTP Headers, except they are sent after the response body is sent. For IIS and HTTP.sys, only HTTP/2 response trailers are supported.

```
if (httpContext.Response.SupportsTrailers())
{
    httpContext.Response.DeclareTrailer("trailername");	

    // Write body
    httpContext.Response.WriteAsync("Hello world");

    httpContext.Response.AppendTrailer("trailername", "TrailerValue");
}
```

In the preceding example code:

*   `SupportsTrailers` ensures that trailers are supported for the response.
*   `DeclareTrailer` adds the given trailer name to the `Trailer` response header. Declaring a response's trailers is optional, but recommended. If `DeclareTrailer` is called, it must be before the response headers are sent.
*   `AppendTrailer` appends the trailer.

Reset allows for the server to reset a HTTP/2 request with a specified error code. A reset request is considered aborted.

```
var resetFeature = httpContext.Features.Get<IHttpResetFeature>();
resetFeature.Reset(errorCode: 2);
```

`Reset` in the preceding code example specifies the `INTERNAL_ERROR` error code. For more information about HTTP/2 error codes, visit the [HTTP/2 specification error code section](https://tools.ietf.org/html/rfc7540#page-50).

For information about how to get traces from HTTP.sys, see [HTTP.sys Manageability Scenarios](https://learn.microsoft.com/en-us/windows/win32/http/http-sys-manageability-scenarios).

The memory pools used by Kestrel, IIS, and HTTP.sys automatically evict memory blocks when the application is idle or under low load. The feature runs automatically and doesn't need to be enabled or configured manually.

In versions of .NET earlier than 10, memory allocated by the pool remains reserved, even when not in use. This automatic eviction feature reduces overall memory usage and helps applications stay responsive under varying workloads.

The default memory pool used by the ASP.NET Core server implementations includes metrics, which can be used to monitor and analyze memory usage patterns. The metrics are under the name `"Microsoft.AspNetCore.MemoryPool"`.

For information about metrics and how to use them, see [ASP.NET Core metrics](https://learn.microsoft.com/en-us/aspnet/core/log-mon/metrics/metrics?view=aspnetcore-10.0).

Besides using memory pools efficiently by evicting unneeded memory blocks, ASP.NET Core provides a built-in [IMemoryPoolFactory](https://source.dot.net/#Microsoft.AspNetCore.Connections.Abstractions/IMemoryPoolFactory.cs) and an implementation. It makes the implementation available to your application through dependency injection.

The following code example shows a simple background service that uses the built-in memory pool factory implementation to create memory pools. These pools benefit from the automatic eviction feature:

```
public class MyBackgroundService : BackgroundService
{
    private readonly MemoryPool<byte> _memoryPool;

    public MyBackgroundService(IMemoryPoolFactory<byte> factory)
    {
        _memoryPool = factory.Create();
    }

    protected override async Task ExecuteAsync(CancellationToken stoppingToken)
    {
        while (!stoppingToken.IsCancellationRequested)
        {
            try
            {
                await Task.Delay(20, stoppingToken);
                // do work that needs memory
                // consider checking _memoryPool.MaxBufferSize
                var rented = _memoryPool.Rent(100);
                rented.Dispose();
            }
            catch (OperationCanceledException)
            {
                return;
            }
        }
    }
}
```

To use a custom memory pool factory, make a class that implements `IMemoryPoolFactory` and register it with dependency injection, as the following example does. Memory pools created this way do not benefit from the automatic eviction feature unless you implement similar eviction logic in your custom factory:

```
services.AddSingleton<IMemoryPoolFactory<byte>,
CustomMemoryPoolFactory>();

public class CustomMemoryPoolFactory : IMemoryPoolFactory<byte>
{
    public MemoryPool<byte> Create()
    {
        // Return a custom MemoryPool implementation
        // or the default, as is shown here.
        return MemoryPool<byte>.Shared;
    }
}
```

When you're using a memory pool, be aware of the pool's [MaxBufferSize](https://learn.microsoft.com/en-us/dotnet/api/system.buffers.memorypool-1.maxbuffersize#system-buffers-memorypool-1-maxbuffersize).

*   [Enable Windows Authentication with HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-10.0#httpsys)
*   [HTTP Server API](https://learn.microsoft.com/en-us/windows/win32/http/http-api-start-page)
*   [aspnet/HttpSysServer GitHub repository (source code)](https://github.com/aspnet/HttpSysServer/)
*   [The host](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#host)
*   [Troubleshoot and debug ASP.NET Core projects](https://learn.microsoft.com/en-us/aspnet/core/test/troubleshoot?view=aspnetcore-10.0)

[HTTP.sys](https://learn.microsoft.com/en-us/iis/get-started/introduction-to-iis/introduction-to-iis-architecture#hypertext-transfer-protocol-stack-httpsys) is a [web server for ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0) that only runs on Windows. HTTP.sys is an alternative to [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server and offers some features that Kestrel doesn't provide.

Important

HTTP.sys isn't compatible with the [ASP.NET Core Module](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/aspnet-core-module?view=aspnetcore-10.0) and can't be used with IIS or IIS Express.

HTTP.sys supports the following features:

*   [Windows Authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-10.0)
*   Port sharing
*   HTTPS with SNI
*   HTTP/2 over TLS (Windows 10 or later)
*   Direct file transmission
*   Response caching
*   WebSockets (Windows 8 or later)

Supported Windows versions:

*   Windows 7 or later
*   Windows Server 2008 R2 or later

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/servers/httpsys/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

HTTP.sys is useful for deployments where:

*   There's a need to expose the server directly to the Internet without using IIS.

![Image 5: HTTP.sys communicates directly with the Internet](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/httpsys-to-internet.png?view=aspnetcore-10.0)

*   An internal deployment requires a feature not available in Kestrel. For more information, see [Kestrel vs. HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0#kestrel-vs-httpsys)

![Image 6: HTTP.sys communicates directly with the internal network](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/httpsys-to-internal.png?view=aspnetcore-10.0)

HTTP.sys is mature technology that protects against many types of attacks and provides the robustness, security, and scalability of a full-featured web server. IIS itself runs as an HTTP listener on top of HTTP.sys.

[HTTP/2](https://httpwg.org/specs/rfc7540.html) is enabled for ASP.NET Core apps when the following base requirements are met:

*   Windows Server 2016/Windows 10 or later
*   [Application-Layer Protocol Negotiation (ALPN)](https://tools.ietf.org/html/rfc7301#section-3) connection
*   TLS 1.2 or later connection

If an HTTP/2 connection is established, [HttpRequest.Protocol](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httprequest.protocol) reports `HTTP/2`.

HTTP/2 is enabled by default. If an HTTP/2 connection isn't established, the connection falls back to HTTP/1.1. In a future release of Windows, HTTP/2 configuration flags will be available, including the ability to disable HTTP/2 with HTTP.sys.

[HTTP/3](https://datatracker.ietf.org/doc/rfc9114/) is enabled for ASP.NET Core apps when the following base requirements are met:

*   Windows Server 2022/Windows 11 or later
*   An `https` url binding is used.
*   The [EnableHttp3 registry key](https://techcommunity.microsoft.com/t5/networking-blog/enabling-http-3-support-on-windows-server-2022/ba-p/2676880) is set.

The preceding Windows 11 Build versions may require the use of a [Windows Insider](https://insider.windows.com/) build.

HTTP/3 is discovered as an upgrade from HTTP/1.1 or HTTP/2 via the `alt-svc` header. That means the first request will normally use HTTP/1.1 or HTTP/2 before switching to HTTP/3. Http.Sys doesn't automatically add the `alt-svc` header, it must be added by the application. The following code is a middleware example that adds the `alt-svc` response header.

```
app.Use((context, next) =>
{
    context.Response.Headers.AltSvc = "h3=\":443\"";
    return next(context);
});
```

Place the preceding code early in the request pipeline.

Http.Sys also supports sending an AltSvc HTTP/2 protocol message rather than a response header to notify the client that HTTP/3 is available. See the [EnableAltSvc registry key](https://techcommunity.microsoft.com/t5/networking-blog/enabling-http-3-support-on-windows-server-2022/ba-p/2676880). This requires netsh sslcert bindings that use host names rather than IP addresses.

HTTP.sys delegates to kernel mode authentication with the Kerberos authentication protocol. User mode authentication isn't supported with Kerberos and HTTP.sys. The machine account must be used to decrypt the Kerberos token/ticket that's obtained from Active Directory and forwarded by the client to the server to authenticate the user. Register the Service Principal Name (SPN) for the host, not the user of the app.

Call the [UseHttpSys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.webhostbuilderhttpsysextensions.usehttpsys) extension method when building the host, specifying any required [HttpSysOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions). The following example sets options to their default values:

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseHttpSys(options =>
            {
                options.AllowSynchronousIO = false;
                options.Authentication.Schemes = AuthenticationSchemes.None;
                options.Authentication.AllowAnonymous = true;
                options.MaxConnections = null;
                options.MaxRequestBodySize = 30000000;
                options.UrlPrefixes.Add("http://localhost:5005");
            });
            webBuilder.UseStartup<Startup>();
        });
```

Additional HTTP.sys configuration is handled through [registry settings](https://support.microsoft.com/help/820129/http-sys-registry-settings-for-windows).

For more information about HTTP.sys options, see [HttpSysOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions).

**MaxRequestBodySize**

The maximum allowed size of any request body in bytes. When set to `null`, the maximum request body size is unlimited. This limit has no effect on upgraded connections, which are always unlimited.

The recommended method to override the limit in an ASP.NET Core MVC app for a single `IActionResult` is to use the [RequestSizeLimitAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.requestsizelimitattribute) attribute on an action method:

```
[RequestSizeLimit(100000000)]
public IActionResult MyActionMethod()
```

An exception is thrown if the app attempts to configure the limit on a request after the app has started reading the request. An `IsReadOnly` property can be used to indicate if the `MaxRequestBodySize` property is in a read-only state, meaning it's too late to configure the limit.

If the app should override [MaxRequestBodySize](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.maxrequestbodysize#microsoft-aspnetcore-server-httpsys-httpsysoptions-maxrequestbodysize) per-request, use the [IHttpMaxRequestBodySizeFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.features.ihttpmaxrequestbodysizefeature):

```
public void Configure(IApplicationBuilder app, IWebHostEnvironment env, 
    ILogger<Startup> logger, IServer server)
{
    app.Use(async (context, next) =>
    {
        context.Features.Get<IHttpMaxRequestBodySizeFeature>()
            .MaxRequestBodySize = 10 * 1024;

        var serverAddressesFeature = 
            app.ServerFeatures.Get<IServerAddressesFeature>();
        var addresses = string.Join(", ", serverAddressesFeature?.Addresses);

        logger.LogInformation("Addresses: {Addresses}", addresses);

        await next.Invoke();
    });

    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
    else
    {
        app.UseExceptionHandler("/Error");
    }

    app.UseStaticFiles();
    app.UseRouting();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapRazorPages();
    });
}
```

If using Visual Studio, make sure the app isn't configured to run IIS or IIS Express.

In Visual Studio, the default launch profile is for IIS Express. To run the project as a console app, manually change the selected profile, as shown in the following screenshot:

![Image 7: Select console app profile](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/vs-choose-profile.png?view=aspnetcore-10.0)

1.   Determine the ports to open for the app and use [Windows Firewall](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/create-an-inbound-port-rule) or the [New-NetFirewallRule](https://learn.microsoft.com/en-us/powershell/module/netsecurity/new-netfirewallrule) PowerShell cmdlet to open firewall ports to allow traffic to reach HTTP.sys. In the following commands and app configuration, port 443 is used.

2.   When deploying to an Azure VM, open the ports in the [Network Security Group](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/nsg-quickstart-portal). In the following commands and app configuration, port 443 is used.

3.   Obtain and install X.509 certificates, if required.

On Windows, create self-signed certificates using the [New-SelfSignedCertificate PowerShell cmdlet](https://learn.microsoft.com/en-us/powershell/module/pki/new-selfsignedcertificate). For an unsupported example, see [UpdateIISExpressSSLForChrome.ps1](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/includes/make-x509-cert/UpdateIISExpressSSLForChrome.ps1).

Install either self-signed or CA-signed certificates in the server's **Local Machine**>**Personal** store.

4.   If the app is a [framework-dependent deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/#framework-dependent-deployments-fdd), install .NET, .NET Framework, or both (if the app is a .NET app targeting the .NET Framework).

    *   **.NET**: If the app requires .NET, obtain and run the **.NET Runtime** installer from [.NET Downloads](https://dotnet.microsoft.com/download). Don't install the full SDK on the server.
    *   **.NET Framework**: If the app requires .NET Framework, see the [.NET Framework installation guide](https://learn.microsoft.com/en-us/dotnet/framework/install/). Install the required .NET Framework. The installer for the latest .NET Framework is available from the [.NET Downloads](https://dotnet.microsoft.com/download) page.

If the app is a [self-contained deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/#self-contained-deployments-scd), the app includes the runtime in its deployment. No framework installation is required on the server.

5.   Configure URLs and ports in the app.

By default, ASP.NET Core binds to `http://localhost:5000`. To configure URL prefixes and ports, options include:

    *   [UseUrls](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.hostingabstractionswebhostbuilderextensions.useurls)
    *   `urls` command-line argument
    *   `ASPNETCORE_URLS` environment variable
    *   [UrlPrefixes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.urlprefixes#microsoft-aspnetcore-server-httpsys-httpsysoptions-urlprefixes)

The following code example shows how to use [UrlPrefixes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.urlprefixes#microsoft-aspnetcore-server-httpsys-httpsysoptions-urlprefixes) with the server's local IP address `10.0.0.4` on port 443:

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseHttpSys(options =>
            {
                options.UrlPrefixes.Add("https://10.0.0.4:443");
            });
            webBuilder.UseStartup<Startup>();
        });
```

An advantage of `UrlPrefixes` is that an error message is generated immediately for improperly formatted prefixes.

The settings in `UrlPrefixes` override `UseUrls`/`urls`/`ASPNETCORE_URLS` settings. Therefore, an advantage of `UseUrls`, `urls`, and the `ASPNETCORE_URLS` environment variable is that it's easier to switch between Kestrel and HTTP.sys.

HTTP.sys uses the [HTTP Server API UrlPrefix string formats](https://learn.microsoft.com/en-us/windows/win32/http/urlprefix-strings).

Warning

Top-level wildcard bindings (`http://*:80/` and `http://+:80`) should **not** be used. Top-level wildcard bindings create app security vulnerabilities. This applies to both strong and weak wildcards. Use explicit host names or IP addresses rather than wildcards. Subdomain wildcard binding (for example, `*.mysub.com`) isn't a security risk if you control the entire parent domain (as opposed to `*.com`, which is vulnerable). For more information, see [RFC 9110: Section 7.2: Host and :authority](https://www.rfc-editor.org/rfc/rfc9110#field.host).

6.   Preregister URL prefixes on the server.

The built-in tool for configuring HTTP.sys is _netsh.exe_. _netsh.exe_ is used to reserve URL prefixes and assign X.509 certificates. The tool requires administrator privileges.

Use the _netsh.exe_ tool to register URLs for the app:

```
netsh http add urlacl url=<URL> user=<USER>
```

    *   `<URL>`: The fully qualified Uniform Resource Locator (URL). Don't use a wildcard binding. Use a valid hostname or local IP address. _The URL must include a trailing slash._
    *   `<USER>`: Specifies the user or user-group name.

In the following example, the local IP address of the server is `10.0.0.4`:

```
netsh http add urlacl url=https://10.0.0.4:443/ user=Users
```

When a URL is registered, the tool responds with `URL reservation successfully added`.

To delete a registered URL, use the `delete urlacl` command:

```
netsh http delete urlacl url=<URL>
```
7.   Register X.509 certificates on the server.

Use the _netsh.exe_ tool to register certificates for the app:

```
netsh http add sslcert ipport=<IP>:<PORT> certhash=<THUMBPRINT> appid="{<GUID>}"
```

    *   `<IP>`: Specifies the local IP address for the binding. Don't use a wildcard binding. Use a valid IP address.
    *   `<PORT>`: Specifies the port for the binding.
    *   `<THUMBPRINT>`: The X.509 certificate thumbprint.
    *   `<GUID>`: A developer-generated GUID to represent the app for informational purposes.

For reference purposes, store the GUID in the app as a package tag:

    *   In Visual Studio: 
        *   Open the app's project properties by right-clicking on the app in **Solution Explorer** and selecting **Properties**.
        *   Select the **Package** tab.
        *   Enter the GUID that you created in the **Tags** field.

    *   When not using Visual Studio: 
        *   Open the app's project file.

        *   Add a `<PackageTags>` property to a new or existing `<PropertyGroup>` with the GUID that you created:

```
<PropertyGroup>
  <PackageTags>00001111-aaaa-2222-bbbb-3333cccc4444</PackageTags>
</PropertyGroup>
```

In the following example:

    *   The local IP address of the server is `10.0.0.4`.
    *   An online random GUID generator provides the `appid` value.

```
netsh http add sslcert 
    ipport=10.0.0.4:443 
    certhash=b66ee04419d4ee37464ab8785ff02449980eae10 
    appid="{00001111-aaaa-2222-bbbb-3333cccc4444}"
```

When a certificate is registered, the tool responds with `SSL Certificate successfully added`.

To delete a certificate registration, use the `delete sslcert` command:

```
netsh http delete sslcert ipport=<IP>:<PORT>
```

Reference documentation for _netsh.exe_:

    *   [Netsh Commands for Hypertext Transfer Protocol (HTTP)](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc725882(v=ws.10))
    *   [UrlPrefix Strings](https://learn.microsoft.com/en-us/windows/win32/http/urlprefix-strings)

8.   Run the app.

Administrator privileges aren't required to run the app when binding to localhost using HTTP (not HTTPS) with a port number greater than 1024. For other configurations (for example, using a local IP address or binding to port 443), run the app with administrator privileges.

The app responds at the server's public IP address. In this example, the server is reached from the Internet at its public IP address of `104.214.79.47`.

A development certificate is used in this example. The page loads securely after bypassing the browser's untrusted certificate warning.

![Image 8: Browser window showing the app's Index page loaded](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/browser.png?view=aspnetcore-10.0)

For apps hosted by HTTP.sys that interact with requests from the Internet or a corporate network, additional configuration might be required when hosting behind proxy servers and load balancers. For more information, see [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0).

Additional HTTP/2 features in HTTP.sys support gRPC, including support for response trailers and sending reset frames.

Requirements to run gRPC with HTTP.sys:

*   Windows 11 Build 22000 or later, Windows Server 2022 Build 20348 or later.
*   TLS 1.2 or later connection.

HTTP Trailers are similar to HTTP Headers, except they are sent after the response body is sent. For IIS and HTTP.sys, only HTTP/2 response trailers are supported.

```
if (httpContext.Response.SupportsTrailers())
{
    httpContext.Response.DeclareTrailer("trailername");	

    // Write body
    httpContext.Response.WriteAsync("Hello world");

    httpContext.Response.AppendTrailer("trailername", "TrailerValue");
}
```

In the preceding example code:

*   `SupportsTrailers` ensures that trailers are supported for the response.
*   `DeclareTrailer` adds the given trailer name to the `Trailer` response header. Declaring a response's trailers is optional, but recommended. If `DeclareTrailer` is called, it must be before the response headers are sent.
*   `AppendTrailer` appends the trailer.

Reset allows for the server to reset a HTTP/2 request with a specified error code. A reset request is considered aborted.

```
var resetFeature = httpContext.Features.Get<IHttpResetFeature>();
resetFeature.Reset(errorCode: 2);
```

`Reset` in the preceding code example specifies the `INTERNAL_ERROR` error code. For more information about HTTP/2 error codes, visit the [HTTP/2 specification error code section](https://tools.ietf.org/html/rfc7540#page-50).

*   [Enable Windows Authentication with HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-10.0#httpsys)
*   [HTTP Server API](https://learn.microsoft.com/en-us/windows/win32/http/http-api-start-page)
*   [aspnet/HttpSysServer GitHub repository (source code)](https://github.com/aspnet/HttpSysServer/)
*   [The host](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#host)
*   [Troubleshoot and debug ASP.NET Core projects](https://learn.microsoft.com/en-us/aspnet/core/test/troubleshoot?view=aspnetcore-10.0)

[HTTP.sys](https://learn.microsoft.com/en-us/iis/get-started/introduction-to-iis/introduction-to-iis-architecture#hypertext-transfer-protocol-stack-httpsys) is a [web server for ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0) that only runs on Windows. HTTP.sys is an alternative to [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server and offers some features that Kestrel doesn't provide.

Important

HTTP.sys isn't compatible with the [ASP.NET Core Module](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/aspnet-core-module?view=aspnetcore-10.0) and can't be used with IIS or IIS Express.

HTTP.sys supports the following features:

*   [Windows Authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-10.0)
*   Port sharing
*   HTTPS with SNI
*   HTTP/2 over TLS (Windows 10 or later)
*   Direct file transmission
*   Response caching
*   WebSockets (Windows 8 or later)

Supported Windows versions:

*   Windows 7 or later
*   Windows Server 2008 R2 or later

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/servers/httpsys/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

HTTP.sys is useful for deployments where:

*   There's a need to expose the server directly to the Internet without using IIS.

![Image 9: HTTP.sys communicates directly with the Internet](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/httpsys-to-internet.png?view=aspnetcore-10.0)

*   An internal deployment requires a feature not available in Kestrel. For more information, see [Kestrel vs. HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0#kestrel-vs-httpsys)

![Image 10: HTTP.sys communicates directly with the internal network](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/httpsys-to-internal.png?view=aspnetcore-10.0)

HTTP.sys is mature technology that protects against many types of attacks and provides the robustness, security, and scalability of a full-featured web server. IIS itself runs as an HTTP listener on top of HTTP.sys.

[HTTP/2](https://httpwg.org/specs/rfc7540.html) is enabled for ASP.NET Core apps if the following base requirements are met:

*   Windows Server 2016/Windows 10 or later
*   [Application-Layer Protocol Negotiation (ALPN)](https://tools.ietf.org/html/rfc7301#section-3) connection
*   TLS 1.2 or later connection

If an HTTP/2 connection is established, [HttpRequest.Protocol](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httprequest.protocol) reports `HTTP/2`.

HTTP/2 is enabled by default. If an HTTP/2 connection isn't established, the connection falls back to HTTP/1.1. In a future release of Windows, HTTP/2 configuration flags will be available, including the ability to disable HTTP/2 with HTTP.sys.

HTTP.sys delegates to kernel mode authentication with the Kerberos authentication protocol. User mode authentication isn't supported with Kerberos and HTTP.sys. The machine account must be used to decrypt the Kerberos token/ticket that's obtained from Active Directory and forwarded by the client to the server to authenticate the user. Register the Service Principal Name (SPN) for the host, not the user of the app.

Call the [UseHttpSys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.webhostbuilderhttpsysextensions.usehttpsys) extension method when building the host, specifying any required [HttpSysOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions). The following example sets options to their default values:

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseHttpSys(options =>
            {
                options.AllowSynchronousIO = false;
                options.Authentication.Schemes = AuthenticationSchemes.None;
                options.Authentication.AllowAnonymous = true;
                options.MaxConnections = null;
                options.MaxRequestBodySize = 30000000;
                options.UrlPrefixes.Add("http://localhost:5005");
            });
            webBuilder.UseStartup<Startup>();
        });
```

Additional HTTP.sys configuration is handled through [registry settings](https://support.microsoft.com/help/820129/http-sys-registry-settings-for-windows).

**HTTP.sys options**

| Property | Description | Default |
| --- | --- | --- |
| [AllowSynchronousIO](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.allowsynchronousio#microsoft-aspnetcore-server-httpsys-httpsysoptions-allowsynchronousio) | Control whether synchronous input/output is allowed for the `HttpContext.Request.Body` and `HttpContext.Response.Body`. | `false` |
| [Authentication.AllowAnonymous](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.authenticationmanager.allowanonymous#microsoft-aspnetcore-server-httpsys-authenticationmanager-allowanonymous) | Allow anonymous requests. | `true` |
| [Authentication.Schemes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.authenticationmanager.schemes#microsoft-aspnetcore-server-httpsys-authenticationmanager-schemes) | Specify the allowed authentication schemes. May be modified at any time prior to disposing the listener. Values are provided by the [AuthenticationSchemes enum](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.authenticationschemes): `Basic`, `Kerberos`, `Negotiate`, `None`, and `NTLM`. | `None` |
| [EnableResponseCaching](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.enableresponsecaching#microsoft-aspnetcore-server-httpsys-httpsysoptions-enableresponsecaching) | Attempt [kernel-mode](https://learn.microsoft.com/en-us/windows-hardware/drivers/gettingstarted/user-mode-and-kernel-mode) caching for responses with eligible headers. The response may not include `Set-Cookie`, `Vary`, or `Pragma` headers. It must include a `Cache-Control` header that's `public` and either a `shared-max-age` or `max-age` value, or an `Expires` header. | `true` |
| [Http503Verbosity](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.http503verbosity#microsoft-aspnetcore-server-httpsys-httpsysoptions-http503verbosity) | The HTTP.sys behavior when rejecting requests due to throttling conditions. | [Http503VerbosityLevel. Basic](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.http503verbositylevel) |
| [MaxAccepts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.maxaccepts#microsoft-aspnetcore-server-httpsys-httpsysoptions-maxaccepts) | The maximum number of concurrent accepts. | 5 × [Environment. ProcessorCount](https://learn.microsoft.com/en-us/dotnet/api/system.environment.processorcount#system-environment-processorcount) |
| [MaxConnections](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.maxconnections#microsoft-aspnetcore-server-httpsys-httpsysoptions-maxconnections) | The maximum number of concurrent connections to accept. Use `-1` for infinite. Use `null` to use the registry's machine-wide setting. | `null` (machine-wide setting) |
| [MaxRequestBodySize](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.maxrequestbodysize#microsoft-aspnetcore-server-httpsys-httpsysoptions-maxrequestbodysize) | See the [MaxRequestBodySize](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0#maxrequestbodysize) section. | 30000000 bytes (~28.6 MB) |
| [RequestQueueLimit](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.requestqueuelimit#microsoft-aspnetcore-server-httpsys-httpsysoptions-requestqueuelimit) | The maximum number of requests that can be queued. | 1000 |
| `RequestQueueMode` | This indicates whether the server is responsible for creating and configuring the request queue, or if it should attach to an existing queue. Most existing configuration options do not apply when attaching to an existing queue. | `RequestQueueMode.Create` |
| `RequestQueueName` | The name of the HTTP.sys request queue. | `null` (Anonymous queue) |
| [ThrowWriteExceptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.throwwriteexceptions#microsoft-aspnetcore-server-httpsys-httpsysoptions-throwwriteexceptions) | Indicate if response body writes that fail due to client disconnects should throw exceptions or complete normally. | `false` (complete normally) |
| [Timeouts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.timeouts#microsoft-aspnetcore-server-httpsys-httpsysoptions-timeouts) | Expose the HTTP.sys [TimeoutManager](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.timeoutmanager) configuration, which may also be configured in the registry. Follow the API links to learn more about each setting, including default values: * [TimeoutManager.DrainEntityBody](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.timeoutmanager.drainentitybody#microsoft-aspnetcore-server-httpsys-timeoutmanager-drainentitybody): Time allowed for the HTTP Server API to drain the entity body on a Keep-Alive connection. * [TimeoutManager.EntityBody](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.timeoutmanager.entitybody#microsoft-aspnetcore-server-httpsys-timeoutmanager-entitybody): Time allowed for the request entity body to arrive. * [TimeoutManager.HeaderWait](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.timeoutmanager.headerwait#microsoft-aspnetcore-server-httpsys-timeoutmanager-headerwait): Time allowed for the HTTP Server API to parse the request header. * [TimeoutManager.IdleConnection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.timeoutmanager.idleconnection#microsoft-aspnetcore-server-httpsys-timeoutmanager-idleconnection): Time allowed for an idle connection. * [TimeoutManager.MinSendBytesPerSecond](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.timeoutmanager.minsendbytespersecond#microsoft-aspnetcore-server-httpsys-timeoutmanager-minsendbytespersecond): The minimum send rate for the response. * [TimeoutManager.RequestQueue](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.timeoutmanager.requestqueue#microsoft-aspnetcore-server-httpsys-timeoutmanager-requestqueue): Time allowed for the request to remain in the request queue before the app picks it up. |  |
| [UrlPrefixes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.urlprefixes#microsoft-aspnetcore-server-httpsys-httpsysoptions-urlprefixes) | Specify the [UrlPrefixCollection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.urlprefixcollection) to register with HTTP.sys. The most useful is [UrlPrefixCollection.Add](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.urlprefixcollection.add), which is used to add a prefix to the collection. These may be modified at any time prior to disposing the listener. |  |

**MaxRequestBodySize**

The maximum allowed size of any request body in bytes. When set to `null`, the maximum request body size is unlimited. This limit has no effect on upgraded connections, which are always unlimited.

The recommended method to override the limit in an ASP.NET Core MVC app for a single `IActionResult` is to use the [RequestSizeLimitAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.requestsizelimitattribute) attribute on an action method:

```
[RequestSizeLimit(100000000)]
public IActionResult MyActionMethod()
```

An exception is thrown if the app attempts to configure the limit on a request after the app has started reading the request. An `IsReadOnly` property can be used to indicate if the `MaxRequestBodySize` property is in a read-only state, meaning it's too late to configure the limit.

If the app should override [MaxRequestBodySize](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.maxrequestbodysize#microsoft-aspnetcore-server-httpsys-httpsysoptions-maxrequestbodysize) per-request, use the [IHttpMaxRequestBodySizeFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.features.ihttpmaxrequestbodysizefeature):

```
public void Configure(IApplicationBuilder app, IWebHostEnvironment env, 
    ILogger<Startup> logger, IServer server)
{
    app.Use(async (context, next) =>
    {
        context.Features.Get<IHttpMaxRequestBodySizeFeature>()
            .MaxRequestBodySize = 10 * 1024;

        var serverAddressesFeature = 
            app.ServerFeatures.Get<IServerAddressesFeature>();
        var addresses = string.Join(", ", serverAddressesFeature?.Addresses);

        logger.LogInformation("Addresses: {Addresses}", addresses);

        await next.Invoke();
    });

    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
    else
    {
        app.UseExceptionHandler("/Error");
    }

    app.UseStaticFiles();
    app.UseRouting();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapRazorPages();
    });
}
```

If using Visual Studio, make sure the app isn't configured to run IIS or IIS Express.

In Visual Studio, the default launch profile is for IIS Express. To run the project as a console app, manually change the selected profile, as shown in the following screen shot:

![Image 11: Select console app profile](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/vs-choose-profile.png?view=aspnetcore-10.0)

1.   Determine the ports to open for the app and use [Windows Firewall](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/create-an-inbound-port-rule) or the [New-NetFirewallRule](https://learn.microsoft.com/en-us/powershell/module/netsecurity/new-netfirewallrule) PowerShell cmdlet to open firewall ports to allow traffic to reach HTTP.sys. In the following commands and app configuration, port 443 is used.

2.   When deploying to an Azure VM, open the ports in the [Network Security Group](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/nsg-quickstart-portal). In the following commands and app configuration, port 443 is used.

3.   Obtain and install X.509 certificates, if required.

On Windows, create self-signed certificates using the [New-SelfSignedCertificate PowerShell cmdlet](https://learn.microsoft.com/en-us/powershell/module/pki/new-selfsignedcertificate). For an unsupported example, see [UpdateIISExpressSSLForChrome.ps1](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/includes/make-x509-cert/UpdateIISExpressSSLForChrome.ps1).

Install either self-signed or CA-signed certificates in the server's **Local Machine**>**Personal** store.

4.   If the app is a [framework-dependent deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/#framework-dependent-deployments-fdd), install .NET, .NET Framework, or both (if the app is a .NET app targeting the .NET Framework).

    *   **.NET**: If the app requires .NET, obtain and run the **.NET Runtime** installer from [.NET Downloads](https://dotnet.microsoft.com/download). Don't install the full SDK on the server.
    *   **.NET Framework**: If the app requires .NET Framework, see the [.NET Framework installation guide](https://learn.microsoft.com/en-us/dotnet/framework/install/). Install the required .NET Framework. The installer for the latest .NET Framework is available from the [.NET Downloads](https://dotnet.microsoft.com/download) page.

If the app is a [self-contained deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/#self-contained-deployments-scd), the app includes the runtime in its deployment. No framework installation is required on the server.

5.   Configure URLs and ports in the app.

By default, ASP.NET Core binds to `http://localhost:5000`. To configure URL prefixes and ports, options include:

    *   [UseUrls](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.hostingabstractionswebhostbuilderextensions.useurls)
    *   `urls` command-line argument
    *   `ASPNETCORE_URLS` environment variable
    *   [UrlPrefixes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.urlprefixes#microsoft-aspnetcore-server-httpsys-httpsysoptions-urlprefixes)

The following code example shows how to use [UrlPrefixes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.urlprefixes#microsoft-aspnetcore-server-httpsys-httpsysoptions-urlprefixes) with the server's local IP address `10.0.0.4` on port 443:

```
public static IHostBuilder CreateHostBuilder(string[] args) =>
    Host.CreateDefaultBuilder(args)
        .ConfigureWebHostDefaults(webBuilder =>
        {
            webBuilder.UseHttpSys(options =>
            {
                options.UrlPrefixes.Add("https://10.0.0.4:443");
            });
            webBuilder.UseStartup<Startup>();
        });
```

An advantage of `UrlPrefixes` is that an error message is generated immediately for improperly formatted prefixes.

The settings in `UrlPrefixes` override `UseUrls`/`urls`/`ASPNETCORE_URLS` settings. Therefore, an advantage of `UseUrls`, `urls`, and the `ASPNETCORE_URLS` environment variable is that it's easier to switch between Kestrel and HTTP.sys.

HTTP.sys uses the [HTTP Server API UrlPrefix string formats](https://learn.microsoft.com/en-us/windows/win32/http/urlprefix-strings).

Warning

Top-level wildcard bindings (`http://*:80/` and `http://+:80`) should **not** be used. Top-level wildcard bindings create app security vulnerabilities. This applies to both strong and weak wildcards. Use explicit host names or IP addresses rather than wildcards. Subdomain wildcard binding (for example, `*.mysub.com`) isn't a security risk if you control the entire parent domain (as opposed to `*.com`, which is vulnerable). For more information, see [RFC 9110: Section 7.2: Host and :authority](https://www.rfc-editor.org/rfc/rfc9110#field.host).

6.   Preregister URL prefixes on the server.

The built-in tool for configuring HTTP.sys is _netsh.exe_. _netsh.exe_ is used to reserve URL prefixes and assign X.509 certificates. The tool requires administrator privileges.

Use the _netsh.exe_ tool to register URLs for the app:

```
netsh http add urlacl url=<URL> user=<USER>
```

    *   `<URL>`: The fully qualified Uniform Resource Locator (URL). Don't use a wildcard binding. Use a valid hostname or local IP address. _The URL must include a trailing slash._
    *   `<USER>`: Specifies the user or user-group name.

In the following example, the local IP address of the server is `10.0.0.4`:

```
netsh http add urlacl url=https://10.0.0.4:443/ user=Users
```

When a URL is registered, the tool responds with `URL reservation successfully added`.

To delete a registered URL, use the `delete urlacl` command:

```
netsh http delete urlacl url=<URL>
```
7.   Register X.509 certificates on the server.

Use the _netsh.exe_ tool to register certificates for the app:

```
netsh http add sslcert ipport=<IP>:<PORT> certhash=<THUMBPRINT> appid="{<GUID>}"
```

    *   `<IP>`: Specifies the local IP address for the binding. Don't use a wildcard binding. Use a valid IP address.
    *   `<PORT>`: Specifies the port for the binding.
    *   `<THUMBPRINT>`: The X.509 certificate thumbprint.
    *   `<GUID>`: A developer-generated GUID to represent the app for informational purposes.

For reference purposes, store the GUID in the app as a package tag:

    *   In Visual Studio: 
        *   Open the app's project properties by right-clicking on the app in **Solution Explorer** and selecting **Properties**.
        *   Select the **Package** tab.
        *   Enter the GUID that you created in the **Tags** field.

    *   When not using Visual Studio: 
        *   Open the app's project file.

        *   Add a `<PackageTags>` property to a new or existing `<PropertyGroup>` with the GUID that you created:

```
<PropertyGroup>
  <PackageTags>00001111-aaaa-2222-bbbb-3333cccc4444</PackageTags>
</PropertyGroup>
```

In the following example:

    *   The local IP address of the server is `10.0.0.4`.
    *   An online random GUID generator provides the `appid` value.

```
netsh http add sslcert 
    ipport=10.0.0.4:443 
    certhash=b66ee04419d4ee37464ab8785ff02449980eae10 
    appid="{00001111-aaaa-2222-bbbb-3333cccc4444}"
```

When a certificate is registered, the tool responds with `SSL Certificate successfully added`.

To delete a certificate registration, use the `delete sslcert` command:

```
netsh http delete sslcert ipport=<IP>:<PORT>
```

Reference documentation for _netsh.exe_:

    *   [Netsh Commands for Hypertext Transfer Protocol (HTTP)](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc725882(v=ws.10))
    *   [UrlPrefix Strings](https://learn.microsoft.com/en-us/windows/win32/http/urlprefix-strings)

8.   Run the app.

Administrator privileges aren't required to run the app when binding to localhost using HTTP (not HTTPS) with a port number greater than 1024. For other configurations (for example, using a local IP address or binding to port 443), run the app with administrator privileges.

The app responds at the server's public IP address. In this example, the server is reached from the Internet at its public IP address of `104.214.79.47`.

A development certificate is used in this example. The page loads securely after bypassing the browser's untrusted certificate warning.

![Image 12: Browser window showing the app's Index page loaded](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/browser.png?view=aspnetcore-10.0)

For apps hosted by HTTP.sys that interact with requests from the Internet or a corporate network, additional configuration might be required when hosting behind proxy servers and load balancers. For more information, see [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0).

Additional HTTP/2 features in HTTP.sys support gRPC, including support for response trailers and sending reset frames.

Requirements to run gRPC with HTTP.sys:

*   Windows 10, OS Build 19041.508 or later
*   TLS 1.2 or later connection

HTTP Trailers are similar to HTTP Headers, except they are sent after the response body is sent. For IIS and HTTP.sys, only HTTP/2 response trailers are supported.

```
if (httpContext.Response.SupportsTrailers())
{
    httpContext.Response.DeclareTrailer("trailername");	

    // Write body
    httpContext.Response.WriteAsync("Hello world");

    httpContext.Response.AppendTrailer("trailername", "TrailerValue");
}
```

In the preceding example code:

*   `SupportsTrailers` ensures that trailers are supported for the response.
*   `DeclareTrailer` adds the given trailer name to the `Trailer` response header. Declaring a response's trailers is optional, but recommended. If `DeclareTrailer` is called, it must be before the response headers are sent.
*   `AppendTrailer` appends the trailer.

Reset allows for the server to reset a HTTP/2 request with a specified error code. A reset request is considered aborted.

```
var resetFeature = httpContext.Features.Get<IHttpResetFeature>();
resetFeature.Reset(errorCode: 2);
```

`Reset` in the preceding code example specifies the `INTERNAL_ERROR` error code. For more information about HTTP/2 error codes, visit the [HTTP/2 specification error code section](https://tools.ietf.org/html/rfc7540#page-50).

*   [Enable Windows Authentication with HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-10.0#httpsys)
*   [HTTP Server API](https://learn.microsoft.com/en-us/windows/win32/http/http-api-start-page)
*   [aspnet/HttpSysServer GitHub repository (source code)](https://github.com/aspnet/HttpSysServer/)
*   [The host](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#host)
*   [Troubleshoot and debug ASP.NET Core projects](https://learn.microsoft.com/en-us/aspnet/core/test/troubleshoot?view=aspnetcore-10.0)

[HTTP.sys](https://learn.microsoft.com/en-us/iis/get-started/introduction-to-iis/introduction-to-iis-architecture#hypertext-transfer-protocol-stack-httpsys) is a [web server for ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0) that only runs on Windows. HTTP.sys is an alternative to [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server and offers some features that Kestrel doesn't provide.

Important

HTTP.sys isn't compatible with the [ASP.NET Core Module](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/aspnet-core-module?view=aspnetcore-10.0) and can't be used with IIS or IIS Express.

HTTP.sys supports the following features:

*   [Windows Authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-10.0)
*   Port sharing
*   HTTPS with SNI
*   HTTP/2 over TLS (Windows 10 or later)
*   HTTP/3 over TLS (Windows 11 or later)
*   Direct file transmission
*   Response caching
*   WebSockets (Windows 8 or later)
*   Customizable security descriptors

Supported Windows versions:

*   Windows 7 or later
*   Windows Server 2008 R2 or later

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/servers/httpsys/samples) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

HTTP.sys is useful for deployments where:

*   There's a need to expose the server directly to the Internet without using IIS.

![Image 13: HTTP.sys communicates directly with the Internet](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/httpsys-to-internet.png?view=aspnetcore-10.0)

*   An internal deployment requires a feature not available in Kestrel. For more information, see [Kestrel vs. HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/?view=aspnetcore-10.0#kestrel-vs-httpsys)

![Image 14: HTTP.sys communicates directly with the internal network](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/httpsys-to-internal.png?view=aspnetcore-10.0)

HTTP.sys is mature technology that protects against many types of attacks and provides the robustness, security, and scalability of a full-featured web server. IIS itself runs as an HTTP listener on top of HTTP.sys.

[HTTP/2](https://httpwg.org/specs/rfc7540.html) is enabled for ASP.NET Core apps when the following base requirements are met:

*   Windows Server 2016/Windows 10 or later
*   [Application-Layer Protocol Negotiation (ALPN)](https://tools.ietf.org/html/rfc7301#section-3) connection
*   TLS 1.2 or later connection

If an HTTP/2 connection is established, [HttpRequest.Protocol](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httprequest.protocol) reports `HTTP/2`.

HTTP/2 is enabled by default. If an HTTP/2 connection isn't established, the connection falls back to HTTP/1.1. In a future release of Windows, HTTP/2 configuration flags will be available, including the ability to disable HTTP/2 with HTTP.sys.

[HTTP/3](https://datatracker.ietf.org/doc/rfc9114/) is enabled for ASP.NET Core apps when the following base requirements are met:

*   Windows Server 2022/Windows 11 or later
*   An `https` url binding is used.
*   The [EnableHttp3 registry key](https://techcommunity.microsoft.com/t5/networking-blog/enabling-http-3-support-on-windows-server-2022/ba-p/2676880) is set.

The preceding Windows 11 Build versions may require the use of a [Windows Insider](https://www.microsoft.com/en-us/windowsinsider/) build.

HTTP/3 is discovered as an upgrade from HTTP/1.1 or HTTP/2 via the `alt-svc` header. That means the first request will normally use HTTP/1.1 or HTTP/2 before switching to HTTP/3. Http.Sys doesn't automatically add the `alt-svc` header, it must be added by the application. The following code is a middleware example that adds the `alt-svc` response header.

```
app.Use((context, next) =>
{
    context.Response.Headers.AltSvc = "h3=\":443\"";
    return next(context);
});
```

Place the preceding code early in the request pipeline.

Http.Sys also supports sending an AltSvc HTTP/2 protocol message rather than a response header to notify the client that HTTP/3 is available. See the [EnableAltSvc registry key](https://techcommunity.microsoft.com/t5/networking-blog/enabling-http-3-support-on-windows-server-2022/ba-p/2676880). This requires netsh sslcert bindings that use host names rather than IP addresses.

HTTP.sys delegates to kernel mode authentication with the Kerberos authentication protocol. User mode authentication isn't supported with Kerberos and HTTP.sys. The machine account must be used to decrypt the Kerberos token/ticket that's obtained from Active Directory and forwarded by the client to the server to authenticate the user. Register the Service Principal Name (SPN) for the host, not the user of the app.

In some scenarios, high volumes of small writes with high latency can cause significant performance impact to `HTTP.sys`. This impact is due to the lack of a [Pipe](https://learn.microsoft.com/en-us/dotnet/api/system.io.pipelines.pipe) buffer in the `HTTP.sys` implementation. To improve performance in these scenarios, support for response buffering is included in `HTTP.sys`. Enable buffering by setting [HttpSysOptions.EnableKernelResponseBuffering](https://github.com/dotnet/aspnetcore/blob/main/src/Servers/HttpSys/src/HttpSysOptions.cs#L120) to `true`. Response buffering should be enabled by an app that does synchronous I/O, or asynchronous I/O with no more than one outstanding write at a time. In these scenarios, response buffering can significantly improve throughput over high-latency connections.

Apps that use asynchronous I/O and that may have more than one write outstanding at a time should **_not_** use this flag. Enabling this flag can result in higher CPU and memory usage by HTTP.Sys.

Call the [UseHttpSys](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.webhostbuilderhttpsysextensions.usehttpsys) extension method when building the host, specifying any required [HttpSysOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions). The following example sets options to their default values:

```
using Microsoft.AspNetCore.Hosting.Server;
using Microsoft.AspNetCore.Hosting.Server.Features;
using Microsoft.AspNetCore.Http.Features;
using Microsoft.AspNetCore.Server.HttpSys;

var builder = WebApplication.CreateBuilder(args);

builder.WebHost.UseHttpSys(options =>
{
    options.AllowSynchronousIO = false;
    options.Authentication.Schemes = AuthenticationSchemes.None;
    options.Authentication.AllowAnonymous = true;
    options.MaxConnections = null;
    options.MaxRequestBodySize = 30_000_000;
    options.UrlPrefixes.Add("http://localhost:5005");
});

builder.Services.AddRazorPages();

var app = builder.Build();
```

Additional HTTP.sys configuration is handled through [registry settings](https://support.microsoft.com/help/820129/http-sys-registry-settings-for-windows).

For more information about HTTP.sys options, see [HttpSysOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions).

**MaxRequestBodySize**

The maximum allowed size of any request body in bytes. When set to `null`, the maximum request body size is unlimited. This limit has no effect on upgraded connections, which are always unlimited.

The recommended method to override the limit in an ASP.NET Core MVC app for a single `IActionResult` is to use the [RequestSizeLimitAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.requestsizelimitattribute) attribute on an action method:

```
[RequestSizeLimit(100000000)]
public IActionResult MyActionMethod()
```

An exception is thrown if the app attempts to configure the limit on a request after the app has started reading the request. An `IsReadOnly` property can be used to indicate if the `MaxRequestBodySize` property is in a read-only state, meaning it's too late to configure the limit.

If the app should override [MaxRequestBodySize](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.maxrequestbodysize#microsoft-aspnetcore-server-httpsys-httpsysoptions-maxrequestbodysize) per-request, use the [IHttpMaxRequestBodySizeFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.features.ihttpmaxrequestbodysizefeature):

```
app.Use((context, next) =>
{
    context.Features.GetRequiredFeature<IHttpMaxRequestBodySizeFeature>()
                                             .MaxRequestBodySize = 10 * 1024;

    var server = context.RequestServices
        .GetRequiredService<IServer>();
    var serverAddressesFeature = server.Features
                                 .GetRequiredFeature<IServerAddressesFeature>();

    var addresses = string.Join(", ", serverAddressesFeature.Addresses);

    var loggerFactory = context.RequestServices
        .GetRequiredService<ILoggerFactory>();
    var logger = loggerFactory.CreateLogger("Sample");

    logger.LogInformation("Addresses: {addresses}", addresses);

    return next(context);
});
```

If using Visual Studio, make sure the app isn't configured to run IIS or IIS Express.

In Visual Studio, the default launch profile is for IIS Express. To run the project as a console app, manually change the selected profile, as shown in the following screenshot:

![Image 15: Select console app profile](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/vs-choose-profile.png?view=aspnetcore-10.0)

1.   Determine the ports to open for the app and use [Windows Firewall](https://learn.microsoft.com/en-us/windows/security/threat-protection/windows-firewall/create-an-inbound-port-rule) or the [New-NetFirewallRule](https://learn.microsoft.com/en-us/powershell/module/netsecurity/new-netfirewallrule) PowerShell cmdlet to open firewall ports to allow traffic to reach HTTP.sys. In the following commands and app configuration, port 443 is used.

2.   When deploying to an Azure VM, open the ports in the [Network Security Group](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/nsg-quickstart-portal). In the following commands and app configuration, port 443 is used.

3.   Obtain and install X.509 certificates, if required.

On Windows, create self-signed certificates using the [New-SelfSignedCertificate PowerShell cmdlet](https://learn.microsoft.com/en-us/powershell/module/pki/new-selfsignedcertificate). For an unsupported example, see [UpdateIISExpressSSLForChrome.ps1](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/includes/make-x509-cert/UpdateIISExpressSSLForChrome.ps1).

Install either self-signed or CA-signed certificates in the server's **Local Machine**>**Personal** store.

4.   If the app is a [framework-dependent deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/#framework-dependent-deployments-fdd), install .NET, .NET Framework, or both (if the app is a .NET app targeting the .NET Framework).

    *   **.NET**: If the app requires .NET, obtain and run the **.NET Runtime** installer from [.NET Downloads](https://dotnet.microsoft.com/download). Don't install the full SDK on the server.
    *   **.NET Framework**: If the app requires .NET Framework, see the [.NET Framework installation guide](https://learn.microsoft.com/en-us/dotnet/framework/install/). Install the required .NET Framework. The installer for the latest .NET Framework is available from the [.NET Downloads](https://dotnet.microsoft.com/download) page.

If the app is a [self-contained deployment](https://learn.microsoft.com/en-us/dotnet/core/deploying/#self-contained-deployments-scd), the app includes the runtime in its deployment. No framework installation is required on the server.

5.   Configure URLs and ports in the app.

By default, ASP.NET Core binds to `http://localhost:5000`. To configure URL prefixes and ports, options include:

    *   [UseUrls](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.hostingabstractionswebhostbuilderextensions.useurls)
    *   `urls` command-line argument
    *   `ASPNETCORE_URLS` environment variable
    *   [UrlPrefixes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.urlprefixes#microsoft-aspnetcore-server-httpsys-httpsysoptions-urlprefixes)

The following code example shows how to use [UrlPrefixes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysoptions.urlprefixes#microsoft-aspnetcore-server-httpsys-httpsysoptions-urlprefixes) with the server's local IP address `10.0.0.4` on port 443:

```
var builder = WebApplication.CreateBuilder(args);

builder.WebHost.UseHttpSys(options =>
{
    options.UrlPrefixes.Add("https://10.0.0.4:443");
});

builder.Services.AddRazorPages();

var app = builder.Build();
```

An advantage of `UrlPrefixes` is that an error message is generated immediately for improperly formatted prefixes.

The settings in `UrlPrefixes` override `UseUrls`/`urls`/`ASPNETCORE_URLS` settings. Therefore, an advantage of `UseUrls`, `urls`, and the `ASPNETCORE_URLS` environment variable is that it's easier to switch between Kestrel and HTTP.sys.

HTTP.sys recognizes two types of wild cards in URL prefixes:

    *   `*` is a _weak binding_, also known as a _fallback binding_. If the URL prefix is `http://*:5000`, and something else is bound to port 5000, this binding won't be used.
    *   `+` is a _strong binding_. If the URL prefix is `http://+:5000`, this binding will be used before other port 5000 bindings.

For more information, see [UrlPrefix Strings](https://learn.microsoft.com/en-us/windows/win32/http/urlprefix-strings).

Warning

Top-level wildcard bindings (`http://*:80/` and `http://+:80`) should **not** be used. Top-level wildcard bindings create app security vulnerabilities. This applies to both strong and weak wildcards. Use explicit host names or IP addresses rather than wildcards. Subdomain wildcard binding (for example, `*.mysub.com`) isn't a security risk if you control the entire parent domain (as opposed to `*.com`, which is vulnerable). For more information, see [RFC 9110: Section 7.2: Host and :authority](https://www.rfc-editor.org/rfc/rfc9110#field.host).

Apps and containers are often given only a port to listen on, like port 80, without additional constraints like host or path. HTTP_PORTS and HTTPS_PORTS are config keys that specify the listening ports for the Kestrel and HTTP.sys servers. These keys may be specified as environment variables defined with the `DOTNET_` or `ASPNETCORE_` prefixes, or specified directly through any other config input, such as `appsettings.json`. Each is a semicolon-delimited list of port values, as shown in the following example:

```
ASPNETCORE_HTTP_PORTS=80;8080
ASPNETCORE_HTTPS_PORTS=443;8081
```

The preceding example is shorthand for the following configuration, which specifies the scheme (HTTP or HTTPS) and any host or IP.

```
ASPNETCORE_URLS=http://*:80/;http://*:8080/;https://*:443/;https://*:8081/
```

The HTTP_PORTS and HTTPS_PORTS configuration keys are lower priority and are overridden by URLS or values provided directly in code. Certificates still need to be configured separately via server-specific mechanics for HTTPS.

These configuration keys are equivalent to top-level wildcard bindings. They're convenient for development and container scenarios, but avoid wildcards when running on a machine that may also host other services.

6.   Preregister URL prefixes on the server.

The built-in tool for configuring HTTP.sys is _netsh.exe_. _netsh.exe_ is used to reserve URL prefixes and assign X.509 certificates. The tool requires administrator privileges.

Use the _netsh.exe_ tool to register URLs for the app:

```
netsh http add urlacl url=<URL> user=<USER>
```

    *   `<URL>`: The fully qualified Uniform Resource Locator (URL). Don't use a wildcard binding. Use a valid hostname or local IP address. _The URL must include a trailing slash._
    *   `<USER>`: Specifies the user or user-group name.

In the following example, the local IP address of the server is `10.0.0.4`:

```
netsh http add urlacl url=https://10.0.0.4:443/ user=Users
```

When a URL is registered, the tool responds with `URL reservation successfully added`.

To delete a registered URL, use the `delete urlacl` command:

```
netsh http delete urlacl url=<URL>
```
7.   Register X.509 certificates on the server.

Use the _netsh.exe_ tool to register certificates for the app:

```
netsh http add sslcert ipport=<IP>:<PORT> certhash=<THUMBPRINT> appid="{<GUID>}"
```

    *   `<IP>`: Specifies the local IP address for the binding. Don't use a wildcard binding. Use a valid IP address.
    *   `<PORT>`: Specifies the port for the binding.
    *   `<THUMBPRINT>`: The X.509 certificate thumbprint.
    *   `<GUID>`: A developer-generated GUID to represent the app for informational purposes.

For reference purposes, store the GUID in the app as a package tag:

    *   In Visual Studio: 
        *   Open the app's project properties by right-clicking on the app in **Solution Explorer** and selecting **Properties**.
        *   Select the **Package** tab.
        *   Enter the GUID that you created in the **Tags** field.

    *   When not using Visual Studio: 
        *   Open the app's project file.

        *   Add a `<PackageTags>` property to a new or existing `<PropertyGroup>` with the GUID that you created:

```
<PropertyGroup>
  <PackageTags>00001111-aaaa-2222-bbbb-3333cccc4444</PackageTags>
</PropertyGroup>
```

In the following example:

    *   The local IP address of the server is `10.0.0.4`.
    *   An online random GUID generator provides the `appid` value.

```
netsh http add sslcert 
    ipport=10.0.0.4:443 
    certhash=b66ee04419d4ee37464ab8785ff02449980eae10 
    appid="{00001111-aaaa-2222-bbbb-3333cccc4444}"
```

When a certificate is registered, the tool responds with `SSL Certificate successfully added`.

To delete a certificate registration, use the `delete sslcert` command:

```
netsh http delete sslcert ipport=<IP>:<PORT>
```

Reference documentation for _netsh.exe_:

    *   [Netsh Commands for Hypertext Transfer Protocol (HTTP)](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2008-R2-and-2008/cc725882(v=ws.10))
    *   [UrlPrefix Strings](https://learn.microsoft.com/en-us/windows/win32/http/urlprefix-strings)

8.   Run the app.

Administrator privileges aren't required to run the app when binding to localhost using HTTP (not HTTPS) with a port number greater than 1024. For other configurations (for example, using a local IP address or binding to port 443), run the app with administrator privileges.

The app responds at the server's public IP address. In this example, the server is reached from the Internet at its public IP address of `104.214.79.47`.

A development certificate is used in this example. The page loads securely after bypassing the browser's untrusted certificate warning.

![Image 16: Browser window showing the app's Index page loaded](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys/_static/browser.png?view=aspnetcore-10.0)

For apps hosted by HTTP.sys that interact with requests from the Internet or a corporate network, additional configuration might be required when hosting behind proxy servers and load balancers. For more information, see [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0).

[IHttpSysRequestTimingFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.ihttpsysrequesttimingfeature) provides detailed timing information for requests:

*   Timestamps are obtained using [QueryPerformanceCounter](https://learn.microsoft.com/en-us/windows/win32/api/profileapi/nf-profileapi-queryperformancecounter).
*   The timestamp frequency can be obtained via [QueryPerformanceFrequency](https://learn.microsoft.com/en-us/windows/win32/api/profileapi/nf-profileapi-queryperformancefrequency).
*   The index of the timing can be cast to [HttpSysRequestTimingType](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.httpsysrequesttimingtype) to know what the timing represents.
*   The value may be 0 if the timing isn't available for the current request.
*   Requires Windows 10 version 2004, Windows Server 2022, or later.

```
using Microsoft.AspNetCore.Http.Features;
using Microsoft.AspNetCore.Server.HttpSys;

var builder = WebApplication.CreateBuilder(args);

builder.WebHost.UseHttpSys();

var app = builder.Build();

app.Use((context, next) =>
{
    var feature = context.Features.GetRequiredFeature<IHttpSysRequestTimingFeature>();
    
    var loggerFactory = context.RequestServices.GetRequiredService<ILoggerFactory>();
    var logger = loggerFactory.CreateLogger("Sample");

    var timestamps = feature.Timestamps;

    for (var i = 0; i < timestamps.Length; i++)
    {
        var timestamp = timestamps[i];
        var timingType = (HttpSysRequestTimingType)i;

        logger.LogInformation("Timestamp {timingType}: {timestamp}",
                                          timingType, timestamp);
    }

    return next(context);
});

app.MapGet("/", () => Results.Ok());

app.Run();
```

[IHttpSysRequestTimingFeature.TryGetTimestamp](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.server.httpsys.ihttpsysrequesttimingfeature.trygettimestamp) retrieves the timestamp for the provided timing type:

```
using Microsoft.AspNetCore.Http.Features;
using Microsoft.AspNetCore.Server.HttpSys;
var builder = WebApplication.CreateBuilder(args);

builder.WebHost.UseHttpSys();

var app = builder.Build();

app.Use((context, next) =>
{
    var feature = context.Features.GetRequiredFeature<IHttpSysRequestTimingFeature>();

    var loggerFactory = context.RequestServices.GetRequiredService<ILoggerFactory>();
    var logger = loggerFactory.CreateLogger("Sample");

    var timingType = HttpSysRequestTimingType.RequestRoutingEnd;

    if (feature.TryGetTimestamp(timingType, out var timestamp))
    {
        logger.LogInformation("Timestamp {timingType}: {timestamp}",
                                          timingType, timestamp);
    }
    else
    {
        logger.LogInformation("Timestamp {timingType}: not available for the "
                                           + "current request",    timingType);
    }

    return next(context);
});

app.MapGet("/", () => Results.Ok());

app.Run();
```

[IHttpSysRequestTimingFeature.TryGetElapsedTime](/dotnet/api/microsoft.aspnetcore.server.httpsys.ihttpsysrequesttimingfeature.trygetelapsedtime yields the elapsed time between two specified timings:

```
using Microsoft.AspNetCore.Http.Features;
using Microsoft.AspNetCore.Server.HttpSys;

var builder = WebApplication.CreateBuilder(args);

builder.WebHost.UseHttpSys();

var app = builder.Build();

app.Use((context, next) =>
{
    var feature = context.Features.GetRequiredFeature<IHttpSysRequestTimingFeature>();

    var loggerFactory = context.RequestServices.GetRequiredService<ILoggerFactory>();
    var logger = loggerFactory.CreateLogger("Sample");

    var startingTimingType = HttpSysRequestTimingType.RequestRoutingStart;
    var endingTimingType = HttpSysRequestTimingType.RequestRoutingEnd;

    if (feature.TryGetElapsedTime(startingTimingType, endingTimingType, out var elapsed))
    {
        logger.LogInformation(
            "Elapsed time {startingTimingType} to {endingTimingType}: {elapsed}",
            startingTimingType,
            endingTimingType,
            elapsed);
    }
    else
    {
        logger.LogInformation(
            "Elapsed time {startingTimingType} to {endingTimingType}:"
            + " not available for the current request.",
            startingTimingType,
            endingTimingType);
    }

    return next(context);
});

app.MapGet("/", () => Results.Ok());

app.Run();
```

Additional HTTP/2 features in HTTP.sys support gRPC, including support for response trailers and sending reset frames.

Requirements to run gRPC with HTTP.sys:

*   Windows 11 Build 22000 or later, Windows Server 2022 Build 20348 or later.
*   TLS 1.2 or later connection.

HTTP Trailers are similar to HTTP Headers, except they are sent after the response body is sent. For IIS and HTTP.sys, only HTTP/2 response trailers are supported.

```
if (httpContext.Response.SupportsTrailers())
{
    httpContext.Response.DeclareTrailer("trailername");	

    // Write body
    httpContext.Response.WriteAsync("Hello world");

    httpContext.Response.AppendTrailer("trailername", "TrailerValue");
}
```

In the preceding example code:

*   `SupportsTrailers` ensures that trailers are supported for the response.
*   `DeclareTrailer` adds the given trailer name to the `Trailer` response header. Declaring a response's trailers is optional, but recommended. If `DeclareTrailer` is called, it must be before the response headers are sent.
*   `AppendTrailer` appends the trailer.

Reset allows for the server to reset a HTTP/2 request with a specified error code. A reset request is considered aborted.

```
var resetFeature = httpContext.Features.Get<IHttpResetFeature>();
resetFeature.Reset(errorCode: 2);
```

`Reset` in the preceding code example specifies the `INTERNAL_ERROR` error code. For more information about HTTP/2 error codes, visit the [HTTP/2 specification error code section](https://tools.ietf.org/html/rfc7540#page-50).

For information about how to get traces from HTTP.sys, see [HTTP.sys Manageability Scenarios](https://learn.microsoft.com/en-us/windows/win32/http/http-sys-manageability-scenarios).

*   [Enable Windows Authentication with HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/windowsauth?view=aspnetcore-10.0#httpsys)
*   [HTTP Server API](https://learn.microsoft.com/en-us/windows/win32/http/http-api-start-page)
*   [aspnet/HttpSysServer GitHub repository (source code)](https://github.com/aspnet/HttpSysServer/)
*   [The host](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#host)
*   [Troubleshoot and debug ASP.NET Core projects](https://learn.microsoft.com/en-us/aspnet/core/test/troubleshoot?view=aspnetcore-10.0)
