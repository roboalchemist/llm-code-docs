# Source: https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html

Title: Load Balancer — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html

Markdown Content:
Ocelot can load balance across available downstream services for each route. This means you can scale your downstream services, and Ocelot can use them effectively.

`LoadBalancerOptions` Schema[¶](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#loadbalanceroptions-schema "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------

The following is the full _load balancer_ configuration, used in both the [Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-route-schema) and the [Dynamic Route Schema](https://ocelot.readthedocs.io/en/latest/features/configuration.html#config-dynamic-route-schema). Not all of these options need to be configured; however, the `Type` option is mandatory.

"LoadBalancerOptions": {
 "Type": "",
 "Key": "", // CookieStickySessions balancer
 "Expiry": 1 // ms, CookieStickySessions balancer
}

| _Option_ | _Description_ |
| --- | --- |
| `Type` | An in-built _load balancer_ type selected from the list of available [Balancers](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#lb-balancers), or a user-defined type (refer to the “[Custom Balancers](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#lb-custom-balancers)” section). |
| `Key` | The name of the cookie you wish to use for sticky sessions. This option is applicable only to the [CookieStickySessions type](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#lb-cookiestickysessions-type). |
| `Expiry` | Expiration period specifies how long, in milliseconds, the session should remain sticky. This value refreshes with each request to mimic typical session behavior. Note: This option applies only to the [CookieStickySessions type](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#lb-cookiestickysessions-type). |

The actual `LoadBalancerOptions` schema with all the properties can be found in the C# [FileLoadBalancerOptions](https://github.com/ThreeMammals/Ocelot/blob/main/src/Ocelot/Configuration/File/FileLoadBalancerOptions.cs) class.

Configuration[¶](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

The following shows how to set up multiple downstream services for a static route using [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json) and then select the `LeastConnection`_load balancer_. This is the simplest way to configure load balancing without using service discovery.

{
 "UpstreamPathTemplate": "/posts/{postId}",
 "UpstreamHttpMethod": [ "Put", "Delete" ],
 "DownstreamPathTemplate": "/api/posts/{postId}",
 "DownstreamScheme": "https",
 "DownstreamHostAndPorts": [
 { "Host": "10.0.1.10", "Port": 5000 },
 { "Host": "10.0.1.11", "Port": 5000 }
 ],
 "LoadBalancerOptions": { "Type": "LeastConnection" }}

The following shows how to set up a route using [Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html) and then select the `RoundRobin`_load balancer_.

{
 // ...
 "ServiceName": "product",
 "LoadBalancerOptions": {
 "Type": "RoundRobin"
 }
}

When this is set up, Ocelot will look up the downstream host and port from the [Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html) provider and load balance requests across any available services. If you add and remove services from the [Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html) provider [[1]](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#f1), Ocelot should respect this and stop calling services that have been removed and start calling services that have been added.

### Global Configuration [[2]](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#f2)[¶](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#global-configuration "Link to this heading")

A complete configuration consists of both route-level and global _load balancing_. You can configure the following options in the `GlobalConfiguration` section of [ocelot.json](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Basic/ocelot.json):

"Routes": [
 {
 "Key": "R0", // optional
 "LoadBalancerOptions": { "Type": "CookieStickySessions", "Key": ".AspNetCore.Session", "Expiry": 1200000 // milliseconds, 20 minutes } },
 {
 "Key": "R1", // this route is part of a group
 "LoadBalancerOptions": {} // optional due to grouping }
],
"GlobalConfiguration": {
 "BaseUrl": "https://ocelot.net",
 "LoadBalancerOptions": { "RouteKeys": ["R1"], // if undefined or empty array, opts will apply to all routes "Type": "LeastConnection" }}

[Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html) dynamic routes intentionally override the global [dynamic routing](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#sd-dynamic-routing) configuration:

"DynamicRoutes": [
 {
 "Key": "", // optional
 "ServiceName": "my-service",
 "LoadBalancerOptions": { "Type": "LeastConnection" // switch from RoundRobin to LeastConnection } }
],
"GlobalConfiguration": {
 "BaseUrl": "https://ocelot.net",
 "DownstreamScheme": "http",
 "ServiceDiscoveryProvider": {
 // required section for dynamic routing
 },
 "LoadBalancerOptions": { "RouteKeys": [], // no grouping, thus opts apply to all dynamic routes "Type": "RoundRobin" }}

In this configuration, the `RoundRobin` balancer is used for all implicit dynamic routes. However, for the “my-service” service, the load balancer type has been explicitly switched from `RoundRobin` to `LeastConnection`.

Note

1. If the `RouteKeys` option is not defined or the array is empty in the global `LoadBalancerOptions`, the global options will apply to all routes. If the array contains route keys, it defines a single group of routes to which the global options apply. Routes excluded from this group must specify their own route-level `LoadBalancerOptions`.

2. Prior to version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global `LoadBalancerOptions` were only accessible in the special [Dynamic Routing](https://ocelot.readthedocs.io/en/latest/features/routing.html#routing-dynamic) mode. Since version [24.1](https://github.com/ThreeMammals/Ocelot/releases/tag/24.1.0), global configuration has been available for both static and dynamic routes. As a team, we would consider the idea of implementing such a global configuration for aggregated routes. However, an aggregated route is essentially a combination of static routes.

Balancers[¶](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#balancers "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

The available types of built-in _load balancers_ are:

| _Type_ | _Description_ |
| --- | --- |
| `CookieStickySessions` | This uses a cookie to stick all requests to a specific server. More information can be found in the “[CookieStickySessions Type](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#lb-cookiestickysessions-type)” section. |
| `LeastConnection` | This tracks which services are dealing with requests and sends new requests to the service with the fewest (“least”) existing requests. The algorithm state is not distributed across a cluster of Ocelots. |
| `RoundRobin` | This loops through available services and sends requests. The algorithm state is not distributed across a cluster of Ocelots. |
| `NoLoadBalancer` | This takes the first available service from [configuration](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#lb-configuration) or [Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html) provider. |

You must choose which _load balancer_ to use in your [configuration](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#lb-configuration).

`CookieStickySessions` Type [[3]](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#f3)[¶](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#cookiestickysessions-type "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

We have implemented a basic sticky session type of _load balancer_. The scenario it is meant to support involves having a number of downstream servers that do not share session state. If you receive more than one request for one of these servers, it should go to the same server each time; otherwise, the session state might be incorrect for the given user.

In order to set up the `CookieStickySessions`_load balancer_, you need to do something like the following:

{
 "UpstreamPathTemplate": "/posts/{postId}",
 "UpstreamHttpMethod": [ "Put", "Delete" ],
 "DownstreamPathTemplate": "/api/posts/{postId}",
 "DownstreamScheme": "https",
 "DownstreamHostAndPorts": [
 { "Host": "10.0.1.10", "Port": 5000 },
 { "Host": "10.0.1.11", "Port": 5000 }
 ],
 "LoadBalancerOptions": {
 "Type": "CookieStickySessions",
 "Key": ".AspNetCore.Session",
 "Expiry": 1200000 // milliseconds, 20 minutes
 }
}

These `LoadBalancerOptions` configure the `CookieStickySessions` load balancer using the standard session cookie `Key` for ASP.NET Core apps with sessions enabled. The default expiration time is 20 minutes, matching the default session timeout in ASP.NET Core.

> **Note 1**: If you have multiple routes with the same `LoadBalancerOptions`, then all of those routes will use the same _load balancer_ for their subsequent requests. This means the sessions will be stuck across routes.
> 
> 
> **Note 2**: If you define more than one `DownstreamHostAndPort`, or if you are using a [Service Discovery](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html) provider such as [Consul](https://ocelot.readthedocs.io/en/latest/features/servicediscovery.html#sd-consul) and it returns more than one service, then `CookieStickySessions` uses `RoundRobin` to select the next server. This is hard-coded at the moment but could be changed.

Custom Balancers [[4]](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#f4)[¶](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#custom-balancers "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In order to create and use a custom _load balancer_, you can do the following. Below, we set up a basic load balancing configuration, and note that the `Type` is `MyLoadBalancer`, which is the name of a class we will set up to perform load balancing.

{
 // ...
 "DownstreamHostAndPorts": [
 { "Host": "10.0.1.10", "Port": 5000 },
 { "Host": "10.0.1.11", "Port": 5000 }
 ],
 "LoadBalancerOptions": {
 "Type": "MyLoadBalancer"
 }
}

Then, you need to create a class that implements the `ILoadBalancer` interface. Below is a simple round-robin example:

using Ocelot.LoadBalancer.LoadBalancers;
using Ocelot.Responses;
using Ocelot.Values;

public class MyLoadBalancer : ILoadBalancer
{
 private readonly Func<Task<List<Service>>> _services;
 private static object Locker = new();
 private int _last;

 public MyLoadBalancer() { }
 public MyLoadBalancer(Func<Task<List<Service>>> services)
 => _services = services;

 public string Type => nameof(MyLoadBalancer);
 public void Release(ServiceHostAndPort hostAndPort) { }

 public async Task<Response<ServiceHostAndPort>> LeaseAsync(HttpContext context)
 {
 var services = await _services.Invoke();
 lock (Locker)
 {
 _last = (_last >= services.Count) ? 0 : _last;
 var next = services[_last++];
 return new OkResponse<ServiceHostAndPort>(next.HostAndPort);
 }
 }
}

Finally, you need to register this class with Ocelot. We have used the most complex example below to show all of the data and types that can be passed into the factory that creates _load balancers_.

using Ocelot.Configuration;
using Ocelot.DependencyInjection;
using Ocelot.ServiceDiscovery.Providers;

Func<IServiceProvider, DownstreamRoute, IServiceDiscoveryProvider, MyLoadBalancer> lbFactory
 = (serviceProvider, Route, discoveryProvider) => new MyLoadBalancer(discoveryProvider.GetAsync);
builder.Services
 .AddOcelot(builder.Configuration)
 .AddCustomLoadBalancer(lbFactory);

However, there is a much simpler example that will work the same way:

using Ocelot.DependencyInjection;

builder.Services
 .AddOcelot(builder.Configuration)
 .AddCustomLoadBalancer<MyLoadBalancer>();

Note

1. There are numerous `IOcelotBuilder`[methods](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22IOcelotBuilder+AddCustomLoadBalancer%3CT%3E%28%22+language%3AC%23&type=code) to add a custom _load balancer_. The interface is as follows:

IOcelotBuilder AddCustomLoadBalancer<T>()
 where T : ILoadBalancer, new();
IOcelotBuilder AddCustomLoadBalancer<T>(Func<T> loadBalancerFactoryFunc)
 where T : ILoadBalancer;
IOcelotBuilder AddCustomLoadBalancer<T>(Func<IServiceProvider, T> loadBalancerFactoryFunc)
 where T : ILoadBalancer;
IOcelotBuilder AddCustomLoadBalancer<T>(Func<DownstreamRoute, IServiceDiscoveryProvider, T> loadBalancerFactoryFunc)
 where T : ILoadBalancer;
IOcelotBuilder AddCustomLoadBalancer<T>(Func<IServiceProvider, DownstreamRoute, IServiceDiscoveryProvider, T> loadBalancerFactoryFunc)
 where T : ILoadBalancer;

1.   When you enable custom _load balancers_, Ocelot looks up your _load balancer_ by its class name when it decides whether to perform load balancing.

*   If it finds a match, it will use your load balancer to load balance.

*   If Ocelot cannot match the _load balancer_ type in your configuration with the name of the registered _load balancer_ class, then you will receive an HTTP [500 Internal Server Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500).

*   If your _load balancer_ factory throws an exception when Ocelot calls it, you will receive an HTTP [500 Internal Server Error](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500).

Warning

Remember, if you specify no _load balancer_ in your [Configuration](https://ocelot.readthedocs.io/en/latest/features/loadbalancer.html#lb-configuration), Ocelot will not attempt to load balance.

* * *
