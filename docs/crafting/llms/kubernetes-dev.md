# Develop on Kubernetes

Source: https://docs.sandboxes.cloud/docs/kubernetes-dev.md

In this page, we describes how to use Crafting platform to develop on Kubernetes apps, including following topics:

* [Use on-demand per-dev Kubernetes namespace with sandbox](#use-on-demand-per-dev-kubernetes-namespace)
* [Intercept traffic from Kubernetes to instantly iterate on your code](#intercept-traffic-from-kubernetes)
  * [Conditional interception to use a large shared Kubernetes namespace for testing your services in isolation](#conditional-interception)
* [Demo video](#demo-video)

Here we assume your team has already setup Crafting for Kubernetes properly, and talk about the day-to-day usage from a developer point of view. To learn how to set up, please see [Setup for Kubernetes](https://docs.sandboxes.cloud/docs/kubernetes-setup) for details. Basically the team should setup in advance of following things:

* Connect Crafting platform to a shared Kubernetes cluster for hosting the namespaces
* \[optional] Setup direct Kubernetes API server access to run `kubectl` in sandbox
* \[optional] Setup the template that include a Kubernetes resource for per-dev namespace

## Use on-demand per-dev Kubernetes namespace

Crafting enables each developer to launch a dedicated namespace with services running end-to-end in it to support their development and testing work. In this model, each sandbox is launched with a dedicated namespaces along side. The workspaces in the sandbox can directly access services running in the namespace. Developers using different sandboxes will have their own namespaces in Kubernetes.

More importantly, the life-cycle of the Kubernetes namespaces are managed by the sandbox so that:

* When the sandbox is created, the namespace is created,
* When the sandbox is deleted, the namespace is deleted as well, freeing up resources.
* When the sandbox is suspended/resumed, the number of replicas for the services in the namespace can be scaled down to 0/scaled back, respectively, further improving resource utilization.

<Image align="center" className="border" border={true} src="https://files.readme.io/e7a3af8-use-case-kubernetes-lifecycle.png" />

The mechanism is to leverage Crafting's resource model, define a specially configured `Kubernetes resource` to implement the namespace management, and include that in the sandbox template. Read [here](kubernetes-setup#orchestrate-deployment-of-per-dev-namespace-from-sandbox) for more details about setup. The following guide assumes that setup is already done by the team.

<Image align="center" className="border" border={true} src="https://files.readme.io/3d68928-use-case-kubernetes-resource.JPG" />

Shown in the figure above, this sandbox has a workspace and a Kubernetes resource already setup. After launch, the sandbox is created and the corresponding hook to launch the Kubernetes namespace is executed in the workspace (e.g. `dev`).

<Image align="center" className="border" border={true} src="https://files.readme.io/a09c985-use-case-kubernetes-namespace.JPG" />

We can monitor the creation of the namespace from the `Kubernetes Clusters` menu, by selecting the connected cluster and namespace (Note that it may take a few refreshes to have the newly created namespace listed). We can see the new namespace is created and the services are getting started in it. When the sandbox launching is done, we can see all services are ready and we can also see them from the workspace with `kubectl` command

<Image align="center" className="border" border={true} src="https://files.readme.io/355d725-use-case-kubernetes-info.JPG" />

At this point, we have a dedicated Kubernetes environment for testing and debugging. We can run the product flow end-to-end by hitting the Kubernetes Ingress (or Load Balancer Service), or through the endpoint in sandbox, which can be setup to hit any service in the Kubernetes namespace, as shown below.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/b168e6f-image.png" />

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/5fc5c46-use-case-kubernetes-run.JPG" />

When the sandbox is suspended (or auto-suspended), the corresponding namespace will be scaled to zero, as shown below, and upon resuming, it will be scaled back quickly.

<Image align="center" className="border" width="60% " border={true} src="https://files.readme.io/52681cd-image.png" />

<Image align="center" className="border" border={true} src="https://files.readme.io/5f5b45b-image.png" />

### Intercept traffic from Kubernetes

With Crafting, a developer can replace a service running in a Kubernetes cluster with the dev version running in the Crafting sandbox to develop business logic end-to-end. This is great for quickly iterating the code without rebuilding container every time. You can see your change live instantly.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/e541952-use-case-kubernetes-interception.png" />

Crafting does that via traffic interception on a Kubernetes workload. As shown in the figure above, `Developer A` intercepts the `API service`, so that the traffic hitting the `API service` inside the cluster will be rerouted to the `API service` running in `Crafting Sandbox 1`'s workspace. That way `Developer A` directly modify the code in the sandbox and rebuild/restart service in the workspace, and then the new version will directly receive traffic from the cluster.

When interception is active, the modified service can also call to other services in the cluster directly using the in-cluster DNS names or Pod/Service IP addresses (such as `backend`). If there is any callback from other services to the `API service`, the dev version will receive it. In summary, it's virtually plugged in and replaced the `API service` in the cluster, effective in an end-to-end flow.

Crafting allows multiple interceptions to be done to the same or different sandbox for an integration testing. In the above figure, `Developer B` intercepts the `Cart service` at the same time, so the `Cart service` in `Crafting Sandbox 2` is the effective `Cart service` used in the cluster. That way, `Developer A` and `Developer B` can let their dev version of the service working in the same product flow together for integration testing. Crafting also supports conditional interception for only intercepting specific traffic stream into the services to avoid developers interfering each other. Please see [conditional interception](#conditional-interception) for more information.

> 📘 Did you know?
>
> Traffic interception can be done in any Kubernetes namespaces in the connected cluster, not limited to the per-dev namespace described in [Use on-demand per-dev Kubernetes namespace](#use-on-demand-per-dev-kubernetes-namespace). It can also be used for debugging any Kubernetes deployment in the cluster (e.g. shared staging environment).

To start an interception, we can go to the namespace under `Kubernetes Cluster`  menu item, and click the `Start interception` for the target service (highlighted below).

<Image align="center" className="border" border={true} src="https://files.readme.io/ce70789-image.png" />

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/85b55b7-image.png" />

In the dialog, select the sandbox and workspace we want to intercept the traffic to and select the source and destination port. After clicking `Confirm`, the traffic interception is established.

<Image align="center" className="border" border={true} src="https://files.readme.io/4d7ba58-image.png" />

At this time, if we go to the sandbox page, we can see an active interception. Here we can see the detailed information regarding the interception and can stop the interception. Note that we can also start an interception from the sandbox page by clicking the `Start interception` in the `Actions`

We can also start or stop Kubernetes interception using CLI

```shell
$ cs kubernetes intercept [start|stop]
```

#### Conditional interception

Crafting supports `Conditional traffic interception`, i.e., only intercepting the requests that match specific headers from Kubernetes to sandbox. With conditional interception, Many developers can use a shared Kubernetes deployment as the base environment, and conditionally intercept their own testing traffic to hit the dev version of the service running in their sandbox, without letting their dev version of the service interfere with the rest.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/6f02ad7-Slide_16_9_-_33_1.png" />

As shown above, only the traffic from Developer A (Green arrow) is subject to the interception to replace `API-Service`, while traffic from Developer B (Yellow arrow) is not. Similarly, only the traffic from Developer B (Yellow arrow) is intercepted for service `Cart`. That way, each developer can test their dev version of the service using a shared environment without affecting each other.

This is especially useful when building a per-dev namespace to include all the services is not economical. Specifically, we recommend using conditional routing in either of the following cases:

* For a large Kubernetes environment with hundreds or thousands of services
* For a large engineering team with hundreds or thousands of developers.

Conditional interception depends on headers in the request to identify which traffic stream it belongs to, and decide whether to reroute it. Therefore, the services themselves need to support header propagation so that the traffic headers can be passed along. Please see the [setup guide](https://docs.sandboxes.cloud/docs/kubernetes-setup#use-sandbox-endpoint-for-conditional-interception) regarding how to set it up.

To start a conditional interception, after opening the interception dialog and selecting workloads, ports, etc., uncheck the `Intercept all traffic to the sandbox` as shown below.

<Image align="center" className="border" width="70% " border={true} src="https://files.readme.io/98f1a34-image.png" />

After clicking `NEXT`, you can get to the conditional routing dialog, where you can add endpoints in your sandbox which will inject headers that can be propagated by common tracing libraries for proper conditional interception.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/5260c00-image.png" />

For example here, we can add an endpoint named `test` and select the `frontend` service in our target namespace as entry point (as shown below).

<Image align="center" className="border" width="65% " border={true} src="https://files.readme.io/20b1966-image.png" />

After setting the endpoint, we click `START` to start the interception.

<Image align="center" className="border" width="80% " border={true} src="https://files.readme.io/9bd68a5-image.png" />

As shown in the above interception status, now the endpoint `test` is added to send traffic with special headers to the `frontend` service. And *only* traffic with these headers will be routed to the dev version of the checkout service running in the sandbox.

You can start testing your dev version of the checkout service with context of the target Kubernetes namespace without worrying about interfering other developers using the same Kubernetes namespace for their testing.

## Demo Video

A demo video for how to develop Kubernetes on Crafting can be found [here](https://youtu.be/J8LbuUVP_Do)

<Embed url="https://www.youtube.com/watch?v=J8LbuUVP_Do" title="Crafting Demo - Kubernetes" favicon="https://www.google.com/favicon.ico" image="https://i.ytimg.com/vi/J8LbuUVP_Do/hqdefault.jpg" provider="youtube.com" href="https://www.youtube.com/watch?v=J8LbuUVP_Do" typeOfEmbed="youtube" html="%3Ciframe%20class%3D%22embedly-embed%22%20src%3D%22%2F%2Fcdn.embedly.com%2Fwidgets%2Fmedia.html%3Fsrc%3Dhttps%253A%252F%252Fwww.youtube.com%252Fembed%252FJ8LbuUVP_Do%253Ffeature%253Doembed%26display_name%3DYouTube%26url%3Dhttps%253A%252F%252Fwww.youtube.com%252Fwatch%253Fv%253DJ8LbuUVP_Do%26image%3Dhttps%253A%252F%252Fi.ytimg.com%252Fvi%252FJ8LbuUVP_Do%252Fhqdefault.jpg%26key%3D7788cb384c9f4d5dbbdbeffd9fe4b92f%26type%3Dtext%252Fhtml%26schema%3Dyoutube%22%20width%3D%22854%22%20height%3D%22480%22%20scrolling%3D%22no%22%20title%3D%22YouTube%20embed%22%20frameborder%3D%220%22%20allow%3D%22autoplay%3B%20fullscreen%22%20allowfullscreen%3D%22true%22%3E%3C%2Fiframe%3E" />
