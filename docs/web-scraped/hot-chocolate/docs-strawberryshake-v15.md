# Source: https://chillicream.com/docs/strawberryshake/v15

Title: Introduction - Strawberry Shake

URL Source: https://chillicream.com/docs/strawberryshake/v15

Markdown Content:
Introduction - Strawberry Shake - ChilliCream GraphQL Platform
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

Strawberry Shake v15

##### Table of contents

Strawberry Shake v15

[###### Nitro (fka Banana Cake Pop) GraphQL API Management](https://chillicream.com/docs/nitro)[###### Fusion Federated GraphQL Gateway](https://chillicream.com/docs/fusion/v15)[###### Hot Chocolate GraphQL Server / Gateway](https://chillicream.com/docs/hotchocolate/v15)[###### Strawberry Shake GraphQL Client for .NET](https://chillicream.com/docs/strawberryshake/v15)

[v16](https://chillicream.com/docs/strawberryshake/v16)[v15](https://chillicream.com/docs/strawberryshake/v15)[v14](https://chillicream.com/docs/strawberryshake/v14)[v13](https://chillicream.com/docs/strawberryshake/v13)[v12](https://chillicream.com/docs/strawberryshake/v12)

1.   [Introduction](https://chillicream.com/docs/strawberryshake/v15)
2.   
Get Started 

    1.   [Blazor](https://chillicream.com/docs/strawberryshake/v15/get-started)
    2.   [Xamarin](https://chillicream.com/docs/strawberryshake/v15/get-started/xamarin)
    3.   [Console](https://chillicream.com/docs/strawberryshake/v15/get-started/console)

3.   [Subscriptions](https://chillicream.com/docs/strawberryshake/v15/subscriptions)
4.   [Tooling / CLI](https://chillicream.com/docs/strawberryshake/v15/tooling)
5.   
Caching 

    1.   [Overview](https://chillicream.com/docs/strawberryshake/v15/caching)
    2.   [Entities](https://chillicream.com/docs/strawberryshake/v15/caching/entities)
    3.   [Invalidation](https://chillicream.com/docs/strawberryshake/v15/caching/invalidation)

6.   
Performance 

    1.   [Overview](https://chillicream.com/docs/strawberryshake/v15/performance)
    2.   [Persisted Operations](https://chillicream.com/docs/strawberryshake/v15/performance/persisted-operations)
    3.   [Persisted State](https://chillicream.com/docs/strawberryshake/v15/performance/persisted-state)

7.   
Networking 

    1.   [Protocols](https://chillicream.com/docs/strawberryshake/v15/networking)
    2.   [Authentication](https://chillicream.com/docs/strawberryshake/v15/networking/authentication)

8.   [Scalars](https://chillicream.com/docs/strawberryshake/v15/scalars)
9.   
Migrating 

    1.   [Migrate from 14 to 15](https://chillicream.com/docs/strawberryshake/v15/migrating/migrate-from-14-to-15)
    2.   [Migrate from 13 to 14](https://chillicream.com/docs/strawberryshake/v15/migrating/migrate-from-13-to-14)
    3.   [Migrate from 12 to 13](https://chillicream.com/docs/strawberryshake/v15/migrating/migrate-from-12-to-13)

Table of contents About this article

Introduction
============

Strawberry Shake is an open-source GraphQL client that is compliant with the newest [GraphQL draft spec](https://spec.graphql.org/), which makes Strawberry Shake compatible with all GraphQL compliant servers like [Hot Chocolate](https://chillicream.com/docs/hotchocolate/v15), [Apollo Server](https://www.apollographql.com/docs/apollo-server), [GraphQL Java](https://www.graphql-java.com/) and various other servers out there.

Strawberry Shake removes the complexity of state management and lets you interact with local and remote data through GraphQL.

You can use Strawberry Shake to:

*   Generate a C# .NET client from your GraphQL queries.
*   Interact with local and remote data through GraphQL.
*   Use reactive APIs to interact with your state.

Let's [get started](https://chillicream.com/docs/strawberryshake/v15/get-started) with Strawberry Shake!

Last updated on **2026-02-17** by**Tobias Tengler**

##### About this article

###### Help us improving our content

1.   [Edit on GitHub](https://github.com/ChilliCream/graphql-platform/blob/master/website/src/docs/strawberryshake/v15/index.md)
2.   [Discuss on Slack](https://slack.chillicream.com/)

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
