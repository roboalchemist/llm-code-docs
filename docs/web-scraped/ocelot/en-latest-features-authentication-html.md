# Source: https://ocelot.readthedocs.io/en/latest/features/authentication.html

Title: Authentication — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/authentication.html

Markdown Content:
In order to authenticate routes and subsequently use any of Ocelot’s claims based features such as authorization or modifying the request with values from the token, users must register authentication services in their [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs) as usual but they provide a [scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/#authentication-scheme) (authentication provider key) with each registration e.g.

const string AuthenticationProviderKey = "MyKey"; // aka scheme
builder.Services
 .AddAuthentication()
 .AddJwtBearer(AuthenticationProviderKey, options =>
 {
 // authentication setup via options initialization
 });

In this example, `MyKey` is the [scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/#authentication-scheme) with which this provider has been registered, but for JWT bearer authentication, the scheme is usually `Bearer`. We then map this to a route in the configuration using the following [AuthenticationOptions Schema](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-options-schema) options:

*   `AuthenticationProviderKey` is a string, the legacy definition of [Single Authentication Scheme](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-scheme).

*   `AuthenticationProviderKeys` is an array of strings, the recommended definition of [Multiple Authentication Schemes](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-multiple) feature.

`AuthenticationOptions` Schema[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authenticationoptions-schema "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------

The following is the full _authentication_ configuration, used in both the [Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-route-schema) and the [Dynamic Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-dynamic-route-schema). Not all of these options need to be configured; however, the `AuthenticationProviderKeys` option is mandatory when `AuthenticationProviderKey` is absent.

"AuthenticationOptions": {
 "AllowAnonymous": false, // nullable boolean
 "AllowedScopes": [], // array of strings
 "AuthenticationProviderKey": "", // deprecated! -> use AuthenticationProviderKeys
 "AuthenticationProviderKeys": [] // array of strings
}

| _Option_ | _Description_ |
| --- | --- |
| `AllowAnonymous` | Excludes a route from global _authentication options_ by setting it to `true`. If the global option disables authentication by forcibly having a `true` value, then at the route level the option can include a route to be authenticated by setting it to `false`. For more details, refer to the “[Configuration and AllowAnonymous](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-configuration)” section. |
| `AllowedScopes` | If specified, enables authorization based on the `scope` claim after successful authentication by a configured authentication provider. For more details, refer to the “[Allowed Scopes](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-allowed-scopes)” section. |
| `AuthenticationProviderKey` | Maps a configured authentication provider, identified by a key (scheme), to a route that requires authentication. _Note: This option is deprecated—see the warning below._ For more details, refer to the “[Single Authentication Scheme](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-scheme)” section. |
| `AuthenticationProviderKeys` | Maps all configured authentication providers, identified by their schemes, to a route that requires authentication. For more details, refer to the “[Multiple Authentication Schemes](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-multiple)” section. |

Warning

The `AuthenticationProviderKey` option is deprecated in version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0)! Use the `AuthenticationProviderKeys` array option instead. Note that `AuthenticationProviderKey` will be removed in version [25.0](https://github.com/ThreeMammals/Ocelot/milestone/13). For backward compatibility in version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), the `AuthenticationProviderKey` option takes precedence over the schemes in the `AuthenticationProviderKeys` array. If the `AuthenticationProviderKey` scheme provider fails, the remaining schemes in the `AuthenticationProviderKeys` array will enforce the appropriate authentication providers in the specified order.

Single Authentication Scheme [[1]](https://ocelot.readthedocs.io/en/latest/features/authentication.html#f1)[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#single-authentication-scheme "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Option: `AuthenticationProviderKey`

We map authentication provider to a Route in the configuration e.g.

"AuthenticationOptions": {
 "AuthenticationProviderKey": "MyKey",
 "AllowedScopes": []
}

When Ocelot runs it will look at this routes `AuthenticationProviderKey` and check that there is an authentication provider registered with the given key. If there isn’t then Ocelot will not start up. If there is then the route will use that provider when it executes.

If a route is authenticated, Ocelot will invoke whatever scheme is associated with it while executing the authentication middleware. If the request fails authentication, Ocelot returns a HTTP status code [401 Unauthorized](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/401).

Multiple Authentication Schemes [[2]](https://ocelot.readthedocs.io/en/latest/features/authentication.html#f2)[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#multiple-authentication-schemes "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

> Option: `AuthenticationProviderKeys`

In the real world of ASP.NET Core, apps may need to support multiple types of authentication by a single Ocelot app instance. To register [multiple authentication schemes](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme#use-multiple-authentication-schemes) ([authentication provider keys](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20AuthenticationProviderKey&type=code)) for each appropriate authentication provider, use and develop this abstract configuration of two or more schemes:

var DefaultScheme = JwtBearerDefaults.AuthenticationScheme; // Bearer
builder.Services
 .AddAuthentication()
 .AddJwtBearer(DefaultScheme, options => { /* JWT setup */ })
 // AddJwtBearer, AddCookie, AddIdentityServerAuthentication etc.
 .AddMyProvider("MyKey", options => { /* Custom auth setup */ });

In this example, the `MyKey` and `Bearer` schemes represent the keys with which these providers were registered. We then map these schemes to a route in the configuration as shown below.

"AuthenticationOptions": {
 "AuthenticationProviderKeys": [ "Bearer", "MyKey" ] // The order matters!
 "AllowedScopes": []
}

Afterward, Ocelot applies all steps that are specified for `AuthenticationProviderKey` as [Single Authentication Scheme](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-scheme). The order of the keys in an array definition does matter! We use a “First One Wins” authentication strategy.

Configuration and `AllowAnonymous`[[3]](https://ocelot.readthedocs.io/en/latest/features/authentication.html#f3)[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#configuration-and-allowanonymous "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To configure _authentication options_ uniformly across all static routes, define them in `GlobalConfiguration` section using the [AuthenticationOptions Schema](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-options-schema). If _authentication options_ are specified in both `GlobalConfiguration` and a route (i.e., `AuthenticationProviderKey` or `AuthenticationProviderKeys` are set), the route-level configuration takes precedence.

Excluding a route from global _authentication options_ is possible by setting `AllowAnonymous` option to `true`. This prevents the route from requiring authentication, keeping it open and anonymous.

In the following example:

*   The first route is authenticated using the `MyGlobalKey` provider’s scheme.

*   The second route uses the `MyKey` provider’s scheme.

*   The third route is not authenticated.

"Routes": [
 {
 // route #1 props...
 "AuthenticationOptions": {} },
 {
 // route #2 props...
 "AuthenticationOptions": { "AuthenticationProviderKeys": [ "MyKey" ], "AllowedScopes": [ "Bob" ] } },
 {
 // route #3 props...
 "AuthenticationOptions": { "AllowAnonymous": true } }
],
"GlobalConfiguration": {
 "BaseUrl": "http://ocelot.net",
 "AuthenticationOptions": { "RouteKeys": [], // empty -> no grouping, thus opts will apply to all routes "AuthenticationProviderKeys": [ "MyGlobalKey" ], "AllowedScopes": [ "Admin" ] }}

> **Note**: Ocelot performs a per-option merging algorithm to combine route and global `AuthenticationOptions`. If global `AuthenticationProviderKeys` are defined together with global `AllowedScopes`, then route options should be specified as a pair of scheme and scopes; otherwise, a scope should not belong to the global authentication provider. Moreover, the route scopes array entirely overrides the global scopes array, so the two collections are not merged but rather interchangeable.

Global Configuration [[4]](https://ocelot.readthedocs.io/en/latest/features/authentication.html#f4)[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#global-configuration "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Since the global configuration for static routes has already been described above, here are additional details regarding dynamic routes, whose configuration was not supported in versions prior to [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0). Starting with version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global and route _authentication options_ for [Dynamic Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-dynamic) were introduced. These global options may also be overridden in the `DynamicRoutes` configuration section, as defined by the [Dynamic Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-dynamic-route-schema).

{
 "DynamicRoutes": [
 {
 "Key": "R1", // optional
 "ServiceName": "my-service",
 "AuthenticationOptions": { "AuthenticationProviderKeys": ["MyKey"], // custom authentication provider "AllowedScopes": ["my-service"] // require authorization with a 'scope' claim set to the value 'my-service' } }
 ],
 "GlobalConfiguration": {
 "BaseUrl": "https://ocelot.net",
 "DownstreamScheme": "http",
 "ServiceDiscoveryProvider": {
 // required section for dynamic routing
 },
 "AuthenticationOptions": { "RouteKeys": [], // or null, no grouping, thus opts apply to all dynamic routes "AuthenticationProviderKeys": ["Bearer"], // use a global JWT bearer auth provider for all discovered services "AllowedScopes": ["oc-admin"] // require the global 'scope' claim to gain access to all discovered services } }
}

In this configuration, an `oc-admin` scope authorization is applied to all implicit dynamic routes by the global `Bearer` JWT signing service. However, for the “my-service” service, authorization with the `my-service` scope is applied, and authentication is provided by another source of tokens named `MyKey`.

Note

1. If the `RouteKeys` option is not defined or the array is empty in the global `AuthenticationOptions`, the global options will apply to all routes. If the array contains route keys, it defines a single group of routes to which the global options apply. Routes excluded from this group must specify their own route-level `AuthenticationOptions`.

2. Prior to version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global and dynamic route `AuthenticationOptions` were not available. Starting with version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global configuration is supported for both static and dynamic routes.

Allowed Scopes[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#allowed-scopes "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------

> Option: `AllowedScopes`

To set up authorization by scopes from the `AllowedScopes` collection, after successful authentication by the middleware and after claims have been transformed, the authorization middleware in Ocelot retrieves all user claims (from the token) of the ‘`scope`’ type and ensures that the user has at least one of the scopes in the list. This provides a way to restrict access to a route on a per-scope basis.

Note

[[5]](https://ocelot.readthedocs.io/en/latest/features/authentication.html#f5) Depending on the authentication provider, incoming tokens embed the ‘`scope`’ claim value in the body either as an array or as a single space-separated string of multiple values. For instance, [Identity Server Bearer Tokens](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-identity-server) use an array, whereas most [JWT Tokens](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-jwt-tokens) providers generate a space-separated list of scopes, in accordance with [RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693), as stated in section “[4.2. “scope” (Scopes) Claim](https://datatracker.ietf.org/doc/html/rfc8693#name-scope-scopes-claim)”. Since version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), Ocelot supports [RFC 8693](https://datatracker.ietf.org/doc/html/rfc8693) (OAuth 2.0 Token Exchange) for the `scope` claim in the `ScopesAuthorizer` service, also known as the `IScopesAuthorizer` service in the DI container.

Note

Starting with version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), specifying global _allowed scopes_ is exclusively supported. Be cautious when overriding the global `AllowedScopes` array with a route-level `AllowedScopes` array; a combination of the route scheme (`AuthenticationProviderKeys` array) and its _allowed scopes_ might be required, since new _allowed scopes_ could belong to another authentication provider’s security model. For more details, refer to the “[Configuration and AllowAnonymous](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-configuration)” and “[Global Configuration](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-global-configuration)” sections.

JWT Tokens[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#jwt-tokens "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

If you want to authenticate using JWT tokens maybe from a provider like [Auth0](https://auth0.com/), you can register your authentication middleware as normal e.g.

builder.Services
 .AddAuthentication()
 .AddJwtBearer("Auth0", options =>
 {
 options.Authority = "test";
 options.Audience = "test";
 });
builder.Services
 .AddOcelot(builder.Configuration);

Then map the authentication provider key to a route in your configuration e.g.

"AuthenticationOptions": {
 "AuthenticationProviderKeys": ["Auth0"],
}

**JWT Tokens Docs**

> *   Microsoft Learn: [Authentication and authorization in minimal APIs](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/minimal-apis/security)
> 
> *   Andrew Lock | .NET Escapades: [A look behind the JWT bearer authentication middleware in ASP.NET Core](https://andrewlock.net/a-look-behind-the-jwt-bearer-authentication-middleware-in-asp-net-core/)

Identity Server Bearer Tokens[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-identity-server "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to use [IdentityServer](https://github.com/IdentityServer) bearer tokens, register your IdentityServer services as usual in [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs) with a [scheme](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/#authentication-scheme) (key). If you don’t understand how to do this, please consult the IdentityServer [documentation](https://identityserver4.readthedocs.io/).

Action<JwtBearerOptions> options = o =>
{
 o.Authority = "https://whereyouridentityserverlives.com";
 // ...
};
builder.Services
 .AddAuthentication()
 .AddJwtBearer("IS4", options);
builder.Services
 .AddOcelot(builder.Configuration);

Then map the authentication provider key to a route in your configuration e.g.

"AuthenticationOptions": {
 "AuthenticationProviderKeys": ["IS4"],
}

Auth0 by Okta[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#auth0-by-okta "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

Yet another identity provider by [Okta](https://www.okta.com/), see [Auth0 Developer Resources](https://developer.auth0.com/).

Add the following, at minimum, to your startup [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs):

builder.Services
 .AddAuthentication()
 .AddJwtBearer("Okta", o =>
 {
 var conf = builder.Configuration;
 o.Audience = conf["Authentication:Okta:Audience"]; // Okta Authorization server Audience
 o.Authority = conf["Authentication:Okta:Server"]; // Okta Authorization Issuer URI URL e.g. https://{subdomain}.okta.com/oauth2/{authidentifier}
 });
builder.Services
 .AddOcelot(builder.Configuration);

var app = builder.Build();
await app
 .UseAuthentication()
 .UseOcelot();
await app.RunAsync();

In order to get Ocelot to view the scope claim from Okta properly, you have to add the following to map the default Okta `scp` claim to `scope`:

// Map Okta "scp" to "scope" claims instead of http://schemas.microsoft.com/identity/claims/scope to allow Ocelot to read/verify them
JsonWebTokenHandler.DefaultInboundClaimTypeMap.Remove("scp");
JsonWebTokenHandler.DefaultInboundClaimTypeMap.Add("scp", "scope");

**Okta Notes**

> 1.   Issue [446](https://github.com/ThreeMammals/Ocelot/issues/446) contains some code and examples that might help with Okta integration.
> 
> 2.   Here is documentation for better clarity on claims mapping: [Mapping, customizing, and transforming claims in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/claims?view=aspnetcore-9.0).
> 
> 3.   It is highly advisable to read and understand the [Warnings](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-warnings) related to the critical changes in authentication when utilizing .NET 8.

Warnings[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#warnings "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

Warning

.NET 8 introduced a breaking change where `JwtSecurityToken` was replaced with `JsonWebToken` to enhance performance and reliability. Consequently, their handlers were changed `JwtSecurityTokenHandler` to `JsonWebTokenHandler`. For a complete understanding of .NET 8 breaking change related to JWT tokens, please refer to the Microsoft Learn documentation: “[Security token events return a JsonWebToken](https://learn.microsoft.com/en-us/dotnet/core/compatibility/aspnet-core/8.0/securitytoken-events)”.

Links[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#links "Link to this heading")
-----------------------------------------------------------------------------------------------------------

*   Microsoft Learn: [Overview of ASP.NET Core authentication](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/)

*   Microsoft Learn: [Authorize with a specific scheme in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authorization/limitingidentitybyscheme)

*   Microsoft Learn: [Policy schemes in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/policyschemes)

*   Microsoft Learn: [Mapping, customizing, and transforming claims in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/security/authentication/claims?view=aspnetcore-9.0)

*   Microsoft .NET Blog: [ASP.NET Core Authentication with IdentityServer4](https://devblogs.microsoft.com/dotnet/asp-net-core-authentication-with-identityserver4/)

Roadmap[¶](https://ocelot.readthedocs.io/en/latest/features/authentication.html#roadmap "Link to this heading")
---------------------------------------------------------------------------------------------------------------

Nothing is currently in the stack, but the Ocelot team is rethinking a new version of the “[Administration](https://ocelot.readthedocs.io/en/latest/features/administration.html)” feature, which is closely dependent on authentication.

We invite you to add more examples if you have integrated with other identity providers and the integration solution is working. Please open a “[Show and tell](https://github.com/ThreeMammals/Ocelot/discussions/categories/show-and-tell)” discussion in the repository.

* * *
