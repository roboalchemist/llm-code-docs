# Source: https://ocelot.readthedocs.io/en/latest/features/methodtransformation.html

Title: Method Transformation — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/methodtransformation.html

Markdown Content:
Method Transformation — Ocelot Gateway 24.1 "Globality" documentation
===============

Method Transformation [[1]](https://ocelot.readthedocs.io/en/latest/features/methodtransformation.html#f1)[¶](https://ocelot.readthedocs.io/en/latest/features/methodtransformation.html#method-transformation "Link to this heading")
======================================================================================================================================================================================================================================

Ocelot allows users to modify the HTTP request method used when making requests to a downstream service. This is achieved by setting the following route configuration:

{
 "UpstreamPathTemplate": "/{everything}",
 "DownstreamPathTemplate": "/{everything}",
 // other props and opts...
 "UpstreamHttpMethod": [ "Get" ], // we transform HTTP verb...
 "DownstreamHttpMethod": "Post" // ...from GET to POST
}

The key property here is `DownstreamHttpMethod`, which is set to `POST`, and the route will only match `GET`, as specified by `UpstreamHttpMethod`.

This feature is useful when interacting with downstream APIs that only support `POST` while presenting a RESTful interface.

* * *

[[1](https://ocelot.readthedocs.io/en/latest/features/methodtransformation.html#id1)]
The _“Method Transformation”_ feature was released in version [14.0.8](https://github.com/ThreeMammals/Ocelot/releases/tag/14.0.8).

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
*   [GraphQL](https://ocelot.readthedocs.io/en/latest/features/graphql.html)
*   [Headers Transformation](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html)
*   [Kubernetes (K8s)](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html)
*   [Load Balancer](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html)
*   [Logging](https://ocelot.readthedocs.io/en/latest/features/logging.html)
*   [Metadata](https://ocelot.readthedocs.io/en/latest/features/metadata.html)
*   [Method Transformation](https://ocelot.readthedocs.io/en/latest/features/methodtransformation.html#)
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
    *   Previous: [Metadata](https://ocelot.readthedocs.io/en/latest/features/metadata.html "previous chapter")
    *   Next: [Middleware Injection](https://ocelot.readthedocs.io/en/latest/features/middlewareinjection.html "next chapter")

 © 2016-2025 Three Mammals. | Powered by [Sphinx 9.0.4](https://www.sphinx-doc.org/)&[Alabaster 1.0.0](https://alabaster.readthedocs.io/) | [Page source](https://ocelot.readthedocs.io/en/latest/_sources/features/methodtransformation.rst.txt)

[**Augment Code Review**Beats Copilot, Cursor & Claude on Code Review**Install Now**](https://server.ethicalads.io/proxy/click/10129/019cde6f-cba8-7240-b9f5-dd85e17dc516/)

[Ads by EthicalAds](https://www.ethicalads.io/advertisers/topics/backend-web/?ref=ea-text)

Close Ad

![Image 1](https://server.ethicalads.io/proxy/view/10129/019cde6f-cba8-7240-b9f5-dd85e17dc516/)
