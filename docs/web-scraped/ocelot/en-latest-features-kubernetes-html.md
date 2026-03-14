# Source: https://ocelot.readthedocs.io/en/latest/features/kubernetes.html

Title: Kubernetes (K8s) — Ocelot Gateway 24.1 "Globality" documentation

URL Source: https://ocelot.readthedocs.io/en/latest/features/kubernetes.html

Markdown Content:
Ocelot will call the [K8s](https://kubernetes.io/) endpoints API in a given namespace to get all of the endpoints for a pod and then load balance across them. Ocelot used to use the services API to send requests to the [K8s](https://kubernetes.io/) service but this was changed in pull request [1134](https://github.com/ThreeMammals/Ocelot/pull/1134) because the service did not load balance as expected.

Our NuGet [Ocelot.Provider.Kubernetes](https://www.nuget.org/packages/Ocelot.Provider.Kubernetes) extension package is based on the [KubeClient](https://www.nuget.org/packages/KubeClient) package. For a comprehensive understanding, it is essential refer to the [KubeClient](https://www.nuget.org/packages/KubeClient) documentation.

Install[¶](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#install "Link to this heading")
-----------------------------------------------------------------------------------------------------------

The first thing you need to do is install the [package](https://www.nuget.org/packages/Ocelot.Provider.Kubernetes) that provides [![Image 1: kubernetes logo](https://ocelot.readthedocs.io/en/latest/_images/k8s-logo-kubernetes.png)](https://kubernetes.io/) support in Ocelot:

Install-Package Ocelot.Provider.Kubernetes

`AddKubernetes(bool)` method[¶](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#addkubernetes-bool-method "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------

public static class OcelotBuilderExtensions
{
 public static IOcelotBuilder AddKubernetes(this IOcelotBuilder builder, bool usePodServiceAccount = true);}

This extension-method adds [K8s](https://kubernetes.io/) services **with** or **without** using a pod service account. Then add the following to your [Program](https://github.com/ThreeMammals/Ocelot/blob/main/samples/Kubernetes/ApiGateway/Program.cs):

builder.Services
 .AddOcelot(builder.Configuration)
 .AddKubernetes(); // usePodServiceAccount is true

If you have services deployed in Kubernetes, you will normally use the naming service to access them.

1.   By default the `useServiceAccount` argument is true, which means that Service Account using Pod to access the service of the [K8s](https://kubernetes.io/) cluster needs to be Service Account based on RBAC authorization:

You can replicate a Permissive using RBAC role bindings (see [Permissive RBAC Permissions](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#permissive-rbac-permissions)), [K8s](https://kubernetes.io/) API server and token will read from pod.

kubectl create clusterrolebinding permissive-binding --clusterrole=cluster-admin --user=admin --user=kubelet --group=system:serviceaccounts 
Finally, it creates the [KubeClient](https://www.nuget.org/packages/KubeClient) from pod service account.

2.   When the `useServiceAccount` argument is false, you need to provide [KubeClientOptions](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20KubeClientOptions&type=code) to create [KubeClient](https://www.nuget.org/packages/KubeClient) using them. You have to bind the options configuration section for the DI `IOptions<KubeClientOptions>` interface or register a custom action to initialize the options:

 Action<KubeClientOptions> configureKubeClient = opts =>
 {
 opts.ApiEndPoint = new UriBuilder("https", "my-host", 443).Uri;
 opts.AccessToken = "my-token";
 opts.AuthStrategy = KubeAuthStrategy.BearerToken;
 opts.AllowInsecure = true;
 };
 builder.Services
 .AddOptions<KubeClientOptions>() .Configure(configureKubeClient); // manual binding options via IOptions<KubeClientOptions> builder.Services
 .AddOcelot(builder.Configuration)
 .AddKubernetes(false); // don't use pod service account, and IOptions<KubeClientOptions> is reused 
> **Note**, this could also be written like this (shortened version):
> 
> builder.Services
>  .AddKubeClientOptions(opts => {
>  opts.ApiEndPoint = new UriBuilder("https", "my-host", 443).Uri;
>  opts.AuthStrategy = KubeAuthStrategy.BearerToken;
>  opts.AccessToken = "my-token";
>  opts.AllowInsecure = true;
>  })
>  .AddOcelot(builder.Configuration)
>  .AddKubernetes(false); // don't use pod service account, and client options provided via AddKubeClientOptions

Finally, it creates the [KubeClient](https://www.nuget.org/packages/KubeClient) from your options.

> **Note 1**: For understanding the `IOptions<TOptions>` interface, please refer to the Microsoft Learn documentation: [Options pattern in .NET](https://learn.microsoft.com/en-us/dotnet/core/extensions/options).
> 
> 
> **Note 2**: Please consider this Case 2 as an example of manual setup when you **do not** use a pod service account. We recommend using our official extension method, which receives an `Action<KubeClientOptions>` argument with your options: refer to the [AddKubernetes(Action<KubeClientOptions>) method 2](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-addkubernetes-action-method) below.

`AddKubernetes(Action<KubeClientOptions>)` method [[2]](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#f2)[¶](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#addkubernetes-action-kubeclientoptions-method "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

public static class OcelotBuilderExtensions
{
 public static IOcelotBuilder AddKubernetes(this IOcelotBuilder builder, Action<KubeClientOptions> configureOptions, /*optional params*/);}

This extension method adds [K8s](https://kubernetes.io/) services **without** using a pod service account, explicitly calling an action to initialize configuration options for [KubeClient](https://www.nuget.org/packages/KubeClient). It operates in two modes:

1.   If `configureOptions` is provided (action is not null), it calls the action, ignoring all optional arguments.

Action<KubeClientOptions> configureKubeClient = opts =>
{
 opts.ApiEndPoint = new UriBuilder("https", "my-host", 443).Uri;
 // ...
};
builder.Services
 .AddOcelot(builder.Configuration)
 .AddKubernetes(configureKubeClient); // without optional arguments 

> **Note**: Optional arguments do not make sense; all settings are defined inside the `configureKubeClient` action.

1.   If `configureOptions` is not provided (action is null), it reads the global `ServiceDiscoveryProvider`[Configuration](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-configuration) options and reuses them to initialize the following properties: `ApiEndPoint`, `AccessToken`, and `KubeNamespace`, finally initializing the rest of the properties with optional arguments.

builder.Services
 .AddOcelot(builder.Configuration)
 .AddKubernetes(null, allowInsecure: true, /*optional args*/) // shortened version // or
 .AddKubernetes(configureOptions: null, allowInsecure: true, /*optional args*/); // long version 

> **Note**: Optional arguments must be used here in addition to the options coming from the global `ServiceDiscoveryProvider`[Configuration](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-configuration). Find the comprehensive documentation in the C# code of the [AddKubernetes](https://github.com/search?q=repo%3AThreeMammals%2FOcelot+%22public+static+IOcelotBuilder+AddKubernetes%28this+IOcelotBuilder+builder%2C%22+language%3AC%23&type=code) methods.

Configuration[¶](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#configuration "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

The following examples show how to set up a route that will work in Kubernetes. The most important thing is the `ServiceName` which is made up of the Kubernetes service name. We also need to set up the `ServiceDiscoveryProvider` in `GlobalConfiguration`.

Regarding global and route configurations, if your downstream service resides in a different namespace, you can override the global setting at the route level by specifying a `ServiceNamespace`.

"Routes": [
 {
 "ServiceName": "my-service",
 "ServiceNamespace": "my-namespace"
 }
]

`Kube` provider[¶](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#kube-provider "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------

The example here shows a typical configuration:

"Routes": [
 {
 "ServiceName": "my-service",
 // ...
 }
],
"GlobalConfiguration": {
 "ServiceDiscoveryProvider": {
 "Scheme": "https",
 "Host": "my-host",
 "Port": 443,
 "Token": "my-token",
 "Namespace": "Dev",
 "Type": "Kube"
 }
}

Service deployment in `Dev` namespace, and discovery provider type is `Kube`, you also can set [PollKube](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-pollkube-provider) or [WatchKube](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-watchkube-provider) provider type.

> **Note 1**: `Scheme`, `Host`, `Port`, and `Token` are not used if `usePodServiceAccount` is true when [KubeClient](https://www.nuget.org/packages/KubeClient) is created from a pod service account. Please refer to the [Install](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-install) section for technical details.
> 
> 
> **Note 2**: The `Kube` provider searches for the service entry using `ServiceName` and then retrieves the first available port from the `EndpointSubsetV1.Ports` collection. Therefore, if the port name is not specified, the default downstream scheme will be `http`; Please refer to the “[Downstream Scheme vs Port Names](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-downstream-scheme-vs-port-names)” section for technical details.

`PollKube` provider [[3]](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#f3)[¶](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#pollkube-provider "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You use Ocelot to poll Kubernetes for latest service information rather than per request. If you want to poll Kubernetes for the latest services rather than per request (default behaviour of the [Kube provider](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-kube-provider)) then you need to set the following configuration:

"ServiceDiscoveryProvider": {
 "Namespace": "dev",
 "Type": "PollKube",
 "PollingInterval": 100 // ms
}

The polling interval is in milliseconds and tells Ocelot how often to call Kubernetes for changes in service configuration.

> **Note**, there are tradeoffs here. If you poll Kubernetes, it is possible Ocelot will not know if a service is down depending on your polling interval and you might get more errors than if you get the latest services per request. This really depends on how volatile your services are. We doubt it will matter for most people and polling may give a tiny performance improvement over calling Kubernetes per request. There is no way for Ocelot to work these out for you, except perhaps through a [discussion](https://github.com/ThreeMammals/Ocelot/discussions).

`WatchKube` provider [[4]](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#f4)[¶](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#watchkube-provider "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

With this configuration, [Kubernetes API](https://kubernetes.io/docs/reference/using-api/) “[watch requests](https://kubernetes.io/docs/reference/using-api/api-concepts/#efficient-detection-of-changes)” are used to fetch service configuration. Essentially, it establishes one streamed HTTP connection with the [Kubernetes API](https://kubernetes.io/docs/reference/using-api/) per downstream service. Changes streamed through this connection will be used to update the list of available endpoints.

"ServiceDiscoveryProvider": {
 "Namespace": "dev",
 "Type": "WatchKube"
}

Note

The `WatchKube` provider is specifically designed for high-load Ocelot vs. Kubernetes environments with high RPS ratios. To better understand which type is suitable for your needs, we have added a table [Comparing providers](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-comparing-providers).

The provider has an implicit configuration for fine-tuned watching, which are available and can only be initialized in C# code.

*   `WatchKube.FirstResultsFetchingTimeoutSeconds`: [This](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20FirstResultsFetchingTimeoutSeconds&type=code) is the default number of seconds to wait after Ocelot starts, following the provider’s creation, to fetch the first result from the Kubernetes endpoint. 1

*   `WatchKube.FailedSubscriptionRetrySeconds`: [This](https://github.com/search?q=repo%3AThreeMammals%2FOcelot%20FailedSubscriptionRetrySeconds&type=code) is the default number of seconds to wait before scheduling the next retry for the subscription operation. 1

> 1 For both `static int` properties, the default value is 1 (one) second. The constraint ensures that the assigned value is greater than or equal to 1 (one). Therefore, the minimum value is 1 (one) second.

Comparing providers[¶](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#comparing-providers "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------

This table explains the most important indicators that may influence Ocelot vs. Kubernetes deployment or DevOps strategy. The evolution path of all providers follows: `Kube` ->`PollKube` ->`WatchKube`, with `WatchKube` being the most advanced provider.

| _Indicators \ Providers_ | [Kube](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-kube-provider) | [PollKube](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-pollkube-provider) | [WatchKube](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-watchkube-provider) |
| --- | --- | --- | --- |
| Extra latency | One hop per route | - | - |
| Speed of response to endpoints changes | High | Low 1 | High |
| Pressure on [Kubernetes API](https://kubernetes.io/docs/reference/using-api/) | High | Low 1 | Low |
| Ocelot load (estimated) 2 | < 1000 RPS | > 1000 RPS | > 5000 RPS |
| Ocelot deployment 3 | Single instance | Multiple instances | Cluster of instances |

> 1 Depends on the `PollingInterval` option.
> 
> 
> 2 Please consider this a rough load estimation, as our team has not provided any tests or benchmarks.
> 
> 
> 3 The term “instance” refers to an Ocelot instance, not a Kubernetes one.

Downstream Scheme vs Port Names [[5]](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#f5)[¶](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#downstream-scheme-vs-port-names "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Kubernetes configuration permits the definition of multiple ports with names for each address of an endpoint subset. When binding multiple ports, you assign a name to each subset port. To allow the `Kube` provider to recognize the desired port by its name, you need to specify the `DownstreamScheme` with the port’s name; if not, the collection’s first port entry will be chosen by default.

For instance, consider a service on Kubernetes that exposes two ports: `https` for 443 and `http` for 80, as follows:

Name:         my-service
Namespace:    default
Subsets:
  Addresses:  10.1.161.59
  Ports:
    Name   Port  Protocol
    ----   ----  --------
    https  443   TCP
    http   80    TCP

**When** you need to use the `http` port while intentionally bypassing the default `https` port (first one), you must define `DownstreamScheme` to enable the provider to recognize the desired `http` port by comparing `DownstreamScheme` with the port name as follows:

"Routes": [
 {
 "ServiceName": "my-service",
 "DownstreamScheme": "http", // port name -> http -> port is 80
 }
]

Note

In the absence of a specified `DownstreamScheme` (the default behavior), the [Kube provider](https://ocelot.readthedocs.io/en/latest/features/kubernetes.html#k8s-kube-provider)—as well as other providers—will select _the first available port_ from the `EndpointSubsetV1.Ports` collection. Consequently, if the port name is not designated, the default downstream scheme utilized will be `http`.

* * *
