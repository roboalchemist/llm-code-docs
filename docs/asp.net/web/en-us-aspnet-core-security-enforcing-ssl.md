# Source: https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0

Title: Enforce HTTPS in ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0

Published Time: Thu, 22 Jan 2026 23:58:07 GMT

Markdown Content:
By [David Galvan](https://www.linkedin.com/in/dave-galvan/) and [Rick Anderson](https://twitter.com/RickAndMSFT)

this article shows how to:

*   Require HTTPS for all requests.
*   Redirect all HTTP requests to HTTPS.

No API can prevent a client from sending sensitive data on the first request.

Warning

API projects
------------

Do **not** use [RequireHttpsAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.requirehttpsattribute) on Web APIs that receive sensitive information. `RequireHttpsAttribute` uses HTTP status codes to redirect browsers from HTTP to HTTPS. API clients may not understand or obey redirects from HTTP to HTTPS. Such clients may send information over HTTP. Web APIs should either:

*   Not listen on HTTP.
*   Close the connection with status code 400 (Bad Request) and not serve the request.

To disable HTTP redirection in an API, set the `ASPNETCORE_URLS` environment variable or use the `--urls` command line flag. For more information, see [ASP.NET Core runtime environments](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0) and [8 ways to set the URLs for an ASP.NET Core app](https://andrewlock.net/8-ways-to-set-the-urls-for-an-aspnetcore-app/) by Andrew Lock.

HSTS and API projects
---------------------

The default API projects don't include [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#hsts) because [HSTS](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) is generally a browser only instruction. Other callers, such as phone or desktop apps, do **not** obey the instruction. Even within browsers, a single authenticated call to an API over HTTP has risks on insecure networks. The secure approach is to configure API projects to only listen to and respond over HTTPS.

Requests to an endpoint using HTTP that are redirected to HTTPS by [UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection) fail with `ERR_INVALID_REDIRECT` on the CORS preflight request.

API projects can reject HTTP requests rather than use `UseHttpsRedirection` to redirect requests to HTTPS.

We recommend that production ASP.NET Core web apps use:

*   HTTPS Redirection Middleware ([UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection)) to redirect HTTP requests to HTTPS.
*   HSTS Middleware ([UseHsts](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts)) to send HTTP Strict Transport Security Protocol (HSTS) headers to clients.

Note

Apps deployed in a reverse proxy configuration allow the proxy to handle connection security (HTTPS). If the proxy also handles HTTPS redirection, there's no need to use HTTPS Redirection Middleware. If the proxy server also handles writing HSTS headers (for example, [native HSTS support in IIS 10.0 (1709) or later](https://learn.microsoft.com/en-us/iis/get-started/whats-new-in-iis-10-version-1709/iis-10-version-1709-hsts#iis-100-version-1709-native-hsts-support)), HSTS Middleware isn't required by the app. For more information, see [Opt-out of HTTPS/HSTS on project creation](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#opt-out-of-httpshsts-on-project-creation).

The following code calls [UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection) in the `Program.cs` file:

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

The preceding highlighted code:

*   Uses the default [HttpsRedirectionOptions.RedirectStatusCode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.redirectstatuscode#microsoft-aspnetcore-httpspolicy-httpsredirectionoptions-redirectstatuscode) ([Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect)).
*   Uses the default [HttpsRedirectionOptions.HttpsPort](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.httpsport#microsoft-aspnetcore-httpspolicy-httpsredirectionoptions-httpsport) (null) unless overridden by the `ASPNETCORE_HTTPS_PORT` environment variable or [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature).

We recommend using temporary redirects rather than permanent redirects. Link caching can cause unstable behavior in development environments. If you prefer to send a permanent redirect status code when the app is in a non-`Development` environment, see the [Configure permanent redirects in production](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#configure-permanent-redirects-in-production) section. We recommend using [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) to signal to clients that only secure resource requests should be sent to the app (only in production).

A port must be available for the middleware to redirect an insecure request to HTTPS. If no port is available:

*   Redirection to HTTPS doesn't occur.
*   The middleware logs the warning "Failed to determine the https port for redirect."

Specify the HTTPS port using any of the following approaches:

*   Set [HttpsRedirectionOptions.HttpsPort](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#options).

*   Set the `https_port`[host setting](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0#https_port):

    *   In host configuration.

    *   By setting the `ASPNETCORE_HTTPS_PORT` environment variable.

    *   By adding a top-level entry in `appsettings.json`:

```
{
  "https_port": 443,
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

*   Indicate a port with the secure scheme using the [ASPNETCORE_URLS environment variable](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0#urls). The environment variable configures the server. The middleware indirectly discovers the HTTPS port via [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature). This approach doesn't work in reverse proxy deployments.

*   The ASP.NET Core web templates set an HTTPS URL in `Properties/launchsettings.json` for both Kestrel and IIS Express. `launchsettings.json` is only used on the local machine.

*   Configure an HTTPS URL endpoint for a public-facing edge deployment of [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server or [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0) server. Only **one HTTPS port** is used by the app. The middleware discovers the port via [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature).

Note

When an app is run in a reverse proxy configuration, [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature) isn't available. Set the port using one of the other approaches described in this section.

When [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) or [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0) is used as a public-facing edge server, Kestrel or HTTP.sys must be configured to listen on both:

*   The secure port where the client is redirected (typically, 443 in production and 5001 in development).
*   The insecure port (typically, 80 in production and 5000 in development).

The insecure port must be accessible by the client in order for the app to receive an insecure request and redirect the client to the secure port.

For more information, see [Kestrel endpoint configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0#endpoint-configuration) or [HTTP.sys web server implementation in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0).

Any firewall between the client and server must also have communication ports open for traffic.

If requests are forwarded in a reverse proxy configuration, use [Forwarded Headers Middleware](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0) before calling HTTPS Redirection Middleware. Forwarded Headers Middleware updates the `Request.Scheme`, using the `X-Forwarded-Proto` header. The middleware permits redirect URIs and other security policies to work correctly. When Forwarded Headers Middleware isn't used, the backend app might not receive the correct scheme and end up in a redirect loop. A common end user error message is that too many redirects have occurred.

When deploying to Azure App Service, follow the guidance in [Tutorial: Bind an existing custom SSL certificate to Azure Web Apps](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-ssl).

The following highlighted code calls [AddHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpsredirectionservicesextensions.addhttpsredirection) to configure middleware options:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

builder.Services.AddHsts(options =>
{
    options.Preload = true;
    options.IncludeSubDomains = true;
    options.MaxAge = TimeSpan.FromDays(60);
    options.ExcludedHosts.Add("example.com");
    options.ExcludedHosts.Add("www.example.com");
});

builder.Services.AddHttpsRedirection(options =>
{
    options.RedirectStatusCode = Status307TemporaryRedirect;
    options.HttpsPort = 5001;
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

Calling `AddHttpsRedirection` is only necessary to change the values of `HttpsPort` or `RedirectStatusCode`.

The preceding highlighted code:

*   Sets [HttpsRedirectionOptions.RedirectStatusCode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.redirectstatuscode) to [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect), which is the default value. Use the fields of the [StatusCodes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes) class for assignments to `RedirectStatusCode`.
*   Sets the HTTPS port to 5001.

The middleware defaults to sending a [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect) with all redirects. If you prefer to send a permanent redirect status code when the app is in a non-`Development` environment, wrap the middleware options configuration in a conditional check for a non-`Development` environment.

When configuring services in `Program.cs`:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

if (!builder.Environment.IsDevelopment())
{
    builder.Services.AddHttpsRedirection(options =>
    {
        options.RedirectStatusCode = Status308PermanentRedirect;
        options.HttpsPort = 443;
    });
}

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");

    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

An alternative to using HTTPS Redirection Middleware (`UseHttpsRedirection`) is to use URL Rewriting Middleware (`AddRedirectToHttps`). `AddRedirectToHttps` can also set the status code and port when the redirect is executed. For more information, see [URL Rewriting Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting?view=aspnetcore-10.0).

When redirecting to HTTPS without the requirement for additional redirect rules, we recommend using HTTPS Redirection Middleware (`UseHttpsRedirection`) described in this article.

Per [OWASP](https://www.owasp.org/index.php/About_The_Open_Web_Application_Security_Project), [HTTP Strict Transport Security (HSTS)](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html) is an opt-in security enhancement that's specified by a web app through the use of a response header. When a [browser that supports HSTS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html#browser-support) receives this header:

*   The browser stores configuration for the domain that prevents sending any communication over HTTP. The browser forces all communication over HTTPS.
*   The browser prevents the user from using untrusted or invalid certificates. The browser disables prompts that allow a user to temporarily trust such a certificate.

Because [HSTS](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) is enforced by the client, it has some limitations:

*   The client must support HSTS.
*   HSTS requires at least one successful HTTPS request to establish the HSTS policy.
*   The application must check every HTTP request and redirect or reject the HTTP request.

ASP.NET Core implements HSTS with the [UseHsts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.hstsbuilderextensions.usehsts) extension method. The following code calls `UseHsts` when the app isn't in [development mode](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0):

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

`UseHsts` isn't recommended in development because the HSTS settings are highly cacheable by browsers. By default, `UseHsts` excludes the local loopback address.

For production environments that are implementing HTTPS for the first time, set the initial [HstsOptions.MaxAge](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.hstsoptions.maxage) to a small value using one of the [TimeSpan](https://learn.microsoft.com/en-us/dotnet/api/system.timespan) methods. Set the value from hours to no more than a single day in case you need to revert the HTTPS infrastructure to HTTP. After you're confident in the sustainability of the HTTPS configuration, increase the HSTS `max-age` value; a commonly used value is one year.

The following highlighted code:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

builder.Services.AddHsts(options =>
{
    options.Preload = true;
    options.IncludeSubDomains = true;
    options.MaxAge = TimeSpan.FromDays(60);
    options.ExcludedHosts.Add("example.com");
    options.ExcludedHosts.Add("www.example.com");
});

builder.Services.AddHttpsRedirection(options =>
{
    options.RedirectStatusCode = Status307TemporaryRedirect;
    options.HttpsPort = 5001;
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

*   Sets the preload parameter of the `Strict-Transport-Security` header. Preload isn't part of the [RFC HSTS specification](https://tools.ietf.org/html/rfc6797), but is supported by web browsers to preload HSTS sites on fresh install. For more information, see [https://hstspreload.org/](https://hstspreload.org/).
*   Enables [includeSubDomain](https://tools.ietf.org/html/rfc6797#section-6.1.2), which applies the HSTS policy to Host subdomains.
*   Explicitly sets the `max-age` parameter of the `Strict-Transport-Security` header to 60 days. If not set, defaults to 30 days. For more information, see the [max-age directive](https://tools.ietf.org/html/rfc6797#section-6.1.1).
*   Adds `example.com` to the list of hosts to exclude.

`UseHsts` excludes the following loopback hosts:

*   `localhost` : The IPv4 loopback address.
*   `127.0.0.1` : The IPv4 loopback address.
*   `[::1]` : The IPv6 loopback address.

In some backend service scenarios where connection security is handled at the public-facing edge of the network, configuring connection security at each node isn't required. Web apps that are generated from the templates in Visual Studio or from the [dotnet new](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new) command enable [HTTPS redirection](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#require-https) and [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts). For deployments that don't require these scenarios, you can opt-out of HTTPS/HSTS when the app is created from the template.

To opt-out of HTTPS/HSTS:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [.NET CLI](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#tabpanel_1_net-cli)

Uncheck the **Configure for HTTPS** checkbox.

![Image 1: New ASP.NET Core Web Application dialog showing the Configure for HTTPS checkbox unselected.](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl/_static/out-vs2019.png?view=aspnetcore-10.0)

The .NET SDK includes an HTTPS development certificate. The certificate is installed as part of the first-run experience. For example, `dotnet --info` produces a variation of the following output:

```
ASP.NET Core
------------
Successfully installed the ASP.NET Core HTTPS Development Certificate.
To trust the certificate run 'dotnet dev-certs https --trust' (Windows and macOS only).
For establishing trust on other platforms refer to the platform specific documentation.
For more information on configuring HTTPS see https://go.microsoft.com/fwlink/?linkid=848054.
```

Installing the .NET SDK installs the ASP.NET Core HTTPS development certificate to the local user certificate store. The certificate has been installed, but it's not trusted. To trust the certificate, perform the one-time step to run the `dotnet dev-certs` tool:

```
dotnet dev-certs https --trust
```

The following command provides help on the `dotnet dev-certs` tool:

```
dotnet dev-certs https --help
```

Warning

Do not create a development certificate in an environment that will be redistributed, such as a container image or virtual machine. Doing so can lead to spoofing and elevation of privilege. To help prevent this, set the `DOTNET_GENERATE_ASPNET_CERTIFICATE` environment variable to `false` prior to calling the .NET CLI for the first time. This will skip the automatic generation of the ASP.NET Core development certificate during the CLI's first-run experience.

See [this GitHub issue](https://github.com/dotnet/AspNetCore.Docs/issues/6199).

Linux distros differ substantially in how they mark certificates as trusted. While `dotnet dev-certs` is expected to be broadly applicable it is only officially supported on Ubuntu and Fedora and specifically aims to ensure trust in Firefox and Chromium-based browsers (Edge, Chrome, and Chromium).

To establish OpenSSL trust, the `openssl` tool must be on the path.

To establish browser trust (for example in Edge or Firefox), the `certutil` tool must be on the path.

When the ASP.NET Core development certificate is trusted, it is exported to a folder in the current user's home directory. To have [OpenSSL](https://www.openssl.org/) (and clients that consume it) pick up this folder, you need to set the `SSL_CERT_DIR` environment variable. You can either do this in a single session by running a command like `export SSL_CERT_DIR=$HOME/.aspnet/dev-certs/trust:/usr/lib/ssl/certs` (the exact value will be in the output when `--verbose` is passed) or by adding it your (distro- and shell-specific) configuration file (for example `.profile`).

This is required to make tools like `curl` trust the development certificate. Or, alternatively, you can pass `-CAfile` or `-CApath` to each individual `curl` invocation.

Note that this requires 1.1.1h or later or 3.0.0 or later, depending on which major version you're using.

If OpenSSL trust gets into a bad state (for example if `dotnet dev-certs https --clean` fails to remove it), it is frequently possible to set things right using the [`c_rehash`](https://docs.openssl.org/master/man1/openssl-rehash/) tool.

If you're using another browser with its own Network Security Services (NSS) store, you can use the `DOTNET_DEV_CERTS_NSSDB_PATHS` environment variable to specify a colon-delimited list of NSS directories (for example, the directory containing `cert9.db`) to which to add the development certificate.

If you store the certificates you want OpenSSL to trust in a specific directory, you can use the `DOTNET_DEV_CERTS_OPENSSL_CERTIFICATE_DIRECTORY` environment variable to indicate where that is.

Warning

If you set either of these variables, it is important that they are set to the same values each time trust is updated. If they change, the tool won't know about certificates in the former locations (for example to clean them up).

As on other platforms, development certificates are stored and trusted separately for each user. As a result, if you run `dotnet dev-certs` as a different user (for example by using `sudo`), it is _that_ user (for example `root`) that will trust the development certificate.

[linux-dev-certs](https://github.com/tmds/linux-dev-certs) is an open-source, community-supported, .NET global tool that provides a convenient way to create and trust a developer certificate on Linux. The tool is not maintained or supported by Microsoft.

The following commands install the tool and create a trusted developer certificate:

```
dotnet tool update -g linux-dev-certs
dotnet linux-dev-certs install
```

For more information or to report issues, see the [linux-dev-certs GitHub repository](https://github.com/tmds/linux-dev-certs).

This section provides help when the ASP.NET Core HTTPS development certificate has been [installed and trusted](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust), but you still have browser warnings that the certificate is not trusted. The ASP.NET Core HTTPS development certificate is used by [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).

To repair the IIS Express certificate, see [this Stackoverflow](https://stackoverflow.com/a/20048613/502537) issue.

Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app. Certificate trust is cached by browsers.

The preceding commands solve most browser trust issues. If the browser is still not trusting the certificate, follow the platform-specific suggestions that follow.

*   Delete the _C:\Users{USER}\AppData\Roaming\ASP.NET\Https_ folder.
*   Clean the solution. Delete the _bin_ and _obj_ folders.
*   Restart the development tool. For example, Visual Studio or Visual Studio Code.

*   Check the certificates in the certificate store. There should be a `localhost` certificate with the `ASP.NET Core HTTPS development certificate` friendly name both under `Current User > Personal > Certificates` and `Current User > Trusted root certification authorities > Certificates`
*   Remove all the found certificates from both Personal and Trusted root certification authorities. Do **not** remove the IIS Express localhost certificate.
*   Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app.

*   Open KeyChain Access.
*   Select the System keychain.
*   Check for the presence of a localhost certificate.
*   Check that it contains a `+` symbol on the icon to indicate it's trusted for all users.
*   Remove the certificate from the system keychain.
*   Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app.

See [HTTPS Error using IIS Express (dotnet/AspNetCore #16892)](https://github.com/dotnet/AspNetCore/issues/16892) for troubleshooting certificate issues with Visual Studio.

Check that the certificate being configured for trust is the user HTTPS developer certificate that will be used by the Kestrel server.

Check the current user default HTTPS developer Kestrel certificate at the following location:

```
ls -la ~/.dotnet/corefx/cryptography/x509stores/my
```

The HTTPS developer Kestrel certificate file is the SHA1 thumbprint. When the file is deleted via `dotnet dev-certs https --clean`, it's regenerated when needed with a different thumbprint. Check the thumbprint of the exported certificate matches with the following command:

```
openssl x509 -noout -fingerprint -sha1 -inform pem -in /usr/local/share/ca-certificates/aspnet/https.crt
```

If the certificate doesn't match, it could be one of the following:

*   An old certificate.
*   An exported a developer certificate for the root user. For this case, export the certificate.

The root user certificate can be checked at:

```
ls -la /root/.dotnet/corefx/cryptography/x509stores/my
```

To fix problems with the IIS Express certificate, select **Repair** from the Visual Studio installer. For more information, see [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/16892).

In some cases, group policy may prevent self-signed certificates from being trusted. For more information, see [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/21173).

*   [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0)
*   [Host ASP.NET Core on Linux with Nginx: HTTPS configuration](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0#https-configuration)
*   [How to Set Up SSL on IIS](https://learn.microsoft.com/en-us/iis/manage/configuring-security/how-to-set-up-ssl-on-iis)
*   [Configure endpoints for the ASP.NET Core Kestrel web server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/endpoints?view=aspnetcore-10.0)
*   [OWASP HSTS browser support](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet#Browser_Support)

Warning

API projects
------------

Do **not** use [RequireHttpsAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.requirehttpsattribute) on Web APIs that receive sensitive information. `RequireHttpsAttribute` uses HTTP status codes to redirect browsers from HTTP to HTTPS. API clients may not understand or obey redirects from HTTP to HTTPS. Such clients may send information over HTTP. Web APIs should either:

*   Not listen on HTTP.
*   Close the connection with status code 400 (Bad Request) and not serve the request.

To disable HTTP redirection in an API, set the `ASPNETCORE_URLS` environment variable or use the `--urls` command line flag. For more information, see [ASP.NET Core runtime environments](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0) and [8 ways to set the URLs for an ASP.NET Core app](https://andrewlock.net/8-ways-to-set-the-urls-for-an-aspnetcore-app/) by Andrew Lock.

HSTS and API projects
---------------------

The default API projects don't include [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#hsts) because [HSTS](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) is generally a browser only instruction. Other callers, such as phone or desktop apps, do **not** obey the instruction. Even within browsers, a single authenticated call to an API over HTTP has risks on insecure networks. The secure approach is to configure API projects to only listen to and respond over HTTPS.

Requests to an endpoint using HTTP that are redirected to HTTPS by [UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection) fail with `ERR_INVALID_REDIRECT` on the CORS preflight request.

API projects can reject HTTP requests rather than use `UseHttpsRedirection` to redirect requests to HTTPS.

We recommend that production ASP.NET Core web apps use:

*   HTTPS Redirection Middleware ([UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection)) to redirect HTTP requests to HTTPS.
*   HSTS Middleware ([UseHsts](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts)) to send HTTP Strict Transport Security Protocol (HSTS) headers to clients.

Note

Apps deployed in a reverse proxy configuration allow the proxy to handle connection security (HTTPS). If the proxy also handles HTTPS redirection, there's no need to use HTTPS Redirection Middleware. If the proxy server also handles writing HSTS headers (for example, [native HSTS support in IIS 10.0 (1709) or later](https://learn.microsoft.com/en-us/iis/get-started/whats-new-in-iis-10-version-1709/iis-10-version-1709-hsts#iis-100-version-1709-native-hsts-support)), HSTS Middleware isn't required by the app. For more information, see [Opt-out of HTTPS/HSTS on project creation](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#opt-out-of-httpshsts-on-project-creation).

The following code calls [UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection) in the `Program.cs` file:

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

The preceding highlighted code:

*   Uses the default [HttpsRedirectionOptions.RedirectStatusCode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.redirectstatuscode#microsoft-aspnetcore-httpspolicy-httpsredirectionoptions-redirectstatuscode) ([Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect)).
*   Uses the default [HttpsRedirectionOptions.HttpsPort](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.httpsport#microsoft-aspnetcore-httpspolicy-httpsredirectionoptions-httpsport) (null) unless overridden by the `ASPNETCORE_HTTPS_PORT` environment variable or [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature).

We recommend using temporary redirects rather than permanent redirects. Link caching can cause unstable behavior in development environments. If you prefer to send a permanent redirect status code when the app is in a non-`Development` environment, see the [Configure permanent redirects in production](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#configure-permanent-redirects-in-production) section. We recommend using [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) to signal to clients that only secure resource requests should be sent to the app (only in production).

A port must be available for the middleware to redirect an insecure request to HTTPS. If no port is available:

*   Redirection to HTTPS doesn't occur.
*   The middleware logs the warning "Failed to determine the https port for redirect."

Specify the HTTPS port using any of the following approaches:

*   Set [HttpsRedirectionOptions.HttpsPort](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#options).

*   Set the `https_port`[host setting](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0#https_port):

    *   In host configuration.

    *   By setting the `ASPNETCORE_HTTPS_PORT` environment variable.

    *   By adding a top-level entry in `appsettings.json`:

```
{
  "https_port": 443,
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

*   Indicate a port with the secure scheme using the [ASPNETCORE_URLS environment variable](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0#urls). The environment variable configures the server. The middleware indirectly discovers the HTTPS port via [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature). This approach doesn't work in reverse proxy deployments.

*   The ASP.NET Core web templates set an HTTPS URL in `Properties/launchsettings.json` for both Kestrel and IIS Express. `launchsettings.json` is only used on the local machine.

*   Configure an HTTPS URL endpoint for a public-facing edge deployment of [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server or [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0) server. Only **one HTTPS port** is used by the app. The middleware discovers the port via [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature).

Note

When an app is run in a reverse proxy configuration, [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature) isn't available. Set the port using one of the other approaches described in this section.

When [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) or [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0) is used as a public-facing edge server, Kestrel or HTTP.sys must be configured to listen on both:

*   The secure port where the client is redirected (typically, 443 in production and 5001 in development).
*   The insecure port (typically, 80 in production and 5000 in development).

The insecure port must be accessible by the client in order for the app to receive an insecure request and redirect the client to the secure port.

For more information, see [Kestrel endpoint configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0#endpoint-configuration) or [HTTP.sys web server implementation in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0).

Any firewall between the client and server must also have communication ports open for traffic.

If requests are forwarded in a reverse proxy configuration, use [Forwarded Headers Middleware](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0) before calling HTTPS Redirection Middleware. Forwarded Headers Middleware updates the `Request.Scheme`, using the `X-Forwarded-Proto` header. The middleware permits redirect URIs and other security policies to work correctly. When Forwarded Headers Middleware isn't used, the backend app might not receive the correct scheme and end up in a redirect loop. A common end user error message is that too many redirects have occurred.

When deploying to Azure App Service, follow the guidance in [Tutorial: Bind an existing custom SSL certificate to Azure Web Apps](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-ssl).

The following highlighted code calls [AddHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpsredirectionservicesextensions.addhttpsredirection) to configure middleware options:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

builder.Services.AddHsts(options =>
{
    options.Preload = true;
    options.IncludeSubDomains = true;
    options.MaxAge = TimeSpan.FromDays(60);
    options.ExcludedHosts.Add("example.com");
    options.ExcludedHosts.Add("www.example.com");
});

builder.Services.AddHttpsRedirection(options =>
{
    options.RedirectStatusCode = Status307TemporaryRedirect;
    options.HttpsPort = 5001;
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

Calling `AddHttpsRedirection` is only necessary to change the values of `HttpsPort` or `RedirectStatusCode`.

The preceding highlighted code:

*   Sets [HttpsRedirectionOptions.RedirectStatusCode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.redirectstatuscode) to [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect), which is the default value. Use the fields of the [StatusCodes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes) class for assignments to `RedirectStatusCode`.
*   Sets the HTTPS port to 5001.

The middleware defaults to sending a [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect) with all redirects. If you prefer to send a permanent redirect status code when the app is in a non-`Development` environment, wrap the middleware options configuration in a conditional check for a non-`Development` environment.

When configuring services in `Program.cs`:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

if (!builder.Environment.IsDevelopment())
{
    builder.Services.AddHttpsRedirection(options =>
    {
        options.RedirectStatusCode = Status308PermanentRedirect;
        options.HttpsPort = 443;
    });
}

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");

    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

An alternative to using HTTPS Redirection Middleware (`UseHttpsRedirection`) is to use URL Rewriting Middleware (`AddRedirectToHttps`). `AddRedirectToHttps` can also set the status code and port when the redirect is executed. For more information, see [URL Rewriting Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting?view=aspnetcore-10.0).

When redirecting to HTTPS without the requirement for additional redirect rules, we recommend using HTTPS Redirection Middleware (`UseHttpsRedirection`) described in this article.

Per [OWASP](https://www.owasp.org/index.php/About_The_Open_Web_Application_Security_Project), [HTTP Strict Transport Security (HSTS)](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html) is an opt-in security enhancement that's specified by a web app through the use of a response header. When a [browser that supports HSTS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html#browser-support) receives this header:

*   The browser stores configuration for the domain that prevents sending any communication over HTTP. The browser forces all communication over HTTPS.
*   The browser prevents the user from using untrusted or invalid certificates. The browser disables prompts that allow a user to temporarily trust such a certificate.

Because [HSTS](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) is enforced by the client, it has some limitations:

*   The client must support HSTS.
*   HSTS requires at least one successful HTTPS request to establish the HSTS policy.
*   The application must check every HTTP request and redirect or reject the HTTP request.

ASP.NET Core implements HSTS with the [UseHsts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.hstsbuilderextensions.usehsts) extension method. The following code calls `UseHsts` when the app isn't in [development mode](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0):

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

`UseHsts` isn't recommended in development because the HSTS settings are highly cacheable by browsers. By default, `UseHsts` excludes the local loopback address.

For production environments that are implementing HTTPS for the first time, set the initial [HstsOptions.MaxAge](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.hstsoptions.maxage) to a small value using one of the [TimeSpan](https://learn.microsoft.com/en-us/dotnet/api/system.timespan) methods. Set the value from hours to no more than a single day in case you need to revert the HTTPS infrastructure to HTTP. After you're confident in the sustainability of the HTTPS configuration, increase the HSTS `max-age` value; a commonly used value is one year.

The following highlighted code:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

builder.Services.AddHsts(options =>
{
    options.Preload = true;
    options.IncludeSubDomains = true;
    options.MaxAge = TimeSpan.FromDays(60);
    options.ExcludedHosts.Add("example.com");
    options.ExcludedHosts.Add("www.example.com");
});

builder.Services.AddHttpsRedirection(options =>
{
    options.RedirectStatusCode = Status307TemporaryRedirect;
    options.HttpsPort = 5001;
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

*   Sets the preload parameter of the `Strict-Transport-Security` header. Preload isn't part of the [RFC HSTS specification](https://tools.ietf.org/html/rfc6797), but is supported by web browsers to preload HSTS sites on fresh install. For more information, see [https://hstspreload.org/](https://hstspreload.org/).
*   Enables [includeSubDomain](https://tools.ietf.org/html/rfc6797#section-6.1.2), which applies the HSTS policy to Host subdomains.
*   Explicitly sets the `max-age` parameter of the `Strict-Transport-Security` header to 60 days. If not set, defaults to 30 days. For more information, see the [max-age directive](https://tools.ietf.org/html/rfc6797#section-6.1.1).
*   Adds `example.com` to the list of hosts to exclude.

`UseHsts` excludes the following loopback hosts:

*   `localhost` : The IPv4 loopback address.
*   `127.0.0.1` : The IPv4 loopback address.
*   `[::1]` : The IPv6 loopback address.

In some backend service scenarios where connection security is handled at the public-facing edge of the network, configuring connection security at each node isn't required. Web apps that are generated from the templates in Visual Studio or from the [dotnet new](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new) command enable [HTTPS redirection](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#require-https) and [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts). For deployments that don't require these scenarios, you can opt-out of HTTPS/HSTS when the app is created from the template.

To opt-out of HTTPS/HSTS:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [.NET CLI](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#tabpanel_1_net-cli)

Uncheck the **Configure for HTTPS** checkbox.

![Image 2: New ASP.NET Core Web Application dialog showing the Configure for HTTPS checkbox unselected.](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl/_static/out-vs2019.png?view=aspnetcore-10.0)

For the Firefox browser, see the next section.

The .NET Core SDK includes an HTTPS development certificate. The certificate is installed as part of the first-run experience. For example, `dotnet --info` produces a variation of the following output:

```
ASP.NET Core
------------
Successfully installed the ASP.NET Core HTTPS Development Certificate.
To trust the certificate run 'dotnet dev-certs https --trust' (Windows and macOS only).
For establishing trust on other platforms refer to the platform specific documentation.
For more information on configuring HTTPS see https://go.microsoft.com/fwlink/?linkid=848054.
```

Installing the .NET Core SDK installs the ASP.NET Core HTTPS development certificate to the local user certificate store. The certificate has been installed, but it's not trusted. To trust the certificate, perform the one-time step to run the `dotnet dev-certs` tool:

```
dotnet dev-certs https --trust
```

The following command provides help on the `dotnet dev-certs` tool:

```
dotnet dev-certs https --help
```

Warning

Do not create a development certificate in an environment that will be redistributed, such as a container image or virtual machine. Doing so can lead to spoofing and elevation of privilege. To help prevent this, set the `DOTNET_GENERATE_ASPNET_CERTIFICATE` environment variable to `false` prior to calling the .NET CLI for the first time. This will skip the automatic generation of the ASP.NET Core development certificate during the CLI's first-run experience.

The Firefox browser uses its own certificate store, and therefore doesn't trust the [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview) or [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) developer certificates.

There are two approaches to trusting the HTTPS certificate with Firefox, create a policy file or configure with the FireFox browser. Configuring with the browser creates the policy file, so the two approaches are equivalent.

Create a policy file (`policies.json`) at:

*   Windows: `%PROGRAMFILES%\Mozilla Firefox\distribution\`
*   MacOS: `Firefox.app/Contents/Resources/distribution`
*   Linux: See [Trust the certificate with Firefox on Linux](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff-linux) in this article.

Add the following JSON to the Firefox policy file:

```
{
  "policies": {
    "Certificates": {
      "ImportEnterpriseRoots": true
    }
  }
}
```

The preceding policy file makes Firefox trust certificates from the trusted certificates in the Windows certificate store. The next section provides an alternative approach to create the preceding policy file by using the Firefox browser.

Set `security.enterprise_roots.enabled` = `true` using the following instructions:

1.   Enter `about:config` in the FireFox browser.
2.   Select **Accept the Risk and Continue** if you accept the risk.
3.   Select **Show All**
4.   Set `security.enterprise_roots.enabled` = `true`
5.   Exit and restart Firefox

For more information, see [Setting Up Certificate Authorities (CAs) in Firefox](https://support.mozilla.org/kb/setting-certificate-authorities-firefox) and the [mozilla/policy-templates/README file](https://github.com/mozilla/policy-templates/blob/master/README.md).

See [this GitHub issue](https://github.com/dotnet/AspNetCore.Docs/issues/6199).

Establishing trust is distribution and browser specific. The following sections provide instructions for some popular distributions and the Chromium browsers (Edge and Chrome) and for Firefox.

The following instructions don't work for some Ubuntu versions, such as 20.04. For more information, see GitHub issue [dotnet/AspNetCore.Docs #23686](https://github.com/dotnet/AspNetCore.Docs/issues/23686).

1.   Install [OpenSSL](https://www.openssl.org/) 1.1.1h or later. See your distribution for instructions on how to update OpenSSL.

2.   Run the following commands:

```
dotnet dev-certs https
sudo -E dotnet dev-certs https -ep /usr/local/share/ca-certificates/aspnet/https.crt --format PEM
sudo update-ca-certificates
```

The preceding commands:

*   Ensure the current user's developer certificate is created.
*   Exports the certificate with elevated permissions needed for the `ca-certificates` folder, using the current user's environment.
*   Removing the `-E` flag exports the root user certificate, generating it if necessary. Each newly generated certificate has a different thumbprint. When running as root, `sudo` and `-E` are not needed.

The path in the preceding command is specific for Ubuntu. For other distributions, select an appropriate path or use the path for the Certificate Authorities (CAs).

See:

*   [This GitHub comment](https://github.com/dotnet/aspnetcore/issues/32361#issuecomment-837111639)
*   [Fedora: Using Shared System Certificates](https://docs.fedoraproject.org/en-US/quick-docs/using-shared-system-certificates/)
*   [Set up a .NET development environment](https://fedoramagazine.org/set-up-a-net-development-environment/) on Fedora.

See [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/32842).

The following instructions don't work for some Linux distributions, such as Ubuntu 20.04. For more information, see GitHub issue [dotnet/AspNetCore.Docs #23686](https://github.com/dotnet/AspNetCore.Docs/issues/23686).

The [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about) generates an HTTPS self-signed development certificate, which by default isn't trusted in Windows. The easiest way to have Windows trust the WSL certificate, is to configure WSL to use the same certificate as Windows:

*   On _**Windows**_, export the developer certificate to a file:

```
dotnet dev-certs https -ep https.pfx -p $CREDENTIAL_PLACEHOLDER$ --trust
```

Where `$CREDENTIAL_PLACEHOLDER$` is a password.

*   In a WSL window, import the exported certificate on the WSL instance:

```
dotnet dev-certs https --clean --import <<path-to-pfx>> --password $CREDENTIAL_PLACEHOLDER$
```

The preceding approach is a one time operation per certificate and per WSL distribution. It's easier than exporting the certificate over and over. If you update or regenerate the certificate on windows, you might need to run the preceding commands again.

This section provides help when the ASP.NET Core HTTPS development certificate has been [installed and trusted](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust), but you still have browser warnings that the certificate is not trusted. The ASP.NET Core HTTPS development certificate is used by [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).

To repair the IIS Express certificate, see [this Stackoverflow](https://stackoverflow.com/a/20048613/502537) issue.

Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app. Certificate trust is cached by browsers.

The preceding commands solve most browser trust issues. If the browser is still not trusting the certificate, follow the platform-specific suggestions that follow.

*   Delete the _C:\Users{USER}\AppData\Roaming\ASP.NET\Https_ folder.
*   Clean the solution. Delete the _bin_ and _obj_ folders.
*   Restart the development tool. For example, Visual Studio or Visual Studio Code.

*   Check the certificates in the certificate store. There should be a `localhost` certificate with the `ASP.NET Core HTTPS development certificate` friendly name both under `Current User > Personal > Certificates` and `Current User > Trusted root certification authorities > Certificates`
*   Remove all the found certificates from both Personal and Trusted root certification authorities. Do **not** remove the IIS Express localhost certificate.
*   Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app.

*   Open KeyChain Access.
*   Select the System keychain.
*   Check for the presence of a localhost certificate.
*   Check that it contains a `+` symbol on the icon to indicate it's trusted for all users.
*   Remove the certificate from the system keychain.
*   Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app.

See [HTTPS Error using IIS Express (dotnet/AspNetCore #16892)](https://github.com/dotnet/AspNetCore/issues/16892) for troubleshooting certificate issues with Visual Studio.

Check that the certificate being configured for trust is the user HTTPS developer certificate that will be used by the Kestrel server.

Check the current user default HTTPS developer Kestrel certificate at the following location:

```
ls -la ~/.dotnet/corefx/cryptography/x509stores/my
```

The HTTPS developer Kestrel certificate file is the SHA1 thumbprint. When the file is deleted via `dotnet dev-certs https --clean`, it's regenerated when needed with a different thumbprint. Check the thumbprint of the exported certificate matches with the following command:

```
openssl x509 -noout -fingerprint -sha1 -inform pem -in /usr/local/share/ca-certificates/aspnet/https.crt
```

If the certificate doesn't match, it could be one of the following:

*   An old certificate.
*   An exported a developer certificate for the root user. For this case, export the certificate.

The root user certificate can be checked at:

```
ls -la /root/.dotnet/corefx/cryptography/x509stores/my
```

To fix problems with the IIS Express certificate, select **Repair** from the Visual Studio installer. For more information, see [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/16892).

In some cases, group policy may prevent self-signed certificates from being trusted. For more information, see [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/21173).

*   [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0)
*   [Host ASP.NET Core on Linux with Nginx: HTTPS configuration](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0#https-configuration)
*   [How to Set Up SSL on IIS](https://learn.microsoft.com/en-us/iis/manage/configuring-security/how-to-set-up-ssl-on-iis)
*   [Configure endpoints for the ASP.NET Core Kestrel web server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/endpoints?view=aspnetcore-10.0)
*   [OWASP HSTS browser support](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet#Browser_Support)

Warning

API projects
------------

Do **not** use [RequireHttpsAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.requirehttpsattribute) on Web APIs that receive sensitive information. `RequireHttpsAttribute` uses HTTP status codes to redirect browsers from HTTP to HTTPS. API clients may not understand or obey redirects from HTTP to HTTPS. Such clients may send information over HTTP. Web APIs should either:

*   Not listen on HTTP.
*   Close the connection with status code 400 (Bad Request) and not serve the request.

To disable HTTP redirection in an API, set the `ASPNETCORE_URLS` environment variable or use the `--urls` command line flag. For more information, see [ASP.NET Core runtime environments](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0) and [5 ways to set the URLs for an ASP.NET Core app](https://andrewlock.net/5-ways-to-set-the-urls-for-an-aspnetcore-app/) by Andrew Lock.

HSTS and API projects
---------------------

The default API projects don't include [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#hsts) because HSTS is generally a browser only instruction. Other callers, such as phone or desktop apps, do **not** obey the instruction. Even within browsers, a single authenticated call to an API over HTTP has risks on insecure networks. The secure approach is to configure API projects to only listen to and respond over HTTPS.

We recommend that production ASP.NET Core web apps use:

*   HTTPS Redirection Middleware ([UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection)) to redirect HTTP requests to HTTPS.
*   HSTS Middleware ([UseHsts](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts)) to send HTTP Strict Transport Security Protocol (HSTS) headers to clients.

Note

Apps deployed in a reverse proxy configuration allow the proxy to handle connection security (HTTPS). If the proxy also handles HTTPS redirection, there's no need to use HTTPS Redirection Middleware. If the proxy server also handles writing HSTS headers (for example, [native HSTS support in IIS 10.0 (1709) or later](https://learn.microsoft.com/en-us/iis/get-started/whats-new-in-iis-10-version-1709/iis-10-version-1709-hsts#iis-100-version-1709-native-hsts-support)), HSTS Middleware isn't required by the app. For more information, see [Opt-out of HTTPS/HSTS on project creation](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#opt-out-of-httpshsts-on-project-creation).

The following code calls `UseHttpsRedirection` in the `Startup` class:

```
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
    else
    {
        app.UseExceptionHandler("/Error");
        // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
        app.UseHsts();
    }

    app.UseHttpsRedirection();
    app.UseStaticFiles();

    app.UseRouting();

    app.UseAuthorization();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapRazorPages();
    });
}
```

The preceding highlighted code:

*   Uses the default [HttpsRedirectionOptions.RedirectStatusCode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.redirectstatuscode#microsoft-aspnetcore-httpspolicy-httpsredirectionoptions-redirectstatuscode) ([Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect)).
*   Uses the default [HttpsRedirectionOptions.HttpsPort](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.httpsport#microsoft-aspnetcore-httpspolicy-httpsredirectionoptions-httpsport) (null) unless overridden by the `ASPNETCORE_HTTPS_PORT` environment variable or [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature).

We recommend using temporary redirects rather than permanent redirects. Link caching can cause unstable behavior in development environments. If you prefer to send a permanent redirect status code when the app is in a non-`Development` environment, see the [Configure permanent redirects in production](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#configure-permanent-redirects-in-production) section. We recommend using [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) to signal to clients that only secure resource requests should be sent to the app (only in production).

A port must be available for the middleware to redirect an insecure request to HTTPS. If no port is available:

*   Redirection to HTTPS doesn't occur.
*   The middleware logs the warning "Failed to determine the https port for redirect."

Specify the HTTPS port using any of the following approaches:

*   Set [HttpsRedirectionOptions.HttpsPort](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#options).

*   Set the `https_port`[host setting](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0#https_port):

    *   In host configuration.

    *   By setting the `ASPNETCORE_HTTPS_PORT` environment variable.

    *   By adding a top-level entry in `appsettings.json`:

```
{
    "https_port": 443,
    "Logging": {
        "LogLevel": {
            "Default": "Information",
            "Microsoft": "Warning",
            "Microsoft.Hosting.Lifetime": "Information"
        }
    },
    "AllowedHosts": "*"
}
```

*   Indicate a port with the secure scheme using the [ASPNETCORE_URLS environment variable](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0#urls). The environment variable configures the server. The middleware indirectly discovers the HTTPS port via [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature). This approach doesn't work in reverse proxy deployments.

*   In development, set an HTTPS URL in `launchsettings.json`. Enable HTTPS when IIS Express is used.

*   Configure an HTTPS URL endpoint for a public-facing edge deployment of [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server or [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0) server. Only **one HTTPS port** is used by the app. The middleware discovers the port via [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature).

Note

When an app is run in a reverse proxy configuration, [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature) isn't available. Set the port using one of the other approaches described in this section.

When Kestrel or HTTP.sys is used as a public-facing edge server, Kestrel or HTTP.sys must be configured to listen on both:

*   The secure port where the client is redirected (typically, 443 in production and 5001 in development).
*   The insecure port (typically, 80 in production and 5000 in development).

The insecure port must be accessible by the client in order for the app to receive an insecure request and redirect the client to the secure port.

For more information, see [Kestrel endpoint configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0#endpoint-configuration) or [HTTP.sys web server implementation in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0).

Any firewall between the client and server must also have communication ports open for traffic.

If requests are forwarded in a reverse proxy configuration, use [Forwarded Headers Middleware](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0) before calling HTTPS Redirection Middleware. Forwarded Headers Middleware updates the `Request.Scheme`, using the `X-Forwarded-Proto` header. The middleware permits redirect URIs and other security policies to work correctly. When Forwarded Headers Middleware isn't used, the backend app might not receive the correct scheme and end up in a redirect loop. A common end user error message is that too many redirects have occurred.

When deploying to Azure App Service, follow the guidance in [Tutorial: Bind an existing custom SSL certificate to Azure Web Apps](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-ssl).

The following highlighted code calls [AddHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpsredirectionservicesextensions.addhttpsredirection) to configure middleware options:

```
public void ConfigureServices(IServiceCollection services)
{
    services.AddRazorPages();

    services.AddHsts(options =>
    {
        options.Preload = true;
        options.IncludeSubDomains = true;
        options.MaxAge = TimeSpan.FromDays(60);
        options.ExcludedHosts.Add("example.com");
        options.ExcludedHosts.Add("www.example.com");
    });

    services.AddHttpsRedirection(options =>
    {
        options.RedirectStatusCode = (int) HttpStatusCode.TemporaryRedirect;
        options.HttpsPort = 5001;
    });
}
```

Calling `AddHttpsRedirection` is only necessary to change the values of `HttpsPort` or `RedirectStatusCode`.

The preceding highlighted code:

*   Sets [HttpsRedirectionOptions.RedirectStatusCode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.redirectstatuscode) to [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect), which is the default value. Use the fields of the [StatusCodes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes) class for assignments to `RedirectStatusCode`.
*   Sets the HTTPS port to 5001.

The middleware defaults to sending a [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect) with all redirects. If you prefer to send a permanent redirect status code when the app is in a non-`Development` environment, wrap the middleware options configuration in a conditional check for a non-`Development` environment.

When configuring services in `Startup.cs`:

```
public void ConfigureServices(IServiceCollection services)
{
    // IWebHostEnvironment (stored in _env) is injected into the Startup class.
    if (!_env.IsDevelopment())
    {
        services.AddHttpsRedirection(options =>
        {
            options.RedirectStatusCode = (int) HttpStatusCode.PermanentRedirect;
            options.HttpsPort = 443;
        });
    }
}
```

An alternative to using HTTPS Redirection Middleware (`UseHttpsRedirection`) is to use URL Rewriting Middleware (`AddRedirectToHttps`). `AddRedirectToHttps` can also set the status code and port when the redirect is executed. For more information, see [URL Rewriting Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting?view=aspnetcore-10.0).

When redirecting to HTTPS without the requirement for additional redirect rules, we recommend using HTTPS Redirection Middleware (`UseHttpsRedirection`) described in this article.

Per [OWASP](https://www.owasp.org/index.php/About_The_Open_Web_Application_Security_Project), [HTTP Strict Transport Security (HSTS)](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html) is an opt-in security enhancement that's specified by a web app through the use of a response header. When a [browser that supports HSTS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html#browser-support) receives this header:

*   The browser stores configuration for the domain that prevents sending any communication over HTTP. The browser forces all communication over HTTPS.
*   The browser prevents the user from using untrusted or invalid certificates. The browser disables prompts that allow a user to temporarily trust such a certificate.

Because HSTS is enforced by the client, it has some limitations:

*   The client must support HSTS.
*   HSTS requires at least one successful HTTPS request to establish the HSTS policy.
*   The application must check every HTTP request and redirect or reject the HTTP request.

ASP.NET Core implements HSTS with the `UseHsts` extension method. The following code calls `UseHsts` when the app isn't in [development mode](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0):

```
public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
{
    if (env.IsDevelopment())
    {
        app.UseDeveloperExceptionPage();
    }
    else
    {
        app.UseExceptionHandler("/Error");
        // The default HSTS value is 30 days. You may want to change this for production scenarios, see https://aka.ms/aspnetcore-hsts.
        app.UseHsts();
    }

    app.UseHttpsRedirection();
    app.UseStaticFiles();

    app.UseRouting();

    app.UseAuthorization();

    app.UseEndpoints(endpoints =>
    {
        endpoints.MapRazorPages();
    });
}
```

`UseHsts` isn't recommended in development because the HSTS settings are highly cacheable by browsers. By default, `UseHsts` excludes the local loopback address.

For production environments that are implementing HTTPS for the first time, set the initial [HstsOptions.MaxAge](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.hstsoptions.maxage) to a small value using one of the [TimeSpan](https://learn.microsoft.com/en-us/dotnet/api/system.timespan) methods. Set the value from hours to no more than a single day in case you need to revert the HTTPS infrastructure to HTTP. After you're confident in the sustainability of the HTTPS configuration, increase the HSTS `max-age` value; a commonly used value is one year.

The following code:

```
public void ConfigureServices(IServiceCollection services)
{
    services.AddRazorPages();

    services.AddHsts(options =>
    {
        options.Preload = true;
        options.IncludeSubDomains = true;
        options.MaxAge = TimeSpan.FromDays(60);
        options.ExcludedHosts.Add("example.com");
        options.ExcludedHosts.Add("www.example.com");
    });

    services.AddHttpsRedirection(options =>
    {
        options.RedirectStatusCode = (int) HttpStatusCode.TemporaryRedirect;
        options.HttpsPort = 5001;
    });
}
```

*   Sets the preload parameter of the `Strict-Transport-Security` header. Preload isn't part of the [RFC HSTS specification](https://tools.ietf.org/html/rfc6797), but is supported by web browsers to preload HSTS sites on fresh install. For more information, see [https://hstspreload.org/](https://hstspreload.org/).
*   Enables [includeSubDomain](https://tools.ietf.org/html/rfc6797#section-6.1.2), which applies the HSTS policy to Host subdomains.
*   Explicitly sets the `max-age` parameter of the `Strict-Transport-Security` header to 60 days. If not set, defaults to 30 days. For more information, see the [max-age directive](https://tools.ietf.org/html/rfc6797#section-6.1.1).
*   Adds `example.com` to the list of hosts to exclude.

`UseHsts` excludes the following loopback hosts:

*   `localhost` : The IPv4 loopback address.
*   `127.0.0.1` : The IPv4 loopback address.
*   `[::1]` : The IPv6 loopback address.

In some backend service scenarios where connection security is handled at the public-facing edge of the network, configuring connection security at each node isn't required. Web apps that are generated from the templates in Visual Studio or from the [dotnet new](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new) command enable [HTTPS redirection](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#require-https) and [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts). For deployments that don't require these scenarios, you can opt-out of HTTPS/HSTS when the app is created from the template.

To opt-out of HTTPS/HSTS:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#tabpanel_3_visual-studio)
*   [.NET CLI](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#tabpanel_3_net-cli)

Uncheck the **Configure for HTTPS** checkbox.

![Image 3: Additional information dialog for New ASP.NET Core Web App template, showing the Configure for HTTPS checkbox](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl/_static/out-vs2022.png?view=aspnetcore-10.0)

For the Firefox browser, see the next section.

The .NET Core SDK includes an HTTPS development certificate. The certificate is installed as part of the first-run experience. For example, running `dotnet new webapp` for the first time produces a variation of the following output:

```
Installed an ASP.NET Core HTTPS development certificate.
To trust the certificate, run 'dotnet dev-certs https --trust'
Learn about HTTPS: https://aka.ms/dotnet-https
```

Installing the .NET Core SDK installs the ASP.NET Core HTTPS development certificate to the local user certificate store. The certificate has been installed, but it's not trusted. To trust the certificate, perform the one-time step to run the `dotnet dev-certs` tool:

```
dotnet dev-certs https --trust
```

The following command provides help on the `dotnet dev-certs` tool:

```
dotnet dev-certs https --help
```

Warning

Do not create a development certificate in an environment that will be redistributed, such as a container image or virtual machine. Doing so can lead to spoofing and elevation of privilege. To help prevent this, set the `DOTNET_GENERATE_ASPNET_CERTIFICATE` environment variable to `false` prior to calling the .NET CLI for the first time. This will skip the automatic generation of the ASP.NET Core development certificate during the CLI's first-run experience.

The Firefox browser uses its own certificate store, and therefore doesn't trust the [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview) or [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) developer certificates.

There are two approaches to trusting the HTTPS certificate with Firefox, create a policy file or configure with the FireFox browser. Configuring with the browser creates the policy file, so the two approaches are equivalent.

Create a policy file (`policies.json`) at:

*   Windows: `%PROGRAMFILES%\Mozilla Firefox\distribution\`
*   MacOS: `Firefox.app/Contents/Resources/distribution`
*   Linux: See [Trust the certificate with Firefox on Linux](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff-linux) later in this article.

Add the following JSON to the Firefox policy file:

```
{
  "policies": {
    "Certificates": {
      "ImportEnterpriseRoots": true
    }
  }
}
```

The preceding policy file makes Firefox trust certificates from the trusted certificates in the Windows certificate store. The next section provides an alternative approach to create the preceding policy file by using the Firefox browser.

Set `security.enterprise_roots.enabled` = `true` using the following instructions:

1.   Enter `about:config` in the FireFox browser.
2.   Select **Accept the Risk and Continue** if you accept the risk.
3.   Select **Show All**.
4.   Set `security.enterprise_roots.enabled` = `true`.
5.   Exit and restart Firefox.

For more information, see [Setting Up Certificate Authorities (CAs) in Firefox](https://support.mozilla.org/kb/setting-certificate-authorities-firefox) and the [mozilla/policy-templates/README file](https://github.com/mozilla/policy-templates/blob/master/README.md).

See [this GitHub issue](https://github.com/dotnet/AspNetCore.Docs/issues/6199).

Establishing trust is distribution and browser specific. The following sections provide instructions for some popular distributions and the Chromium browsers (Edge and Chrome) and for Firefox.

1.   Install [OpenSSL](https://www.openssl.org/) 1.1.1h or later. See your distribution for instructions on how to update OpenSSL.

2.   Run the following commands:

```
dotnet dev-certs https
sudo -E dotnet dev-certs https -ep /usr/local/share/ca-certificates/aspnet/https.crt --format PEM
sudo update-ca-certificates
```

The preceding commands:

*   Ensure the current user's developer certificate is created.
*   Export the certificate with elevated permissions needed for the `ca-certificates` folder, using the current user's environment.
*   Remove the `-E` flag to export the root user certificate, generating it if necessary. Each newly generated certificate has a different thumbprint. When running as root, `sudo` and `-E` are not needed.

The path in the preceding command is specific for Ubuntu. For other distributions, select an appropriate path or use the path for the Certificate Authorities (CAs).

For chromium browsers on Linux:

*   Install the `libnss3-tools` for your distribution.

*   Create or verify the `$HOME/.pki/nssdb` folder exists on the machine.

*   Export the certificate with the following command:

```
dotnet dev-certs https
sudo -E dotnet dev-certs https -ep /usr/local/share/ca-certificates/aspnet/https.crt --format PEM
```

The path in the preceding command is specific for Ubuntu. For other distributions, select an appropriate path or use the path for the Certificate Authorities (CAs).

*   Run the following commands:

```
certutil -d sql:$HOME/.pki/nssdb -A -t "P,," -n localhost -i /usr/local/share/ca-certificates/aspnet/https.crt
```
*   Exit and restart the browser.

*   Export the certificate with the following command:

```
dotnet dev-certs https
sudo -E dotnet dev-certs https -ep /usr/local/share/ca-certificates/aspnet/https.crt --format PEM
```

The path in the preceding command is specific for Ubuntu. For other distributions, select an appropriate path or use the path for the Certificate Authorities (CAs).

*   Create a JSON file at `/usr/lib/firefox/distribution/policies.json` with the following contents:

```
cat <<EOF | sudo tee /usr/lib/firefox/distribution/policies.json
{
    "policies": {
        "Certificates": {
            "Install": [
                "/usr/local/share/ca-certificates/aspnet/https.crt"
            ]
        }
    }
}
EOF
```

See [Configure trust of HTTPS certificate using Firefox browser](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff-ba) in this article for an alternative way to configure the policy file using the browser.

```
echo 'pref("general.config.filename", "firefox.cfg");
pref("general.config.obscure_value", 0);' > ./autoconfig.js

echo '//Enable policies.json
lockPref("browser.policies.perUserDir", false);' > firefox.cfg

echo "{
    \"policies\": {
        \"Certificates\": {
            \"Install\": [
                \"aspnetcore-localhost-https.crt\"
            ]
        }
    }
}" > policies.json

dotnet dev-certs https -ep localhost.crt --format PEM

sudo mv autoconfig.js /usr/lib64/firefox/
sudo mv firefox.cfg /usr/lib64/firefox/
sudo mv policies.json /usr/lib64/firefox/distribution/
mkdir -p ~/.mozilla/certificates
cp localhost.crt ~/.mozilla/certificates/aspnetcore-localhost-https.crt
rm localhost.crt
```

```
sudo cp localhost.crt /etc/pki/tls/certs/localhost.pem
sudo update-ca-trust
rm localhost.crt
```

See [this GitHub comment](https://github.com/dotnet/aspnetcore/issues/32361#issuecomment-837111639) for more information.

See [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/32842).

The [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about) generates an HTTPS self-signed development certificate. To configure the Windows certificate store to trust the WSL certificate:

*   Export the developer certificate to a file on _**Windows**_:

```
dotnet dev-certs https -ep C:\<<path-to-folder>>\aspnetcore.pfx -p $CREDENTIAL_PLACEHOLDER$
```

Where `$CREDENTIAL_PLACEHOLDER$` is a password.

*   In a WSL window, import the exported certificate on the WSL instance:

```
dotnet dev-certs https --clean --import /mnt/c/<<path-to-folder>>/aspnetcore.pfx -p $CREDENTIAL_PLACEHOLDER$
```

The preceding approach is a one time operation per certificate and per WSL distribution. It's easier than exporting the certificate over and over. If you update or regenerate the certificate on windows, you might need to run the preceding commands again.

This section provides help when the ASP.NET Core HTTPS development certificate has been [installed and trusted](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust), but you still have browser warnings that the certificate is not trusted. The ASP.NET Core HTTPS development certificate is used by [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).

To repair the IIS Express certificate, see [this Stackoverflow](https://stackoverflow.com/a/20048613/502537) issue.

Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances that are open. Open a new browser window to the app. Certificate trust is cached by browsers.

The preceding commands solve most browser trust issues. If the browser is still not trusting the certificate, follow the platform-specific suggestions that follow.

*   Delete the _C:\Users{USER}\AppData\Roaming\ASP.NET\Https_ folder.
*   Clean the solution. Delete the _bin_ and _obj_ folders.
*   Restart the development tool. For example, Visual Studio, Visual Studio Code, or Visual Studio for Mac.

*   Check the certificates in the certificate store. There should be a `localhost` certificate with the `ASP.NET Core HTTPS development certificate` friendly name both under `Current User > Personal > Certificates` and `Current User > Trusted root certification authorities > Certificates`
*   Remove all the found certificates from both Personal and Trusted root certification authorities. Do **not** remove the IIS Express localhost certificate.
*   Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances that are open. Open a new browser window to the app. Certificate trust is cached by browsers.

*   Open KeyChain Access.
*   Select the System keychain.
*   Check for the presence of a localhost certificate.
*   Check that it contains a `+` symbol on the icon to indicate it's trusted for all users.
*   Remove the certificate from the system keychain.
*   Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances that are open. Open a new browser window to the app. Certificate trust is cached by browsers.

See [HTTPS Error using IIS Express (dotnet/AspNetCore #16892)](https://github.com/dotnet/AspNetCore/issues/16892) for troubleshooting certificate issues with Visual Studio.

Check that the certificate being configured for trust is the user HTTPS developer certificate that will be used by the Kestrel server.

Check the current user default HTTPS developer Kestrel certificate at the following location:

```
ls -la ~/.dotnet/corefx/cryptography/x509stores/my
```

The HTTPS developer Kestrel certificate file is the SHA1 thumbprint. When the file is deleted via `dotnet dev-certs https --clean`, it's regenerated when needed with a different thumbprint. Check the thumbprint of the exported certificate matches with the following command:

```
openssl x509 -noout -fingerprint -sha1 -inform pem -in /usr/local/share/ca-certificates/aspnet/https.crt
```

If the certificate doesn't match, it could be one of the following:

*   An old certificate.
*   An exported a developer certificate for the root user. For this case, export the certificate.

The root user certificate can be checked at:

```
ls -la /root/.dotnet/corefx/cryptography/x509stores/my
```

To fix problems with the IIS Express certificate, select **Repair** from the Visual Studio installer. For more information, see [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/16892).

*   [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0)
*   [Host ASP.NET Core on Linux with Nginx: HTTPS configuration](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0#https-configuration)
*   [How to Set Up SSL on IIS](https://learn.microsoft.com/en-us/iis/manage/configuring-security/how-to-set-up-ssl-on-iis)
*   [OWASP HSTS browser support](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet#Browser_Support)
*   [`dotnet dev-certs`](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-dev-certs)

Warning

API projects
------------

Do **not** use [RequireHttpsAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.requirehttpsattribute) on Web APIs that receive sensitive information. `RequireHttpsAttribute` uses HTTP status codes to redirect browsers from HTTP to HTTPS. API clients may not understand or obey redirects from HTTP to HTTPS. Such clients may send information over HTTP. Web APIs should either:

*   Not listen on HTTP.
*   Close the connection with status code 400 (Bad Request) and not serve the request.

To disable HTTP redirection in an API, set the `ASPNETCORE_URLS` environment variable or use the `--urls` command line flag. For more information, see [ASP.NET Core runtime environments](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0) and [8 ways to set the URLs for an ASP.NET Core app](https://andrewlock.net/8-ways-to-set-the-urls-for-an-aspnetcore-app/) by Andrew Lock.

HSTS and API projects
---------------------

The default API projects don't include [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#hsts) because [HSTS](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) is generally a browser only instruction. Other callers, such as phone or desktop apps, do **not** obey the instruction. Even within browsers, a single authenticated call to an API over HTTP has risks on insecure networks. The secure approach is to configure API projects to only listen to and respond over HTTPS.

Requests to an endpoint using HTTP that are redirected to HTTPS by [UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection) fail with `ERR_INVALID_REDIRECT` on the CORS preflight request.

API projects can reject HTTP requests rather than use `UseHttpsRedirection` to redirect requests to HTTPS.

We recommend that production ASP.NET Core web apps use:

*   HTTPS Redirection Middleware ([UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection)) to redirect HTTP requests to HTTPS.
*   HSTS Middleware ([UseHsts](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts)) to send HTTP Strict Transport Security Protocol (HSTS) headers to clients.

Note

Apps deployed in a reverse proxy configuration allow the proxy to handle connection security (HTTPS). If the proxy also handles HTTPS redirection, there's no need to use HTTPS Redirection Middleware. If the proxy server also handles writing HSTS headers (for example, [native HSTS support in IIS 10.0 (1709) or later](https://learn.microsoft.com/en-us/iis/get-started/whats-new-in-iis-10-version-1709/iis-10-version-1709-hsts#iis-100-version-1709-native-hsts-support)), HSTS Middleware isn't required by the app. For more information, see [Opt-out of HTTPS/HSTS on project creation](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#opt-out-of-httpshsts-on-project-creation).

The following code calls [UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection) in the `Program.cs` file:

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

The preceding highlighted code:

*   Uses the default [HttpsRedirectionOptions.RedirectStatusCode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.redirectstatuscode#microsoft-aspnetcore-httpspolicy-httpsredirectionoptions-redirectstatuscode) ([Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect)).
*   Uses the default [HttpsRedirectionOptions.HttpsPort](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.httpsport#microsoft-aspnetcore-httpspolicy-httpsredirectionoptions-httpsport) (null) unless overridden by the `ASPNETCORE_HTTPS_PORT` environment variable or [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature).

We recommend using temporary redirects rather than permanent redirects. Link caching can cause unstable behavior in development environments. If you prefer to send a permanent redirect status code when the app is in a non-`Development` environment, see the [Configure permanent redirects in production](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#configure-permanent-redirects-in-production) section. We recommend using [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) to signal to clients that only secure resource requests should be sent to the app (only in production).

A port must be available for the middleware to redirect an insecure request to HTTPS. If no port is available:

*   Redirection to HTTPS doesn't occur.
*   The middleware logs the warning "Failed to determine the https port for redirect."

Specify the HTTPS port using any of the following approaches:

*   Set [HttpsRedirectionOptions.HttpsPort](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#options).

*   Set the `https_port`[host setting](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0#https_port):

    *   In host configuration.

    *   By setting the `ASPNETCORE_HTTPS_PORT` environment variable.

    *   By adding a top-level entry in `appsettings.json`:

```
{
  "https_port": 443,
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

*   Indicate a port with the secure scheme using the [ASPNETCORE_URLS environment variable](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0#urls). The environment variable configures the server. The middleware indirectly discovers the HTTPS port via [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature). This approach doesn't work in reverse proxy deployments.

*   The ASP.NET Core web templates set an HTTPS URL in `Properties/launchsettings.json` for both Kestrel and IIS Express. `launchsettings.json` is only used on the local machine.

*   Configure an HTTPS URL endpoint for a public-facing edge deployment of [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server or [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0) server. Only **one HTTPS port** is used by the app. The middleware discovers the port via [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature).

Note

When an app is run in a reverse proxy configuration, [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature) isn't available. Set the port using one of the other approaches described in this section.

When [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) or [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0) is used as a public-facing edge server, Kestrel or HTTP.sys must be configured to listen on both:

*   The secure port where the client is redirected (typically, 443 in production and 5001 in development).
*   The insecure port (typically, 80 in production and 5000 in development).

The insecure port must be accessible by the client in order for the app to receive an insecure request and redirect the client to the secure port.

For more information, see [Kestrel endpoint configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0#endpoint-configuration) or [HTTP.sys web server implementation in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0).

Any firewall between the client and server must also have communication ports open for traffic.

If requests are forwarded in a reverse proxy configuration, use [Forwarded Headers Middleware](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0) before calling HTTPS Redirection Middleware. Forwarded Headers Middleware updates the `Request.Scheme`, using the `X-Forwarded-Proto` header. The middleware permits redirect URIs and other security policies to work correctly. When Forwarded Headers Middleware isn't used, the backend app might not receive the correct scheme and end up in a redirect loop. A common end user error message is that too many redirects have occurred.

When deploying to Azure App Service, follow the guidance in [Tutorial: Bind an existing custom SSL certificate to Azure Web Apps](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-ssl).

The following highlighted code calls [AddHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpsredirectionservicesextensions.addhttpsredirection) to configure middleware options:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

builder.Services.AddHsts(options =>
{
    options.Preload = true;
    options.IncludeSubDomains = true;
    options.MaxAge = TimeSpan.FromDays(60);
    options.ExcludedHosts.Add("example.com");
    options.ExcludedHosts.Add("www.example.com");
});

builder.Services.AddHttpsRedirection(options =>
{
    options.RedirectStatusCode = Status307TemporaryRedirect;
    options.HttpsPort = 5001;
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

Calling `AddHttpsRedirection` is only necessary to change the values of `HttpsPort` or `RedirectStatusCode`.

The preceding highlighted code:

*   Sets [HttpsRedirectionOptions.RedirectStatusCode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.redirectstatuscode) to [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect), which is the default value. Use the fields of the [StatusCodes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes) class for assignments to `RedirectStatusCode`.
*   Sets the HTTPS port to 5001.

The middleware defaults to sending a [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect) with all redirects. If you prefer to send a permanent redirect status code when the app is in a non-`Development` environment, wrap the middleware options configuration in a conditional check for a non-`Development` environment.

When configuring services in `Program.cs`:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

if (!builder.Environment.IsDevelopment())
{
    builder.Services.AddHttpsRedirection(options =>
    {
        options.RedirectStatusCode = Status308PermanentRedirect;
        options.HttpsPort = 443;
    });
}

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");

    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

An alternative to using HTTPS Redirection Middleware (`UseHttpsRedirection`) is to use URL Rewriting Middleware (`AddRedirectToHttps`). `AddRedirectToHttps` can also set the status code and port when the redirect is executed. For more information, see [URL Rewriting Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting?view=aspnetcore-10.0).

When redirecting to HTTPS without the requirement for additional redirect rules, we recommend using HTTPS Redirection Middleware (`UseHttpsRedirection`) described in this article.

Per [OWASP](https://www.owasp.org/index.php/About_The_Open_Web_Application_Security_Project), [HTTP Strict Transport Security (HSTS)](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html) is an opt-in security enhancement that's specified by a web app through the use of a response header. When a [browser that supports HSTS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html#browser-support) receives this header:

*   The browser stores configuration for the domain that prevents sending any communication over HTTP. The browser forces all communication over HTTPS.
*   The browser prevents the user from using untrusted or invalid certificates. The browser disables prompts that allow a user to temporarily trust such a certificate.

Because [HSTS](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) is enforced by the client, it has some limitations:

*   The client must support HSTS.
*   HSTS requires at least one successful HTTPS request to establish the HSTS policy.
*   The application must check every HTTP request and redirect or reject the HTTP request.

ASP.NET Core implements HSTS with the [UseHsts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.hstsbuilderextensions.usehsts) extension method. The following code calls `UseHsts` when the app isn't in [development mode](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0):

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

`UseHsts` isn't recommended in development because the HSTS settings are highly cacheable by browsers. By default, `UseHsts` excludes the local loopback address.

For production environments that are implementing HTTPS for the first time, set the initial [HstsOptions.MaxAge](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.hstsoptions.maxage) to a small value using one of the [TimeSpan](https://learn.microsoft.com/en-us/dotnet/api/system.timespan) methods. Set the value from hours to no more than a single day in case you need to revert the HTTPS infrastructure to HTTP. After you're confident in the sustainability of the HTTPS configuration, increase the HSTS `max-age` value; a commonly used value is one year.

The following highlighted code:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

builder.Services.AddHsts(options =>
{
    options.Preload = true;
    options.IncludeSubDomains = true;
    options.MaxAge = TimeSpan.FromDays(60);
    options.ExcludedHosts.Add("example.com");
    options.ExcludedHosts.Add("www.example.com");
});

builder.Services.AddHttpsRedirection(options =>
{
    options.RedirectStatusCode = Status307TemporaryRedirect;
    options.HttpsPort = 5001;
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

*   Sets the preload parameter of the `Strict-Transport-Security` header. Preload isn't part of the [RFC HSTS specification](https://tools.ietf.org/html/rfc6797), but is supported by web browsers to preload HSTS sites on fresh install. For more information, see [https://hstspreload.org/](https://hstspreload.org/).
*   Enables [includeSubDomain](https://tools.ietf.org/html/rfc6797#section-6.1.2), which applies the HSTS policy to Host subdomains.
*   Explicitly sets the `max-age` parameter of the `Strict-Transport-Security` header to 60 days. If not set, defaults to 30 days. For more information, see the [max-age directive](https://tools.ietf.org/html/rfc6797#section-6.1.1).
*   Adds `example.com` to the list of hosts to exclude.

`UseHsts` excludes the following loopback hosts:

*   `localhost` : The IPv4 loopback address.
*   `127.0.0.1` : The IPv4 loopback address.
*   `[::1]` : The IPv6 loopback address.

In some backend service scenarios where connection security is handled at the public-facing edge of the network, configuring connection security at each node isn't required. Web apps that are generated from the templates in Visual Studio or from the [dotnet new](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new) command enable [HTTPS redirection](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#require-https) and [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts). For deployments that don't require these scenarios, you can opt-out of HTTPS/HSTS when the app is created from the template.

To opt-out of HTTPS/HSTS:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [.NET CLI](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#tabpanel_1_net-cli)

Uncheck the **Configure for HTTPS** checkbox.

![Image 4: New ASP.NET Core Web Application dialog showing the Configure for HTTPS checkbox unselected.](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl/_static/out-vs2019.png?view=aspnetcore-10.0)

For the Firefox browser, see the next section.

The .NET Core SDK includes an HTTPS development certificate. The certificate is installed as part of the first-run experience. For example, `dotnet --info` produces a variation of the following output:

```
ASP.NET Core
------------
Successfully installed the ASP.NET Core HTTPS Development Certificate.
To trust the certificate run 'dotnet dev-certs https --trust' (Windows and macOS only).
For establishing trust on other platforms refer to the platform specific documentation.
For more information on configuring HTTPS see https://go.microsoft.com/fwlink/?linkid=848054.
```

Installing the .NET Core SDK installs the ASP.NET Core HTTPS development certificate to the local user certificate store. The certificate has been installed, but it's not trusted. To trust the certificate, perform the one-time step to run the `dotnet dev-certs` tool:

```
dotnet dev-certs https --trust
```

The following command provides help on the `dotnet dev-certs` tool:

```
dotnet dev-certs https --help
```

Warning

Do not create a development certificate in an environment that will be redistributed, such as a container image or virtual machine. Doing so can lead to spoofing and elevation of privilege. To help prevent this, set the `DOTNET_GENERATE_ASPNET_CERTIFICATE` environment variable to `false` prior to calling the .NET CLI for the first time. This will skip the automatic generation of the ASP.NET Core development certificate during the CLI's first-run experience.

The Firefox browser uses its own certificate store, and therefore doesn't trust the [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview) or [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) developer certificates.

There are two approaches to trusting the HTTPS certificate with Firefox, create a policy file or configure with the FireFox browser. Configuring with the browser creates the policy file, so the two approaches are equivalent.

Create a policy file (`policies.json`) at:

*   Windows: `%PROGRAMFILES%\Mozilla Firefox\distribution\`
*   MacOS: `Firefox.app/Contents/Resources/distribution`
*   Linux: See [Trust the certificate with Firefox on Linux](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust-ff-linux) in this article.

Add the following JSON to the Firefox policy file:

```
{
  "policies": {
    "Certificates": {
      "ImportEnterpriseRoots": true
    }
  }
}
```

The preceding policy file makes Firefox trust certificates from the trusted certificates in the Windows certificate store. The next section provides an alternative approach to create the preceding policy file by using the Firefox browser.

Set `security.enterprise_roots.enabled` = `true` using the following instructions:

1.   Enter `about:config` in the FireFox browser.
2.   Select **Accept the Risk and Continue** if you accept the risk.
3.   Select **Show All**
4.   Set `security.enterprise_roots.enabled` = `true`
5.   Exit and restart Firefox

For more information, see [Setting Up Certificate Authorities (CAs) in Firefox](https://support.mozilla.org/kb/setting-certificate-authorities-firefox) and the [mozilla/policy-templates/README file](https://github.com/mozilla/policy-templates/blob/master/README.md).

See [this GitHub issue](https://github.com/dotnet/AspNetCore.Docs/issues/6199).

Establishing trust is distribution and browser specific. The following sections provide instructions for some popular distributions and the Chromium browsers (Edge and Chrome) and for Firefox.

The following instructions don't work for some Ubuntu versions, such as 20.04. For more information, see GitHub issue [dotnet/AspNetCore.Docs #23686](https://github.com/dotnet/AspNetCore.Docs/issues/23686).

1.   Install [OpenSSL](https://www.openssl.org/) 1.1.1h or later. See your distribution for instructions on how to update OpenSSL.

2.   Run the following commands:

```
dotnet dev-certs https
sudo -E dotnet dev-certs https -ep /usr/local/share/ca-certificates/aspnet/https.crt --format PEM
sudo update-ca-certificates
```

The preceding commands:

*   Ensure the current user's developer certificate is created.
*   Exports the certificate with elevated permissions needed for the `ca-certificates` folder, using the current user's environment.
*   Removing the `-E` flag exports the root user certificate, generating it if necessary. Each newly generated certificate has a different thumbprint. When running as root, `sudo` and `-E` are not needed.

The path in the preceding command is specific for Ubuntu. For other distributions, select an appropriate path or use the path for the Certificate Authorities (CAs).

See:

*   [This GitHub comment](https://github.com/dotnet/aspnetcore/issues/32361#issuecomment-837111639)
*   [Fedora: Using Shared System Certificates](https://docs.fedoraproject.org/en-US/quick-docs/using-shared-system-certificates/)
*   [Set up a .NET development environment](https://fedoramagazine.org/set-up-a-net-development-environment/) on Fedora.

See [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/32842).

The following instructions don't work for some Linux distributions, such as Ubuntu 20.04. For more information, see GitHub issue [dotnet/AspNetCore.Docs #23686](https://github.com/dotnet/AspNetCore.Docs/issues/23686).

The [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about) generates an HTTPS self-signed development certificate, which by default isn't trusted in Windows. The easiest way to have Windows trust the WSL certificate, is to configure WSL to use the same certificate as Windows:

*   On _**Windows**_, export the developer certificate to a file:

```
dotnet dev-certs https -ep https.pfx -p $CREDENTIAL_PLACEHOLDER$ --trust
```

Where `$CREDENTIAL_PLACEHOLDER$` is a password.

*   In a WSL window, import the exported certificate on the WSL instance:

```
dotnet dev-certs https --clean --import <<path-to-pfx>> --password $CREDENTIAL_PLACEHOLDER$
```

The preceding approach is a one time operation per certificate and per WSL distribution. It's easier than exporting the certificate over and over. If you update or regenerate the certificate on windows, you might need to run the preceding commands again.

This section provides help when the ASP.NET Core HTTPS development certificate has been [installed and trusted](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust), but you still have browser warnings that the certificate is not trusted. The ASP.NET Core HTTPS development certificate is used by [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).

To repair the IIS Express certificate, see [this Stackoverflow](https://stackoverflow.com/a/20048613/502537) issue.

Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app. Certificate trust is cached by browsers.

The preceding commands solve most browser trust issues. If the browser is still not trusting the certificate, follow the platform-specific suggestions that follow.

*   Delete the _C:\Users{USER}\AppData\Roaming\ASP.NET\Https_ folder.
*   Clean the solution. Delete the _bin_ and _obj_ folders.
*   Restart the development tool. For example, Visual Studio or Visual Studio Code.

*   Check the certificates in the certificate store. There should be a `localhost` certificate with the `ASP.NET Core HTTPS development certificate` friendly name both under `Current User > Personal > Certificates` and `Current User > Trusted root certification authorities > Certificates`
*   Remove all the found certificates from both Personal and Trusted root certification authorities. Do **not** remove the IIS Express localhost certificate.
*   Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app.

*   Open KeyChain Access.
*   Select the System keychain.
*   Check for the presence of a localhost certificate.
*   Check that it contains a `+` symbol on the icon to indicate it's trusted for all users.
*   Remove the certificate from the system keychain.
*   Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app.

See [HTTPS Error using IIS Express (dotnet/AspNetCore #16892)](https://github.com/dotnet/AspNetCore/issues/16892) for troubleshooting certificate issues with Visual Studio.

Check that the certificate being configured for trust is the user HTTPS developer certificate that will be used by the Kestrel server.

Check the current user default HTTPS developer Kestrel certificate at the following location:

```
ls -la ~/.dotnet/corefx/cryptography/x509stores/my
```

The HTTPS developer Kestrel certificate file is the SHA1 thumbprint. When the file is deleted via `dotnet dev-certs https --clean`, it's regenerated when needed with a different thumbprint. Check the thumbprint of the exported certificate matches with the following command:

```
openssl x509 -noout -fingerprint -sha1 -inform pem -in /usr/local/share/ca-certificates/aspnet/https.crt
```

If the certificate doesn't match, it could be one of the following:

*   An old certificate.
*   An exported a developer certificate for the root user. For this case, export the certificate.

The root user certificate can be checked at:

```
ls -la /root/.dotnet/corefx/cryptography/x509stores/my
```

To fix problems with the IIS Express certificate, select **Repair** from the Visual Studio installer. For more information, see [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/16892).

In some cases, group policy may prevent self-signed certificates from being trusted. For more information, see [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/21173).

*   [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0)
*   [Host ASP.NET Core on Linux with Nginx: HTTPS configuration](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0#https-configuration)
*   [How to Set Up SSL on IIS](https://learn.microsoft.com/en-us/iis/manage/configuring-security/how-to-set-up-ssl-on-iis)
*   [Configure endpoints for the ASP.NET Core Kestrel web server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/endpoints?view=aspnetcore-10.0)
*   [OWASP HSTS browser support](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet#Browser_Support)

Warning

API projects
------------

Do **not** use [RequireHttpsAttribute](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.mvc.requirehttpsattribute) on Web APIs that receive sensitive information. `RequireHttpsAttribute` uses HTTP status codes to redirect browsers from HTTP to HTTPS. API clients may not understand or obey redirects from HTTP to HTTPS. Such clients may send information over HTTP. Web APIs should either:

*   Not listen on HTTP.
*   Close the connection with status code 400 (Bad Request) and not serve the request.

To disable HTTP redirection in an API, set the `ASPNETCORE_URLS` environment variable or use the `--urls` command line flag. For more information, see [ASP.NET Core runtime environments](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0) and [8 ways to set the URLs for an ASP.NET Core app](https://andrewlock.net/8-ways-to-set-the-urls-for-an-aspnetcore-app/) by Andrew Lock.

HSTS and API projects
---------------------

The default API projects don't include [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#hsts) because [HSTS](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) is generally a browser only instruction. Other callers, such as phone or desktop apps, do **not** obey the instruction. Even within browsers, a single authenticated call to an API over HTTP has risks on insecure networks. The secure approach is to configure API projects to only listen to and respond over HTTPS.

Requests to an endpoint using HTTP that are redirected to HTTPS by [UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection) fail with `ERR_INVALID_REDIRECT` on the CORS preflight request.

API projects can reject HTTP requests rather than use `UseHttpsRedirection` to redirect requests to HTTPS.

We recommend that production ASP.NET Core web apps use:

*   HTTPS Redirection Middleware ([UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection)) to redirect HTTP requests to HTTPS.
*   HSTS Middleware ([UseHsts](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts)) to send HTTP Strict Transport Security Protocol (HSTS) headers to clients.

Note

Apps deployed in a reverse proxy configuration allow the proxy to handle connection security (HTTPS). If the proxy also handles HTTPS redirection, there's no need to use HTTPS Redirection Middleware. If the proxy server also handles writing HSTS headers (for example, [native HSTS support in IIS 10.0 (1709) or later](https://learn.microsoft.com/en-us/iis/get-started/whats-new-in-iis-10-version-1709/iis-10-version-1709-hsts#iis-100-version-1709-native-hsts-support)), HSTS Middleware isn't required by the app. For more information, see [Opt-out of HTTPS/HSTS on project creation](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#opt-out-of-httpshsts-on-project-creation).

The following code calls [UseHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpspolicybuilderextensions.usehttpsredirection) in the `Program.cs` file:

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

The preceding highlighted code:

*   Uses the default [HttpsRedirectionOptions.RedirectStatusCode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.redirectstatuscode#microsoft-aspnetcore-httpspolicy-httpsredirectionoptions-redirectstatuscode) ([Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect)).
*   Uses the default [HttpsRedirectionOptions.HttpsPort](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.httpsport#microsoft-aspnetcore-httpspolicy-httpsredirectionoptions-httpsport) (null) unless overridden by the `ASPNETCORE_HTTPS_PORT` environment variable or [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature).

We recommend using temporary redirects rather than permanent redirects. Link caching can cause unstable behavior in development environments. If you prefer to send a permanent redirect status code when the app is in a non-`Development` environment, see the [Configure permanent redirects in production](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#configure-permanent-redirects-in-production) section. We recommend using [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts) to signal to clients that only secure resource requests should be sent to the app (only in production).

A port must be available for the middleware to redirect an insecure request to HTTPS. If no port is available:

*   Redirection to HTTPS doesn't occur.
*   The middleware logs the warning "Failed to determine the https port for redirect."

Specify the HTTPS port using any of the following approaches:

*   Set [HttpsRedirectionOptions.HttpsPort](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#options).

*   Set the `https_port`[host setting](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0#https_port):

    *   In host configuration.

    *   By setting the `ASPNETCORE_HTTPS_PORT` environment variable.

    *   By adding a top-level entry in `appsettings.json`:

```
{
  "https_port": 443,
  "Logging": {
    "LogLevel": {
      "Default": "Information",
      "Microsoft.AspNetCore": "Warning"
    }
  },
  "AllowedHosts": "*"
}
```

*   Indicate a port with the secure scheme using the [ASPNETCORE_URLS environment variable](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/host/generic-host?view=aspnetcore-10.0#urls). The environment variable configures the server. The middleware indirectly discovers the HTTPS port via [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature). This approach doesn't work in reverse proxy deployments.

*   The ASP.NET Core web templates set an HTTPS URL in `Properties/launchsettings.json` for both Kestrel and IIS Express. `launchsettings.json` is only used on the local machine.

*   Configure an HTTPS URL endpoint for a public-facing edge deployment of [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) server or [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0) server. Only **one HTTPS port** is used by the app. The middleware discovers the port via [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature).

Note

When an app is run in a reverse proxy configuration, [IServerAddressesFeature](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.hosting.server.features.iserveraddressesfeature) isn't available. Set the port using one of the other approaches described in this section.

When [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) or [HTTP.sys](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0) is used as a public-facing edge server, Kestrel or HTTP.sys must be configured to listen on both:

*   The secure port where the client is redirected (typically, 443 in production and 5001 in development).
*   The insecure port (typically, 80 in production and 5000 in development).

The insecure port must be accessible by the client in order for the app to receive an insecure request and redirect the client to the secure port.

For more information, see [Kestrel endpoint configuration](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0#endpoint-configuration) or [HTTP.sys web server implementation in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0).

Any firewall between the client and server must also have communication ports open for traffic.

If requests are forwarded in a reverse proxy configuration, use [Forwarded Headers Middleware](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0) before calling HTTPS Redirection Middleware. Forwarded Headers Middleware updates the `Request.Scheme`, using the `X-Forwarded-Proto` header. The middleware permits redirect URIs and other security policies to work correctly. When Forwarded Headers Middleware isn't used, the backend app might not receive the correct scheme and end up in a redirect loop. A common end user error message is that too many redirects have occurred.

When deploying to Azure App Service, follow the guidance in [Tutorial: Bind an existing custom SSL certificate to Azure Web Apps](https://learn.microsoft.com/en-us/azure/app-service/app-service-web-tutorial-custom-ssl).

The following highlighted code calls [AddHttpsRedirection](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.httpsredirectionservicesextensions.addhttpsredirection) to configure middleware options:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

builder.Services.AddHsts(options =>
{
    options.Preload = true;
    options.IncludeSubDomains = true;
    options.MaxAge = TimeSpan.FromDays(60);
    options.ExcludedHosts.Add("example.com");
    options.ExcludedHosts.Add("www.example.com");
});

builder.Services.AddHttpsRedirection(options =>
{
    options.RedirectStatusCode = Status307TemporaryRedirect;
    options.HttpsPort = 5001;
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

Calling `AddHttpsRedirection` is only necessary to change the values of `HttpsPort` or `RedirectStatusCode`.

The preceding highlighted code:

*   Sets [HttpsRedirectionOptions.RedirectStatusCode](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.httpsredirectionoptions.redirectstatuscode) to [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect), which is the default value. Use the fields of the [StatusCodes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes) class for assignments to `RedirectStatusCode`.
*   Sets the HTTPS port to 5001.

The middleware defaults to sending a [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect) with all redirects. If you prefer to send a permanent redirect status code when the app is in a non-`Development` environment, wrap the middleware options configuration in a conditional check for a non-`Development` environment.

When configuring services in `Program.cs`:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

if (!builder.Environment.IsDevelopment())
{
    builder.Services.AddHttpsRedirection(options =>
    {
        options.RedirectStatusCode = Status308PermanentRedirect;
        options.HttpsPort = 443;
    });
}

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");

    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

An alternative to using HTTPS Redirection Middleware (`UseHttpsRedirection`) is to use URL Rewriting Middleware (`AddRedirectToHttps`). `AddRedirectToHttps` can also set the status code and port when the redirect is executed. For more information, see [URL Rewriting Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting?view=aspnetcore-10.0).

When redirecting to HTTPS without the requirement for additional redirect rules, we recommend using HTTPS Redirection Middleware (`UseHttpsRedirection`) described in this article.

Per [OWASP](https://www.owasp.org/index.php/About_The_Open_Web_Application_Security_Project), [HTTP Strict Transport Security (HSTS)](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Strict_Transport_Security_Cheat_Sheet.html) is an opt-in security enhancement that's specified by a web app through the use of a response header. When a [browser that supports HSTS](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html#browser-support) receives this header:

*   The browser stores configuration for the domain that prevents sending any communication over HTTP. The browser forces all communication over HTTPS.
*   The browser prevents the user from using untrusted or invalid certificates. The browser disables prompts that allow a user to temporarily trust such a certificate.

Because [HSTS](https://developer.mozilla.org/docs/Web/HTTP/Headers/Strict-Transport-Security) is enforced by the client, it has some limitations:

*   The client must support HSTS.
*   HSTS requires at least one successful HTTPS request to establish the HSTS policy.
*   The application must check every HTTP request and redirect or reject the HTTP request.

ASP.NET Core implements HSTS with the [UseHsts](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.hstsbuilderextensions.usehsts) extension method. The following code calls `UseHsts` when the app isn't in [development mode](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/environments?view=aspnetcore-10.0):

```
var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

`UseHsts` isn't recommended in development because the HSTS settings are highly cacheable by browsers. By default, `UseHsts` excludes the local loopback address.

For production environments that are implementing HTTPS for the first time, set the initial [HstsOptions.MaxAge](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.httpspolicy.hstsoptions.maxage) to a small value using one of the [TimeSpan](https://learn.microsoft.com/en-us/dotnet/api/system.timespan) methods. Set the value from hours to no more than a single day in case you need to revert the HTTPS infrastructure to HTTP. After you're confident in the sustainability of the HTTPS configuration, increase the HSTS `max-age` value; a commonly used value is one year.

The following highlighted code:

```
using static Microsoft.AspNetCore.Http.StatusCodes;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddRazorPages();

builder.Services.AddHsts(options =>
{
    options.Preload = true;
    options.IncludeSubDomains = true;
    options.MaxAge = TimeSpan.FromDays(60);
    options.ExcludedHosts.Add("example.com");
    options.ExcludedHosts.Add("www.example.com");
});

builder.Services.AddHttpsRedirection(options =>
{
    options.RedirectStatusCode = Status307TemporaryRedirect;
    options.HttpsPort = 5001;
});

var app = builder.Build();

if (!app.Environment.IsDevelopment())
{
    app.UseExceptionHandler("/Error");
    app.UseHsts();
}

app.UseHttpsRedirection();
app.UseStaticFiles();

app.UseRouting();

app.UseAuthorization();

app.MapRazorPages();

app.Run();
```

*   Sets the preload parameter of the `Strict-Transport-Security` header. Preload isn't part of the [RFC HSTS specification](https://tools.ietf.org/html/rfc6797), but is supported by web browsers to preload HSTS sites on fresh install. For more information, see [https://hstspreload.org/](https://hstspreload.org/).
*   Enables [includeSubDomain](https://tools.ietf.org/html/rfc6797#section-6.1.2), which applies the HSTS policy to Host subdomains.
*   Explicitly sets the `max-age` parameter of the `Strict-Transport-Security` header to 60 days. If not set, defaults to 30 days. For more information, see the [max-age directive](https://tools.ietf.org/html/rfc6797#section-6.1.1).
*   Adds `example.com` to the list of hosts to exclude.

`UseHsts` excludes the following loopback hosts:

*   `localhost` : The IPv4 loopback address.
*   `127.0.0.1` : The IPv4 loopback address.
*   `[::1]` : The IPv6 loopback address.

In some backend service scenarios where connection security is handled at the public-facing edge of the network, configuring connection security at each node isn't required. Web apps that are generated from the templates in Visual Studio or from the [dotnet new](https://learn.microsoft.com/en-us/dotnet/core/tools/dotnet-new) command enable [HTTPS redirection](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#require-https) and [HSTS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#http-strict-transport-security-protocol-hsts). For deployments that don't require these scenarios, you can opt-out of HTTPS/HSTS when the app is created from the template.

To opt-out of HTTPS/HSTS:

*   [Visual Studio](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#tabpanel_1_visual-studio)
*   [.NET CLI](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#tabpanel_1_net-cli)

Uncheck the **Configure for HTTPS** checkbox.

![Image 5: New ASP.NET Core Web Application dialog showing the Configure for HTTPS checkbox unselected.](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl/_static/out-vs2019.png?view=aspnetcore-10.0)

For the Firefox browser, see the next section.

The .NET SDK includes an HTTPS development certificate. The certificate is installed as part of the first-run experience. For example, `dotnet --info` produces a variation of the following output:

```
ASP.NET Core
------------
Successfully installed the ASP.NET Core HTTPS Development Certificate.
To trust the certificate run 'dotnet dev-certs https --trust' (Windows and macOS only).
For establishing trust on other platforms refer to the platform specific documentation.
For more information on configuring HTTPS see https://go.microsoft.com/fwlink/?linkid=848054.
```

Installing the .NET SDK installs the ASP.NET Core HTTPS development certificate to the local user certificate store. The certificate has been installed, but it's not trusted. To trust the certificate, perform the one-time step to run the `dotnet dev-certs` tool:

```
dotnet dev-certs https --trust
```

The following command provides help on the `dotnet dev-certs` tool:

```
dotnet dev-certs https --help
```

Warning

Do not create a development certificate in an environment that will be redistributed, such as a container image or virtual machine. Doing so can lead to spoofing and elevation of privilege. To help prevent this, set the `DOTNET_GENERATE_ASPNET_CERTIFICATE` environment variable to `false` prior to calling the .NET CLI for the first time. This will skip the automatic generation of the ASP.NET Core development certificate during the CLI's first-run experience.

The Firefox browser uses its own certificate store, and therefore doesn't trust the [IIS Express](https://learn.microsoft.com/en-us/iis/extensions/introduction-to-iis-express/iis-express-overview) or [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0) developer certificates.

There are two approaches to trusting the HTTPS certificate with Firefox, create a policy file or configure with the FireFox browser. Configuring with the browser creates the policy file, so the two approaches are equivalent.

Create a policy file (`policies.json`) at:

*   Windows: `%PROGRAMFILES%\Mozilla Firefox\distribution\`
*   MacOS: `Firefox.app/Contents/Resources/distribution`
*   Linux: See [Trust the certificate with Firefox on Linux](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?tabs=visual-studio%2Clinux-ubuntu%2Clinux-sles#trust-the-certificate-with-firefox-on-linux) in this article.

Add the following JSON to the Firefox policy file:

```
{
  "policies": {
    "Certificates": {
      "ImportEnterpriseRoots": true
    }
  }
}
```

The preceding policy file makes Firefox trust certificates from the trusted certificates in the Windows certificate store. The next section provides an alternative approach to create the preceding policy file by using the Firefox browser.

Set `security.enterprise_roots.enabled` = `true` using the following instructions:

1.   Enter `about:config` in the FireFox browser.
2.   Select **Accept the Risk and Continue** if you accept the risk.
3.   Select **Show All**
4.   Set `security.enterprise_roots.enabled` = `true`
5.   Exit and restart Firefox

For more information, see [Setting Up Certificate Authorities (CAs) in Firefox](https://support.mozilla.org/kb/setting-certificate-authorities-firefox) and the [mozilla/policy-templates/README file](https://github.com/mozilla/policy-templates/blob/master/README.md).

See [this GitHub issue](https://github.com/dotnet/AspNetCore.Docs/issues/6199).

Establishing trust is distribution and browser specific. The following sections provide instructions for some popular distributions and the Chromium browsers (Edge and Chrome) and for Firefox.

[linux-dev-certs](https://github.com/tmds/linux-dev-certs) is an open-source, community-supported, .NET global tool that provides a convenient way to create and trust a developer certificate on Linux. The tool is not maintained or supported by Microsoft.

The following commands install the tool and create a trusted developer certificate:

```
dotnet tool update -g linux-dev-certs
dotnet linux-dev-certs install
```

For more information or to report issues, see the [linux-dev-certs GitHub repository](https://github.com/tmds/linux-dev-certs).

The following instructions don't work for some Ubuntu versions, such as 20.04. For more information, see GitHub issue [dotnet/AspNetCore.Docs #23686](https://github.com/dotnet/AspNetCore.Docs/issues/23686).

1.   Install [OpenSSL](https://www.openssl.org/) 1.1.1h or later. See your distribution for instructions on how to update OpenSSL.

2.   Run the following commands:

```
dotnet dev-certs https
sudo -E dotnet dev-certs https -ep /usr/local/share/ca-certificates/aspnet/https.crt --format PEM
sudo update-ca-certificates
```

The preceding commands:

*   Ensure the current user's developer certificate is created.
*   Exports the certificate with elevated permissions needed for the `ca-certificates` folder, using the current user's environment.
*   Removing the `-E` flag exports the root user certificate, generating it if necessary. Each newly generated certificate has a different thumbprint. When running as root, `sudo` and `-E` are not needed.

The path in the preceding command is specific for Ubuntu. For other distributions, select an appropriate path or use the path for the Certificate Authorities (CAs).

See:

*   [This GitHub comment](https://github.com/dotnet/aspnetcore/issues/32361#issuecomment-837111639)
*   [Fedora: Using Shared System Certificates](https://docs.fedoraproject.org/en-US/quick-docs/using-shared-system-certificates/)
*   [Set up a .NET development environment](https://fedoramagazine.org/set-up-a-net-development-environment/) on Fedora.

See [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/32842).

The following instructions don't work for some Linux distributions, such as Ubuntu 20.04. For more information, see GitHub issue [dotnet/AspNetCore.Docs #23686](https://github.com/dotnet/AspNetCore.Docs/issues/23686).

The [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/en-us/windows/wsl/about) generates an HTTPS self-signed development certificate, which by default isn't trusted in Windows. The easiest way to have Windows trust the WSL certificate, is to configure WSL to use the same certificate as Windows:

*   On _**Windows**_, export the developer certificate to a file:

```
dotnet dev-certs https -ep https.pfx -p $CREDENTIAL_PLACEHOLDER$ --trust
```

Where `$CREDENTIAL_PLACEHOLDER$` is a password.

*   In a WSL window, import the exported certificate on the WSL instance:

```
dotnet dev-certs https --clean --import <<path-to-pfx>> --password $CREDENTIAL_PLACEHOLDER$
```

The preceding approach is a one time operation per certificate and per WSL distribution. It's easier than exporting the certificate over and over. If you update or regenerate the certificate on windows, you might need to run the preceding commands again.

This section provides help when the ASP.NET Core HTTPS development certificate has been [installed and trusted](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#trust), but you still have browser warnings that the certificate is not trusted. The ASP.NET Core HTTPS development certificate is used by [Kestrel](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel?view=aspnetcore-10.0).

To repair the IIS Express certificate, see [this Stackoverflow](https://stackoverflow.com/a/20048613/502537) issue.

Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app. Certificate trust is cached by browsers.

The preceding commands solve most browser trust issues. If the browser is still not trusting the certificate, follow the platform-specific suggestions that follow.

*   Delete the _C:\Users{USER}\AppData\Roaming\ASP.NET\Https_ folder.
*   Clean the solution. Delete the _bin_ and _obj_ folders.
*   Restart the development tool. For example, Visual Studio or Visual Studio Code.

*   Check the certificates in the certificate store. There should be a `localhost` certificate with the `ASP.NET Core HTTPS development certificate` friendly name both under `Current User > Personal > Certificates` and `Current User > Trusted root certification authorities > Certificates`
*   Remove all the found certificates from both Personal and Trusted root certification authorities. Do **not** remove the IIS Express localhost certificate.
*   Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app.

*   Open KeyChain Access.
*   Select the System keychain.
*   Check for the presence of a localhost certificate.
*   Check that it contains a `+` symbol on the icon to indicate it's trusted for all users.
*   Remove the certificate from the system keychain.
*   Run the following commands:

```
dotnet dev-certs https --clean
dotnet dev-certs https --trust
```

Close any browser instances open. Open a new browser window to app.

See [HTTPS Error using IIS Express (dotnet/AspNetCore #16892)](https://github.com/dotnet/AspNetCore/issues/16892) for troubleshooting certificate issues with Visual Studio.

Check that the certificate being configured for trust is the user HTTPS developer certificate that will be used by the Kestrel server.

Check the current user default HTTPS developer Kestrel certificate at the following location:

```
ls -la ~/.dotnet/corefx/cryptography/x509stores/my
```

The HTTPS developer Kestrel certificate file is the SHA1 thumbprint. When the file is deleted via `dotnet dev-certs https --clean`, it's regenerated when needed with a different thumbprint. Check the thumbprint of the exported certificate matches with the following command:

```
openssl x509 -noout -fingerprint -sha1 -inform pem -in /usr/local/share/ca-certificates/aspnet/https.crt
```

If the certificate doesn't match, it could be one of the following:

*   An old certificate.
*   An exported a developer certificate for the root user. For this case, export the certificate.

The root user certificate can be checked at:

```
ls -la /root/.dotnet/corefx/cryptography/x509stores/my
```

To fix problems with the IIS Express certificate, select **Repair** from the Visual Studio installer. For more information, see [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/16892).

In some cases, group policy may prevent self-signed certificates from being trusted. For more information, see [this GitHub issue](https://github.com/dotnet/aspnetcore/issues/21173).

*   [Configure ASP.NET Core to work with proxy servers and load balancers](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/proxy-load-balancer?view=aspnetcore-10.0)
*   [Host ASP.NET Core on Linux with Nginx: HTTPS configuration](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/linux-nginx?view=aspnetcore-10.0#https-configuration)
*   [How to Set Up SSL on IIS](https://learn.microsoft.com/en-us/iis/manage/configuring-security/how-to-set-up-ssl-on-iis)
*   [Configure endpoints for the ASP.NET Core Kestrel web server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/kestrel/endpoints?view=aspnetcore-10.0)
*   [OWASP HSTS browser support](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet#Browser_Support)
