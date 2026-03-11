# Source: https://ocelot.readthedocs.io/en/latest/features/caching.html

Title: Caching — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/caching.html

Markdown Content:
[[1]](https://ocelot.readthedocs.io/en/latest/features/caching.html#f1) Ocelot currently supports caching on the URL of the downstream service and setting a TTL in seconds to expire the cache. Users can also clear the cache for a specific region by using Ocelot’s [Administration API](https://ocelot.readthedocs.io/en/latest/features/administration.html#administration-api).

Ocelot utilizes some very rudimentary caching at the moment provider by the [CacheManager](https://github.com/MichaCo/CacheManager) project. This is an amazing project that is solving a lot of caching problems. We would recommend using this package to cache with Ocelot.

The following example shows how to add _CacheManager_ to Ocelot so that you can do output caching.

Install[¶](https://ocelot.readthedocs.io/en/latest/features/caching.html#install "Link to this heading")
--------------------------------------------------------------------------------------------------------

First of all, add the following [Ocelot.Cache.CacheManager](https://www.nuget.org/packages/Ocelot.Cache.CacheManager) package:

Install-Package Ocelot.Cache.CacheManager

This will give you access to the Ocelot cache manager extension methods. The second step is to add the following to your [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs):

using Ocelot.Cache.CacheManager;

builder.Services
 .AddOcelot(builder.Configuration)
 .AddCacheManager(x => x.WithDictionaryHandle());

`CacheOptions` Schema[¶](https://ocelot.readthedocs.io/en/latest/features/caching.html#cacheoptions-schema "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------

The following is the full _caching_ configuration, used in both the [Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-route-schema) and the [Dynamic Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-dynamic-route-schema). Not all of these options need to be configured; however, the `TtlSeconds` option is mandatory.

"CacheOptions": {
 "TtlSeconds": 1, // nullable integer
 "Region": "", // string
 "Header": "", // string
 "EnableContentHashing": false // nullable boolean
}

| _Option_ | _Description_ |
| --- | --- |
| `TtlSeconds` | Time-To-Live (TTL) in seconds for the cached downstream response, i.e., the absolute expiration timeout starting from when the item is added to the cache. This option is required. If undefined, it defaults to 0 (zero), which disables caching. |
| `Region` | Specifies the cache region to be cleared via Ocelot’s [Administration API](https://ocelot.readthedocs.io/en/latest/features/administration.html#administration-api). See: `DELETE {adminPath}/outputcache/{region}` |
| `Header` | Specifies the header name used for native Ocelot caching control, defaulting to the special `OC-Cache-Control` header. If the header is present, its value is included in the cache key constructed by the `ICacheKeyGenerator` service. Varying header values result in different cache keys, effectively invalidating the cache. |
| `EnableContentHashing` | Toggles inclusion of request body hashing in the cache key. Disabled by default (`false`) due to potential performance impact. Recommended for POST/PUT routes where request body affects response. Refer to the [EnableContentHashing option](https://ocelot.readthedocs.io/en/latest/features/caching.html#caching-enablecontenthashing-option) section. |

The actual `CacheOptions` schema with all the properties can be found in the C# [FileCacheOptions](https://github.com/ThreeMammals/Ocelot/blob/main/src/Ocelot/Configuration/File/FileCacheOptions.cs) class.

Configuration[¶](https://ocelot.readthedocs.io/en/latest/features/caching.html#configuration "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

Finally, in order to use caching on a route in your route configuration add these sections:

"CacheOptions": {
 "TtlSeconds": 15,
 "Region": "europe-central",
 "Header": "OC-Cache-Control",
 "EnableContentHashing": false // my route has GET verb only, assigning 'true' for requests with body: POST, PUT etc.
},
// Warning! FileCacheOptions section is deprecated! -> use CacheOptions
"FileCacheOptions": {
 "TtlSeconds": 15,
 "Region": "europe-central",
 "Header": "OC-Cache-Control",
 "EnableContentHashing": false // my route has GET verb only, assigning 'true' for requests with body: POST, PUT etc.
}

*   In this example, `TtlSeconds` is set to 15, which means the cache will expire 15 seconds after the response is stored.

*   The `Region` property specifies a cache region. Cache entries within a region can be cleared by calling Ocelot’s [Administration API](https://ocelot.readthedocs.io/en/latest/features/administration.html#administration-api).

*   If a header name is defined in the `Header` property, its value is retrieved from the `HttpRequest` headers. If the header is present, its value is included in the cache key constructed by the `ICacheKeyGenerator` service. Varying header values result in different cache keys, effectively invalidating the cache.

*   Finally, `EnableContentHashing` is disabled due to the current route using the `GET` verb, which does not include a request body.

Warning

According to the static [Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-route-schema), the `FileCacheOptions` section has been deprecated!

The [old schema](https://github.com/ThreeMammals/Ocelot/blob/24.1.0/src/Ocelot/Configuration/File/FileRoute.cs#L86-L88)`FileCacheOptions` section is deprecated in version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0)! Use `CacheOptions` instead of `FileCacheOptions`! Note that `FileCacheOptions` will be removed in version [25.0](https://github.com/ThreeMammals/Ocelot/milestone/13)! For backward compatibility in version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), the `FileCacheOptions` section takes precedence over the `CacheOptions` section.

`EnableContentHashing` option [[2]](https://ocelot.readthedocs.io/en/latest/features/caching.html#f2)[¶](https://ocelot.readthedocs.io/en/latest/features/caching.html#enablecontenthashing-option "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Previously, in versions prior to [23.0](https://github.com/ThreeMammals/Ocelot/releases/tag/23.0.0), the request body was used to compute the cache key. However, due to potential performance issues arising from request body hashing, it has been disabled by default. Clearly, this constitutes a breaking change and presents challenges for users who require cache key calculations that consider the request body (e.g., for the POST method). To address this issue, it is recommended to enable the option either at the route level or globally in the “[Global Configuration](https://ocelot.readthedocs.io/en/latest/features/caching.html#caching-global-configuration)” section:

"CacheOptions": {
 // ...
 "EnableContentHashing": true
}

Ocelot Team Recommendation

Although the community raised concerns about backward compatibility in issue [2234](https://github.com/ThreeMammals/Ocelot/issues/2234), Ocelot team maintains that _caching_ performance takes precedence over backward compatibility when migrating from versions prior to [23.0](https://github.com/ThreeMammals/Ocelot/releases/tag/23.0.0). The proposed option clarifies that `POST` requests should **not** be cached; only `GET` requests are eligible for caching. Therefore, `POST` and `GET` verbs must be separated into distinct routes:

*   POST routes with _caching_ disabled

*   GET routes with _caching_ enabled

Global Configuration [[3]](https://ocelot.readthedocs.io/en/latest/features/caching.html#f3)[¶](https://ocelot.readthedocs.io/en/latest/features/caching.html#global-configuration "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Copying route-level properties for each static route is no longer necessary, as version [23.3](https://github.com/ThreeMammals/Ocelot/releases/tag/23.3.0) allows these values to be set in the `GlobalConfiguration` section. This convenience applies to `Header` and `Region` as well. However, if no global `TtlSeconds` value is defined, this option must still be explicitly set per route to enable caching. As a result, the final configuration for static routes might look like:

{
 "Routes": [
 {
 "Key": "R0", // optional
 "CacheOptions": { "TtlSeconds": 60 // 1-minute short-term caching }, // ...
 },
 {
 "Key": "R1", // this route is part of a group
 "CacheOptions": {}, // optional due to grouping // ...
 }
 ],
 "GlobalConfiguration": {
 "BaseUrl": "https://ocelot.net",
 "CacheOptions": { "RouteKeys": ["R1",], // if undefined or empty array, opts will apply to all routes "TtlSeconds": 300 // enable global caching for a duration of 5 minutes }, // ...
 }
}

Dynamic routes were not supported in versions prior to [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0). Starting with version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global _cache options_ for [Dynamic Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-dynamic) were introduced. These global options may also be overridden in the `DynamicRoutes` configuration section, as defined by the [Dynamic Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-dynamic-route-schema).

{
 "DynamicRoutes": [
 {
 "Key": "", // optional
 "ServiceName": "my-service",
 "CacheOptions": { "TtlSeconds": 60 // 1-minute short-term caching } }
 ],
 "GlobalConfiguration": {
 "BaseUrl": "https://ocelot.net",
 "DownstreamScheme": "http",
 "ServiceDiscoveryProvider": {
 // required section for dynamic routing
 },
 "CacheOptions": { "RouteKeys": [], // or null, no grouping, thus opts apply to all dynamic routes "TtlSeconds": 300 // enable global caching for a duration of 5 minutes } }
}

In this configuration, a 5-minute _caching_ duration is applied to all implicit dynamic routes. However, for the “my-service” service, the _caching_ TTL has been explicitly reduced from 5 minutes to 1 minute.

Note

1. If the `RouteKeys` option is not defined or the array is empty in the global `CacheOptions`, the global options will apply to all routes. If the array contains route keys, it defines a single group of routes to which the global options apply. Routes excluded from this group must specify their own route-level `CacheOptions`.

2. Prior to version [23.3](https://github.com/ThreeMammals/Ocelot/releases/tag/23.3.0), global `CacheOptions` were not available. Starting with version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global configuration is supported for both static and dynamic routes.

Custom Caching[¶](https://ocelot.readthedocs.io/en/latest/features/caching.html#custom-caching "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

If you want to add your own caching method, implement the following interfaces and register them in DI e.g.

builder.Services
 .AddSingleton<IOcelotCache<CachedResponse>, MyCache>();

*   `IOcelotCache<CachedResponse>` this is for output caching.

*   `IOcelotCache<FileConfiguration>` this is for caching the file configuration if you are calling something remote to get your config such as Consul.

Roadmap[¶](https://ocelot.readthedocs.io/en/latest/features/caching.html#roadmap "Link to this heading")
--------------------------------------------------------------------------------------------------------

Please dig into the Ocelot source code to find more. We would really appreciate it if anyone wants to implement [Redis](https://redis.io/), [Memcached](http://www.memcached.org/) etc. Please, open a new [Show and tell](https://github.com/ThreeMammals/Ocelot/discussions/categories/show-and-tell) thread in [Discussions](https://github.com/ThreeMammals/Ocelot/discussions) space of the repository.

* * *
