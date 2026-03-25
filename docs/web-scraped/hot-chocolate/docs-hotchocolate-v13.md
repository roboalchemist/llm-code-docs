# Source: https://chillicream.com/docs/hotchocolate/v13

Title: Introduction - Hot Chocolate v13

URL Source: https://chillicream.com/docs/hotchocolate/v13

Published Time: Tue, 17 Feb 2026 16:19:04 GMT

Markdown Content:
Introduction - Hot Chocolate v13 - ChilliCream GraphQL Platform
===============

[](https://chillicream.com/)

[](https://chillicream.com/)

1.   [Platform](https://chillicream.com/platform)
2.   [Services](https://chillicream.com/services)
3.   [Developers](https://chillicream.com/docs)
4.   [Company](https://chillicream.com/resources)
5.   [Pricing](https://chillicream.com/pricing)
6.   [Help](https://chillicream.com/help)
7.   [Request a Demo](https://chillicream.com/cdn-cgi/l/email-protection#6a0905041e0b091e2a09020306060309180f0b074409050755191f08000f091e572e0f0705)[Launch](https://nitro.chillicream.com/)

[Star](https://github.com/ChilliCream/graphql-platform)

[Request a Demo](https://chillicream.com/cdn-cgi/l/email-protection#ddbeb2b3a9bcbea99dbeb5b4b1b1b4beafb8bcb0f3beb2b0e2aea8bfb7b8bea9e099b8b0b2)[Launch](https://nitro.chillicream.com/)

Hot Chocolate v13

##### Table of contents

Hot Chocolate v13

[###### Nitro (fka Banana Cake Pop) GraphQL API Management](https://chillicream.com/docs/nitro)[###### Fusion Federated GraphQL Gateway](https://chillicream.com/docs/fusion/v15)[###### Hot Chocolate GraphQL Server / Gateway](https://chillicream.com/docs/hotchocolate/v15)[###### Strawberry Shake GraphQL Client for .NET](https://chillicream.com/docs/strawberryshake/v15)

[v16](https://chillicream.com/docs/hotchocolate/v16)[v15](https://chillicream.com/docs/hotchocolate/v15)[v14](https://chillicream.com/docs/hotchocolate/v14)[v13](https://chillicream.com/docs/hotchocolate/v13)[v12](https://chillicream.com/docs/hotchocolate/v12)[v11](https://chillicream.com/docs/hotchocolate/v11)[v10](https://chillicream.com/docs/hotchocolate/v10)

1.   [Introduction](https://chillicream.com/docs/hotchocolate/v13)
2.   [Get Started](https://chillicream.com/docs/hotchocolate/v13/get-started-with-graphql-in-net-core)
3.   
Defining a schema 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema)
    2.   [Queries](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/queries)
    3.   [Mutations](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/mutations)
    4.   [Subscriptions](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/subscriptions)
    5.   [Object Types](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/object-types)
    6.   [Scalars](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/scalars)
    7.   [Arguments](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/arguments)
    8.   [Input Object Types](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/input-object-types)
    9.   [Lists](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/lists)
    10.   [Non-Null](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/non-null)
    11.   [Enums](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/enums)
    12.   [Interfaces](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/interfaces)
    13.   [Unions](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/unions)
    14.   [Extending Types](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/extending-types)
    15.   [Directives](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/directives)
    16.   [Documentation](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/documentation)
    17.   [Versioning](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/versioning)
    18.   [Relay](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/relay)
    19.   [Dynamic Schemas](https://chillicream.com/docs/hotchocolate/v13/defining-a-schema/dynamic-schemas)

4.   
Fetching data 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v13/fetching-data)
    2.   [Resolvers](https://chillicream.com/docs/hotchocolate/v13/fetching-data/resolvers)
    3.   [Fetching from Databases](https://chillicream.com/docs/hotchocolate/v13/fetching-data/fetching-from-databases)
    4.   [Fetching from REST](https://chillicream.com/docs/hotchocolate/v13/fetching-data/fetching-from-rest)
    5.   [DataLoader](https://chillicream.com/docs/hotchocolate/v13/fetching-data/dataloader)
    6.   [Pagination](https://chillicream.com/docs/hotchocolate/v13/fetching-data/pagination)
    7.   [Filtering](https://chillicream.com/docs/hotchocolate/v13/fetching-data/filtering)
    8.   [Sorting](https://chillicream.com/docs/hotchocolate/v13/fetching-data/sorting)
    9.   [Projections](https://chillicream.com/docs/hotchocolate/v13/fetching-data/projections)

5.   
Execution Engine 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v13/execution-engine)
    2.   [Field middleware](https://chillicream.com/docs/hotchocolate/v13/execution-engine/field-middleware)

6.   
Integrations 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v13/integrations)
    2.   [Entity Framework](https://chillicream.com/docs/hotchocolate/v13/integrations/entity-framework)
    3.   [MongoDB](https://chillicream.com/docs/hotchocolate/v13/integrations/mongodb)
    4.   [Neo4J](https://chillicream.com/docs/hotchocolate/v13/integrations/neo4j)
    5.   [Spatial Data](https://chillicream.com/docs/hotchocolate/v13/integrations/spatial-data)
    6.   [Marten](https://chillicream.com/docs/hotchocolate/v13/integrations/marten)

7.   
Server 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v13/server)
    2.   [Endpoints](https://chillicream.com/docs/hotchocolate/v13/server/endpoints)
    3.   [HTTP transport](https://chillicream.com/docs/hotchocolate/v13/server/http-transport)
    4.   [Interceptors](https://chillicream.com/docs/hotchocolate/v13/server/interceptors)
    5.   [Dependency injection](https://chillicream.com/docs/hotchocolate/v13/server/dependency-injection)
    6.   [Global State](https://chillicream.com/docs/hotchocolate/v13/server/global-state)
    7.   [Introspection](https://chillicream.com/docs/hotchocolate/v13/server/introspection)
    8.   [Files](https://chillicream.com/docs/hotchocolate/v13/server/files)
    9.   [Instrumentation](https://chillicream.com/docs/hotchocolate/v13/server/instrumentation)
    10.   [Batching](https://chillicream.com/docs/hotchocolate/v13/server/batching)
    11.   [Command Line](https://chillicream.com/docs/hotchocolate/v13/server/command-line)

8.   
Distributed Schemas 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v13/distributed-schema)
    2.   [Schema Stitching](https://chillicream.com/docs/hotchocolate/v13/distributed-schema/schema-stitching)
    3.   [Schema Federations](https://chillicream.com/docs/hotchocolate/v13/distributed-schema/schema-federations)
    4.   [Schema Configuration](https://chillicream.com/docs/hotchocolate/v13/distributed-schema/schema-configuration)

9.   
Performance 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v13/performance)
    2.   [Persisted queries](https://chillicream.com/docs/hotchocolate/v13/performance/persisted-queries)
    3.   [Automatic persisted queries](https://chillicream.com/docs/hotchocolate/v13/performance/automatic-persisted-queries)

10.   
Security 

    1.   [Overview](https://chillicream.com/docs/hotchocolate/v13/security)
    2.   [Authentication](https://chillicream.com/docs/hotchocolate/v13/security/authentication)
    3.   [Authorization](https://chillicream.com/docs/hotchocolate/v13/security/authorization)
    4.   [Operation Complexity](https://chillicream.com/docs/hotchocolate/v13/security/operation-complexity)

11.   
API Reference 

    1.   [Custom Attributes](https://chillicream.com/docs/hotchocolate/v13/api-reference/custom-attributes)
    2.   [Errors](https://chillicream.com/docs/hotchocolate/v13/api-reference/errors)
    3.   [Language](https://chillicream.com/docs/hotchocolate/v13/api-reference/language)
    4.   [Extending Filtering](https://chillicream.com/docs/hotchocolate/v13/api-reference/extending-filtering)
    5.   [Visitors](https://chillicream.com/docs/hotchocolate/v13/api-reference/visitors)
    6.   [Apollo Federation](https://chillicream.com/docs/hotchocolate/v13/api-reference/apollo-federation)
    7.   [Executable](https://chillicream.com/docs/hotchocolate/v13/api-reference/executable)

12.   
Migrating 

    1.   [Migrate from 12 to 13](https://chillicream.com/docs/hotchocolate/v13/migrating/migrate-from-12-to-13)
    2.   [Migrate from 11 to 12](https://chillicream.com/docs/hotchocolate/v13/migrating/migrate-from-11-to-12)
    3.   [Migrate from 10 to 11](https://chillicream.com/docs/hotchocolate/v13/migrating/migrate-from-10-to-11)

Table of contents About this article

This is documentation for **v13**, which is no longer actively maintained.

For up-to-date documentation, see the[latest stable version](https://chillicream.com/docs/hotchocolate/v15).

Introduction
============

Hot Chocolate is an open-source GraphQL server for the [Microsoft .NET platform](https://dotnet.microsoft.com/) that is compliant with the newest [GraphQL October 2021 spec + Drafts](https://spec.graphql.org/), which makes Hot Chocolate compatible to all GraphQL compliant clients like [Strawberry Shake](https://chillicream.com/docs/strawberryshake/v13), [Relay](https://relay.dev/), [Apollo Client](https://www.apollographql.com/docs/react/), and [various other GraphQL clients and tools](https://graphql.org/code).

Hot Chocolate takes the complexity away from building a fully-fledged GraphQL server and lets you focus on delivering the next big thing.

[![Image 1: Platform](https://chillicream.com/static/cfd2ddde71f95ed876541f87c15b2a08/78d47/platform.png)](https://chillicream.com/static/cfd2ddde71f95ed876541f87c15b2a08/f97d7/platform.png)

You can use Hot Chocolate Server as:

*   Stand-alone [ASP.NET Core](https://learn.microsoft.com/aspnet/core) GraphQL Server.
*   Serverless [Azure Function](https://azure.microsoft.com/products/functions) or [AWS Lambda](https://aws.amazon.com/lambda) that serves up a GraphQL server.
*   [GraphQL Gateway](https://chillicream.com/docs/hotchocolate/v13/distributed-schema) for a federated data graph that pulls all your data sources together to create the one source of truth.

Hot Chocolate is very easy to set up and takes the clutter away from writing GraphQL schemas. We update Hot Chocolate continuously and implement new spec features as they hit draft status. This lets you pick up new GraphQL features incrementally to open up new development opportunities for your ideas.

Let's [get started](https://chillicream.com/docs/hotchocolate/v13/get-started-with-graphql-in-net-core) with Hot Chocolate!

Join us on [YouTube](https://youtube.chillicream.com/) for Hot Chocolate deep dives.

Last updated on **2026-02-17** by**Tobias Tengler**

##### About this article

###### Help us improving our content

1.   [Edit on GitHub](https://github.com/ChilliCream/graphql-platform/blob/master/website/src/docs/hotchocolate/v13/index.md)
2.   [Discuss on Slack](https://slack.chillicream.com/)

[](https://chillicream.com/)

16192 Coastal Highway

Lewes, DE 19958

United States

[Star](https://github.com/ChilliCream/graphql-platform)

### Platform

[Analytics](https://chillicream.com/platform/analytics)[Continuous Integration](https://chillicream.com/platform/continuous-integration)[Ecosystem](https://chillicream.com/platform/ecosystem)[Nitro](https://chillicream.com/products/nitro)

### Services

[Advisory](https://chillicream.com/services/advisory)[Support](https://chillicream.com/services/support)[Training](https://chillicream.com/services/training)

### Documentation

[Nitro (fka Banana Cake Pop)](https://chillicream.com/docs/nitro)[Fusion](https://chillicream.com/docs/fusion/v15)[Hot Chocolate](https://chillicream.com/docs/hotchocolate/v15)[Strawberry Shake](https://chillicream.com/docs/strawberryshake/v15)

### Company

[Contact](https://chillicream.com/cdn-cgi/l/email-protection#8deee2e3f9eceef9cdeee5e4e1e1e4eeffe8ece0a3eee2e0)[Shop](https://store.chillicream.com/)[Acceptable Use Policy](https://chillicream.com/legal/acceptable-use-policy)[Cookie Policy](https://chillicream.com/legal/cookie-policy)[Privacy Policy](https://chillicream.com/legal/privacy-policy)[Terms of Service](https://chillicream.com/legal/terms-of-service)[ChilliCream License](https://chillicream.com/licensing/chillicream-license)

[to read the latest stuff](https://chillicream.com/blog)[to work with us on the platform](https://github.com/ChilliCream/graphql-platform)[to get in touch with us](https://slack.chillicream.com/)[to learn new stuff](https://www.youtube.com/c/ChilliCream)[to stay up-to-date](https://x.com/Chilli_Cream)[to connect](https://www.linkedin.com/company/chillicream)

© 2026 ChilliCream, Inc. ・ All Rights Reserved
