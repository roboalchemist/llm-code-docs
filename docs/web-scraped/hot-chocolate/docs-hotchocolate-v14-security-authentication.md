# Source: https://chillicream.com/docs/hotchocolate/v14/security/authentication

Title: Authentication - Hot Chocolate v14

URL Source: https://chillicream.com/docs/hotchocolate/v14/security/authentication

Markdown Content:
Authentication - Hot Chocolate v14 - ChilliCream GraphQL Platform
===============

[](https://chillicream.com/)

[](https://chillicream.com/)

1.   [Platform](https://chillicream.com/platform)
2.   [Services](https://chillicream.com/services)
3.   [Developers](https://chillicream.com/docs)
4.   [Company](https://chillicream.com/resources)
5.   [Pricing](https://chillicream.com/pricing)
6.   [Help](https://chillicream.com/help)
7.   [Request a Demo](mailto:contact@chillicream.com?subject=Demo)[Launch](https://nitro.chillicream.com/)

[Request a Demo](mailto:contact@chillicream.com?subject=Demo)[Launch](https://nitro.chillicream.com/)

Hot Chocolate v14

##### Table of contents

Hot Chocolate v14

[###### Nitro (fka Banana Cake Pop) GraphQL API Management](https://chillicream.com/docs/nitro)[###### Fusion Federated GraphQL Gateway](https://chillicream.com/docs/fusion/v15)[###### Hot Chocolate GraphQL Server / Gateway](https://chillicream.com/docs/hotchocolate/v15)[###### Strawberry Shake GraphQL Client for .NET](https://chillicream.com/docs/strawberryshake/v15)

[v16](https://chillicream.com/docs/hotchocolate/v16/security/authentication)[v15](https://chillicream.com/docs/hotchocolate/v15/security/authentication)[v14](https://chillicream.com/docs/hotchocolate/v14/security/authentication)[v13](https://chillicream.com/docs/hotchocolate/v13/security/authentication)[v12](https://chillicream.com/docs/hotchocolate/v12/security/authentication)[v11](https://chillicream.com/docs/hotchocolate/v11/security/authentication)[v10](https://chillicream.com/docs/hotchocolate/v10/security/authentication)

1.   [Introduction](https://chillicream.com/docs/hotchocolate/v14)
2.   [Getting Started](https://chillicream.com/docs/hotchocolate/v14/get-started-with-graphql-in-net-core)
3.   
Defining a schema 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema)
    2.   [Queries](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/queries)
    3.   [Mutations](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/mutations)
    4.   [Subscriptions](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/subscriptions)
    5.   [Object Types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/object-types)
    6.   [Scalars](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/scalars)
    7.   [Arguments](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/arguments)
    8.   [Input Object Types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/input-object-types)
    9.   [Lists](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/lists)
    10.   [Non-Null](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/non-null)
    11.   [Enums](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/enums)
    12.   [Interfaces](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/interfaces)
    13.   [Unions](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/unions)
    14.   [Extending Types](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/extending-types)
    15.   [Directives](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/directives)
    16.   [Documentation](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/documentation)
    17.   [Versioning](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/versioning)
    18.   [Relay](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/relay)
    19.   [Dynamic Schemas](https://chillicream.com/docs/hotchocolate/v14/defining-a-schema/dynamic-schemas)

4.   
Fetching data 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v14/fetching-data)
    2.   [Resolvers](https://chillicream.com/docs/hotchocolate/v14/fetching-data/resolvers)
    3.   [Fetching from Databases](https://chillicream.com/docs/hotchocolate/v14/fetching-data/fetching-from-databases)
    4.   [Fetching from REST](https://chillicream.com/docs/hotchocolate/v14/fetching-data/fetching-from-rest)
    5.   [DataLoader](https://chillicream.com/docs/hotchocolate/v14/fetching-data/dataloader)
    6.   [Pagination](https://chillicream.com/docs/hotchocolate/v14/fetching-data/pagination)
    7.   [Filtering](https://chillicream.com/docs/hotchocolate/v14/fetching-data/filtering)
    8.   [Sorting](https://chillicream.com/docs/hotchocolate/v14/fetching-data/sorting)
    9.   [Projections](https://chillicream.com/docs/hotchocolate/v14/fetching-data/projections)

5.   
Execution Engine 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v14/execution-engine)
    2.   [Field middleware](https://chillicream.com/docs/hotchocolate/v14/execution-engine/field-middleware)

6.   
Integrations 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v14/integrations)
    2.   [Entity Framework](https://chillicream.com/docs/hotchocolate/v14/integrations/entity-framework)
    3.   [MongoDB](https://chillicream.com/docs/hotchocolate/v14/integrations/mongodb)
    4.   [Spatial Data](https://chillicream.com/docs/hotchocolate/v14/integrations/spatial-data)
    5.   [Marten](https://chillicream.com/docs/hotchocolate/v14/integrations/marten)

7.   
Server 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v14/server)
    2.   [Endpoints](https://chillicream.com/docs/hotchocolate/v14/server/endpoints)
    3.   [HTTP transport](https://chillicream.com/docs/hotchocolate/v14/server/http-transport)
    4.   [Interceptors](https://chillicream.com/docs/hotchocolate/v14/server/interceptors)
    5.   [Dependency injection](https://chillicream.com/docs/hotchocolate/v14/server/dependency-injection)
    6.   [Global State](https://chillicream.com/docs/hotchocolate/v14/server/global-state)
    7.   [Introspection](https://chillicream.com/docs/hotchocolate/v14/server/introspection)
    8.   [Files](https://chillicream.com/docs/hotchocolate/v14/server/files)
    9.   [Instrumentation](https://chillicream.com/docs/hotchocolate/v14/server/instrumentation)
    10.   [Batching](https://chillicream.com/docs/hotchocolate/v14/server/batching)
    11.   [Command Line](https://chillicream.com/docs/hotchocolate/v14/server/command-line)

8.   
Performance 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v14/performance)
    2.   [Persisted operations](https://chillicream.com/docs/hotchocolate/v14/performance/persisted-operations)
    3.   [Automatic persisted operations](https://chillicream.com/docs/hotchocolate/v14/performance/automatic-persisted-operations)

9.   
Security 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v14/security)
    2.   [Authentication](https://chillicream.com/docs/hotchocolate/v14/security/authentication)
    3.   [Authorization](https://chillicream.com/docs/hotchocolate/v14/security/authorization)
    4.   [Cost Analysis](https://chillicream.com/docs/hotchocolate/v14/security/cost-analysis)

10.   
API Reference 

    1.   [Custom Attributes](https://chillicream.com/docs/hotchocolate/v14/api-reference/custom-attributes)
    2.   [Errors](https://chillicream.com/docs/hotchocolate/v14/api-reference/errors)
    3.   [Language](https://chillicream.com/docs/hotchocolate/v14/api-reference/language)
    4.   [Extending Filtering](https://chillicream.com/docs/hotchocolate/v14/api-reference/extending-filtering)
    5.   [Visitors](https://chillicream.com/docs/hotchocolate/v14/api-reference/visitors)
    6.   [Apollo Federation](https://chillicream.com/docs/hotchocolate/v14/api-reference/apollo-federation)
    7.   [Executable](https://chillicream.com/docs/hotchocolate/v14/api-reference/executable)

11.   
Migrating 

    1.   [Migrate from 13 to 14](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-13-to-14)
    2.   [Migrate from 12 to 13](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-12-to-13)
    3.   [Migrate from 11 to 12](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-11-to-12)
    4.   [Migrate from 10 to 11](https://chillicream.com/docs/hotchocolate/v14/migrating/migrate-from-10-to-11)

Table of contents About this article

This is documentation for **v14**, which is no longer actively maintained.

For up-to-date documentation, see the[latest stable version](https://chillicream.com/docs/hotchocolate/v15/security/authentication).

Authentication
==============

Authentication allows us to determine a user's identity. This is of course a prerequisite for authorization, but it also allows us to access the authenticated user in our resolvers. This is useful, if we for example want to build a `me` field that fetches details about the authenticated user.

Hot Chocolate fully embraces the authentication capabilities of ASP.NET Core, making it easy to reuse existing authentication configuration and integrating a variety of authentication providers.

[Learn more about authentication in ASP.NET Core](https://docs.microsoft.com/aspnet/core/security/authentication)

[](https://chillicream.com/docs/hotchocolate/v14/security/authentication#setup)Setup
====================================================================================

Setting up authentication is largely the same as in any other ASP.NET Core application.

**In the following example we are using JWTs, but we could use any other authentication scheme supported by ASP.NET Core.**

1.   Install the `Microsoft.AspNetCore.Authentication.JwtBearer` package

CLI Visual Studio

Bash

dotnet add package Microsoft.AspNetCore.Authentication.JwtBearer

1.   Register the JWT authentication scheme

C#

var signingKey = new SymmetricSecurityKey(

 Encoding.UTF8.GetBytes("MySuperSecretKey"));

builder.Services

 .AddAuthentication(JwtBearerDefaults.AuthenticationScheme)

 .AddJwtBearer(options =>

 {

 options.TokenValidationParameters =

 new TokenValidationParameters

 {

 ValidIssuer = "https://auth.chillicream.com",

 ValidAudience = "https://graphql.chillicream.com",

 ValidateIssuerSigningKey = true,

 IssuerSigningKey = signingKey

 };

 });

Warning

This is an example configuration that's not intended for use in a real world application.

1.   Register the ASP.NET Core authentication middleware with the request pipeline by calling `UseAuthentication`

C#

app.UseRouting();

app.UseAuthentication();

app.UseEndpoints(endpoints =>

{

 endpoints.MapGraphQL();

});

The above takes care of parsing and validating an incoming HTTP request.

In order to make the authentication result available to our resolvers, we need to complete some additional, Hot Chocolate specific steps.

1.   Install the `HotChocolate.AspNetCore.Authorization` package

CLI Visual Studio

Bash

dotnet add package HotChocolate.AspNetCore.Authorization

Warning

All `HotChocolate.*` packages need to have the same version.

1.   Call `AddAuthorization()` on the `IRequestExecutorBuilder`

C#

builder.Services

 .AddGraphQLServer()

 .AddAuthorization()

 .AddQueryType<Query>();

All of this does not yet lock out unauthenticated users. It only exposes the identity of the authenticated user to our application through a `ClaimsPrincipal`. If we want to prevent certain users from querying our graph, we need to utilize authorization.

[Learn more about authorization](https://chillicream.com/docs/hotchocolate/v14/security/authorization)

[](https://chillicream.com/docs/hotchocolate/v14/security/authentication#accessing-the-claimsprincipal)Accessing the ClaimsPrincipal
====================================================================================================================================

The [ClaimsPrincipal](https://docs.microsoft.com/dotnet/api/system.security.claims.claimsprincipal) of an authenticated user can be accessed in our resolvers like the following.

Implementation-first Code-first Schema-first

C#

public class Query

{

 public User GetMe(ClaimsPrincipal claimsPrincipal)

 {

 // Omitted code for brevity

 }

}

With the authenticated user's `ClaimsPrincipal`, we can now access their claims.

C#

var userId = claimsPrincipal.FindFirstValue(ClaimTypes.NameIdentifier);

Last updated on **2026-02-17** by**Tobias Tengler**

##### About this article

###### Help us improving our content

1.   [Edit on GitHub](https://github.com/ChilliCream/graphql-platform/blob/master/website/src/docs/hotchocolate/v14/security/authentication.md)
2.   [Discuss on Slack](https://slack.chillicream.com/)

###### In this Article

*   [Setup](https://chillicream.com/docs/hotchocolate/v14/security/authentication/#setup)

*   [Accessing the ClaimsPrincipal](https://chillicream.com/docs/hotchocolate/v14/security/authentication/#accessing-the-claimsprincipal)

[](https://chillicream.com/)

16192 Coastal Highway

Lewes, DE 19958

United States

### Platform

[Analytics](https://chillicream.com/platform/analytics)[Continuous Integration](https://chillicream.com/platform/continuous-integration)[Ecosystem](https://chillicream.com/platform/ecosystem)[Nitro](https://chillicream.com/products/nitro)

### Services

[Advisory](https://chillicream.com/services/advisory)[Support](https://chillicream.com/services/support)[Training](https://chillicream.com/services/training)

### Documentation

[Nitro (fka Banana Cake Pop)](https://chillicream.com/docs/nitro)[Fusion](https://chillicream.com/docs/fusion/v15)[Hot Chocolate](https://chillicream.com/docs/hotchocolate/v15)[Strawberry Shake](https://chillicream.com/docs/strawberryshake/v15)

### Company

[Contact](mailto:contact@chillicream.com)[Shop](https://store.chillicream.com/)[Acceptable Use Policy](https://chillicream.com/legal/acceptable-use-policy)[Cookie Policy](https://chillicream.com/legal/cookie-policy)[Privacy Policy](https://chillicream.com/legal/privacy-policy)[Terms of Service](https://chillicream.com/legal/terms-of-service)[ChilliCream License](https://chillicream.com/licensing/chillicream-license)

[to read the latest stuff](https://chillicream.com/blog)[to work with us on the platform](https://github.com/ChilliCream/graphql-platform)[to get in touch with us](https://slack.chillicream.com/)[to learn new stuff](https://www.youtube.com/c/ChilliCream)[to stay up-to-date](https://x.com/Chilli_Cream)[to connect](https://www.linkedin.com/company/chillicream)

© 2026 ChilliCream, Inc. ・ All Rights Reserved

This website uses cookies to ensure you get the best experience on our website. [Learn more](https://chillicream.com/legal/cookie-policy.html)

Got it!

##### Getting Started with GraphQL in .NET

Learn to build modern APIs like those used by Facebook and Netflix in our self-paced getting started course on Dometrain.

[Check it out!](https://courses.chillicream.com/)
