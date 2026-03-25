# Source: https://ocelot.readthedocs.io/en/latest/features/graphql.html

Title: GraphQL — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/graphql.html

Markdown Content:
GraphQL — Ocelot Gateway 24.1 "Globality" documentation
===============

[![Image 2: GraphQL Logo](https://avatars.githubusercontent.com/u/13958777)](https://avatars.githubusercontent.com/u/13958777) GraphQL[¶](https://ocelot.readthedocs.io/en/latest/features/graphql.html#graphql-logo-graphql "Link to this heading")
====================================================================================================================================================================================================================================================

Ocelot does not directly support [GraphQL](https://graphql.org/), but many people have asked about it. We wanted to show how easy it is to integrate the [GraphQL for .NET](https://github.com/graphql-dotnet/graphql-dotnet) library.

Sample[¶](https://ocelot.readthedocs.io/en/latest/features/graphql.html#sample "Link to this heading")
------------------------------------------------------------------------------------------------------

> **Sample**: [Ocelot.Samples.GraphQL](https://github.com/ThreeMammals/Ocelot/tree/main/samples/GraphQL)

Please see the sample project [Ocelot.Samples.GraphQL](https://github.com/ThreeMammals/Ocelot/tree/main/samples/GraphQL). Using a combination of the [graphql-dotnet](https://github.com/graphql-dotnet/graphql-dotnet) project and Ocelot [Delegating Handlers](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html) feature, this is pretty easy to do. However, we do not intend to integrate more closely with [GraphQL](https://graphql.org/) at the moment. Check out the sample’s [README.md](https://github.com/ThreeMammals/Ocelot/blob/main/samples/GraphQL/README.md) for detailed instructions on how to do this.

Future[¶](https://ocelot.readthedocs.io/en/latest/features/graphql.html#future "Link to this heading")
------------------------------------------------------------------------------------------------------

If you have sufficient experience with [GraphQL](https://graphql.org/) and the mentioned .NET [graphql-dotnet](https://github.com/graphql-dotnet/graphql-dotnet) package, we would welcome your contribution to the sample. [![Image 3: octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)](https://github.githubassets.com/images/icons/emoji/octocat.png)

Who knows, maybe you will get inspired by the sample development and come up with a design solution in the form of a rough draft of a _GraphQL_ feature to implement in Ocelot. Good luck! And welcome to the [Discussions](https://github.com/ThreeMammals/Ocelot/discussions) space of the repository!

[Ocelot Gateway](https://ocelot.readthedocs.io/en/latest/index.html)
====================================================================

### Navigation

Welcome

*   [Welcome](https://ocelot.readthedocs.io/en/latest/releasenotes.html)

Introduction

*   [Big Picture](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html)
*   [Getting Started](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html)
*   [Not Supported](https://ocelot.readthedocs.io/en/latest/introduction/notsupported.html)
*   [Hosting Gotchas](https://ocelot.readthedocs.io/en/latest/introduction/gotchas.html)

Features

*   [Administration](https://ocelot.readthedocs.io/en/latest/features/administration.html)
*   [Aggregation](https://ocelot.readthedocs.io/en/latest/features/aggregation.html)
*   [Authentication](https://ocelot.readthedocs.io/en/latest/features/authentication.html)
*   [Authorization](https://ocelot.readthedocs.io/en/latest/features/authorization.html)
*   [Caching](https://ocelot.readthedocs.io/en/latest/features/caching.html)
*   [Claims Transformation](https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html)
*   [Configuration](https://ocelot.readthedocs.io/en/latest/features/configuration.html)
*   [Delegating Handlers](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html)
*   [Dependency Injection](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html)
*   [Error Handling](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html)
*   [GraphQL](https://ocelot.readthedocs.io/en/latest/features/graphql.html#)
    *   [Sample](https://ocelot.readthedocs.io/en/latest/features/graphql.html#sample)
    *   [Future](https://ocelot.readthedocs.io/en/latest/features/graphql.html#future)

*   [Headers Transformation](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html)
*   [Kubernetes (K8s)](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html)
*   [Load Balancer](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html)
*   [Logging](https://ocelot.readthedocs.io/en/latest/features/logging.html)
*   [Metadata](https://ocelot.readthedocs.io/en/latest/features/metadata.html)
*   [Method Transformation](https://ocelot.readthedocs.io/en/latest/features/methodtransformation.html)
*   [Middleware Injection](https://ocelot.readthedocs.io/en/latest/features/middlewareinjection.html)
*   [Quality of Service](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html)
*   [Rate Limiting](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html)
*   [Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html)
*   [Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html)
*   [Service Fabric](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html)
*   [Tracing](https://ocelot.readthedocs.io/en/latest/features/tracing.html)
*   [Websockets](https://ocelot.readthedocs.io/en/latest/features/websockets.html)

Building Ocelot

*   [Building](https://ocelot.readthedocs.io/en/latest/building/building.html)
*   [Development Process](https://ocelot.readthedocs.io/en/latest/building/devprocess.html)
*   [Release Process](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html)

### Related Topics

*   [Documentation overview](https://ocelot.readthedocs.io/en/latest/index.html)
    *   Previous: [Error Handling](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html "previous chapter")
    *   Next: [Headers Transformation](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html "next chapter")

 © 2016-2025 Three Mammals. | Powered by [Sphinx 9.0.4](https://www.sphinx-doc.org/)&[Alabaster 1.0.0](https://alabaster.readthedocs.io/) | [Page source](https://ocelot.readthedocs.io/en/latest/_sources/features/graphql.rst.txt)

[**Augment Code Review**Benchmarked #1 Against Cursor, Copilot, Claude**Install Now**](https://server.ethicalads.io/proxy/click/10131/019cde6f-05b9-7530-ba3d-8c0cd5f8f476/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)

Close Ad

![Image 4](https://server.ethicalads.io/proxy/view/10131/019cde6f-05b9-7530-ba3d-8c0cd5f8f476/)
