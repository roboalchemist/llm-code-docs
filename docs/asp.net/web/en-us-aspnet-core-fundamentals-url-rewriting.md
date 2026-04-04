# Source: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting?view=aspnetcore-10.0

Title: URL Rewriting Middleware in ASP.NET Core

URL Source: https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting?view=aspnetcore-10.0

Markdown Content:
By [Kirk Larkin](https://twitter.com/serpent5) and [Rick Anderson](https://twitter.com/RickAndMSFT)

This article introduces URL rewriting with instructions on how to use URL Rewriting Middleware in ASP.NET Core apps.

URL rewriting is the act of modifying request URLs based on one or more predefined rules. URL rewriting creates an abstraction between resource locations and their addresses so that the locations and addresses aren't tightly linked. URL rewriting is valuable in several scenarios to:

*   Move or replace server resources temporarily or permanently and maintain stable locators for those resources.
*   Split request processing across different apps or across areas of one app.
*   Remove, add, or reorganize URL segments on incoming requests.
*   Optimize public URLs for Search Engine Optimization (SEO).
*   Permit the use of friendly public URLs to help visitors predict the content returned by requesting a resource.
*   Redirect insecure requests to secure endpoints.
*   Prevent hotlinking, where an external site uses a hosted static asset on another site by linking the asset into its own content.

_**URL rewriting can reduce the performance of an app**_. Limit the number and complexity of rules.

The difference in wording between _URL redirect_ and _URL rewrite_ is subtle but has important implications for providing resources to clients. ASP.NET Core's URL Rewriting Middleware is capable of meeting the need for both.

A _URL redirect_ involves a client-side operation, where the client is instructed to access a resource at a different address than the client originally requested. This requires a round trip to the server. The redirect URL returned to the client appears in the browser's address bar when the client makes a new request for the resource.

If `/resource` is _redirected_ to `/different-resource`, the server responds that the client should obtain the resource at `/different-resource` with a status code indicating that the redirect is either temporary or permanent.

![Image 1: A WebAPI service endpoint has been temporarily changed from version 1 (v1) to version 2 (v2) on the server. A client makes a request to the service at the version 1 path /v1/api. The server sends back a 302 (Found) response with the new, temporary path for the service at version 2 /v2/api. The client makes a second request to the service at the redirect URL. The server responds with a 200 (OK) status code.](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/url_redirect.png?view=aspnetcore-10.0)

When redirecting requests to a different URL, indicate whether the redirect is permanent or temporary by specifying the status code with the response:

*   The [`301 - Moved Permanently`](https://developer.mozilla.org/docs/Web/HTTP/Status/301) status code is used where the resource has a new, permanent URL and that all future requests for the resource should use the new URL. _The client may cache and reuse the response when a 301 status code is received._

*   The [`302 - Found`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/302) status code is used where the redirection is temporary or generally subject to change. The 302 status code indicates to the client not to store the URL and use it in the future.

For more information on status codes, see [RFC 9110: Status Code Definitions](https://www.rfc-editor.org/rfc/rfc9110#name-status-codes).

A _URL rewrite_ is a server-side operation that provides a resource from a different resource address than the client requested. Rewriting a URL doesn't require a round trip to the server. The rewritten URL isn't returned to the client and doesn't appear in the browser's address bar.

If `/resource` is _rewritten_ to `/different-resource`, the server _internally_ fetches and returns the resource at `/different-resource`.

Although the client might be able to retrieve the resource at the rewritten URL, the client isn't informed that the resource exists at the rewritten URL when it makes its request and receives the response.

![Image 2: A WebAPI service endpoint has been changed from version 1 (v1) to version 2 (v2) on the server. A client makes a request to the service at the version 1 path /v1/api. The request URL is rewritten to access the service at the version 2 path /v2/api. The service responds to the client with a 200 (OK) status code.](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/url_rewrite.png?view=aspnetcore-10.0)

Explore the features of the URL Rewriting Middleware with the [sample app](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/url-rewriting/samples/). The app applies redirect and rewrite rules and shows the redirected or rewritten URL for several scenarios.

Use URL Rewriting Middleware when the following approaches aren't satisfactory:

*   [URL Rewrite module with IIS on Windows Server](https://www.iis.net/downloads/microsoft/url-rewrite)
*   [Apache mod_rewrite module on Apache Server](https://httpd.apache.org/docs/2.4/rewrite/)
*   [URL rewriting on Nginx](https://www.nginx.com/blog/creating-nginx-rewrite-rules/)

Use the URL rewriting middleware when the app is hosted on [HTTP.sys server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0).

The main reasons to use the server-based URL rewriting technologies in IIS, Apache, and Nginx are:

*   The middleware doesn't support the full features of these modules.

Some of the features of the server modules don't work with ASP.NET Core projects, such as the `IsFile` and `IsDirectory` constraints of the IIS Rewrite module. In these scenarios, use the middleware instead.

*   The performance of the middleware probably doesn't match that of the modules.

Benchmarking is the only way to know with certainty which approach degrades performance the most or if degraded performance is negligible.

Establish URL rewrite and redirect rules by creating an instance of the [RewriteOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptions) class with extension methods for each of the rewrite rules. Chain multiple rules _**in the order that they should be processed**_. The `RewriteOptions` are passed into the URL Rewriting Middleware as it's added to the request pipeline with [UseRewriter](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.rewritebuilderextensions.userewriter):

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)
        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

In the preceding code, [`MethodRules`](https://github.com/dotnet/AspNetCore.Docs/blob/main/aspnetcore/fundamentals/url-rewriting/samples/6.x/SampleApp/RewriteRules.cs) is a user defined class. See [`RewriteRules.cs`](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting?view=aspnetcore-10.0#rrr) in this article for more information.

Three options permit the app to redirect non-`www` requests to `www`:

*   [AddRedirectToWwwPermanent](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttowwwpermanent): Permanently redirect the request to the `www` subdomain if the request is non-`www`. Redirects with a [Status308PermanentRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status308permanentredirect#microsoft-aspnetcore-http-statuscodes-status308permanentredirect) status code.

*   [AddRedirectToWww](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttowww): Redirect the request to the `www` subdomain if the incoming request is non-`www`. Redirects with a [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect) status code. An overload permits providing the status code for the response. Use a field of the [StatusCodes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes) class for a status code assignment.

Use [AddRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirect) to redirect requests. The first parameter contains the [.NET regular expression](https://learn.microsoft.com/en-us/dotnet/standard/base-types/regular-expressions) (Regex) for matching on the path of the incoming URL. The second parameter is the replacement string. The third parameter, if present, specifies the status code. If the status code isn't specified, the status code defaults to [302 - Found](https://developer.mozilla.org/docs/Web/HTTP/Status/302), which indicates that the resource is temporarily moved or replaced.

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)
        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

In a browser with developer tools enabled, make a request to the sample app with the path `/redirect-rule/1234/5678`. The regular expression matches the request path on `redirect-rule/(.*)`, and the path is replaced with `/redirected/1234/5678`. The redirect URL is sent back to the client with a _302 - Found_ status code. The browser makes a new request at the redirect URL, which appears in the browser's address bar. Since no rules in the sample app match on the redirect URL:

*   The second request receives a _200 - OK_ response from the app.
*   The body of the response shows the redirect URL.

A round trip is made to the server when a URL is _redirected_.

Warning

Be cautious when establishing redirect rules. Redirect rules are evaluated on every request to the app, including after a redirect. It's easy to accidentally create a loop of _**infinite**_ redirects.

The part of the expression contained within parentheses is called a [capture group](https://learn.microsoft.com/en-us/dotnet/standard/base-types/grouping-constructs-in-regular-expressions). The dot (`.`) of the expression means _match any character_. The asterisk (`*`) indicates _match the preceding character zero or more times_. Therefore, the last two path segments of the URL, `1234/5678`, are captured by capture group `(.*)`. Any value provided in the request URL after `redirect-rule/` is captured by this single capture group.

In the replacement string, captured groups are injected into the string with the dollar sign (`$`) followed by the sequence number of the capture. The first capture group value is obtained with `$1`, the second with `$2`, and they continue in sequence for the capture groups in the regular expression. There's only one captured group in the redirect rule regular expression in `redirect-rule/(.*)`, so there's only one injected group in the replacement string, which is `$1`. When the rule is applied, the URL becomes `/redirected/1234/5678`.

Try `/redirect-rule/1234/5678` with the browser tools on the network tab.

Use [AddRedirectToHttps](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttohttps) to redirect HTTP requests to the same host and path using the HTTPS protocol. If the status code isn't supplied, the middleware defaults to _302 - Found_. If the port isn't supplied:

*   The middleware defaults to `null`.
*   The scheme changes to `https` (HTTPS protocol), and the client accesses the resource on port 443.

The following example shows how to set the status code to `301 - Moved Permanently` and change the port to the HTTPS port used by Kestrel on localhost. In production, the HTTPS port is set to null:

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

int? localhostHTTPSport = null;
if (app.Environment.IsDevelopment())
{
    localhostHTTPSport = Int32.Parse(Environment.GetEnvironmentVariable(
                   "ASPNETCORE_URLS")!.Split(new Char[] { ':', ';' })[2]);
}

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        // localhostHTTPport not needed for production, used only with localhost.
        .AddRedirectToHttps(301, localhostHTTPSport)
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)
        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

Use [AddRedirectToHttpsPermanent](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttohttpspermanent) to redirect insecure requests to the same host and path with secure HTTPS protocol on port 443. The middleware sets the status code to `301 - Moved Permanently`.

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        .AddRedirectToHttpsPermanent()
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)
        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

Note

When redirecting to a secure endpoint without the requirement for additional redirect rules, we recommend using HTTPS Redirection Middleware. For more information, see [Enforce HTTPS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#require-https).

The sample app demonstrates how to use `AddRedirectToHttps` or `AddRedirectToHttpsPermanent`. Make an insecure HTTP request to the app at `http://redirect6.azurewebsites.net/iis-rules-rewrite/xyz`. When testing HTTP to HTTPS redirection with localhost:

*   Use the HTTP URL, which has a different port than the HTTPS URL. The HTTP URL is in the `Properties/launchSettings.json` file.
*   Removing the `s` from `https://localhost/{port}` fails because localhost doesn't respond on HTTP to the HTTPS port.

The following image shows the F12 browser tools image of a request to `http://redirect6.azurewebsites.net/iis-rules-rewrite/xyz` using the preceding code:

![Image 3: Browser window with developer tools tracking the requests and responses: Add redirect to HTTPS](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect_to_https6.png?view=aspnetcore-10.0)

Use [AddRewrite](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addrewrite) to create a rule for rewriting URLs. The first parameter contains the regular expression for matching on the incoming URL path. The second parameter is the replacement string. The third parameter, `skipRemainingRules: {true|false}`, indicates to the middleware whether or not to skip additional rewrite rules if the current rule is applied.

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        .AddRedirectToHttpsPermanent()
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)
        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

Try the request to `https://redirect6.azurewebsites.net/rewrite-rule/1234/5678`

The caret (`^`) at the beginning of the expression means that matching starts at the beginning of the URL path.

In the earlier example with the redirect rule, `redirect-rule/(.*)`, there's no caret (`^`) at the start of the regular expression. Therefore, any characters may precede `redirect-rule/` in the path for a successful match.

| Path | Match |
| --- | --- |
| `/redirect-rule/1234/5678` | Yes |
| `/my-cool-redirect-rule/1234/5678` | Yes |
| `/anotherredirect-rule/1234/5678` | Yes |

The rewrite rule, `^rewrite-rule/(\d+)/(\d+)`, only matches paths if they start with `rewrite-rule/`. In the following table, note the difference in matching.

| Path | Match |
| --- | --- |
| `/rewrite-rule/1234/5678` | Yes |
| `/my-cool-rewrite-rule/1234/5678` | No |
| `/anotherrewrite-rule/1234/5678` | No |

Following the `^rewrite-rule/` portion of the expression, there are two capture groups, `(\d+)/(\d+)`. The `\d` signifies _match a digit (number)_. The plus sign (`+`) means _match one or more of the preceding character_. Therefore, the URL must contain a number followed by a forward-slash followed by another number. These capture groups are injected into the rewritten URL as `$1` and `$2`. The rewrite rule replacement string places the captured groups into the query string. The requested path `/rewrite-rule/1234/5678` is rewritten to return the resource at `/rewritten?var1=1234&var2=5678`. If a query string is present on the original request, it's preserved when the URL is rewritten.

There's no round trip to the server to return the resource. If the resource exists, it's fetched and returned to the client with a _200 - OK_ status code. Because the client isn't redirected, the URL in the browser's address bar doesn't change. Clients can't detect that a URL rewrite operation occurred on the server.

For the fastest response:

*   Order rewrite rules from the most frequently matched rule to the least frequently matched rule.
*   Use `skipRemainingRules: true` whenever possible because matching rules is computationally expensive and increases app response time. Skip the processing of the remaining rules when a match occurs and no additional rule processing is required.

Warning

A malicious user can provide expensive-to-process input to `RegularExpressions` causing a [Denial-of-Service attack](https://www.cisa.gov/news-events/news/understanding-denial-service-attacks). ASP.NET Core framework APIs that use `RegularExpressions` institute a timeout. For example, the Regex timeout (`_regexTimeout`) of the [`RedirectRule` class](https://github.com/dotnet/aspnetcore/blob/main/src/Middleware/Rewrite/src/RedirectRule.cs) and [`RewriteRule` class](https://github.com/dotnet/aspnetcore/blob/main/src/Middleware/Rewrite/src/RewriteRule.cs) classes both pass in a one second timeout.

Apply Apache mod_rewrite rules with [AddApacheModRewrite](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.apachemodrewriteoptionsextensions.addapachemodrewrite). Make sure that the rules file is deployed with the app. For more information and examples of mod_rewrite rules, see [Apache mod_rewrite](https://httpd.apache.org/docs/2.4/rewrite/).

A [StreamReader](https://learn.microsoft.com/en-us/dotnet/api/system.io.streamreader) is used to read the rules from the _ApacheModRewrite.txt_ rules file:

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        .AddRedirectToHttpsPermanent()
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)
        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

The sample app redirects requests from `/apache-mod-rules-redirect/(.\*)` to `/redirected?id=$1`. The response status code is _302 - Found_.

```
# Rewrite path with additional sub directory
RewriteRule ^/apache-mod-rules-redirect/(.*) /redirected?id=$1 [L,R=302]
```

Try the request to `https://redirect6.azurewebsites.net/apache-mod-rules-redirect/1234`

The [Apache middleware](https://github.com/dotnet/aspnetcore/blob/main/src/Middleware/Rewrite/src/ApacheModRewrite/ServerVariables.cs) supports the following Apache mod_rewrite server variables:

*   CONN_REMOTE_ADDR
*   HTTP_ACCEPT
*   HTTP_CONNECTION
*   HTTP_COOKIE
*   HTTP_FORWARDED
*   HTTP_HOST
*   HTTP_REFERER
*   HTTP_USER_AGENT
*   HTTPS
*   IPV6
*   QUERY_STRING
*   REMOTE_ADDR
*   REMOTE_PORT
*   REQUEST_FILENAME
*   REQUEST_METHOD
*   REQUEST_SCHEME
*   REQUEST_URI
*   SCRIPT_FILENAME
*   SERVER_ADDR
*   SERVER_PORT
*   SERVER_PROTOCOL
*   TIME
*   TIME_DAY
*   TIME_HOUR
*   TIME_MIN
*   TIME_MON
*   TIME_SEC
*   TIME_WDAY
*   TIME_YEAR

To use the same rule set that applies to the IIS URL Rewrite Module, use [AddIISUrlRewrite](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.iisurlrewriteoptionsextensions.addiisurlrewrite). Make sure that the rules file is deployed with the app. Don't direct the middleware to use the app's _web.config_ file when running on Windows Server IIS. With IIS, these rules should be stored outside of the app's _web.config_ file in order to avoid conflicts with the IIS Rewrite module. For more information and examples of IIS URL Rewrite Module rules, see [Using Url Rewrite Module 2.0](https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/using-url-rewrite-module-20) and [URL Rewrite Module Configuration Reference](https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/url-rewrite-module-configuration-reference).

A [StreamReader](https://learn.microsoft.com/en-us/dotnet/api/system.io.streamreader) is used to read the rules from the `IISUrlRewrite.xml` rules file:

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        .AddRedirectToHttpsPermanent()
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)
        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

The sample app rewrites requests from `/iis-rules-rewrite/(.*)` to `/rewritten?id=$1`. The response is sent to the client with a _200 - OK_ status code.

```
<rewrite>
  <rules>
    <rule name="Rewrite segment to id querystring" stopProcessing="true">
      <match url="^iis-rules-rewrite/(.*)$" />
      <action type="Rewrite" url="rewritten?id={R:1}" appendQueryString="false"/>
    </rule>
  </rules>
</rewrite>
```

Try the request to `https://redirect6.azurewebsites.net/iis-rules-rewrite/xyz`

Apps that have an active IIS Rewrite Module with server-level rules configured that impacts the app in undesirable ways:

*   Consider disabling the IIS Rewrite Module for the app.
*   For more information, see [Disabling IIS modules](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/modules?view=aspnetcore-10.0#disabling-iis-modules).

The middleware doesn't support the following IIS URL Rewrite Module features:

*   Outbound Rules
*   Custom Server Variables
*   Wildcards
*   LogRewrittenUrl

The [middleware](https://github.com/dotnet/aspnetcore/blob/main/src/Middleware/Rewrite/src/IISUrlRewrite/ServerVariables.cs) supports the following IIS URL Rewrite Module server variables:

*   CONTENT_LENGTH
*   CONTENT_TYPE
*   HTTP_ACCEPT
*   HTTP_CONNECTION
*   HTTP_COOKIE
*   HTTP_HOST
*   HTTP_REFERER
*   HTTP_URL
*   HTTP_USER_AGENT
*   HTTPS
*   LOCAL_ADDR
*   QUERY_STRING
*   REMOTE_ADDR
*   REMOTE_PORT
*   REQUEST_FILENAME
*   REQUEST_URI

[IFileProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.fileproviders.ifileprovider) can be obtained via a [PhysicalFileProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.fileproviders.physicalfileprovider). This approach may provide greater flexibility for the location of rewrite rules files. Make sure that the rewrite rules files are deployed to the server at the path provided.

```
var fileProvider = new PhysicalFileProvider(Directory.GetCurrentDirectory());
```

Use [Add](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.add) to implement custom rule logic in a method. `Add` exposes the [RewriteContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewritecontext), which makes available the [HttpContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext) for use in redirect methods. The [RewriteContext.Result](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewritecontext.result) property determines how additional pipeline processing is handled. Set the value to one of the [RuleResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.ruleresult) fields described in the following table.

| Rewrite context result | Action |
| --- | --- |
| `RuleResult.ContinueRules` (default) | Continue applying rules. |
| `RuleResult.EndResponse` | Stop applying rules and send the response. |
| `RuleResult.SkipRemainingRules` | Stop applying rules and send the context to the next middleware. |

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        .AddRedirectToHttpsPermanent()
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)
        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

The sample app demonstrates a method that redirects requests for paths that end with `.xml`. When a request is made for `/file.xml`:

*   The request is redirected to `/xmlfiles/file.xml`
*   The status code is set to `301 - Moved Permanently`. When the browser makes a new request for `/xmlfiles/file.xml`, Static File Middleware serves the file to the client from the _wwwroot/xmlfiles_ folder. For a redirect, explicitly set the status code of the response. Otherwise, a _200 - OK_ status code is returned, and the redirect doesn't occur on the client.

`RewriteRules.cs`:

```
public static void RedirectXmlFileRequests(RewriteContext context)
{
    var request = context.HttpContext.Request;

    // Because the client is redirecting back to the same app, stop 
    // processing if the request has already been redirected.
    if (request.Path.StartsWithSegments(new PathString("/xmlfiles")) ||
        request.Path.Value==null)
    {
        return;
    }

    if (request.Path.Value.EndsWith(".xml", StringComparison.OrdinalIgnoreCase))
    {
        var response = context.HttpContext.Response;
        response.StatusCode = (int) HttpStatusCode.MovedPermanently;
        context.Result = RuleResult.EndResponse;
        response.Headers[HeaderNames.Location] = 
            "/xmlfiles" + request.Path + request.QueryString;
    }
}
```

This approach can also rewrite requests. The sample app demonstrates rewriting the path for any text file request to serve the _file.txt_ text file from the _wwwroot_ folder. Static File Middleware serves the file based on the updated request path:

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        .AddRedirectToHttpsPermanent()
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)
        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

`RewriteRules.cs`:

```
public static void RewriteTextFileRequests(RewriteContext context)
{
    var request = context.HttpContext.Request;

    if (request.Path.Value != null &&
        request.Path.Value.EndsWith(".txt", StringComparison.OrdinalIgnoreCase))
    {
        context.Result = RuleResult.SkipRemainingRules;
        request.Path = "/file.txt";
    }
}
```

Use [Add](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.add) to use rule logic in a class that implements the [IRule](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.irule) interface. `IRule` provides greater flexibility over using the method-based rule approach. The implementation class may include a constructor that allows passing in parameters for the [ApplyRule](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.irule.applyrule) method.

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        .AddRedirectToHttpsPermanent()
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)
        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

The values of the parameters in the sample app for the `extension` and the `newPath` are checked to meet several conditions. The `extension` must contain a value, and the value must be `.png`, `.jpg`, or `.gif`. If the `newPath` isn't valid, an [ArgumentException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentexception) is thrown. If a request is made for `image.png`, the request is redirected to `/png-images/image.png`. If a request is made for `image.jpg`, the request is redirected to `/jpg-images/image.jpg`. The status code is set to `301 - Moved Permanently`, and the `context.Result` is set to stop processing rules and send the response.

```
public class RedirectImageRequests : IRule
{
    private readonly string _extension;
    private readonly PathString _newPath;

    public RedirectImageRequests(string extension, string newPath)
    {
        if (string.IsNullOrEmpty(extension))
        {
            throw new ArgumentException(nameof(extension));
        }

        if (!Regex.IsMatch(extension, @"^\.(png|jpg|gif)$"))
        {
            throw new ArgumentException("Invalid extension", nameof(extension));
        }

        if (!Regex.IsMatch(newPath, @"(/[A-Za-z0-9]+)+?"))
        {
            throw new ArgumentException("Invalid path", nameof(newPath));
        }

        _extension = extension;
        _newPath = new PathString(newPath);
    }

    public void ApplyRule(RewriteContext context)
    {
        var request = context.HttpContext.Request;

        // Because we're redirecting back to the same app, stop 
        // processing if the request has already been redirected
        if (request.Path.StartsWithSegments(new PathString(_newPath)) ||
            request.Path.Value == null)
        {
            return;
        }

        if (request.Path.Value.EndsWith(_extension, StringComparison.OrdinalIgnoreCase))
        {
            var response = context.HttpContext.Response;
            response.StatusCode = (int) HttpStatusCode.MovedPermanently;
            context.Result = RuleResult.EndResponse;
            response.Headers[HeaderNames.Location] = 
                _newPath + request.Path + request.QueryString;
        }
    }
}
```

Try:

*   PNG request: `https://redirect6.azurewebsites.net/image.png`
*   JPG request: `https://redirect6.azurewebsites.net/image.jpg`

| Goal | Regex String & Match Example | Replacement String & Output Example |
| --- | --- | --- |
| Rewrite path into querystring | `^path/(.*)/(.*)` `/path/abc/123` | `path?var1=$1&var2=$2` `/path?var1=abc&var2=123` |
| Strip trailing slash | `^path2/(.*)/$` `/path2/xyz/` | `$1` `/path2/xyz` |
| Enforce trailing slash | `^path3/(.*[^/])$` `/path3/xyz` | `$1/` `/path3/xyz/` |
| Avoid rewriting specific requests | `^(.*)(?<!\.axd)$` or `^(?!.*\.axd$)(.*)$` Yes: `/path4/resource.htm` No: `/path4/resource.axd` | `rewritten/$1` `/rewritten/resource.htm` `/resource.axd` |
| Rearrange URL segments | `path5/(.*)/(.*)/(.*)` `path5/1/2/3` | `path5/$3/$2/$1` `path5/3/2/1` |
| Replace a URL segment | `^path6/(.*)/segment2/(.*)` `^path6/segment1/segment2/segment3` | `path6/$1/replaced/$2` `/path6/segment1/replaced/segment3` |

The links in the preceding table use the following code deployed to Azure:

```
using Microsoft.AspNetCore.Rewrite;
using RewriteRules;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

using (StreamReader apacheModRewriteStreamReader =
    File.OpenText("ApacheModRewrite.txt"))
using (StreamReader iisUrlRewriteStreamReader =
    File.OpenText("IISUrlRewrite.xml"))
{
    var options = new RewriteOptions()
        .AddRedirectToHttpsPermanent()
        .AddRedirect("redirect-rule/(.*)", "redirected/$1")
        .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2",
            skipRemainingRules: true)

        // Rewrite path to QS.
        .AddRewrite(@"^path/(.*)/(.*)", "path?var1=$1&var2=$2",
            skipRemainingRules: true)
        // Skip trailing slash.
        .AddRewrite(@"^path2/(.*)/$", "path2/$1",
            skipRemainingRules: true)
         // Enforce trailing slash.
         .AddRewrite(@"^path3/(.*[^/])$", "path3/$1/",
            skipRemainingRules: true)
         // Avoid rewriting specific requests.
         .AddRewrite(@"^path4/(.*)(?<!\.axd)$", "rewritten/$1",
            skipRemainingRules: true)
         // Rearrange URL segments
         .AddRewrite(@"^path5/(.*)/(.*)/(.*)", "path5/$3/$2/$1",
            skipRemainingRules: true)
          // Replace a URL segment
          .AddRewrite(@"^path6/(.*)/segment2/(.*)", "path6/$1/replaced/$2",
            skipRemainingRules: true)

        .AddApacheModRewrite(apacheModRewriteStreamReader)
        .AddIISUrlRewrite(iisUrlRewriteStreamReader)
        .Add(MethodRules.RedirectXmlFileRequests)
        .Add(MethodRules.RewriteTextFileRequests)
        .Add(new RedirectImageRequests(".png", "/png-images"))
        .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

    app.UseRewriter(options);
}

app.UseStaticFiles();

app.Run(context => context.Response.WriteAsync(
    $"Rewritten or Redirected Url: " +
    $"{context.Request.Path + context.Request.QueryString}"));

app.Run();
```

In most of the preceding regular expression samples, the literal `path` is used to make unique testable rewrite rules for the deployed sample. Typically the regular expression wouldn't include `path`. For example, see these [regular expression examples](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting?view=aspnetcore-5.0&preserve-view=true#regex5) table.

This document introduces URL rewriting with instructions on how to use URL Rewriting Middleware in ASP.NET Core apps.

URL rewriting is the act of modifying request URLs based on one or more predefined rules. URL rewriting creates an abstraction between resource locations and their addresses so that the locations and addresses aren't tightly linked. URL rewriting is valuable in several scenarios to:

*   Move or replace server resources temporarily or permanently and maintain stable locators for those resources.
*   Split request processing across different apps or across areas of one app.
*   Remove, add, or reorganize URL segments on incoming requests.
*   Optimize public URLs for Search Engine Optimization (SEO).
*   Permit the use of friendly public URLs to help visitors predict the content returned by requesting a resource.
*   Redirect insecure requests to secure endpoints.
*   Prevent hotlinking, where an external site uses a hosted static asset on another site by linking the asset into its own content.

Note

URL rewriting can reduce the performance of an app. Where feasible, limit the number and complexity of rules.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/url-rewriting/samples/) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

The difference in wording between _URL redirect_ and _URL rewrite_ is subtle but has important implications for providing resources to clients. ASP.NET Core's URL Rewriting Middleware is capable of meeting the need for both.

A _URL redirect_ involves a client-side operation, where the client is instructed to access a resource at a different address than the client originally requested. This requires a round trip to the server. The redirect URL returned to the client appears in the browser's address bar when the client makes a new request for the resource.

If `/resource` is _redirected_ to `/different-resource`, the server responds that the client should obtain the resource at `/different-resource` with a status code indicating that the redirect is either temporary or permanent.

![Image 4: A WebAPI service endpoint has been temporarily changed from version 1 (v1) to version 2 (v2) on the server. A client makes a request to the service at the version 1 path /v1/api. The server sends back a 302 (Found) response with the new, temporary path for the service at version 2 /v2/api. The client makes a second request to the service at the redirect URL. The server responds with a 200 (OK) status code.](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/url_redirect.png?view=aspnetcore-10.0)

When redirecting requests to a different URL, indicate whether the redirect is permanent or temporary by specifying the status code with the response:

*   The `301 - Moved Permanently` status code is used where the resource has a new, permanent URL and you wish to instruct the client that all future requests for the resource should use the new URL. _The client may cache and reuse the response when a 301 status code is received._

*   The _302 - Found_ status code is used where the redirection is temporary or generally subject to change. The 302 status code indicates to the client not to store the URL and use it in the future.

For more information on status codes, see [RFC 9110: Status Code Definitions](https://www.rfc-editor.org/rfc/rfc9110#name-status-codes).

A _URL rewrite_ is a server-side operation that provides a resource from a different resource address than the client requested. Rewriting a URL doesn't require a round trip to the server. The rewritten URL isn't returned to the client and doesn't appear in the browser's address bar.

If `/resource` is _rewritten_ to `/different-resource`, the server _internally_ fetches and returns the resource at `/different-resource`.

Although the client might be able to retrieve the resource at the rewritten URL, the client isn't informed that the resource exists at the rewritten URL when it makes its request and receives the response.

![Image 5: A WebAPI service endpoint has been changed from version 1 (v1) to version 2 (v2) on the server. A client makes a request to the service at the version 1 path /v1/api. The request URL is rewritten to access the service at the version 2 path /v2/api. The service responds to the client with a 200 (OK) status code.](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/url_rewrite.png?view=aspnetcore-10.0)

You can explore the features of the URL Rewriting Middleware with the [sample app](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/url-rewriting/samples/). The app applies redirect and rewrite rules and shows the redirected or rewritten URL for several scenarios.

Use URL Rewriting Middleware when you're unable to use the following approaches:

*   [URL Rewrite module with IIS on Windows Server](https://www.iis.net/downloads/microsoft/url-rewrite)
*   [Apache mod_rewrite module on Apache Server](https://httpd.apache.org/docs/2.4/rewrite/)
*   [URL rewriting on Nginx](https://www.nginx.com/blog/creating-nginx-rewrite-rules/)

Use the URL rewriting middleware when the app is hosted on [HTTP.sys server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0).

The main reasons to use the server-based URL rewriting technologies in IIS, Apache, and Nginx are:

*   The middleware doesn't support the full features of these modules.

Some of the features of the server modules don't work with ASP.NET Core projects, such as the `IsFile` and `IsDirectory` constraints of the IIS Rewrite module. In these scenarios, use the middleware instead.

*   The performance of the middleware probably doesn't match that of the modules.

Benchmarking is the only way to know for sure which approach degrades performance the most or if degraded performance is negligible.

URL Rewriting Middleware is provided by the [Microsoft.AspNetCore.Rewrite](https://www.nuget.org/packages/Microsoft.AspNetCore.Rewrite) package, which is implicitly included in ASP.NET Core apps.

Establish URL rewrite and redirect rules by creating an instance of the [RewriteOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptions) class with extension methods for each of your rewrite rules. Chain multiple rules in the order that you would like them processed. The `RewriteOptions` are passed into the URL Rewriting Middleware as it's added to the request pipeline with [UseRewriter](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.rewritebuilderextensions.userewriter):

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

Three options permit the app to redirect non-`www` requests to `www`:

*   [AddRedirectToWwwPermanent](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttowwwpermanent): Permanently redirect the request to the `www` subdomain if the request is non-`www`. Redirects with a [Status308PermanentRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status308permanentredirect#microsoft-aspnetcore-http-statuscodes-status308permanentredirect) status code.

*   [AddRedirectToWww](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttowww): Redirect the request to the `www` subdomain if the incoming request is non-`www`. Redirects with a [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect) status code. An overload permits you to provide the status code for the response. Use a field of the [StatusCodes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes) class for a status code assignment.

Use [AddRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirect) to redirect requests. The first parameter contains your Regex for matching on the path of the incoming URL. The second parameter is the replacement string. The third parameter, if present, specifies the status code. If you don't specify the status code, the status code defaults to _302 - Found_, which indicates that the resource is temporarily moved or replaced.

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

In a browser with developer tools enabled, make a request to the sample app with the path `/redirect-rule/1234/5678`. The regex matches the request path on `redirect-rule/(.*)`, and the path is replaced with `/redirected/1234/5678`. The redirect URL is sent back to the client with a _302 - Found_ status code. The browser makes a new request at the redirect URL, which appears in the browser's address bar. Since no rules in the sample app match on the redirect URL:

*   The second request receives a _200 - OK_ response from the app.
*   The body of the response shows the redirect URL.

A round trip is made to the server when a URL is _redirected_.

Warning

Be cautious when establishing redirect rules. Redirect rules are evaluated on every request to the app, including after a redirect. It's easy to accidentally create a _loop of infinite redirects_.

Original Request: `/redirect-rule/1234/5678`

![Image 6: Add redirect: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect.png?view=aspnetcore-10.0)

The part of the expression contained within parentheses is called a _capture group_. The dot (`.`) of the expression means _match any character_. The asterisk (`*`) indicates _match the preceding character zero or more times_. Therefore, the last two path segments of the URL, `1234/5678`, are captured by capture group `(.*)`. Any value you provide in the request URL after `redirect-rule/` is captured by this single capture group.

In the replacement string, captured groups are injected into the string with the dollar sign (`$`) followed by the sequence number of the capture. The first capture group value is obtained with `$1`, the second with `$2`, and they continue in sequence for the capture groups in your regex. There's only one captured group in the redirect rule regex in the sample app, so there's only one injected group in the replacement string, which is `$1`. When the rule is applied, the URL becomes `/redirected/1234/5678`.

Use [AddRedirectToHttps](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttohttps) to redirect HTTP requests to the same host and path using the HTTPS protocol. If the status code isn't supplied, the middleware defaults to _302 - Found_. If the port isn't supplied:

*   The middleware defaults to `null`.
*   The scheme changes to `https` (HTTPS protocol), and the client accesses the resource on port 443.

The following example shows how to set the status code to `301 - Moved Permanently` and change the port to 5001.

```
public void Configure(IApplicationBuilder app)
{
    var options = new RewriteOptions()
        .AddRedirectToHttps(301, 5001);

    app.UseRewriter(options);
}
```

Use [AddRedirectToHttpsPermanent](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttohttpspermanent) to redirect insecure requests to the same host and path with secure HTTPS protocol on port 443. The middleware sets the status code to `301 - Moved Permanently`.

```
public void Configure(IApplicationBuilder app)
{
    var options = new RewriteOptions()
        .AddRedirectToHttpsPermanent();

    app.UseRewriter(options);
}
```

Note

When redirecting to a secure endpoint without the requirement for additional redirect rules, we recommend using HTTPS Redirection Middleware. For more information, see the [Enforce HTTPS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#require-https) topic.

The sample app is capable of demonstrating how to use `AddRedirectToHttps` or `AddRedirectToHttpsPermanent`. Add the extension method to the `RewriteOptions`. Make an insecure request to the app at any URL. Dismiss the browser security warning that the self-signed certificate is untrusted or create an exception to trust the certificate.

Original Request using `AddRedirectToHttps(301, 5001)`: `http://localhost:5000/secure`

![Image 7: Add redirect to HTTPS: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect_to_https.png?view=aspnetcore-10.0)

Original Request using `AddRedirectToHttpsPermanent`: `http://localhost:5000/secure`

![Image 8: Add redirect to HTTPS permanent: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect_to_https_permanent.png?view=aspnetcore-10.0)

Use [AddRewrite](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addrewrite) to create a rule for rewriting URLs. The first parameter contains the regex for matching on the incoming URL path. The second parameter is the replacement string. The third parameter, `skipRemainingRules: {true|false}`, indicates to the middleware whether or not to skip additional rewrite rules if the current rule is applied.

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

Original Request: `/rewrite-rule/1234/5678`

![Image 9: Add rewrite: Browser window with developer tools tracking the request and response](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_rewrite.png?view=aspnetcore-10.0)

The carat (`^`) at the beginning of the expression means that matching starts at the beginning of the URL path.

In the earlier example with the redirect rule, `redirect-rule/(.*)`, there's no carat (`^`) at the start of the regex. Therefore, any characters may precede `redirect-rule/` in the path for a successful match.

| Path | Match |
| --- | --- |
| `/redirect-rule/1234/5678` | Yes |
| `/my-cool-redirect-rule/1234/5678` | Yes |
| `/anotherredirect-rule/1234/5678` | Yes |

The rewrite rule, `^rewrite-rule/(\d+)/(\d+)`, only matches paths if they start with `rewrite-rule/`. In the following table, note the difference in matching.

| Path | Match |
| --- | --- |
| `/rewrite-rule/1234/5678` | Yes |
| `/my-cool-rewrite-rule/1234/5678` | No |
| `/anotherrewrite-rule/1234/5678` | No |

Following the `^rewrite-rule/` portion of the expression, there are two capture groups, `(\d+)/(\d+)`. The `\d` signifies _match a digit (number)_. The plus sign (`+`) means _match one or more of the preceding character_. Therefore, the URL must contain a number followed by a forward-slash followed by another number. These capture groups are injected into the rewritten URL as `$1` and `$2`. The rewrite rule replacement string places the captured groups into the query string. The requested path of `/rewrite-rule/1234/5678` is rewritten to obtain the resource at `/rewritten?var1=1234&var2=5678`. If a query string is present on the original request, it's preserved when the URL is rewritten.

There's no round trip to the server to obtain the resource. If the resource exists, it's fetched and returned to the client with a _200 - OK_ status code. Because the client isn't redirected, the URL in the browser's address bar doesn't change. Clients can't detect that a URL rewrite operation occurred on the server.

Note

Use `skipRemainingRules: true` whenever possible because matching rules is computationally expensive and increases app response time. For the fastest app response:

*   Order rewrite rules from the most frequently matched rule to the least frequently matched rule.
*   Skip the processing of the remaining rules when a match occurs and no additional rule processing is required.

Apply Apache mod_rewrite rules with [AddApacheModRewrite](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.apachemodrewriteoptionsextensions.addapachemodrewrite). Make sure that the rules file is deployed with the app. For more information and examples of mod_rewrite rules, see [Apache mod_rewrite](https://httpd.apache.org/docs/2.4/rewrite/).

A [StreamReader](https://learn.microsoft.com/en-us/dotnet/api/system.io.streamreader) is used to read the rules from the _ApacheModRewrite.txt_ rules file:

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

The sample app redirects requests from `/apache-mod-rules-redirect/(.\*)` to `/redirected?id=$1`. The response status code is _302 - Found_.

```
# Rewrite path with additional sub directory
RewriteRule ^/apache-mod-rules-redirect/(.*) /redirected?id=$1 [L,R=302]
```

Original Request: `/apache-mod-rules-redirect/1234`

![Image 10: Add Apache mod redirect: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_apache_mod_redirect.png?view=aspnetcore-10.0)

The middleware supports the following Apache mod_rewrite server variables:

*   CONN_REMOTE_ADDR
*   HTTP_ACCEPT
*   HTTP_CONNECTION
*   HTTP_COOKIE
*   HTTP_FORWARDED
*   HTTP_HOST
*   HTTP_REFERER
*   HTTP_USER_AGENT
*   HTTPS
*   IPV6
*   QUERY_STRING
*   REMOTE_ADDR
*   REMOTE_PORT
*   REQUEST_FILENAME
*   REQUEST_METHOD
*   REQUEST_SCHEME
*   REQUEST_URI
*   SCRIPT_FILENAME
*   SERVER_ADDR
*   SERVER_PORT
*   SERVER_PROTOCOL
*   TIME
*   TIME_DAY
*   TIME_HOUR
*   TIME_MIN
*   TIME_MON
*   TIME_SEC
*   TIME_WDAY
*   TIME_YEAR

To use the same rule set that applies to the IIS URL Rewrite Module, use [AddIISUrlRewrite](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.iisurlrewriteoptionsextensions.addiisurlrewrite). Make sure that the rules file is deployed with the app. Don't direct the middleware to use the app's _web.config_ file when running on Windows Server IIS. With IIS, these rules should be stored outside of the app's _web.config_ file in order to avoid conflicts with the IIS Rewrite module. For more information and examples of IIS URL Rewrite Module rules, see [Using Url Rewrite Module 2.0](https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/using-url-rewrite-module-20) and [URL Rewrite Module Configuration Reference](https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/url-rewrite-module-configuration-reference).

A [StreamReader](https://learn.microsoft.com/en-us/dotnet/api/system.io.streamreader) is used to read the rules from the `IISUrlRewrite.xml` rules file:

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

The sample app rewrites requests from `/iis-rules-rewrite/(.*)` to `/rewritten?id=$1`. The response is sent to the client with a _200 - OK_ status code.

```
<rewrite>
  <rules>
    <rule name="Rewrite segment to id querystring" stopProcessing="true">
      <match url="^iis-rules-rewrite/(.*)$" />
      <action type="Rewrite" url="rewritten?id={R:1}" appendQueryString="false"/>
    </rule>
  </rules>
</rewrite>
```

Original Request: `/iis-rules-rewrite/1234`

![Image 11: Add IIS URL rewrite: Browser window with developer tools tracking the request and response](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_iis_url_rewrite.png?view=aspnetcore-10.0)

If you have an active IIS Rewrite Module with server-level rules configured that would impact your app in undesirable ways, you can disable the IIS Rewrite Module for an app. For more information, see [Disabling IIS modules](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/modules?view=aspnetcore-10.0#disabling-iis-modules).

The middleware doesn't support the following IIS URL Rewrite Module features:

*   Outbound Rules
*   Custom Server Variables
*   Wildcards
*   LogRewrittenUrl

The middleware supports the following IIS URL Rewrite Module server variables:

*   CONTENT_LENGTH
*   CONTENT_TYPE
*   HTTP_ACCEPT
*   HTTP_CONNECTION
*   HTTP_COOKIE
*   HTTP_HOST
*   HTTP_REFERER
*   HTTP_URL
*   HTTP_USER_AGENT
*   HTTPS
*   LOCAL_ADDR
*   QUERY_STRING
*   REMOTE_ADDR
*   REMOTE_PORT
*   REQUEST_FILENAME
*   REQUEST_URI

Note

You can also obtain an [IFileProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.fileproviders.ifileprovider) via a [PhysicalFileProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.fileproviders.physicalfileprovider). This approach may provide greater flexibility for the location of your rewrite rules files. Make sure that your rewrite rules files are deployed to the server at the path you provide.

```
PhysicalFileProvider fileProvider = new PhysicalFileProvider(Directory.GetCurrentDirectory());
```

Use [Add](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.add) to implement your own rule logic in a method. `Add` exposes the [RewriteContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewritecontext), which makes available the [HttpContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext) for use in your method. The [RewriteContext.Result](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewritecontext.result) determines how additional pipeline processing is handled. Set the value to one of the [RuleResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.ruleresult) fields described in the following table.

| Rewrite context result | Action |
| --- | --- |
| `RuleResult.ContinueRules` (default) | Continue applying rules. |
| `RuleResult.EndResponse` | Stop applying rules and send the response. |
| `RuleResult.SkipRemainingRules` | Stop applying rules and send the context to the next middleware. |

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

The sample app demonstrates a method that redirects requests for paths that end with `.xml`. If a request is made for `/file.xml`, the request is redirected to `/xmlfiles/file.xml`. The status code is set to `301 - Moved Permanently`. When the browser makes a new request for `/xmlfiles/file.xml`, Static File Middleware serves the file to the client from the _wwwroot/xmlfiles_ folder. For a redirect, explicitly set the status code of the response. Otherwise, a _200 - OK_ status code is returned, and the redirect doesn't occur on the client.

`RewriteRules.cs`:

```
public static void RedirectXmlFileRequests(RewriteContext context)
{
    var request = context.HttpContext.Request;

    // Because the client is redirecting back to the same app, stop 
    // processing if the request has already been redirected.
    if (request.Path.StartsWithSegments(new PathString("/xmlfiles")))
    {
        return;
    }

    if (request.Path.Value.EndsWith(".xml", StringComparison.OrdinalIgnoreCase))
    {
        var response = context.HttpContext.Response;
        response.StatusCode = (int) HttpStatusCode.MovedPermanently;
        context.Result = RuleResult.EndResponse;
        response.Headers[HeaderNames.Location] = 
            "/xmlfiles" + request.Path + request.QueryString;
    }
}
```

This approach can also rewrite requests. The sample app demonstrates rewriting the path for any text file request to serve the _file.txt_ text file from the _wwwroot_ folder. Static File Middleware serves the file based on the updated request path:

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

`RewriteRules.cs`:

```
public static void RewriteTextFileRequests(RewriteContext context)
{
    var request = context.HttpContext.Request;

    if (request.Path.Value.EndsWith(".txt", StringComparison.OrdinalIgnoreCase))
    {
        context.Result = RuleResult.SkipRemainingRules;
        request.Path = "/file.txt";
    }
}
```

Use [Add](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.add) to use rule logic in a class that implements the [IRule](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.irule) interface. `IRule` provides greater flexibility over using the method-based rule approach. Your implementation class may include a constructor that allows you can pass in parameters for the [ApplyRule](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.irule.applyrule) method.

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

The values of the parameters in the sample app for the `extension` and the `newPath` are checked to meet several conditions. The `extension` must contain a value, and the value must be `.png`, `.jpg`, or _.gif_. If the `newPath` isn't valid, an [ArgumentException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentexception) is thrown. If a request is made for `image.png`, the request is redirected to `/png-images/image.png`. If a request is made for `image.jpg`, the request is redirected to `/jpg-images/image.jpg`. The status code is set to `301 - Moved Permanently`, and the `context.Result` is set to stop processing rules and send the response.

```
public class RedirectImageRequests : IRule
{
    private readonly string _extension;
    private readonly PathString _newPath;

    public RedirectImageRequests(string extension, string newPath)
    {
        if (string.IsNullOrEmpty(extension))
        {
            throw new ArgumentException(nameof(extension));
        }

        if (!Regex.IsMatch(extension, @"^\.(png|jpg|gif)$"))
        {
            throw new ArgumentException("Invalid extension", nameof(extension));
        }

        if (!Regex.IsMatch(newPath, @"(/[A-Za-z0-9]+)+?"))
        {
            throw new ArgumentException("Invalid path", nameof(newPath));
        }

        _extension = extension;
        _newPath = new PathString(newPath);
    }

    public void ApplyRule(RewriteContext context)
    {
        var request = context.HttpContext.Request;

        // Because we're redirecting back to the same app, stop 
        // processing if the request has already been redirected
        if (request.Path.StartsWithSegments(new PathString(_newPath)))
        {
            return;
        }

        if (request.Path.Value.EndsWith(_extension, StringComparison.OrdinalIgnoreCase))
        {
            var response = context.HttpContext.Response;
            response.StatusCode = (int) HttpStatusCode.MovedPermanently;
            context.Result = RuleResult.EndResponse;
            response.Headers[HeaderNames.Location] = 
                _newPath + request.Path + request.QueryString;
        }
    }
}
```

Original Request: `/image.png`

![Image 12: For image.png: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect_png_requests.png?view=aspnetcore-10.0)

Original Request: `/image.jpg`

![Image 13: For image.jpg: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect_jpg_requests.png?view=aspnetcore-10.0)

| Goal | Regex String & Match Example | Replacement String & Output Example |
| --- | --- | --- |
| Rewrite path into querystring | `^path/(.*)/(.*)` `/path/abc/123` | `path?var1=$1&var2=$2` `/path?var1=abc&var2=123` |
| Strip trailing slash | `(.*)/$` `/path/` | `$1` `/path` |
| Enforce trailing slash | `(.*[^/])$` `/path` | `$1/` `/path/` |
| Avoid rewriting specific requests | `^(.*)(?<!\.axd)$` or `^(?!.*\.axd$)(.*)$` Yes: `/resource.htm` No: `/resource.axd` | `rewritten/$1` `/rewritten/resource.htm` `/resource.axd` |
| Rearrange URL segments | `path/(.*)/(.*)/(.*)` `path/1/2/3` | `path/$3/$2/$1` `path/3/2/1` |
| Replace a URL segment | `^(.*)/segment2/(.*)` `/segment1/segment2/segment3` | `$1/replaced/$2` `/segment1/replaced/segment3` |

This document introduces URL rewriting with instructions on how to use URL Rewriting Middleware in ASP.NET Core apps.

URL rewriting is the act of modifying request URLs based on one or more predefined rules. URL rewriting creates an abstraction between resource locations and their addresses so that the locations and addresses aren't tightly linked. URL rewriting is valuable in several scenarios to:

*   Move or replace server resources temporarily or permanently and maintain stable locators for those resources.
*   Split request processing across different apps or across areas of one app.
*   Remove, add, or reorganize URL segments on incoming requests.
*   Optimize public URLs for Search Engine Optimization (SEO).
*   Permit the use of friendly public URLs to help visitors predict the content returned by requesting a resource.
*   Redirect insecure requests to secure endpoints.
*   Prevent hotlinking, where an external site uses a hosted static asset on another site by linking the asset into its own content.

Note

URL rewriting can reduce the performance of an app. Where feasible, limit the number and complexity of rules.

[View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/url-rewriting/samples/) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))

The difference in wording between _URL redirect_ and _URL rewrite_ is subtle but has important implications for providing resources to clients. ASP.NET Core's URL Rewriting Middleware is capable of meeting the need for both.

A _URL redirect_ involves a client-side operation, where the client is instructed to access a resource at a different address than the client originally requested. This requires a round trip to the server. The redirect URL returned to the client appears in the browser's address bar when the client makes a new request for the resource.

If `/resource` is _redirected_ to `/different-resource`, the server responds that the client should obtain the resource at `/different-resource` with a status code indicating that the redirect is either temporary or permanent.

![Image 14: A WebAPI service endpoint has been temporarily changed from version 1 (v1) to version 2 (v2) on the server. A client makes a request to the service at the version 1 path /v1/api. The server sends back a 302 (Found) response with the new, temporary path for the service at version 2 /v2/api. The client makes a second request to the service at the redirect URL. The server responds with a 200 (OK) status code.](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/url_redirect.png?view=aspnetcore-10.0)

When redirecting requests to a different URL, indicate whether the redirect is permanent or temporary by specifying the status code with the response:

*   The `301 - Moved Permanently` status code is used where the resource has a new, permanent URL and you wish to instruct the client that all future requests for the resource should use the new URL. _The client may cache and reuse the response when a 301 status code is received._

*   The _302 - Found_ status code is used where the redirection is temporary or generally subject to change. The 302 status code indicates to the client not to store the URL and use it in the future.

For more information on status codes, see [RFC 9110: Status Code Definitions](https://www.rfc-editor.org/rfc/rfc9110#name-status-codes).

A _URL rewrite_ is a server-side operation that provides a resource from a different resource address than the client requested. Rewriting a URL doesn't require a round trip to the server. The rewritten URL isn't returned to the client and doesn't appear in the browser's address bar.

If `/resource` is _rewritten_ to `/different-resource`, the server _internally_ fetches and returns the resource at `/different-resource`.

Although the client might be able to retrieve the resource at the rewritten URL, the client isn't informed that the resource exists at the rewritten URL when it makes its request and receives the response.

![Image 15: A WebAPI service endpoint has been changed from version 1 (v1) to version 2 (v2) on the server. A client makes a request to the service at the version 1 path /v1/api. The request URL is rewritten to access the service at the version 2 path /v2/api. The service responds to the client with a 200 (OK) status code.](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/url_rewrite.png?view=aspnetcore-10.0)

You can explore the features of the URL Rewriting Middleware with the [sample app](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/url-rewriting/samples/). The app applies redirect and rewrite rules and shows the redirected or rewritten URL for several scenarios.

Use URL Rewriting Middleware when you're unable to use the following approaches:

*   [URL Rewrite module with IIS on Windows Server](https://www.iis.net/downloads/microsoft/url-rewrite)
*   [Apache mod_rewrite module on Apache Server](https://httpd.apache.org/docs/2.4/rewrite/)
*   [URL rewriting on Nginx](https://www.nginx.com/blog/creating-nginx-rewrite-rules/)

Also, use the middleware when the app is hosted on [HTTP.sys server](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/servers/httpsys?view=aspnetcore-10.0) (formerly called WebListener).

The main reasons to use the server-based URL rewriting technologies in IIS, Apache, and Nginx are:

*   The middleware doesn't support the full features of these modules.

Some of the features of the server modules don't work with ASP.NET Core projects, such as the `IsFile` and `IsDirectory` constraints of the IIS Rewrite module. In these scenarios, use the middleware instead.

*   The performance of the middleware probably doesn't match that of the modules.

Benchmarking is the only way to know for sure which approach degrades performance the most or if degraded performance is negligible.

To include the middleware in your project, add a package reference to the [Microsoft.AspNetCore.App metapackage](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/metapackage-app?view=aspnetcore-10.0) in the project file, which contains the [Microsoft.AspNetCore.Rewrite](https://www.nuget.org/packages/Microsoft.AspNetCore.Rewrite) package.

When not using the `Microsoft.AspNetCore.App` metapackage, add a project reference to the `Microsoft.AspNetCore.Rewrite` package.

Establish URL rewrite and redirect rules by creating an instance of the [RewriteOptions](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptions) class with extension methods for each of your rewrite rules. Chain multiple rules in the order that you would like them processed. The `RewriteOptions` are passed into the URL Rewriting Middleware as it's added to the request pipeline with [UseRewriter](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.rewritebuilderextensions.userewriter):

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

Three options permit the app to redirect non-`www` requests to `www`:

*   [AddRedirectToWwwPermanent](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttowwwpermanent): Permanently redirect the request to the `www` subdomain if the request is non-`www`. Redirects with a [Status308PermanentRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status308permanentredirect#microsoft-aspnetcore-http-statuscodes-status308permanentredirect) status code.

*   [AddRedirectToWww](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttowww): Redirect the request to the `www` subdomain if the incoming request is non-`www`. Redirects with a [Status307TemporaryRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes.status307temporaryredirect#microsoft-aspnetcore-http-statuscodes-status307temporaryredirect) status code. An overload permits you to provide the status code for the response. Use a field of the [StatusCodes](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.statuscodes) class for a status code assignment.

Use [AddRedirect](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirect) to redirect requests. The first parameter contains your regex for matching on the path of the incoming URL. The second parameter is the replacement string. The third parameter, if present, specifies the status code. If you don't specify the status code, the status code defaults to _302 - Found_, which indicates that the resource is temporarily moved or replaced.

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

In a browser with developer tools enabled, make a request to the sample app with the path `/redirect-rule/1234/5678`. The regex matches the request path on `redirect-rule/(.*)`, and the path is replaced with `/redirected/1234/5678`. The redirect URL is sent back to the client with a _302 - Found_ status code. The browser makes a new request at the redirect URL, which appears in the browser's address bar. Since no rules in the sample app match on the redirect URL:

*   The second request receives a _200 - OK_ response from the app.
*   The body of the response shows the redirect URL.

A round trip is made to the server when a URL is _redirected_.

Warning

Be cautious when establishing redirect rules. Redirect rules are evaluated on every request to the app, including after a redirect. It's easy to accidentally create a _loop of infinite redirects_.

Original Request: `/redirect-rule/1234/5678`

![Image 16: Add redirect: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect.png?view=aspnetcore-10.0)

The part of the expression contained within parentheses is called a _capture group_. The dot (`.`) of the expression means _match any character_. The asterisk (`*`) indicates _match the preceding character zero or more times_. Therefore, the last two path segments of the URL, `1234/5678`, are captured by capture group `(.*)`. Any value you provide in the request URL after `redirect-rule/` is captured by this single capture group.

In the replacement string, captured groups are injected into the string with the dollar sign (`$`) followed by the sequence number of the capture. The first capture group value is obtained with `$1`, the second with `$2`, and they continue in sequence for the capture groups in your regex. There's only one captured group in the redirect rule regex in the sample app, so there's only one injected group in the replacement string, which is `$1`. When the rule is applied, the URL becomes `/redirected/1234/5678`.

Use [AddRedirectToHttps](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttohttps) to redirect HTTP requests to the same host and path using the HTTPS protocol. If the status code isn't supplied, the middleware defaults to _302 - Found_. If the port isn't supplied:

*   The middleware defaults to `null`.
*   The scheme changes to `https` (HTTPS protocol), and the client accesses the resource on port 443.

The following example shows how to set the status code to `301 - Moved Permanently` and change the port to 5001.

```
public void Configure(IApplicationBuilder app)
{
    var options = new RewriteOptions()
        .AddRedirectToHttps(301, 5001);

    app.UseRewriter(options);
}
```

Use [AddRedirectToHttpsPermanent](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addredirecttohttpspermanent) to redirect insecure requests to the same host and path with secure HTTPS protocol on port 443. The middleware sets the status code to `301 - Moved Permanently`.

```
public void Configure(IApplicationBuilder app)
{
    var options = new RewriteOptions()
        .AddRedirectToHttpsPermanent();

    app.UseRewriter(options);
}
```

Note

When redirecting to a secure endpoint without the requirement for additional redirect rules, we recommend using HTTPS Redirection Middleware. For more information, see the [Enforce HTTPS](https://learn.microsoft.com/en-us/aspnet/core/security/enforcing-ssl?view=aspnetcore-10.0#require-https) topic.

The sample app is capable of demonstrating how to use `AddRedirectToHttps` or `AddRedirectToHttpsPermanent`. Add the extension method to the `RewriteOptions`. Make an insecure request to the app at any URL. Dismiss the browser security warning that the self-signed certificate is untrusted or create an exception to trust the certificate.

Original Request using `AddRedirectToHttps(301, 5001)`: `http://localhost:5000/secure`

![Image 17: Add redirect to HTTPS: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect_to_https.png?view=aspnetcore-10.0)

Original Request using `AddRedirectToHttpsPermanent`: `http://localhost:5000/secure`

![Image 18: Add redirect to HTTPS permanent: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect_to_https_permanent.png?view=aspnetcore-10.0)

Use [AddRewrite](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.addrewrite) to create a rule for rewriting URLs. The first parameter contains the regex for matching on the incoming URL path. The second parameter is the replacement string. The third parameter, `skipRemainingRules: {true|false}`, indicates to the middleware whether or not to skip additional rewrite rules if the current rule is applied.

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

Original Request: `/rewrite-rule/1234/5678`

![Image 19: Add rewrite: Browser window with developer tools tracking the request and response](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_rewrite.png?view=aspnetcore-10.0)

The carat (`^`) at the beginning of the expression means that matching starts at the beginning of the URL path.

In the earlier example with the redirect rule, `redirect-rule/(.*)`, there's no carat (`^`) at the start of the regex. Therefore, any characters may precede `redirect-rule/` in the path for a successful match.

| Path | Match |
| --- | --- |
| `/redirect-rule/1234/5678` | Yes |
| `/my-cool-redirect-rule/1234/5678` | Yes |
| `/anotherredirect-rule/1234/5678` | Yes |

The rewrite rule, `^rewrite-rule/(\d+)/(\d+)`, only matches paths if they start with `rewrite-rule/`. In the following table, note the difference in matching.

| Path | Match |
| --- | --- |
| `/rewrite-rule/1234/5678` | Yes |
| `/my-cool-rewrite-rule/1234/5678` | No |
| `/anotherrewrite-rule/1234/5678` | No |

Following the `^rewrite-rule/` portion of the expression, there are two capture groups, `(\d+)/(\d+)`. The `\d` signifies _match a digit (number)_. The plus sign (`+`) means _match one or more of the preceding character_. Therefore, the URL must contain a number followed by a forward-slash followed by another number. These capture groups are injected into the rewritten URL as `$1` and `$2`. The rewrite rule replacement string places the captured groups into the query string. The requested path of `/rewrite-rule/1234/5678` is rewritten to obtain the resource at `/rewritten?var1=1234&var2=5678`. If a query string is present on the original request, it's preserved when the URL is rewritten.

There's no round trip to the server to obtain the resource. If the resource exists, it's fetched and returned to the client with a _200 - OK_ status code. Because the client isn't redirected, the URL in the browser's address bar doesn't change. Clients can't detect that a URL rewrite operation occurred on the server.

Note

Use `skipRemainingRules: true` whenever possible because matching rules is computationally expensive and increases app response time. For the fastest app response:

*   Order rewrite rules from the most frequently matched rule to the least frequently matched rule.
*   Skip the processing of the remaining rules when a match occurs and no additional rule processing is required.

Apply Apache mod_rewrite rules with [AddApacheModRewrite](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.apachemodrewriteoptionsextensions.addapachemodrewrite). Make sure that the rules file is deployed with the app. For more information and examples of mod_rewrite rules, see [Apache mod_rewrite](https://httpd.apache.org/docs/2.4/rewrite/).

A [StreamReader](https://learn.microsoft.com/en-us/dotnet/api/system.io.streamreader) is used to read the rules from the _ApacheModRewrite.txt_ rules file:

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

The sample app redirects requests from `/apache-mod-rules-redirect/(.\*)` to `/redirected?id=$1`. The response status code is _302 - Found_.

```
# Rewrite path with additional sub directory
RewriteRule ^/apache-mod-rules-redirect/(.*) /redirected?id=$1 [L,R=302]
```

Original Request: `/apache-mod-rules-redirect/1234`

![Image 20: Add Apache mod redirect: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_apache_mod_redirect.png?view=aspnetcore-10.0)

The middleware supports the following Apache mod_rewrite server variables:

*   CONN_REMOTE_ADDR
*   HTTP_ACCEPT
*   HTTP_CONNECTION
*   HTTP_COOKIE
*   HTTP_FORWARDED
*   HTTP_HOST
*   HTTP_REFERER
*   HTTP_USER_AGENT
*   HTTPS
*   IPV6
*   QUERY_STRING
*   REMOTE_ADDR
*   REMOTE_PORT
*   REQUEST_FILENAME
*   REQUEST_METHOD
*   REQUEST_SCHEME
*   REQUEST_URI
*   SCRIPT_FILENAME
*   SERVER_ADDR
*   SERVER_PORT
*   SERVER_PROTOCOL
*   TIME
*   TIME_DAY
*   TIME_HOUR
*   TIME_MIN
*   TIME_MON
*   TIME_SEC
*   TIME_WDAY
*   TIME_YEAR

To use the same rule set that applies to the IIS URL Rewrite Module, use [AddIISUrlRewrite](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.iisurlrewriteoptionsextensions.addiisurlrewrite). Make sure that the rules file is deployed with the app. Don't direct the middleware to use the app's _web.config_ file when running on Windows Server IIS. With IIS, these rules should be stored outside of the app's _web.config_ file in order to avoid conflicts with the IIS Rewrite module. For more information and examples of IIS URL Rewrite Module rules, see [Using Url Rewrite Module 2.0](https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/using-url-rewrite-module-20) and [URL Rewrite Module Configuration Reference](https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/url-rewrite-module-configuration-reference).

A [StreamReader](https://learn.microsoft.com/en-us/dotnet/api/system.io.streamreader) is used to read the rules from the `IISUrlRewrite.xml` rules file:

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

The sample app rewrites requests from `/iis-rules-rewrite/(.*)` to `/rewritten?id=$1`. The response is sent to the client with a _200 - OK_ status code.

```
<rewrite>
  <rules>
    <rule name="Rewrite segment to id querystring" stopProcessing="true">
      <match url="^iis-rules-rewrite/(.*)$" />
      <action type="Rewrite" url="rewritten?id={R:1}" appendQueryString="false"/>
    </rule>
  </rules>
</rewrite>
```

Original Request: `/iis-rules-rewrite/1234`

![Image 21: Add IIS URL rewrite: Browser window with developer tools tracking the request and response](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_iis_url_rewrite.png?view=aspnetcore-10.0)

If you have an active IIS Rewrite Module with server-level rules configured that would impact your app in undesirable ways, you can disable the IIS Rewrite Module for an app. For more information, see [Disabling IIS modules](https://learn.microsoft.com/en-us/aspnet/core/host-and-deploy/iis/modules?view=aspnetcore-10.0#disabling-iis-modules).

The middleware released with ASP.NET Core 2.x doesn't support the following IIS URL Rewrite Module features:

*   Outbound Rules
*   Custom Server Variables
*   Wildcards
*   LogRewrittenUrl

The middleware supports the following IIS URL Rewrite Module server variables:

*   CONTENT_LENGTH
*   CONTENT_TYPE
*   HTTP_ACCEPT
*   HTTP_CONNECTION
*   HTTP_COOKIE
*   HTTP_HOST
*   HTTP_REFERER
*   HTTP_URL
*   HTTP_USER_AGENT
*   HTTPS
*   LOCAL_ADDR
*   QUERY_STRING
*   REMOTE_ADDR
*   REMOTE_PORT
*   REQUEST_FILENAME
*   REQUEST_URI

Note

You can also obtain an [IFileProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.fileproviders.ifileprovider) via a [PhysicalFileProvider](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.fileproviders.physicalfileprovider). This approach may provide greater flexibility for the location of your rewrite rules files. Make sure that your rewrite rules files are deployed to the server at the path you provide.

```
PhysicalFileProvider fileProvider = new PhysicalFileProvider(Directory.GetCurrentDirectory());
```

Use [Add](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.add) to implement your own rule logic in a method. `Add` exposes the [RewriteContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewritecontext), which makes available the [HttpContext](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext) for use in your method. The [RewriteContext.Result](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewritecontext.result) determines how additional pipeline processing is handled. Set the value to one of the [RuleResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.ruleresult) fields described in the following table.

| Rewrite context result | Action |
| --- | --- |
| `RuleResult.ContinueRules` (default) | Continue applying rules. |
| `RuleResult.EndResponse` | Stop applying rules and send the response. |
| `RuleResult.SkipRemainingRules` | Stop applying rules and send the context to the next middleware. |

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

The sample app demonstrates a method that redirects requests for paths that end with `.xml`. If a request is made for `/file.xml`, the request is redirected to `/xmlfiles/file.xml`. The status code is set to `301 - Moved Permanently`. When the browser makes a new request for `/xmlfiles/file.xml`, Static File Middleware serves the file to the client from the _wwwroot/xmlfiles_ folder. For a redirect, explicitly set the status code of the response. Otherwise, a _200 - OK_ status code is returned, and the redirect doesn't occur on the client.

`RewriteRules.cs`:

```
public static void RedirectXmlFileRequests(RewriteContext context)
{
    var request = context.HttpContext.Request;

    // Because the client is redirecting back to the same app, stop 
    // processing if the request has already been redirected.
    if (request.Path.StartsWithSegments(new PathString("/xmlfiles")))
    {
        return;
    }

    if (request.Path.Value.EndsWith(".xml", StringComparison.OrdinalIgnoreCase))
    {
        var response = context.HttpContext.Response;
        response.StatusCode = (int) HttpStatusCode.MovedPermanently;
        context.Result = RuleResult.EndResponse;
        response.Headers[HeaderNames.Location] = 
            "/xmlfiles" + request.Path + request.QueryString;
    }
}
```

This approach can also rewrite requests. The sample app demonstrates rewriting the path for any text file request to serve the _file.txt_ text file from the _wwwroot_ folder. Static File Middleware serves the file based on the updated request path:

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

`RewriteRules.cs`:

```
public static void RewriteTextFileRequests(RewriteContext context)
{
    var request = context.HttpContext.Request;

    if (request.Path.Value.EndsWith(".txt", StringComparison.OrdinalIgnoreCase))
    {
        context.Result = RuleResult.SkipRemainingRules;
        request.Path = "/file.txt";
    }
}
```

Use [Add](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.rewriteoptionsextensions.add) to use rule logic in a class that implements the [IRule](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.irule) interface. `IRule` provides greater flexibility over using the method-based rule approach. Your implementation class may include a constructor that allows you can pass in parameters for the [ApplyRule](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.rewrite.irule.applyrule) method.

```
public void Configure(IApplicationBuilder app)
{
    using (StreamReader apacheModRewriteStreamReader = 
        File.OpenText("ApacheModRewrite.txt"))
    using (StreamReader iisUrlRewriteStreamReader = 
        File.OpenText("IISUrlRewrite.xml")) 
    {
        var options = new RewriteOptions()
            .AddRedirect("redirect-rule/(.*)", "redirected/$1")
            .AddRewrite(@"^rewrite-rule/(\d+)/(\d+)", "rewritten?var1=$1&var2=$2", 
                skipRemainingRules: true)
            .AddApacheModRewrite(apacheModRewriteStreamReader)
            .AddIISUrlRewrite(iisUrlRewriteStreamReader)
            .Add(MethodRules.RedirectXmlFileRequests)
            .Add(MethodRules.RewriteTextFileRequests)
            .Add(new RedirectImageRequests(".png", "/png-images"))
            .Add(new RedirectImageRequests(".jpg", "/jpg-images"));

        app.UseRewriter(options);
    }

    app.UseStaticFiles();

    app.Run(context => context.Response.WriteAsync(
        $"Rewritten or Redirected Url: " +
        $"{context.Request.Path + context.Request.QueryString}"));
}
```

The values of the parameters in the sample app for the `extension` and the `newPath` are checked to meet several conditions. The `extension` must contain a value, and the value must be `.png`, `.jpg`, or _.gif_. If the `newPath` isn't valid, an [ArgumentException](https://learn.microsoft.com/en-us/dotnet/api/system.argumentexception) is thrown. If a request is made for `image.png`, the request is redirected to `/png-images/image.png`. If a request is made for `image.jpg`, the request is redirected to `/jpg-images/image.jpg`. The status code is set to `301 - Moved Permanently`, and the `context.Result` is set to stop processing rules and send the response.

```
public class RedirectImageRequests : IRule
{
    private readonly string _extension;
    private readonly PathString _newPath;

    public RedirectImageRequests(string extension, string newPath)
    {
        if (string.IsNullOrEmpty(extension))
        {
            throw new ArgumentException(nameof(extension));
        }

        if (!Regex.IsMatch(extension, @"^\.(png|jpg|gif)$"))
        {
            throw new ArgumentException("Invalid extension", nameof(extension));
        }

        if (!Regex.IsMatch(newPath, @"(/[A-Za-z0-9]+)+?"))
        {
            throw new ArgumentException("Invalid path", nameof(newPath));
        }

        _extension = extension;
        _newPath = new PathString(newPath);
    }

    public void ApplyRule(RewriteContext context)
    {
        var request = context.HttpContext.Request;

        // Because we're redirecting back to the same app, stop 
        // processing if the request has already been redirected
        if (request.Path.StartsWithSegments(new PathString(_newPath)))
        {
            return;
        }

        if (request.Path.Value.EndsWith(_extension, StringComparison.OrdinalIgnoreCase))
        {
            var response = context.HttpContext.Response;
            response.StatusCode = (int) HttpStatusCode.MovedPermanently;
            context.Result = RuleResult.EndResponse;
            response.Headers[HeaderNames.Location] = 
                _newPath + request.Path + request.QueryString;
        }
    }
}
```

Original Request: `/image.png`

![Image 22: For image.png: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect_png_requests.png?view=aspnetcore-10.0)

Original Request: `/image.jpg`

![Image 23: For image.jpg: Browser window with developer tools tracking the requests and responses](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/url-rewriting/_static/add_redirect_jpg_requests.png?view=aspnetcore-10.0)

| Goal | Regex String & Match Example | Replacement String & Output Example |
| --- | --- | --- |
| Rewrite path into querystring | `^path/(.*)/(.*)` `/path/abc/123` | `path?var1=$1&var2=$2` `/path?var1=abc&var2=123` |
| Strip trailing slash | `(.*)/$` `/path/` | `$1` `/path` |
| Enforce trailing slash | `(.*[^/])$` `/path` | `$1/` `/path/` |
| Avoid rewriting specific requests | `^(.*)(?<!\.axd)$` or `^(?!.*\.axd$)(.*)$` Yes: `/resource.htm` No: `/resource.axd` | `rewritten/$1` `/rewritten/resource.htm` `/resource.axd` |
| Rearrange URL segments | `path/(.*)/(.*)/(.*)` `path/1/2/3` | `path/$3/$2/$1` `path/3/2/1` |
| Replace a URL segment | `^(.*)/segment2/(.*)` `/segment1/segment2/segment3` | `$1/replaced/$2` `/segment1/replaced/segment3` |

*   [View or download sample code](https://github.com/dotnet/AspNetCore.Docs/tree/main/aspnetcore/fundamentals/url-rewriting/samples/) ([how to download](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/?view=aspnetcore-10.0#how-to-download-a-sample))
*   [`RewriteMiddleware` (reference source)](https://github.com/dotnet/aspnetcore/blob/main/src/Middleware/Rewrite/src/RewriteMiddleware.cs)
*   [App startup in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/startup?view=aspnetcore-10.0)
*   [ASP.NET Core Middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0)
*   [Regular expressions in .NET](https://learn.microsoft.com/en-us/dotnet/articles/standard/base-types/regular-expressions)
*   [Regular expression language - quick reference](https://learn.microsoft.com/en-us/dotnet/articles/standard/base-types/quick-ref)
*   [Apache mod_rewrite](https://httpd.apache.org/docs/2.4/rewrite/)
*   [Using Url Rewrite Module 2.0 (for IIS)](https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/using-url-rewrite-module-20)
*   [URL Rewrite Module Configuration Reference](https://learn.microsoft.com/en-us/iis/extensions/url-rewrite-module/url-rewrite-module-configuration-reference)
*   [Keep a simple URL structure](https://support.google.com/webmasters/answer/76329?hl=en)
*   [10 URL Rewriting Tips and Tricks](https://ruslany.net/2009/04/10-url-rewriting-tips-and-tricks/)
*   [To slash or not to slash](https://webmasters.googleblog.com/2010/04/to-slash-or-not-to-slash.html)
