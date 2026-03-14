# Source: https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html

Title: Quality of Service — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html

Published Time: Thu, 25 Dec 2025 17:17:36 GMT

Markdown Content:
> Repository Label: [![Image 1: label QoS](https://img.shields.io/badge/-QoS-D3ADAF.svg)](https://github.com/ThreeMammals/Ocelot/labels/QoS)

Ocelot currently supports a single _Quality of Service_ (QoS) capability. It allows you to configure, on a per-route basis, the application of a circuit breaker when making requests to downstream services. This feature leverages a well-regarded .NET library known as [Polly](https://www.pollydocs.org/). For more details, visit the [Polly](https://www.pollydocs.org/) library’s official [repository](https://github.com/App-vNext/Polly).

Note

[Polly](https://www.pollydocs.org/) v7 syntax is no longer supported as of version [23.2](https://github.com/ThreeMammals/Ocelot/releases/tag/23.2.0), when the Ocelot team upgraded Polly [from v7 to v8](https://www.pollydocs.org/migration-v8.html).

Installation[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#installation "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

To utilize the _Quality of Service_ via [Polly](https://www.pollydocs.org/) library, begin by importing the appropriate [Ocelot.Provider.Polly](https://www.nuget.org/packages/Ocelot.Provider.Polly) extension package:

Install-Package Ocelot.Provider.Polly

Next, in your [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs), incorporate [Polly](https://www.pollydocs.org/) services by invoking the `AddPolly()` extension on the `OcelotBuilder`, as shown below [[1]](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#f1):

using Ocelot.Provider.Polly;

builder.Services
 .AddOcelot(builder.Configuration)
 .AddPolly();

`QoSOptions` Schema[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qosoptions-schema "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------

Here is the complete _Quality of Service_ configuration, also known as the “QoS options schema”. Depending on your needs and choosen strategies definition of all properties are not required. If you skip a property then a default value will be substituted as per Ocelot/Polly specification.

"QoSOptions": {
 // Circuit Breaker strategy
 "BreakDuration": 0, // integer
 "MinimumThroughput": 0, // integer
 "FailureRatio": 0.0, // floating number
 "SamplingDuration": 0, // integer
 // Timeout strategy
 "Timeout": 0, // integer
 // Deprecated options
 "DurationOfBreak": 0, // deprecated! -> use BreakDuration
 "ExceptionsAllowedBeforeBreaking": 0, // deprecated! -> use MinimumThroughput
 "TimeoutValue": 0, // deprecated! -> use Timeout
}

| _Ocelot Option and Polly equivalent_ | _Description_ |
| --- | --- |
| `BreakDuration` (formerly `DurationOfBreak`) as [BreakDuration](https://www.pollydocs.org/api/Polly.CircuitBreaker.CircuitBreakerStrategyOptions-1.html#Polly_CircuitBreaker_CircuitBreakerStrategyOptions_1_BreakDuration) | This is duration of break the circuit will stay open before resetting. The unit is milliseconds. |
| `MinimumThroughput` (formerly `ExceptionsAllowedBeforeBreaking`) as [MinimumThroughput](https://www.pollydocs.org/api/Polly.CircuitBreaker.CircuitBreakerStrategyOptions-1.html#Polly_CircuitBreaker_CircuitBreakerStrategyOptions_1_MinimumThroughput), a primary option | This number of actions or more must pass through the circuit within the time slice for the statistics to be considered significant and for the circuit breaker to engage |
| `FailureRatio` is [FailureRatio](https://www.pollydocs.org/api/Polly.CircuitBreaker.CircuitBreakerStrategyOptions-1.html#Polly_CircuitBreaker_CircuitBreakerStrategyOptions_1_FailureRatio) | This is the failure-to-success ratio at which the circuit will break |
| `SamplingDuration` is [SamplingDuration](https://www.pollydocs.org/api/Polly.CircuitBreaker.CircuitBreakerStrategyOptions-1.html#Polly_CircuitBreaker_CircuitBreakerStrategyOptions_1_SamplingDuration) | This is the duration of the sampling over which failure ratios are assessed. The unit is milliseconds. |
| `Timeout` (formerly `TimeoutValue`) as [Timeout](https://www.pollydocs.org/api/Polly.Timeout.TimeoutStrategyOptions.html#Polly_Timeout_TimeoutStrategyOptions_Timeout), a primary option | This is the default timeout. The unit is milliseconds. |

Warning

The following options are deprecated in version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0): `DurationOfBreak`, `ExceptionsAllowedBeforeBreaking`, and `TimeoutValue`! Use the appropriate new options as shown in the table above. These deprecated options will be removed in version [25.0](https://github.com/ThreeMammals/Ocelot/releases/tag/25.0.0). For backward compatibility in version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), a deprecated option takes precedence over its replacement.

> **Note**[[2]](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#f2): Ocelot checks that the values of options are valid during execution. If not, it logs errors or warnings (refer to the [Value constraints](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-notes-value-constraints) section in [Notes](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-notes)). For a complete explanation about strategies and mechanisms, consult Polly’s [Resilience strategies](https://www.pollydocs.org/strategies/index.html) documentation.

Global Configuration [[3]](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#f3)[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#global-configuration "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

According to the [Global Configuration Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-global-configuration-schema), global _Quality of Service_ options for static routes were introduced in version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0). These global options can also be overridden in the `Routes` configuration section, a capability that has been supported for a long time.

{
 "Routes": [
 {
 "Key": "R0", // optional
 "QoSOptions": { "Timeout": 15000 // 15s }, // ...
 },
 {
 "Key": "R1", // this route is part of a group
 "QoSOptions": {}, // optional due to grouping // ...
 }
 ],
 "GlobalConfiguration": {
 "BaseUrl": "https://ocelot.net",
 "QoSOptions": { "RouteKeys": ["R1",], // if undefined or empty array, opts will apply to all routes "BreakDuration": 1000, // 1s "MinimumThroughput": 3 },
 // ...
 }
}

Dynamic routes were not supported in versions prior to [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0). However, global _Quality of Service_ options have been available in [Dynamic Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-dynamic) mode for a long time. Starting with version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global _QoS_ options can also be overridden in the `DynamicRoutes` configuration section, as defined by the [Dynamic Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-dynamic-route-schema).

{
 "DynamicRoutes": [
 {
 "Key": "", // optional
 "ServiceName": "my-service",
 "QoSOptions": { "Timeout": 15000 // 15s }, }
 ],
 "GlobalConfiguration": {
 "BaseUrl": "https://ocelot.net",
 "DownstreamScheme": "http",
 "ServiceDiscoveryProvider": {
 // required section for dynamic routing
 },
 "QoSOptions": { "RouteKeys": [], // or null, no grouping, thus opts apply to all dynamic routes "BreakDuration": 1000, // 1s "MinimumThroughput": 3, "FailureRatio": 0.1, // 10% "SamplingDuration": 30000 // 30s }
 }
}

In this dynamic routing configuration, the [Timeout strategy](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-timeout-strategy) is applied to the `my-service` service in addition to the [Circuit Breaker strategy](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-circuit-breaker-strategy), resulting in [Polly](https://www.pollydocs.org/) timing out after 15 seconds. However, for all implicit dynamic routes, the [Timeout strategy](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-timeout-strategy) is not globally configured, in favor of the standard [Timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-timeout) option managed by the Ocelot Core requester middleware. Lastly, the [Circuit Breaker strategy](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-circuit-breaker-strategy) has been globally configured for all routes due to the absence of route grouping, with the following options: allow 3 errors before breaking the circuit for 1 second, and allow up to 10% errors during the default 30-second sampling period.

Note

1. Please note that route-level options take precedence over global options.

2. If the `RouteKeys` option is not defined or the array is empty in the global `QoSOptions`, the global options will apply to all routes. If the array contains route keys, it defines a single group of routes to which the global options apply. Routes excluded from this group must specify their own route-level `QoSOptions`.

3. Since Ocelot’s Polly provider utilizes the [Resilience pipeline registry](https://www.pollydocs.org/pipelines/resilience-pipeline-registry.html), each route has a dedicated pipeline cached in Polly’s registry using the route’s load-balancing key. For a static route, the load-balancing key uniquely identifies the route by its upstream options, whereas for dynamic routes the load-balancing key is typically the service name from the discovery provider. Thus, Polly’s registry maintains dedicated pipelines for each discovered service, and those pipelines behave independently. Finally, it is important to understand that global _QoS_ options do not create a single shared resilience pipeline in the registry.

4. Dynamic routes were not supported in versions prior to [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0). Beginning with version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global _QoS_ options for [Dynamic Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-dynamic) may be overridden in the `DynamicRoutes` configuration section, as defined by the [Dynamic Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-dynamic-route-schema). Additionally, global configuration for static routes (also known as `Routes`) has been supported since version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0).

Circuit Breaker strategy[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#circuit-breaker-strategy "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------

> Primary option: `MinimumThroughput`, formerly `ExceptionsAllowedBeforeBreaking`

The options `MinimumThroughput` and `BreakDuration` can be configured independently from `Timeout`:

"QoSOptions": {
 "MinimumThroughput": 3,
 "BreakDuration": 1000 // ms
}

Alternatively, you can omit `BreakDuration`, which will default to the implicit 5-second setting as specified in Polly’s [BreakDuration](https://www.pollydocs.org/api/Polly.CircuitBreaker.CircuitBreakerStrategyOptions-1.html#Polly_CircuitBreaker_CircuitBreakerStrategyOptions_1_BreakDuration) documentation:

"QoSOptions": {
 "MinimumThroughput": 3
}

This setup activates only the [Circuit breaker resilience strategy](https://www.pollydocs.org/strategies/circuit-breaker.html).

Additionally, there is a failure handling strategy based on `FailureRatio`, which serves as a counterpart to, or supplement for, the number of failures, also known as `MinimumThroughput`.

"QoSOptions": {
 "MinimumThroughput": 10,
 "FailureRatio": 0.5, // 50%
 "SamplingDuration": 10000, // ms, 10 seconds
}

Thus, a failure ratio of `0.5` indicates that the circuit will break if 50% or more of actions result in handled failures, after reaching the minimum threshold of 10 failures, also known as the `MinimumThroughput` option. Additionally, the 10-second sampling duration defines the time window over which the 50% failure ratio is evaluated.

> **Note**: The `MinimumThroughput` option (also known as Polly’s [MinimumThroughput](https://www.pollydocs.org/api/Polly.CircuitBreaker.CircuitBreakerStrategyOptions-1.html#Polly_CircuitBreaker_CircuitBreakerStrategyOptions_1_MinimumThroughput)) is the primary option that enables the _Circuit Breaker strategy_. Its value must be valid (set to 2 or greater, refer to the [Value constraints](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-notes-value-constraints) section in [Notes](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-notes)) and may be supplemented with additional Circuit Breaker options.

Timeout strategy[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#timeout-strategy "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

> Primary option: `Timeout`, formerly `TimeoutValue`

The `Timeout` can be configured independently from the options of the [Circuit Breaker strategy](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-circuit-breaker-strategy):

"QoSOptions": {
 "Timeout": 5000 // ms
}

This setup activates only the [Timeout resilience strategy](https://www.pollydocs.org/strategies/timeout.html).

To configure a global QoS timeout using the _Timeout strategy_ for all routes (both static and dynamic) set the `Timeout` option as defined in the [Global Configuration Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-global-configuration-schema):

"GlobalConfiguration": {
 // other global props
 "QoSOptions": {
 "Timeout": 10000 // ms, 10 seconds
 }
}

Please note that the route-level timeout takes precedence over the global timeout. For example, a route timeout may be shorter, while the global timeout can be longer and apply to all routes.

> **Note**: There are [Value constraints](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-notes-value-constraints) for `Timeout`: it must be a positive number starting from _1 millisecond_ to enable the _Timeout strategy_. If `Timeout` is undefined, zero or a negative number, the _Timeout strategy_ will not be added to the resilience pipeline. Also, keep in mind Polly’s [Timeout](https://www.pollydocs.org/api/Polly.Timeout.TimeoutStrategyOptions.html#Polly_Timeout_TimeoutStrategyOptions_Timeout) constraint, thus Ocelot validates the `Timeout`. If the value violates Polly’s requirements, it will be rolled back to the default of _30 seconds_.

Notes[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#notes "Link to this heading")
-------------------------------------------------------------------------------------------------------------

### Absolute timeout [[4]](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#f4)[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#absolute-timeout "Link to this heading")

If a _QoS_ section is not included, _QoS_ will not be applied, and Ocelot will enforce an absolute timeout of 90 seconds (defined by the `DownstreamRoute`[DefTimeout](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22const+int+DefTimeout%22&type=code) constant) for all downstream requests. This absolute timeout is configurable via the `DownstreamRoute`[DefaultTimeoutSeconds](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22static+int+DefaultTimeoutSeconds%22&type=code) static C# property. For more information, refer to the [Default timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-default-timeout) section of the [Configuration](https://ocelot.readthedocs.io/en/latest/features/configuration.html) chapter.

### Value constraints[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#value-constraints "Link to this heading")

Starting with [Polly](https://www.pollydocs.org/) v8, the [Resilience strategies](https://www.pollydocs.org/strategies/index.html) documentation outlines the following constraints on values:

*   The `BreakDuration` value must exceed **500** milliseconds and be less than **24** hours (1 day = `86 400 000` milliseconds). If unspecified or invalid, it defaults to **5000** milliseconds (5 seconds); refer to the [BreakDuration](https://www.pollydocs.org/api/Polly.CircuitBreaker.CircuitBreakerStrategyOptions-1.html#Polly_CircuitBreaker_CircuitBreakerStrategyOptions_1_BreakDuration) documentation.

*   The `MinimumThroughput` value must be **2** or greater. If unspecified or invalid, it defaults to **100** failures; refer to the [MinimumThroughput](https://www.pollydocs.org/api/Polly.CircuitBreaker.CircuitBreakerStrategyOptions-1.html#Polly_CircuitBreaker_CircuitBreakerStrategyOptions_1_MinimumThroughput) documentation.

*   The `FailureRatio` must be greater than **0.0** and no more than **1.0**. If unspecified or invalid, it defaults to **0.1** (10%); refer to the [FailureRatio](https://www.pollydocs.org/api/Polly.CircuitBreaker.CircuitBreakerStrategyOptions-1.html#Polly_CircuitBreaker_CircuitBreakerStrategyOptions_1_FailureRatio) documentation.

*   The `SamplingDuration` value must exceed **500** milliseconds and be less than **24** hours (1 day = `86 400 000` milliseconds). If unspecified or invalid, it defaults to **30000** milliseconds (30 seconds); refer to the [SamplingDuration](https://www.pollydocs.org/api/Polly.CircuitBreaker.CircuitBreakerStrategyOptions-1.html#Polly_CircuitBreaker_CircuitBreakerStrategyOptions_1_SamplingDuration) documentation.

*   The `Timeout` must be greater than **10** milliseconds and less than **24** hours (1 day = `86 400 000` milliseconds). If unspecified or invalid, it defaults to **30000** milliseconds (30 seconds); refer to the [Timeout](https://www.pollydocs.org/api/Polly.Timeout.TimeoutStrategyOptions.html#Polly_Timeout_TimeoutStrategyOptions_Timeout) documentation. And please note, when both route-level and global _QoS_ timeouts have positive values but are invalid, a default value will be automatically substituted from the `TimeoutStrategy` class [DefaultTimeout](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+DefaultTimeout+path%3A%2F%5Esrc%5C%2FOcelot.Provider.Polly%5C%2F%2F&type=code) static C# property, which can also be configured in your [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/Program.cs).

Ocelot logs warnings containing failed validation messages for all options, but it does not block Ocelot startup, even when _QoS_ options are invalid. Inspect your logs for these messages and adjust your configuration if necessary.

### QoS and route (global) timeouts[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-and-route-global-timeouts "Link to this heading")

The `Timeout` option in _QoS_ always takes precedence over the route [Timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-timeout) property, so [Timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-timeout) will be ignored in favor of QoS `Timeout`. In Ocelot Core, `Timeout` and configuration [Timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-timeout) are not intended to be used together. Moreover, there is an Ocelot Core design constraint: if the route or global `Timeout` duration is shorter than the _QoS_`Timeout`, you may encounter warning messages in the logs that begin with the following sentence:

Route '/xxx' has Quality of Service settings (QoSOptions) enabled, but either the route Timeout or the QoS Timeout is misconfigured: ...

This warning means that the route or global timeout will occur before the _QoS_[Timeout strategy](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-timeout-strategy) has a chance to handle its own timeout event, which is configured with a longer duration. Technically, this situation results in the functional disabling of the Polly’s [Timeout resilience strategy](https://www.pollydocs.org/strategies/timeout.html). Ocelot handles this misconfiguration by logging a warning and automatically applying a longer timeout to the `TimeoutDelegatingHandler` in order to effectively unblock the _QoS_[Timeout strategy](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#qos-timeout-strategy). To avoid this warning, ensure that your _QoS_ timeouts are shorter than the route or global timeouts, or remove the [Timeout](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-timeout) property from routes where _QoS_ is enabled with the `Timeout` option.

### Global and default QoS timeouts[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#global-and-default-qos-timeouts "Link to this heading")

If a route-level _QoS_ timeout is undefined, the global `Timeout` takes precedence over the default timeout (30 seconds, see the [Timeout](https://www.pollydocs.org/api/Polly.Timeout.TimeoutStrategyOptions.html#Polly_Timeout_TimeoutStrategyOptions_Timeout) docs). This means the global _QoS_ timeout can override Polly’s default of [30 seconds](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22const+int+DefTimeout%22+path%3A%2F%5Esrc%5C%2FOcelot%5C.Provider%5C.Polly%5C%2F%2F&type=code) via the [Global Configuration Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-global-configuration-schema).

Extensibility [[5]](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#f5)[¶](https://ocelot.readthedocs.io/en/latest/features/qualityofservice.html#extensibility "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

To use your `ResiliencePipeline<T>` provider, you can apply the following syntax:

builder.Services
 .AddOcelot(builder.Configuration)
 .AddPolly<MyProvider>();// MyProvider should implement IPollyQoSResiliencePipelineProvider<HttpResponseMessage>
// Note: you can use standard provider PollyQoSResiliencePipelineProvider

Additionally, if you want to utilize your own `DelegatingHandler`, the following syntax can be applied:

builder.Services
 .AddOcelot(builder.Configuration)
 .AddPolly<MyProvider>(MyQosDelegatingHandlerDelegate);// MyQosDelegatingHandlerDelegate is a delegate use to get a DelegatingHandler. Refer to Ocelot's PollyResiliencePipelineDelegatingHandler

Finally, to define your own set of exceptions for mapping, you can apply the following syntax:

static Error CreateError(Exception e) => new RequestTimedOutError(e);
Dictionary<Type, Func<Exception, Error>> MyErrorMapping = new()
{
 {typeof(TaskCanceledException), CreateError},
 {typeof(TimeoutRejectedException), CreateError},
 {typeof(BrokenCircuitException), CreateError},
 {typeof(BrokenCircuitException<HttpResponseMessage>), CreateError},
};
builder.Services
 .AddOcelot(builder.Configuration)
 .AddPolly<MyProvider>(MyErrorMapping);// Note: Default error mapping is defined in the DefaultErrorMapping field of the Ocelot.Provider.Polly.OcelotBuilderExtensions class

* * *
