# Source: https://learn.microsoft.com/en-us/aspnet/core/security/authentication/?view=aspnetcore-10.0

Title: Overview of ASP.NET Core Authentication

URL Source: https://learn.microsoft.com/en-us/aspnet/core/security/authentication/?view=aspnetcore-10.0

Markdown Content:
By [Mike Rousos](https://github.com/mjrousos)

Authentication is the process of determining a user's identity. [Authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/introduction?view=aspnetcore-10.0) is the process of determining whether a user has access to a resource. In ASP.NET Core, authentication is handled by the authentication service, [IAuthenticationService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.iauthenticationservice), which is used by authentication [middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0). The authentication service uses registered authentication handlers to complete authentication-related actions. Examples of authentication-related actions include:

*   Authenticating a user.
*   Responding when an unauthenticated user tries to access a restricted resource.

The registered authentication handlers and their configuration options are called "schemes".

Authentication schemes are specified by registering authentication services in `Program.cs`:

*   By calling a scheme-specific extension method after a call to [AddAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.authenticationservicecollectionextensions.addauthentication), such as [AddJwtBearer](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.jwtbearerextensions.addjwtbearer) or [AddCookie](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.cookieextensions.addcookie). These extension methods use [AuthenticationBuilder.AddScheme](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationbuilder.addscheme) to register schemes with appropriate settings.
*   Less commonly, by calling `AuthenticationBuilder.AddScheme` directly.

For example, the following code registers authentication services and handlers for cookie and JWT bearer authentication schemes:

```
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(JwtBearerDefaults.AuthenticationScheme,
        options => builder.Configuration.Bind("JwtSettings", options))
    .AddCookie(CookieAuthenticationDefaults.AuthenticationScheme,
        options => builder.Configuration.Bind("CookieSettings", options));
```

The `AddAuthentication` parameter [JwtBearerDefaults.AuthenticationScheme](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.jwtbearer.jwtbearerdefaults.authenticationscheme#microsoft-aspnetcore-authentication-jwtbearer-jwtbearerdefaults-authenticationscheme) is the name of the scheme to use by default when a specific scheme isn't requested.

If multiple schemes are used, authorization policies (or authorization attributes) can [specify the authentication scheme (or schemes)](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0) they depend on to authenticate the user. In the example above, the cookie authentication scheme could be used by specifying its name ([CookieAuthenticationDefaults.AuthenticationScheme](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.cookies.cookieauthenticationdefaults.authenticationscheme#microsoft-aspnetcore-authentication-cookies-cookieauthenticationdefaults-authenticationscheme) by default, though a different name could be provided when calling `AddCookie`).

In some cases, the call to `AddAuthentication` is automatically made by other extension methods. For example, when using [ASP.NET Core Identity](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-10.0), `AddAuthentication` is called internally.

The Authentication middleware is added in `Program.cs` by calling [UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication). Calling `UseAuthentication` registers the middleware that uses the previously registered authentication schemes. Call `UseAuthentication` before any middleware that depends on users being authenticated.

Authentication is responsible for providing the [ClaimsPrincipal](https://learn.microsoft.com/en-us/dotnet/api/system.security.claims.claimsprincipal) for authorization to make permission decisions against. There are multiple authentication scheme approaches to select which authentication handler is responsible for generating the correct set of claims:

*   [Authentication scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/?view=aspnetcore-10.0#authentication-scheme)
*   The default authentication scheme, discussed in the next two sections.
*   Directly set [HttpContext.User](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext.user#microsoft-aspnetcore-http-httpcontext-user).

When there is only a single authentication scheme registered, it becomes the default scheme. If multiple schemes are registered and the default scheme isn't specified, a scheme must be specified in the authorize attribute, otherwise, the following error is thrown:

> InvalidOperationException: No authenticationScheme was specified, and there was no DefaultAuthenticateScheme found. The default schemes can be set using either AddAuthentication(string defaultScheme) or AddAuthentication(Action<AuthenticationOptions> configureOptions).

When there is only a single authentication scheme registered, the single authentication scheme:

*   Is automatically used as the [DefaultScheme](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationoptions.defaultscheme#microsoft-aspnetcore-authentication-authenticationoptions-defaultscheme).
*   Eliminates the need to specify the `DefaultScheme` in [AddAuthentication(IServiceCollection)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.authenticationservicecollectionextensions.addauthentication#microsoft-extensions-dependencyinjection-authenticationservicecollectionextensions-addauthentication(microsoft-extensions-dependencyinjection-iservicecollection)) or [AddAuthenticationCore(IServiceCollection)](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.authenticationcoreservicecollectionextensions.addauthenticationcore#microsoft-extensions-dependencyinjection-authenticationcoreservicecollectionextensions-addauthenticationcore(microsoft-extensions-dependencyinjection-iservicecollection)).

To disable automatically using the single authentication scheme as the `DefaultScheme`, call `AppContext.SetSwitch("Microsoft.AspNetCore.Authentication.SuppressAutoDefaultScheme")`.

The [authentication scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0) can select which authentication handler is responsible for generating the correct set of claims. For more information, see [Authorize with a specific scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0).

An authentication scheme is a name that corresponds to:

*   An authentication handler.
*   Options for configuring that specific instance of the handler.

Schemes are useful as a mechanism for referring to the authentication, challenge, and forbid behaviors of the associated handler. For example, an authorization policy can use scheme names to specify which authentication scheme (or schemes) should be used to authenticate the user. When configuring authentication, it's common to specify the default authentication scheme. The default scheme is used unless a resource requests a specific scheme. It's also possible to:

*   Specify different default schemes to use for authenticate, challenge, and forbid actions.
*   Combine multiple schemes into one using [policy schemes](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/policyschemes?view=aspnetcore-10.0).

An authentication handler:

*   Is a type that implements the behavior of a scheme.
*   Is derived from [IAuthenticationHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.iauthenticationhandler) or [AuthenticationHandler<TOptions>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhandler-1).
*   Has the primary responsibility to authenticate users.

Based on the authentication scheme's configuration and the incoming request context, authentication handlers:

*   Construct [AuthenticationTicket](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationticket) objects representing the user's identity if authentication is successful.
*   Return 'no result' or 'failure' if authentication is unsuccessful.
*   Have methods for challenge and forbid actions for when users attempt to access resources: 
    *   They're unauthorized to access (forbid).
    *   When they're unauthenticated (challenge).

[RemoteAuthenticationHandler<TOptions>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.remoteauthenticationhandler-1) is the class for authentication that requires a remote authentication step. When the remote authentication step is finished, the handler calls back to the `CallbackPath` set by the handler. The handler finishes the authentication step using the information passed to the [HandleRemoteAuthenticateAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.twitter.twitterhandler.handleremoteauthenticateasync) callback path. [OAuth 2.0](https://oauth.net/2/) and [OIDC](https://openid.net/developers/how-connect-works/) both use this pattern. JWT and cookies don't since they can directly use the bearer header and cookie to authenticate. The remotely hosted provider in this case:

*   Is the authentication provider.
*   Examples include [Facebook](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/facebook-logins?view=aspnetcore-10.0), [Twitter](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/twitter-logins?view=aspnetcore-10.0), [Google](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/google-logins?view=aspnetcore-10.0), [Microsoft](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/microsoft-logins?view=aspnetcore-10.0), and any other OIDC provider that handles authenticating users using the handlers mechanism.

An authentication scheme's authenticate action is responsible for constructing the user's identity based on request context. It returns an [AuthenticateResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticateresult) indicating whether authentication was successful and, if so, the user's identity in an authentication ticket. See [AuthenticateAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhttpcontextextensions.authenticateasync). Authenticate examples include:

*   A cookie authentication scheme constructing the user's identity from cookies.
*   A JWT bearer scheme deserializing and validating a JWT bearer token to construct the user's identity.

An authentication challenge is invoked by Authorization when an unauthenticated user requests an endpoint that requires authentication. An authentication challenge is issued, for example, when an anonymous user requests a restricted resource or follows a login link. Authorization invokes a challenge using the specified authentication schemes, or the default if none is specified. See [ChallengeAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhttpcontextextensions.challengeasync). Authentication challenge examples include:

*   A cookie authentication scheme redirecting the user to a login page.
*   A JWT bearer scheme returning a 401 result with a `www-authenticate: bearer` header.

A challenge action should let the user know what authentication mechanism to use to access the requested resource.

An authentication scheme's forbid action is called by Authorization when an authenticated user attempts to access a resource they're not permitted to access. See [ForbidAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhttpcontextextensions.forbidasync). Authentication forbid examples include:

*   A cookie authentication scheme redirecting the user to a page indicating access was forbidden.
*   A JWT bearer scheme returning a 403 result.
*   A custom authentication scheme redirecting to a page where the user can request access to the resource.

A forbid action can let the user know:

*   They're authenticated.
*   They're not permitted to access the requested resource.

See the following links for differences between challenge and forbid:

*   [Challenge and forbid with an operational resource handler](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/resourcebased?view=aspnetcore-10.0#challenge-and-forbid-with-an-operational-resource-handler).
*   [Differences between challenge and forbid](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/secure-data?view=aspnetcore-10.0#challenge).

ASP.NET Core doesn't have a built-in solution for multi-tenant authentication. While it's possible for customers to write one using the built-in features, we recommend customers consider [Orchard Core](https://www.orchardcore.net/), [ABP Framework](https://abp.io/), or [Finbuckle.MultiTenant](https://www.finbuckle.com/multitenant) for multi-tenant authentication.

Orchard Core is:

*   An open-source, modular, and multi-tenant app framework built with ASP.NET Core.
*   A content management system (CMS) built on top of that app framework.

See the [Orchard Core](https://github.com/OrchardCMS/OrchardCore) source for an example of authentication providers per tenant.

[ABP Framework](https://abp.io/) supports various architectural patterns including modularity, microservices, domain driven design, and multi-tenancy. See [ABP Framework source on GitHub](https://github.com/abpframework/abp).

Finbuckle.MultiTenant:

*   Open source
*   Provides tenant resolution
*   Lightweight
*   Provides data isolation
*   Configure app behavior uniquely for each tenant

*   [Authorize with a specific scheme in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0)
*   [Policy schemes in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/policyschemes?view=aspnetcore-10.0)
*   [Create an ASP.NET Core app with user data protected by authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/secure-data?view=aspnetcore-10.0)
*   [Globally require authenticated users](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/secure-data?view=aspnetcore-10.0#require-authenticated-users)
*   [GitHub issue on using multiple authentication schemes](https://github.com/dotnet/aspnetcore/issues/26002)

By [Mike Rousos](https://github.com/mjrousos)

Authentication is the process of determining a user's identity. [Authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/introduction?view=aspnetcore-10.0) is the process of determining whether a user has access to a resource. In ASP.NET Core, authentication is handled by the authentication service, [IAuthenticationService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.iauthenticationservice), which is used by authentication [middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0). The authentication service uses registered authentication handlers to complete authentication-related actions. Examples of authentication-related actions include:

*   Authenticating a user.
*   Responding when an unauthenticated user tries to access a restricted resource.

The registered authentication handlers and their configuration options are called "schemes".

Authentication schemes are specified by registering authentication services in `Program.cs`:

*   By calling a scheme-specific extension method after a call to [AddAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.authenticationservicecollectionextensions.addauthentication), such as [AddJwtBearer](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.jwtbearerextensions.addjwtbearer) or [AddCookie](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.cookieextensions.addcookie). These extension methods use [AuthenticationBuilder.AddScheme](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationbuilder.addscheme) to register schemes with appropriate settings.
*   Less commonly, by calling `AuthenticationBuilder.AddScheme` directly.

For example, the following code registers authentication services and handlers for cookie and JWT bearer authentication schemes:

```
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(JwtBearerDefaults.AuthenticationScheme,
        options => builder.Configuration.Bind("JwtSettings", options))
    .AddCookie(CookieAuthenticationDefaults.AuthenticationScheme,
        options => builder.Configuration.Bind("CookieSettings", options));
```

The `AddAuthentication` parameter [JwtBearerDefaults.AuthenticationScheme](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.jwtbearer.jwtbearerdefaults.authenticationscheme#microsoft-aspnetcore-authentication-jwtbearer-jwtbearerdefaults-authenticationscheme) is the name of the scheme to use by default when a specific scheme isn't requested.

If multiple schemes are used, authorization policies (or authorization attributes) can [specify the authentication scheme (or schemes)](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0) they depend on to authenticate the user. In the example above, the cookie authentication scheme could be used by specifying its name ([CookieAuthenticationDefaults.AuthenticationScheme](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.cookies.cookieauthenticationdefaults.authenticationscheme#microsoft-aspnetcore-authentication-cookies-cookieauthenticationdefaults-authenticationscheme) by default, though a different name could be provided when calling `AddCookie`).

In some cases, the call to `AddAuthentication` is automatically made by other extension methods. For example, when using [ASP.NET Core Identity](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-10.0), `AddAuthentication` is called internally.

The Authentication middleware is added in `Program.cs` by calling [UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication). Calling `UseAuthentication` registers the middleware that uses the previously registered authentication schemes. Call `UseAuthentication` before any middleware that depends on users being authenticated.

Authentication is responsible for providing the [ClaimsPrincipal](https://learn.microsoft.com/en-us/dotnet/api/system.security.claims.claimsprincipal) for authorization to make permission decisions against. There are multiple authentication scheme approaches to select which authentication handler is responsible for generating the correct set of claims:

*   [Authentication scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/?view=aspnetcore-10.0#authentication-scheme)
*   The default authentication scheme, discussed in the next section.
*   Directly set [HttpContext.User](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext.user#microsoft-aspnetcore-http-httpcontext-user).

There's no automatic probing of schemes. If the default scheme isn't specified, the scheme must be specified in the authorize attribute, otherwise, the following error is thrown:

> InvalidOperationException: No authenticationScheme was specified, and there was no DefaultAuthenticateScheme found. The default schemes can be set using either AddAuthentication(string defaultScheme) or AddAuthentication(Action<AuthenticationOptions> configureOptions).

The [authentication scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0) can select which authentication handler is responsible for generating the correct set of claims. For more information, see [Authorize with a specific scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0).

An authentication scheme is a name that corresponds to:

*   An authentication handler.
*   Options for configuring that specific instance of the handler.

Schemes are useful as a mechanism for referring to the authentication, challenge, and forbid behaviors of the associated handler. For example, an authorization policy can use scheme names to specify which authentication scheme (or schemes) should be used to authenticate the user. When configuring authentication, it's common to specify the default authentication scheme. The default scheme is used unless a resource requests a specific scheme. It's also possible to:

*   Specify different default schemes to use for authenticate, challenge, and forbid actions.
*   Combine multiple schemes into one using [policy schemes](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/policyschemes?view=aspnetcore-10.0).

An authentication handler:

*   Is a type that implements the behavior of a scheme.
*   Is derived from [IAuthenticationHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.iauthenticationhandler) or [AuthenticationHandler<TOptions>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhandler-1).
*   Has the primary responsibility to authenticate users.

Based on the authentication scheme's configuration and the incoming request context, authentication handlers:

*   Construct [AuthenticationTicket](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationticket) objects representing the user's identity if authentication is successful.
*   Return 'no result' or 'failure' if authentication is unsuccessful.
*   Have methods for challenge and forbid actions for when users attempt to access resources: 
    *   They're unauthorized to access (forbid).
    *   When they're unauthenticated (challenge).

[RemoteAuthenticationHandler<TOptions>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.remoteauthenticationhandler-1) is the class for authentication that requires a remote authentication step. When the remote authentication step is finished, the handler calls back to the `CallbackPath` set by the handler. The handler finishes the authentication step using the information passed to the [HandleRemoteAuthenticateAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.twitter.twitterhandler.handleremoteauthenticateasync) callback path. [OAuth 2.0](https://oauth.net/2/) and [OIDC](https://openid.net/developers/how-connect-works/) both use this pattern. JWT and cookies don't since they can directly use the bearer header and cookie to authenticate. The remotely hosted provider in this case:

*   Is the authentication provider.
*   Examples include [Facebook](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/facebook-logins?view=aspnetcore-10.0), [Twitter](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/twitter-logins?view=aspnetcore-10.0), [Google](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/google-logins?view=aspnetcore-10.0), [Microsoft](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/microsoft-logins?view=aspnetcore-10.0), and any other OIDC provider that handles authenticating users using the handlers mechanism.

An authentication scheme's authenticate action is responsible for constructing the user's identity based on request context. It returns an [AuthenticateResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticateresult) indicating whether authentication was successful and, if so, the user's identity in an authentication ticket. See [AuthenticateAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhttpcontextextensions.authenticateasync). Authenticate examples include:

*   A cookie authentication scheme constructing the user's identity from cookies.
*   A JWT bearer scheme deserializing and validating a JWT bearer token to construct the user's identity.

An authentication challenge is invoked by Authorization when an unauthenticated user requests an endpoint that requires authentication. An authentication challenge is issued, for example, when an anonymous user requests a restricted resource or follows a login link. Authorization invokes a challenge using the specified authentication schemes, or the default if none is specified. See [ChallengeAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhttpcontextextensions.challengeasync). Authentication challenge examples include:

*   A cookie authentication scheme redirecting the user to a login page.
*   A JWT bearer scheme returning a 401 result with a `www-authenticate: bearer` header.

A challenge action should let the user know what authentication mechanism to use to access the requested resource.

An authentication scheme's forbid action is called by Authorization when an authenticated user attempts to access a resource they're not permitted to access. See [ForbidAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhttpcontextextensions.forbidasync). Authentication forbid examples include:

*   A cookie authentication scheme redirecting the user to a page indicating access was forbidden.
*   A JWT bearer scheme returning a 403 result.
*   A custom authentication scheme redirecting to a page where the user can request access to the resource.

A forbid action can let the user know:

*   They're authenticated.
*   They're not permitted to access the requested resource.

See the following links for differences between challenge and forbid:

*   [Challenge and forbid with an operational resource handler](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/resourcebased?view=aspnetcore-10.0#challenge-and-forbid-with-an-operational-resource-handler).
*   [Differences between challenge and forbid](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/secure-data?view=aspnetcore-10.0#challenge).

ASP.NET Core doesn't have a built-in solution for multi-tenant authentication. While it's possible for customers to write one using the built-in features, we recommend customers consider [Orchard Core](https://www.orchardcore.net/) or [ABP Framework](https://abp.io/) for multi-tenant authentication.

Orchard Core is:

*   An open-source, modular, and multi-tenant app framework built with ASP.NET Core.
*   A content management system (CMS) built on top of that app framework.

See the [Orchard Core](https://github.com/OrchardCMS/OrchardCore) source for an example of authentication providers per tenant.

[ABP Framework](https://abp.io/) supports various architectural patterns including modularity, microservices, domain driven design, and multi-tenancy. See [ABP Framework source on GitHub](https://github.com/abpframework/abp).

*   [Authorize with a specific scheme in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0)
*   [Policy schemes in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/policyschemes?view=aspnetcore-10.0)
*   [Create an ASP.NET Core app with user data protected by authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/secure-data?view=aspnetcore-10.0)
*   [Globally require authenticated users](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/secure-data?view=aspnetcore-10.0#require-authenticated-users)
*   [GitHub issue on using multiple authentication schemes](https://github.com/dotnet/aspnetcore/issues/26002)

By [Mike Rousos](https://github.com/mjrousos)

Authentication is the process of determining a user's identity. [Authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/introduction?view=aspnetcore-10.0) is the process of determining whether a user has access to a resource. In ASP.NET Core, authentication is handled by the authentication service, [IAuthenticationService](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.iauthenticationservice), which is used by authentication [middleware](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/middleware/?view=aspnetcore-10.0). The authentication service uses registered authentication handlers to complete authentication-related actions. Examples of authentication-related actions include:

*   Authenticating a user.
*   Responding when an unauthenticated user tries to access a restricted resource.

The registered authentication handlers and their configuration options are called "schemes".

Authentication schemes are specified by registering authentication services in `Startup.ConfigureServices`:

*   By calling a scheme-specific extension method after a call to [AddAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.authenticationservicecollectionextensions.addauthentication) (such as [AddJwtBearer](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.jwtbearerextensions.addjwtbearer) or [AddCookie](https://learn.microsoft.com/en-us/dotnet/api/microsoft.extensions.dependencyinjection.cookieextensions.addcookie), for example). These extension methods use [AuthenticationBuilder.AddScheme](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationbuilder.addscheme) to register schemes with appropriate settings.
*   Less commonly, by calling `AuthenticationBuilder.AddScheme` directly.

For example, the following code registers authentication services and handlers for cookie and JWT bearer authentication schemes:

```
services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddJwtBearer(JwtBearerDefaults.AuthenticationScheme,
        options => Configuration.Bind("JwtSettings", options))
    .AddCookie(CookieAuthenticationDefaults.AuthenticationScheme,
        options => Configuration.Bind("CookieSettings", options));
```

The `AddAuthentication` parameter [JwtBearerDefaults.AuthenticationScheme](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.jwtbearer.jwtbearerdefaults.authenticationscheme#microsoft-aspnetcore-authentication-jwtbearer-jwtbearerdefaults-authenticationscheme) is the name of the scheme to use by default when a specific scheme isn't requested.

If multiple schemes are used, authorization policies (or authorization attributes) can [specify the authentication scheme (or schemes)](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0) they depend on to authenticate the user. In the example above, the cookie authentication scheme could be used by specifying its name ([CookieAuthenticationDefaults.AuthenticationScheme](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.cookies.cookieauthenticationdefaults.authenticationscheme#microsoft-aspnetcore-authentication-cookies-cookieauthenticationdefaults-authenticationscheme) by default, though a different name could be provided when calling `AddCookie`).

In some cases, the call to `AddAuthentication` is automatically made by other extension methods. For example, when using [ASP.NET Core Identity](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-10.0), `AddAuthentication` is called internally.

The Authentication middleware is added in `Startup.Configure` by calling [UseAuthentication](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.authappbuilderextensions.useauthentication). Calling `UseAuthentication` registers the middleware that uses the previously registered authentication schemes. Call `UseAuthentication` before any middleware that depends on users being authenticated. When using endpoint routing, the call to `UseAuthentication` must go:

*   After [UseRouting](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.userouting), so that route information is available for authentication decisions.
*   Before [UseEndpoints](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.builder.endpointroutingapplicationbuilderextensions.useendpoints), so that users are authenticated before accessing the endpoints.

Authentication is responsible for providing the [ClaimsPrincipal](https://learn.microsoft.com/en-us/dotnet/api/system.security.claims.claimsprincipal) for authorization to make permission decisions against. There are multiple authentication scheme approaches to select which authentication handler is responsible for generating the correct set of claims:

*   [Authentication scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/?view=aspnetcore-10.0#authentication-scheme)
*   The default authentication scheme, discussed in the next section.
*   Directly set [HttpContext.User](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.http.httpcontext.user#microsoft-aspnetcore-http-httpcontext-user).

There's no automatic probing of schemes. If the default scheme isn't specified, the scheme must be specified in the authorize attribute, otherwise, the following error is thrown:

> InvalidOperationException: No authenticationScheme was specified, and there was no DefaultAuthenticateScheme found. The default schemes can be set using either AddAuthentication(string defaultScheme) or AddAuthentication(Action<AuthenticationOptions> configureOptions).

The [authentication scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0) can select which authentication handler is responsible for generating the correct set of claims. For more information, see [Authorize with a specific scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0).

An authentication scheme is a name that corresponds to:

*   An authentication handler.
*   Options for configuring that specific instance of the handler.

Schemes are useful as a mechanism for referring to the authentication, challenge, and forbid behaviors of the associated handler. For example, an authorization policy can use scheme names to specify which authentication scheme (or schemes) should be used to authenticate the user. When configuring authentication, it's common to specify the default authentication scheme. The default scheme is used unless a resource requests a specific scheme. It's also possible to:

*   Specify different default schemes to use for authenticate, challenge, and forbid actions.
*   Combine multiple schemes into one using [policy schemes](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/policyschemes?view=aspnetcore-10.0).

An authentication handler:

*   Is a type that implements the behavior of a scheme.
*   Is derived from [IAuthenticationHandler](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.iauthenticationhandler) or [AuthenticationHandler<TOptions>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhandler-1).
*   Has the primary responsibility to authenticate users.

Based on the authentication scheme's configuration and the incoming request context, authentication handlers:

*   Construct [AuthenticationTicket](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationticket) objects representing the user's identity if authentication is successful.
*   Return 'no result' or 'failure' if authentication is unsuccessful.
*   Have methods for challenge and forbid actions for when users attempt to access resources: 
    *   They're unauthorized to access (forbid).
    *   When they're unauthenticated (challenge).

[RemoteAuthenticationHandler<TOptions>](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.remoteauthenticationhandler-1) is the class for authentication that requires a remote authentication step. When the remote authentication step is finished, the handler calls back to the `CallbackPath` set by the handler. The handler finishes the authentication step using the information passed to the [HandleRemoteAuthenticateAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.twitter.twitterhandler.handleremoteauthenticateasync) callback path. [OAuth 2.0](https://oauth.net/2/) and [OIDC](https://openid.net/developers/how-connect-works/) both use this pattern. JWT and cookies don't since they can directly use the bearer header and cookie to authenticate. The remotely hosted provider in this case:

*   Is the authentication provider.
*   Examples include [Facebook](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/facebook-logins?view=aspnetcore-10.0), [Twitter](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/twitter-logins?view=aspnetcore-10.0), [Google](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/google-logins?view=aspnetcore-10.0), [Microsoft](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/social/microsoft-logins?view=aspnetcore-10.0), and any other OIDC provider that handles authenticating users using the handlers mechanism.

An authentication scheme's authenticate action is responsible for constructing the user's identity based on request context. It returns an [AuthenticateResult](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticateresult) indicating whether authentication was successful and, if so, the user's identity in an authentication ticket. See [AuthenticateAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhttpcontextextensions.authenticateasync). Authenticate examples include:

*   A cookie authentication scheme constructing the user's identity from cookies.
*   A JWT bearer scheme deserializing and validating a JWT bearer token to construct the user's identity.

An authentication challenge is invoked by Authorization when an unauthenticated user requests an endpoint that requires authentication. An authentication challenge is issued, for example, when an anonymous user requests a restricted resource or follows a login link. Authorization invokes a challenge using the specified authentication schemes, or the default if none is specified. See [ChallengeAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhttpcontextextensions.challengeasync). Authentication challenge examples include:

*   A cookie authentication scheme redirecting the user to a login page.
*   A JWT bearer scheme returning a 401 result with a `www-authenticate: bearer` header.

A challenge action should let the user know what authentication mechanism to use to access the requested resource.

An authentication scheme's forbid action is called by Authorization when an authenticated user attempts to access a resource they're not permitted to access. See [ForbidAsync](https://learn.microsoft.com/en-us/dotnet/api/microsoft.aspnetcore.authentication.authenticationhttpcontextextensions.forbidasync). Authentication forbid examples include:

*   A cookie authentication scheme redirecting the user to a page indicating access was forbidden.
*   A JWT bearer scheme returning a 403 result.
*   A custom authentication scheme redirecting to a page where the user can request access to the resource.

A forbid action can let the user know:

*   They're authenticated.
*   They're not permitted to access the requested resource.

See the following links for differences between challenge and forbid:

*   [Challenge and forbid with an operational resource handler](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/resourcebased?view=aspnetcore-10.0#challenge-and-forbid-with-an-operational-resource-handler).
*   [Differences between challenge and forbid](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/secure-data?view=aspnetcore-10.0#challenge).

ASP.NET Core framework doesn't have a built-in solution for multi-tenant authentication. While it's possible for customers to write an app with multi-tenant authentication, we recommend using one of the following ASP.NET Core application frameworks that support multi-tenant authentication.

[Orchard Core](https://www.orchardcore.net/) is an open-source, modular, and multi-tenant app framework built with ASP.NET Core that also provides a content management system (CMS). See the [Orchard Core](https://github.com/OrchardCMS/OrchardCore) source for an example of authentication providers per tenant.

[ABP Framework](https://abp.io/) supports various architectural patterns including modularity, microservices, domain-driven design, and multi-tenancy. See [ABP Framework source on GitHub](https://github.com/abpframework/abp).

*   [Authorize with a specific scheme in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme?view=aspnetcore-10.0)
*   [Policy schemes in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/policyschemes?view=aspnetcore-10.0)
*   [Create an ASP.NET Core app with user data protected by authorization](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/secure-data?view=aspnetcore-10.0)
*   [Globally require authenticated users](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/secure-data?view=aspnetcore-10.0#require-authenticated-users)
*   [GitHub issue on using multiple authentication schemes](https://github.com/dotnet/aspnetcore/issues/26002)
