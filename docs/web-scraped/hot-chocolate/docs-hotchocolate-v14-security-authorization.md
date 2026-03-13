# Source: https://chillicream.com/docs/hotchocolate/v14/security/authorization

Title: Authorization - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/security/authorization

Markdown Content:
Authorization allows us to determine a user's permissions within our system. We can for example limit access to resources or only allow certain users to execute specific mutations.

Authentication is a prerequisite of Authorization, as we first need to validate a user's "authenticity" before we can evaluate his authorization claims.

[Learn how to setup authentication](https://chillicream.com/docs/hotchocolate/v14/security/authentication)

[](https://chillicream.com/docs/hotchocolate/v14/security/authorization#setup)Setup
-----------------------------------------------------------------------------------

After we have successfully setup authentication, there are only a few things left to do.

1.   Install the `HotChocolate.AspNetCore.Authorization` package

Bash

dotnet add package HotChocolate.AspNetCore.Authorization

Warning

All `HotChocolate.*` packages need to have the same version.

1.   Register the necessary ASP.NET Core services

C#

builder.Services.AddAuthorization();

builder.Services

.AddGraphQLServer()

.AddAuthorization()

.AddQueryType<Query>();

Warning

We need to call `AddAuthorization()` on the `IServiceCollection`, to register the services needed by ASP.NET Core, and on the `IRequestExecutorBuilder` to register the `@authorize` directive and middleware.

1.   Register the ASP.NET Core authorization middleware with the request pipeline by calling `UseAuthorization`

C#

app.UseRouting();

app.UseAuthentication();

app.UseAuthorization();

app.UseEndpoints(endpoints =>

{

endpoints.MapGraphQL();

});

[](https://chillicream.com/docs/hotchocolate/v14/security/authorization#usage)Usage
-----------------------------------------------------------------------------------

At the core of authorization with Hot Chocolate is the `@authorize` directive. It can be applied to fields and types to denote that they require authorization.

In the implementation-first approach we can use the `[Authorize]` attribute to add the `@authorize` directive.

C#

[Authorize]

public class User

{

public string Name { get; set; }

[Authorize]

public Address Address { get; set; }

}

Warning

We need to use the `HotChocolate.Authorization.AuthorizeAttribute` instead of the `Microsoft.AspNetCore.AuthorizationAttribute`.

Specified on a type the `@authorize` directive will be applied to each field of that type. Its authorization logic is executed once for each individual field, depending on whether it was selected by the requestor or not. If the directive is placed on an individual field, it overrules the one on the type.

If we do not specify any arguments to the `@authorize` directive, it will only enforce that the requestor is authenticated, nothing more. If he is not and tries to access an authorized field, a GraphQL error will be raised and the field result set to `null`.

Warning

Using the @authorize directive, all unauthorized requests by default will return status code 200 and a payload like this:

JSON

{

"errors": [

{

"message": "The current user is not authorized to access this resource.",

"locations": [

{

"line": 2,

"column": 3

}

],

"path": ["welcome"],

"extensions": {

"code": "AUTH_NOT_AUTHENTICATED"

}

}

],

"data": {

"welcome": null

}

}

[](https://chillicream.com/docs/hotchocolate/v14/security/authorization#roles)Roles
-----------------------------------------------------------------------------------

Roles provide a very intuitive way of dividing our users into groups with different access rights.

When building our `ClaimsPrincipal`, we just have to add one or more role claims.

C#

claims.Add(new Claim(ClaimTypes.Role, "Administrator"));

We can then check whether an authenticated user has these role claims.

C#

[Authorize(Roles = new [] { "Guest", "Administrator" })]

public class User

{

public string Name { get; set; }

[Authorize(Roles = new[] { "Administrator" })]

public Address Address { get; set; }

}

Warning

If multiple roles are specified, a user only has to match one of the specified roles, in order to be able to execute the resolver.

[Learn more about role-based authorization in ASP.NET Core](https://docs.microsoft.com/aspnet/core/security/authorization/roles)

[](https://chillicream.com/docs/hotchocolate/v14/security/authorization#policies)Policies
-----------------------------------------------------------------------------------------

Policies allow us to create richer validation logic and decouple the authorization rules from our GraphQL resolvers.

A policy consists of an [IAuthorizationRequirement](https://docs.microsoft.com/aspnet/core/security/authorization/policies#requirements) and an [AuthorizationHandler<T>](https://docs.microsoft.com/aspnet/core/security/authorization/policies#authorization-handlers).

Once defined, we can register our policies like the following.

C#

builder.Services.AddAuthorization(options =>

{

options.AddPolicy("AtLeast21", policy =>

policy.Requirements.Add(new MinimumAgeRequirement(21)));

options.AddPolicy("HasCountry", policy =>

policy.RequireAssertion(context =>

context.User.HasClaim(c => c.Type == ClaimTypes.Country)));

});

builder.Services.AddSingleton<IAuthorizationHandler, MinimumAgeHandler>();

builder.Services

.AddGraphQLServer()

.AddAuthorization()

.AddQueryType<Query>();

We can then use these policies to restrict access to our fields.

C#

[Authorize(Policy = "AllEmployees")]

public class User

{

public string Name { get; }

[Authorize(Policy = "SalesDepartment")]

public Address Address { get; }

}

This essentially uses the provided policy and runs it against the `ClaimsPrincipal` that is associated with the current request.

The `@authorize` directive is also repeatable, which means that we are able to chain the directive and a user is only allowed to access the field if they meet all of the specified conditions.

C#

[Authorize(Policy = "AtLeast21")]

[Authorize(Policy = "HasCountry")]

public class User

{

public string Name { get; set; }

}

[Learn more about policy-based authorization in ASP.NET Core](https://docs.microsoft.com/aspnet/core/security/authorization/policies)

If we need to, we can also access the `IResolverContext` in our `AuthorizationHandler`.

C#

public class MinimumAgeHandler

: AuthorizationHandler<MinimumAgeRequirement, IResolverContext>

{

protected override Task HandleRequirementAsync(

AuthorizationHandlerContext context,

MinimumAgeRequirement requirement,

IResolverContext resolverContext)

{

}

}

[](https://chillicream.com/docs/hotchocolate/v14/security/authorization#allow-anonymous-access)Allow Anonymous Access
---------------------------------------------------------------------------------------------------------------------

In some scenarios, you may want to allow anonymous access to certain fields or actions in your GraphQL schema, bypassing any authentication or authorization that may be in place. This is achieved using the `AllowAnonymous` attribute. This attribute effectively ignores any other authorization attributes present on the field, allowing unauthenticated or anonymous access.

The `AllowAnonymous` attribute, if present, erases all other authorization attributes on the field. **Be careful where you use it to ensure you're not unintentionally allowing access to sensitive information.**

[](https://chillicream.com/docs/hotchocolate/v14/security/authorization#usage-1)Usage
-------------------------------------------------------------------------------------

Here's an example of how you can use the `AllowAnonymous` attribute in conjunction with the `Authorize` attribute:

C#

public class AccountMutations

{

[Authorize]

public Task<User> AddAddressAsync(CancellationToken cancellationToken)

{

}

[AllowAnonymous]

public Task<User> RegisterAsync(CancellationToken cancellationToken)

{

}

}

In this example, only authenticated users can access the `AddAddressAsync` method, as it has the `Authorize` attribute applied. However, the `Register` method is accessible by everyone, regardless of their authentication status, due to the `AllowAnonymous` attribute. This is typical for registration endpoints, where new users who don't yet have an account need to be able to access the endpoint.

> Note: Make sure to use `HotChocolate.AspNetCore.Authorization.AllowAnonymousAttribute` instead of the `Microsoft.AspNetCore.Authorization.AllowAnonymousAttribute`.

[](https://chillicream.com/docs/hotchocolate/v14/security/authorization#global-authorization)Global authorization
-----------------------------------------------------------------------------------------------------------------

We can also apply authorization to our entire GraphQL endpoint. To do this, simply call `RequireAuthorization()` on the `GraphQLEndpointConventionBuilder`.

C#

app.UseRouting();

app.UseAuthentication();

app.UseAuthorization();

app.UseEndpoints(endpoints =>

{

endpoints.MapGraphQL().RequireAuthorization();

});

This method also accepts [roles](https://chillicream.com/docs/hotchocolate/v14/security/authorization#roles) and [policies](https://chillicream.com/docs/hotchocolate/v14/security/authorization#policies) as arguments, similar to the `Authorize` attribute / methods.

Warning

Unlike the `@authorize directive` this will return status code 401 and prevent unauthorized access to all middleware included in `MapGraphQL`. This includes our GraphQL IDE Nitro. If we do not want to block unauthorized access to Nitro, we can split up the `MapGraphQL` middleware and for example only apply the `RequireAuthorization` to the `MapGraphQLHttp` middleware.

[Learn more about available middleware](https://chillicream.com/docs/hotchocolate/v14/server/endpoints)

[](https://chillicream.com/docs/hotchocolate/v14/security/authorization#modifying-the-claimsprincipal)Modifying the ClaimsPrincipal
-----------------------------------------------------------------------------------------------------------------------------------

Sometimes we might want to add additional [ClaimsIdentity](https://docs.microsoft.com/dotnet/api/system.security.claims.claimsidentity) to our `ClaimsPrincipal` or modify the default identity.

Hot Chocolate provides the ability to register an `IHttpRequestInterceptor`, allowing us to modify the incoming HTTP request, before it is passed along to the execution engine.

C#

public class HttpRequestInterceptor : DefaultHttpRequestInterceptor

{

public override ValueTask OnCreateAsync(HttpContext context,

IRequestExecutor requestExecutor, OperationRequestBuilder requestBuilder,

CancellationToken cancellationToken)

{

var identity = new ClaimsIdentity();

identity.AddClaim(new Claim(ClaimTypes.Country, "us"));

context.User.AddIdentity(identity);

return base.OnCreateAsync(context, requestExecutor, requestBuilder,

cancellationToken);

}

}

C#

builder.Services

.AddGraphQLServer()

.AddHttpRequestInterceptor<HttpRequestInterceptor>();

[Learn more about interceptors](https://chillicream.com/docs/hotchocolate/v14/server/interceptors)

Last updated on **2026-02-17** by**Tobias Tengler**
