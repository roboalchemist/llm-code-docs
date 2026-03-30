# Source: https://ocelot.readthedocs.io/en/latest/

Title: Ocelot 24.1 — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/

Markdown Content:
Thanks for taking a look at the Ocelot documentation! Please use the left hand **Navigation** sidebar to get around, or see the [Table of Contents](https://ocelot.readthedocs.io/en/latest/#toc) below.

The team recommends that newcomers to Ocelot’s world start with the “[Introduction](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html)” chapters. For seasoned fans of Ocelot with a Production environment, it is advised to always consult the [Release Notes](https://ocelot.readthedocs.io/en/latest/releasenotes.html#release-notes) in the [Welcome](https://ocelot.readthedocs.io/en/latest/releasenotes.html) section before upgrading the app to the latest [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0) version.

All **Features** are listed in alphabetical order. The primary features include [Configuration](https://ocelot.readthedocs.io/en/latest/features/configuration.html) and [Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html).

Additional tips for building Ocelot can be found in the “[Building Ocelot](https://ocelot.readthedocs.io/en/latest/building/building.html)” section. We adhere to a [Development Process](https://ocelot.readthedocs.io/en/latest/building/devprocess.html) which is a part of [Release Process](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html).

Table of Contents[¶](https://ocelot.readthedocs.io/en/latest/#toc "Link to this heading")
-----------------------------------------------------------------------------------------

> Welcome
> 
> 
> *   [Welcome](https://ocelot.readthedocs.io/en/latest/releasenotes.html)
>     *   [Release Notes](https://ocelot.readthedocs.io/en/latest/releasenotes.html#release-notes)
>     *   [What’s New?](https://ocelot.readthedocs.io/en/latest/releasenotes.html#what-s-new)
>     *   [What’s Updated?](https://ocelot.readthedocs.io/en/latest/releasenotes.html#what-s-updated)
>     *   [Patches Included](https://ocelot.readthedocs.io/en/latest/releasenotes.html#patches-included)
>     *   [Contributing](https://ocelot.readthedocs.io/en/latest/releasenotes.html#contributing)
> 
> 
> 
> Introduction
> 
> 
> *   [Big Picture](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html)
>     *   [Basic Implementation](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html#basic-implementation)
>     *   [Multiple Instances](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html#multiple-instances)
>     *   [With Consul](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html#with-consul)
>     *   [With Service Fabric](https://ocelot.readthedocs.io/en/latest/introduction/bigpicture.html#with-service-fabric)
> 
> *   [Getting Started](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html)
>     *   [Install](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html#install)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html#configuration)
>     *   [Program](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html#program)
>     *   [Samples](https://ocelot.readthedocs.io/en/latest/introduction/gettingstarted.html#samples)
> 
> *   [Not Supported](https://ocelot.readthedocs.io/en/latest/introduction/notsupported.html)
>     *   [Chunked Encoding](https://ocelot.readthedocs.io/en/latest/introduction/notsupported.html#chunked-encoding)
>     *   [Forwarding `Host` header](https://ocelot.readthedocs.io/en/latest/introduction/notsupported.html#forwarding-host-header)
>     *   [Swagger](https://ocelot.readthedocs.io/en/latest/introduction/notsupported.html#swagger)
> 
> *   [Hosting Gotchas](https://ocelot.readthedocs.io/en/latest/introduction/gotchas.html)
>     *   [IIS](https://ocelot.readthedocs.io/en/latest/introduction/gotchas.html#iis)
>     *   [Kestrel](https://ocelot.readthedocs.io/en/latest/introduction/gotchas.html#kestrel)
> 
> 
> 
> Features
> 
> 
> *   [Administration](https://ocelot.readthedocs.io/en/latest/features/administration.html)
>     *   [Your Own IdentityServer](https://ocelot.readthedocs.io/en/latest/features/administration.html#your-own-identityserver)
>     *   [Internal IdentityServer](https://ocelot.readthedocs.io/en/latest/features/administration.html#internal-identityserver)
>     *   [Administration API](https://ocelot.readthedocs.io/en/latest/features/administration.html#administration-api)
> 
> *   [Aggregation](https://ocelot.readthedocs.io/en/latest/features/aggregation.html)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#configuration)
>     *   [Complex Aggregation](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#complex-aggregation)
>     *   [Custom Aggregators](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#custom-aggregators)
>     *   [Gotchas](https://ocelot.readthedocs.io/en/latest/features/aggregation.html#gotchas)
> 
> *   [Authentication](https://ocelot.readthedocs.io/en/latest/features/authentication.html)
>     *   [`AuthenticationOptions` Schema](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authenticationoptions-schema)
>     *   [Single Authentication Scheme](https://ocelot.readthedocs.io/en/latest/features/authentication.html#single-authentication-scheme)
>     *   [Multiple Authentication Schemes](https://ocelot.readthedocs.io/en/latest/features/authentication.html#multiple-authentication-schemes)
>     *   [Configuration and `AllowAnonymous`](https://ocelot.readthedocs.io/en/latest/features/authentication.html#configuration-and-allowanonymous)
>     *   [Global Configuration](https://ocelot.readthedocs.io/en/latest/features/authentication.html#global-configuration)
>     *   [Allowed Scopes](https://ocelot.readthedocs.io/en/latest/features/authentication.html#allowed-scopes)
>     *   [JWT Tokens](https://ocelot.readthedocs.io/en/latest/features/authentication.html#jwt-tokens)
>     *   [Identity Server Bearer Tokens](https://ocelot.readthedocs.io/en/latest/features/authentication.html#authentication-identity-server)
>     *   [Auth0 by Okta](https://ocelot.readthedocs.io/en/latest/features/authentication.html#auth0-by-okta)
>     *   [Warnings](https://ocelot.readthedocs.io/en/latest/features/authentication.html#warnings)
>     *   [Links](https://ocelot.readthedocs.io/en/latest/features/authentication.html#links)
>     *   [Roadmap](https://ocelot.readthedocs.io/en/latest/features/authentication.html#roadmap)
> 
> *   [Authorization](https://ocelot.readthedocs.io/en/latest/features/authorization.html)
>     *   [Authorization Middleware](https://ocelot.readthedocs.io/en/latest/features/authorization.html#authorization-middleware)
> 
> *   [Caching](https://ocelot.readthedocs.io/en/latest/features/caching.html)
>     *   [Install](https://ocelot.readthedocs.io/en/latest/features/caching.html#install)
>     *   [`CacheOptions` Schema](https://ocelot.readthedocs.io/en/latest/features/caching.html#cacheoptions-schema)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/caching.html#configuration)
>     *   [`EnableContentHashing` option](https://ocelot.readthedocs.io/en/latest/features/caching.html#enablecontenthashing-option)
>     *   [Global Configuration](https://ocelot.readthedocs.io/en/latest/features/caching.html#global-configuration)
>     *   [Custom Caching](https://ocelot.readthedocs.io/en/latest/features/caching.html#custom-caching)
>     *   [Roadmap](https://ocelot.readthedocs.io/en/latest/features/caching.html#roadmap)
> 
> *   [Claims Transformation](https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html)
>     *   [Claims to Claims](https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html#claims-to-claims)
>     *   [Claims to Headers](https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html#claims-to-headers)
>     *   [Claims to Query String Parameters](https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html#claims-to-query-string-parameters)
>     *   [Claims to Downstream Path](https://ocelot.readthedocs.io/en/latest/features/claimstransformation.html#claims-to-downstream-path)
> 
> *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/configuration.html)
>     *   [Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#route-schema)
>     *   [Dynamic Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#dynamic-route-schema)
>     *   [Aggregate Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#aggregate-route-schema)
>     *   [Global Configuration Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#global-configuration-schema)
>     *   [Configuration Overview](https://ocelot.readthedocs.io/en/latest/features/configuration.html#configuration-overview)
>     *   [Multiple Environments](https://ocelot.readthedocs.io/en/latest/features/configuration.html#multiple-environments)
>     *   [Merging Files](https://ocelot.readthedocs.io/en/latest/features/configuration.html#merging-files)
>         *   [Keep files in a folder](https://ocelot.readthedocs.io/en/latest/features/configuration.html#keep-files-in-a-folder)
>         *   [Merging files to memory](https://ocelot.readthedocs.io/en/latest/features/configuration.html#merging-files-to-memory)
> 
>     *   [Reload On Change](https://ocelot.readthedocs.io/en/latest/features/configuration.html#reload-on-change)
>     *   [React to Changes](https://ocelot.readthedocs.io/en/latest/features/configuration.html#react-to-changes)
>     *   [Store in Consul](https://ocelot.readthedocs.io/en/latest/features/configuration.html#store-in-consul)
>     *   [Build From Scratch](https://ocelot.readthedocs.io/en/latest/features/configuration.html#build-from-scratch)
>     *   [`HttpHandlerOptions`](https://ocelot.readthedocs.io/en/latest/features/configuration.html#httphandleroptions)
>     *   [SSL Errors](https://ocelot.readthedocs.io/en/latest/features/configuration.html#ssl-errors)
>     *   [`DownstreamHttpVersion`](https://ocelot.readthedocs.io/en/latest/features/configuration.html#downstreamhttpversion)
>         *   [`DownstreamHttpVersionPolicy`](https://ocelot.readthedocs.io/en/latest/features/configuration.html#downstreamhttpversionpolicy)
>         *   [HTTP2 version policy](https://ocelot.readthedocs.io/en/latest/features/configuration.html#http2-version-policy)
> 
>     *   [Dependency Injection](https://ocelot.readthedocs.io/en/latest/features/configuration.html#dependency-injection)
>     *   [Extend with `Metadata`](https://ocelot.readthedocs.io/en/latest/features/configuration.html#extend-with-metadata)
>     *   [`Timeout`](https://ocelot.readthedocs.io/en/latest/features/configuration.html#timeout)
>         *   [Route timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#route-timeout)
>         *   [Global timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#global-timeout)
>         *   [QoS timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#qos-timeout)
>         *   [Default timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#default-timeout)
> 
> 
> *   [Delegating Handlers](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html#configuration)
>     *   [Execution Order](https://ocelot.readthedocs.io/en/latest/features/delegatinghandlers.html#execution-order)
> 
> *   [Dependency Injection](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html)
>     *   [Services Overview](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#services-overview)
>     *   [`IServiceCollection` extensions](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#iservicecollection-extensions)
>         *   [`AddOcelot` method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#addocelot-method)
>         *   [`AddOcelotUsingBuilder` method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#addocelotusingbuilder-method)
> 
>     *   [`OcelotBuilder` class](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#ocelotbuilder-class)
>         *   [`AddDefaultAspNetServices` method](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#adddefaultaspnetservices-method)
> 
>     *   [Custom Builder](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#custom-builder)
>         *   [Problem](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#problem)
>         *   [Solution](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#solution)
> 
>     *   [Configuration Overview](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#configuration-overview)
>     *   [`IConfigurationBuilder` extensions](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#iconfigurationbuilder-extensions)
>         *   [`AddOcelot` methods](https://ocelot.readthedocs.io/en/latest/features/dependencyinjection.html#addocelot-methods)
> 
> 
> *   [Error Handling](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html)
>     *   [Middleware](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html#middleware)
>     *   [Client Error Responses](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html#client-error-responses)
>     *   [Server Error Responses](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html#server-error-responses)
>     *   [Error Mapper](https://ocelot.readthedocs.io/en/latest/features/errorcodes.html#error-mapper)
> 
> *   [GraphQL](https://ocelot.readthedocs.io/en/latest/features/graphql.html)
>     *   [Sample](https://ocelot.readthedocs.io/en/latest/features/graphql.html#sample)
>     *   [Future](https://ocelot.readthedocs.io/en/latest/features/graphql.html#future)
> 
> *   [Headers Transformation](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html)
>     *   [Schema](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#schema)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#configuration)
>     *   [Find and Replace](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#find-and-replace)
>     *   [Add to Request](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#add-to-request)
>     *   [Add to Response](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#add-to-response)
>     *   [Placeholders](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#placeholders)
>     *   [Samples](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#samples)
>         *   [Handling 302 redirects](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#handling-302-redirects)
>         *   [`X-Forwarded-For` header](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#x-forwarded-for-header)
> 
>     *   [Roadmap](https://ocelot.readthedocs.io/en/latest/features/headerstransformation.html#roadmap)
> 
> *   [Kubernetes (K8s)](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html)
>     *   [Install](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#install)
>     *   [`AddKubernetes(bool)` method](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#addkubernetes-bool-method)
>     *   [`AddKubernetes(Action<KubeClientOptions>)` method](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#addkubernetes-action-kubeclientoptions-method)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#configuration)
>     *   [`Kube` provider](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#kube-provider)
>     *   [`PollKube` provider](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#pollkube-provider)
>     *   [`WatchKube` provider](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#watchkube-provider)
>     *   [Comparing providers](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#comparing-providers)
>     *   [Downstream Scheme vs Port Names](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#downstream-scheme-vs-port-names)
> 
> *   [Load Balancer](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html)
>     *   [`LoadBalancerOptions` Schema](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#loadbalanceroptions-schema)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#configuration)
>         *   [Global Configuration](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#global-configuration)
> 
>     *   [Balancers](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#balancers)
>     *   [`CookieStickySessions` Type](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#cookiestickysessions-type)
>     *   [Custom Balancers](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#custom-balancers)
> 
> *   [Logging](https://ocelot.readthedocs.io/en/latest/features/logging.html)
>     *   [Warning](https://ocelot.readthedocs.io/en/latest/features/logging.html#warning)
>     *   [Best Practices](https://ocelot.readthedocs.io/en/latest/features/logging.html#best-practices)
>     *   [Request ID](https://ocelot.readthedocs.io/en/latest/features/logging.html#request-id)
>         *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/logging.html#configuration)
>         *   [Problem](https://ocelot.readthedocs.io/en/latest/features/logging.html#problem)
>         *   [Technical Facts](https://ocelot.readthedocs.io/en/latest/features/logging.html#technical-facts)
> 
>     *   [Performance](https://ocelot.readthedocs.io/en/latest/features/logging.html#performance)
>     *   [Benchmarks](https://ocelot.readthedocs.io/en/latest/features/logging.html#benchmarks)
> 
> *   [Metadata](https://ocelot.readthedocs.io/en/latest/features/metadata.html)
>     *   [Schema](https://ocelot.readthedocs.io/en/latest/features/metadata.html#schema)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/metadata.html#configuration)
>     *   [`GetMetadata<T>` Method](https://ocelot.readthedocs.io/en/latest/features/metadata.html#getmetadata-t-method)
>     *   [Sample](https://ocelot.readthedocs.io/en/latest/features/metadata.html#sample)
> 
> *   [Method Transformation](https://ocelot.readthedocs.io/en/latest/features/methodtransformation.html)
> *   [Middleware Injection](https://ocelot.readthedocs.io/en/latest/features/middlewareinjection.html)
>     *   [`OcelotPipelineConfiguration` Class](https://ocelot.readthedocs.io/en/latest/features/middlewareinjection.html#ocelotpipelineconfiguration-class)
>     *   [Ocelot Pipeline Builder](https://ocelot.readthedocs.io/en/latest/features/middlewareinjection.html#ocelot-pipeline-builder)
>     *   [Roadmap](https://ocelot.readthedocs.io/en/latest/features/middlewareinjection.html#roadmap)
> 
> *   [Quality of Service](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html)
>     *   [Installation](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#installation)
>     *   [`QoSOptions` Schema](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qosoptions-schema)
>     *   [Global Configuration](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#global-configuration)
>     *   [Circuit Breaker strategy](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#circuit-breaker-strategy)
>     *   [Timeout strategy](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#timeout-strategy)
>     *   [Notes](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#notes)
>         *   [Absolute timeout](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#absolute-timeout)
>         *   [Value constraints](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#value-constraints)
>         *   [QoS and route (global) timeouts](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-and-route-global-timeouts)
>         *   [Global and default QoS timeouts](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#global-and-default-qos-timeouts)
> 
>     *   [Extensibility](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#extensibility)
> 
> *   [Rate Limiting](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html)
>     *   [`RateLimitOptions` Schema](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#ratelimitoptions-schema)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#configuration)
>         *   [Deprecated options](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#deprecated-options)
> 
>     *   [Notes](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#notes)
>     *   [Algorithms](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#algorithms)
>     *   [Rules (Partitions)](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#rules-partitions)
>         *   [By Client’s Header](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#by-client-s-header)
> 
>     *   [Roadmap](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#roadmap)
> 
> *   [Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html)
>     *   [Placeholders](https://ocelot.readthedocs.io/en/latest/features/routing.html#placeholders)
>         *   [Embedded Placeholders](https://ocelot.readthedocs.io/en/latest/features/routing.html#embedded-placeholders)
>         *   [Empty Placeholders](https://ocelot.readthedocs.io/en/latest/features/routing.html#empty-placeholders)
> 
>     *   [Catch All](https://ocelot.readthedocs.io/en/latest/features/routing.html#catch-all)
>     *   [Priority](https://ocelot.readthedocs.io/en/latest/features/routing.html#priority)
>     *   [Query Placeholders](https://ocelot.readthedocs.io/en/latest/features/routing.html#query-placeholders)
>         *   [Path to Query String direction](https://ocelot.readthedocs.io/en/latest/features/routing.html#path-to-query-string-direction)
>         *   [Query String to Path direction](https://ocelot.readthedocs.io/en/latest/features/routing.html#query-string-to-path-direction)
>         *   [Catch All Query String](https://ocelot.readthedocs.io/en/latest/features/routing.html#catch-all-query-string)
>         *   [Merging of Query Parameters](https://ocelot.readthedocs.io/en/latest/features/routing.html#merging-of-query-parameters)
> 
>     *   [Upstream Host](https://ocelot.readthedocs.io/en/latest/features/routing.html#upstream-host)
>     *   [Upstream Headers](https://ocelot.readthedocs.io/en/latest/features/routing.html#upstream-headers)
>         *   [Header placeholders](https://ocelot.readthedocs.io/en/latest/features/routing.html#header-placeholders)
> 
>     *   [Security Options](https://ocelot.readthedocs.io/en/latest/features/routing.html#security-options)
>     *   [Dynamic Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html#dynamic-routing)
>     *   [Errors and Gotchas](https://ocelot.readthedocs.io/en/latest/features/routing.html#errors-and-gotchas)
> 
> *   [Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html)
>     *   [Consul](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#consul)
>         *   [Configuration in KV Store](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#configuration-in-kv-store)
>         *   [Configuration Key](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#configuration-key)
>         *   [`Consul` Provider](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#consul-provider)
>         *   [`PollConsul` Provider](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#pollconsul-provider)
>         *   [Service Definition](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#service-definition)
>         *   [ACL Token](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#acl-token)
>         *   [Consul Service Builder](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#consul-service-builder)
> 
>     *   [Eureka](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#eureka)
>     *   [Service Fabric](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#service-fabric)
>     *   [Dynamic Routing](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#dynamic-routing)
>         *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#configuration)
> 
>     *   [Custom Providers](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#custom-providers)
>     *   [Sample](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#sample)
>         *   [DownstreamService](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#downstreamservice)
>         *   [ApiGateway](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#apigateway)
> 
> 
> *   [Service Fabric](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html#configuration)
>     *   [Placeholders](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html#placeholders)
>     *   [Sample](https://ocelot.readthedocs.io/en/latest/features/servicefabric.html#sample)
> 
> *   [Tracing](https://ocelot.readthedocs.io/en/latest/features/tracing.html)
>     *   [OpenTracing](https://ocelot.readthedocs.io/en/latest/features/tracing.html#opentracing-csharp-logo-opentracing)
>     *   [Butterfly](https://ocelot.readthedocs.io/en/latest/features/tracing.html#butterfly)
> 
> *   [Websockets](https://ocelot.readthedocs.io/en/latest/features/websockets.html)
>     *   [Configuration](https://ocelot.readthedocs.io/en/latest/features/websockets.html#configuration)
>     *   [Handy Links](https://ocelot.readthedocs.io/en/latest/features/websockets.html#handy-links)
>     *   [SignalR](https://ocelot.readthedocs.io/en/latest/features/websockets.html#signalr)
>     *   [WebSocket Secure](https://ocelot.readthedocs.io/en/latest/features/websockets.html#websocket-secure)
>     *   [Supported](https://ocelot.readthedocs.io/en/latest/features/websockets.html#supported)
>     *   [Not Supported](https://ocelot.readthedocs.io/en/latest/features/websockets.html#not-supported)
>     *   [Roadmap](https://ocelot.readthedocs.io/en/latest/features/websockets.html#roadmap)
> 
> 
> 
> Building Ocelot
> 
> 
> *   [Building](https://ocelot.readthedocs.io/en/latest/building/building.html)
>     *   [In IDE](https://ocelot.readthedocs.io/en/latest/building/building.html#in-ide)
>     *   [In terminal](https://ocelot.readthedocs.io/en/latest/building/building.html#in-terminal)
>     *   [With Docker](https://ocelot.readthedocs.io/en/latest/building/building.html#with-docker)
>     *   [With CI/CD](https://ocelot.readthedocs.io/en/latest/building/building.html#with-ci-cd)
>     *   [Documentation](https://ocelot.readthedocs.io/en/latest/building/building.html#documentation)
>     *   [Testing](https://ocelot.readthedocs.io/en/latest/building/building.html#testing)
>     *   [SSL certificate](https://ocelot.readthedocs.io/en/latest/building/building.html#ssl-certificate)
> 
> *   [Development Process](https://ocelot.readthedocs.io/en/latest/building/devprocess.html)
>     *   [Stages](https://ocelot.readthedocs.io/en/latest/building/devprocess.html#stages)
>     *   [Notes](https://ocelot.readthedocs.io/en/latest/building/devprocess.html#notes)
>     *   [Best Practices](https://ocelot.readthedocs.io/en/latest/building/devprocess.html#best-practices)
>     *   [Dev Fun](https://ocelot.readthedocs.io/en/latest/building/devprocess.html#dev-fun)
>         *   [EOL Gotchas](https://ocelot.readthedocs.io/en/latest/building/devprocess.html#eol-gotchas)
> 
> 
> *   [Release Process](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html)
>     *   [Stages](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html#stages)
>     *   [Notes](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html#notes)
>     *   [Quality Gates](https://ocelot.readthedocs.io/en/latest/building/releaseprocess.html#quality-gates)
