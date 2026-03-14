# Source: https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html

Title: Rate Limiting — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html

Markdown Content:
Ocelot implements _rate limiting_[[1]](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#f1) for upstream requests to prevent downstream services from being overwhelmed.

`RateLimitOptions` Schema[¶](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#ratelimitoptions-schema "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

As you may already know from the [Configuration](https://ocelot.readthedocs.io/en/latest/features/configuration.html) chapter and the [Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-route-schema) and [Dynamic Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-dynamic-route-schema) sections, there is a special `RateLimitOptions` object schema for routes:

"RateLimitOptions": {
 // rule, partition by
 "ClientIdHeader": "",
 "ClientWhitelist": [""],
 // management opts
 "EnableRateLimiting": true,
 "EnableHeaders": true,
 // algorithm
 "Limit": 1,
 "Period": "",
 "Wait": "",
 // extended opts
 "StatusCode": 1,
 "QuotaMessage": "",
 "KeyPrefix": ""
}

Additionally, the [Global Configuration Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-global-configuration-schema) allows configuring global _Rate Limiting_ options.

> **Note 1**: The complete route-level `RateLimitOptions` schema, including all available properties, is defined in the C# [FileRateLimitByHeaderRule](https://github.com/ThreeMammals/Ocelot/blob/main/src/Ocelot/Configuration/File/FileRateLimitByHeaderRule.cs) class. The global `RateLimitOptions` schema includes an additional `RouteKeys` array option, which allows grouping routes to which the global options will apply (refer to the C# [FileGlobalRateLimitByHeaderRule](https://github.com/ThreeMammals/Ocelot/blob/main/src/Ocelot/Configuration/File/FileGlobalRateLimitByHeaderRule.cs) class for details). If the `RouteKeys` option is not defined in the global `RateLimitOptions`, the global settings will apply to all routes.
> 
> 
> **Note 2**: You do not need to set all of these options due to default values, but the following rule options are required: `Limit` and `Period`. If these required options are undefined and no global configuration is present, Ocelot will fail to start due to an internally generated validation error, which will be visible in the logs.
> 
> 
> **Note 3**: Several [deprecated options](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#rl-deprecated-options) originating from version [24.0](https://github.com/ThreeMammals/Ocelot/releases/tag/24.0.0) and earlier (see [old schema](https://github.com/ThreeMammals/Ocelot/blob/24.0.0/src/Ocelot/Configuration/File/FileRateLimitOptions.cs)) are retained for one release cycle. Both introduced and [deprecated options](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#rl-deprecated-options) are detailed in the [Configuration 2](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#rl-configuration) table below.

Configuration [[2]](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#f2)[¶](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#configuration "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

A complete configuration consists of both route-level and global _Rate Limiting_. You can configure the following options in the `GlobalConfiguration` section of [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main//samples/Basic/ocelot.json):

"Routes": [
 {
 "Key": "R1",
 "RateLimitOptions": {
 "ClientWhitelist": ["ocelot-client1-preshared-key"],
 "Limit": 1000,
 "Period": "20s", // (milli)seconds, minutes, hours, days
 "Wait": "1.5m" // (milli)seconds, minutes, hours, days
 "StatusCode": 418, // I'm a teapot -> this is special status
 "QuotaMessage": "Out of coffee! Our bar can only serve up to {0} cups of coffee every {1}. In the meantime, why not grab some tea and relax for Retry-After seconds until we're ready to serve again?"
 }
 }
],
"GlobalConfiguration": {
 "BaseUrl": "https://api.ocelot.net",
 "RateLimitOptions": {
 "RouteKeys": ["R1"], // if undefined or empty array, opts will apply to all routes
 "ClientIdHeader": "Oc-Client", // std (default) header name
 "Limit": 100,
 "Period": "30s", // ms, s, m, h, d
 "Wait": "1m", // ms, s, m, h, d
 "StatusCode": 429, // Too Many Requests -> standard status
 "QuotaMessage": "Ocelot API calls quota exceeded! Maximum admitted {0} per {1}.", // standard template with 2 parameters
 "KeyPrefix": "ocelot-rate-limiting" // for caching key
 }
}

| [Schema](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#rl-schema) Option | Description |
| --- | --- |
| `ClientIdHeader` | Specifies the header used to identify clients, with “Oc-Client” set as the default. |
| `ClientWhitelist` | An array that contains the clients exempt from _rate limiting_. |
| `EnableRateLimiting` | Enables or disables rate limiting. Defaults to `true` (enabled). |
| `EnableHeaders` | Specifies whether the `X-RateLimit-*` and `Retry-After` headers are enabled. If undefined, defaults to `true` (enabled). |
| `Limit` | The maximum number of requests a client can make within a given time `Period`. |
| `Period` | Rate limiting period (fixed window) can be expressed as milliseconds (1ms), as seconds (1s), minutes (1m), hours (1h), or days (1d). If the exact `Limit` of requests is reached (quota exceeded*), the request is immediately blocked, and if `Wait` is defined, a waiting period begins. |
| `Wait` | Rate limiting wait window (no servicing period) can be expressed as milliseconds (1ms), as seconds (1s), minutes (1m), hours (1h), or days (1d). This option can have shorter or longer durations compared to the fixed window duration specified as `Period`. The waiting interval either extends or shortens the Quota Exceeded period*, which typically ends after the fixed window elapses. |
| `StatusCode` | The rejection status code returned during the Quota Exceeded period*. Default value: 429 ([Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)). |
| `QuotaMessage` | Specifies the message displayed when the quota is exceeded. The value to be used as the formatter for the Quota Exceeded* response message. If none specified the default will be informative. |
| `KeyPrefix` | The counter prefix, used to compose the rate limiting counter caching key to be used by the `IRateLimitStorage` service. Default value: “Ocelot.RateLimiting” |

“Quota Exceeded period” term

The **Quota Exceeded period** refers to the `Wait` window, if defined, or the remaining duration of the fixed `Period` following the moment the request `Limit` is exceeded. During this time, the configured rejection `StatusCode` is returned, and the formatted `QuotaMessage` is written to the response body. To determine when this period ends, clients should inspect the `Retry-After` header, which provides a floating-point value indicating the number of seconds until the next allocated fixed window begins. The `X-RateLimit-*` headers are included in the response during the _Quota Exceeded period_, provided that headers are enabled via the `EnableHeaders` option.

> **Note 1**: If the `RouteKeys` option is not defined or the array is empty in the global `RateLimitOptions`, the global settings will apply to all routes. If the array contains route keys, it defines a single group of routes to which the global options apply. Routes excluded from this group must specify their own route-level `RateLimitOptions`.
> 
> 
> **Note 2**: The string values for the `Period` and `Wait` options must contain a floating-point number followed by one of the supported time units: ‘ms’, ‘s’, ‘m’, ‘h’, or ‘d’. If no unit is specified, the value defaults to milliseconds. For example, “333.5” is interpreted as 333 milliseconds and 500 microseconds (equivalent to “333.5ms”). The floating-point component may be omitted; for example, “10.0s” is equivalent to “10s”. These values are parsed dynamically at runtime, so the required `Period` option in [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main//samples/Basic/ocelot.json) is validated early through fluent validation when the Ocelot app starts. If an invalid value is provided, the _Rate Limiting_ middleware will throw a `FormatException`, which is logged accordingly.

### Deprecated options [[3]](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#f3)[¶](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#deprecated-options "Link to this heading")

Warning

Here are the deprecated options from the [old schema](https://github.com/ThreeMammals/Ocelot/blob/24.0.0/src/Ocelot/Configuration/File/FileRateLimitOptions.cs):

| _Deprecated and Introduced Options_ | _Description_ |
| --- | --- |
| `DisableRateLimitHeaders` and `EnableHeaders` | Specifies whether the `X-RateLimit-*` and `Retry-After` headers are disabled. |
| `PeriodTimespan` and `Wait` | This parameter specifies the time, in **seconds**, after which a retry is allowed. During this interval, the `QuotaExceededMessage` will be included in the response, along with the corresponding `HttpStatusCode`. Clients are encouraged to refer to the `Retry-After` header to determine when subsequent requests can be made. |
| `HttpStatusCode` and `StatusCode` | Specifies the HTTP status code returned during _rate limiting_, with a default value of **429** ([Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429)). |
| `QuotaExceededMessage` and `QuotaMessage` | Specifies the message displayed when the quota is exceeded. This option is optional, and the default message is informative. |
| `RateLimitCounterPrefix` and `KeyPrefix` | Specifies the counter prefix used to construct the _rate limiting_ counter cache key. |

Notes[¶](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#notes "Link to this heading")
---------------------------------------------------------------------------------------------------------

Note

1. Prior to version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global options were only accessible in the special [Dynamic Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-dynamic) mode. Since version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global configuration has been available for both static and dynamic routes. As a team, we would consider the idea of implementing such a global configuration for aggregated routes. However, an aggregated route is essentially a combination of static routes.

2. Global _rate limiting_ options may not be practical as they apply limits to all routes. In a microservices architecture, it is unusual to enforce the same limitations across all routes. Configuring per-route _rate limiting_ could offer a more tailored solution. However, global _rate limiting_ can be logical if all routes share the same downstream hosts, thereby restricting the usage of a single service or a single product.

3. The `DisableRateLimitHeaders` option is deprecated as of version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0). Use `EnableHeaders` instead, applying boolean value negation as needed. If `DisableRateLimitHeaders` is defined, it takes precedence; otherwise, `EnableHeaders` will be used. Do not define both options. This setting is retained for backward compatibility but is subject to change. Therefore, the `DisableRateLimitHeaders` option will be removed in the upcoming major release, version [25.0](https://github.com/ThreeMammals/Ocelot/milestone/13). The same applies to other [deprecated options](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#rl-deprecated-options).

4. Ocelot’s own _rate limiting_ does not utilize built-in ASP.NET Core features, so it is not based on the “[Rate limiting middleware in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/rate-limit)” described in the [Roadmap](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#rl-roadmap) below. The Ocelot team believes that the ASP.NET Core rate limiting middleware enables global limitations through its rate-limiting policies.

Algorithms[¶](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#algorithms "Link to this heading")
-------------------------------------------------------------------------------------------------------------------

The currently implemented rate limiter algorithms in Ocelot are:

*   **Fixed window**: Based on the `Period` option, without the `Wait` option (previously known as the deprecated `PeriodTimespan`).

*   **Hybrid fixed window**: The combination of `Period` and `Wait` enables fixed-window-like behavior with additional control over the duration and handling of the _“Quota Exceeded period”_.

Historically, Ocelot’s rate limiting algorithm was a hybrid, combining the classic “fixed window” approach with a waiting no-service period. Since version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), the hybrid algorithm has been split into two distinct algorithms, allowing the classic “fixed window” to be used independently.

To understand the terminology, please refer to the Handy Articles listed at the beginning of this chapter. For beginners, here is a quick link: [Announcing ASP.NET Core rate limiting algorithms](https://devblogs.microsoft.com/dotnet/announcing-rate-limiting-for-dotnet/#what-is-rate-limiting:~:text=There%20are%20multiple%20different%20rate%20limiting%20algorithms%20to%20control%20the%20flow%20of%20requests.). For professionals, we recommend reading the official Microsoft Learn article “[Rate limiting middleware in ASP.NET Core](https://learn.microsoft.com/en-us/aspnet/core/performance/rate-limit)”, especially the [Rate Limiter Algorithms](https://learn.microsoft.com/en-us/aspnet/core/performance/rate-limit?view=aspnetcore-9.0#rate-limiter-algorithms) section, and/or searching the internet for additional resources.

> **Note 1**: Ocelot’s own rate limiter does not implement other classic algorithms such as “Sliding Window”, “Token Bucket”, or “Concurrency”. However, these algorithms are outlined in the [Roadmap](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#rl-roadmap).
> 
> 
> **Note 2**: Ocelot’s own rate limiter does not manage concurrent HTTP requests via a queue. Therefore, all concurrency handling and decision-making should be implemented on the client side using classic retry patterns to ensure quality of service. The management strategy is deliberately simple: _First-In means First Wins_. If the first request acquires a virtual lease from the limiting quota and the quota is immediately exceeded, the second request will be rejected with a 429 [Too Many Requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) response.

Rules (Partitions)[¶](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#rules-partitions "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

Ocelot’s rate limiting _rule_ is a superset of the configuration options used to set up rate-limited access to a route. It enables partitioned rate limiting by processing the following artifacts through distinct stages: the client’s identifier, a dedicated partition counter (quota), rate limiter algorithms, and the quota-exceeded response behavior.

Roadmap[¶](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#roadmap "Link to this heading")
-------------------------------------------------------------------------------------------------------------

> Feature label: [`Rate Limiting`_](https://ocelot.readthedocs.io/en/latest/features/ratelimiting.html#id17)

*   **Rules**: The Ocelot team is considering a redesign of the _Rate Limiting_ feature in light of the “[Announcing Rate Limiting for .NET](https://devblogs.microsoft.com/dotnet/announcing-rate-limiting-for-dotnet/)” article by Brennan Conroy, published on July 13th, 2022.

As of now, the decision has been made to retain Ocelot’s own [RateLimitingMiddleware](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20RateLimitingMiddleware&type=code) and extend it with an additional rule that will reference the attached ASP.NET Core rate limiting policy. This new rule is highly likely to be delivered in version [25.0](https://github.com/ThreeMammals/Ocelot/milestone/13), following the opening of pull request [2188](https://github.com/ThreeMammals/Ocelot/pull/2188).

*   **Algorithms**: In addition to the currently implemented hybrid “Fixed window” algorithm, which is built into Ocelot, the team plans to introduce other industry-standard algorithms, such as “Sliding window”, “Token bucket”, and “Concurrency, with priority given to “Sliding window” as the first. These lightweight algorithms should be easily configurable via JSON by end users who are not .NET developers, in order to avoid writing additional C# source code. Other interesting algorithms are welcome for discussion.

We encourage you to share your thoughts with us in the [Discussions](https://github.com/ThreeMammals/Ocelot/discussions) of the repository. [![Image 1: octocat](https://github.githubassets.com/images/icons/emoji/octocat.png)](https://github.githubassets.com/images/icons/emoji/octocat.png) Filter the current discussions by the [Rate Limiting](https://github.com/ThreeMammals/Ocelot/discussions?discussions_q=label%3A%22Rate+Limiting%22) label.

* * *
