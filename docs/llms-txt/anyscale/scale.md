# Source: https://docs.anyscale.com/services/scale.md

# Configure replica scaling for Anyscale services

[View Markdown](/services/scale.md)

# Configure replica scaling for Anyscale services

Anyscale recommends deploying production services with replicas to support high availability, increased throughput, and resilience to node failure.

This page provides an overview of support for controlling replica scaling on Anyscale services, including the following:

* Best practices for distributing replicas across nodes and availability zones.
* Autoscaling services on Anyscale.
* How replica compaction works.
* Configuring fixed values for replicas.

## Anyscale features for replica scaling[​](#anyscale-features "Direct link to Anyscale features for replica scaling")

Anyscale services extend on Ray Service feature to provide enhanced autoscaling functionality and greater reliability. The following table outlines some of these features:

| Feature                                    | Description                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fast node deployment                       | Anyscale optimizes worker node deployment, which allows for fast autoscaling and the ability to use spot instance with on-demand fallback. Specific features include the following:- [Fast model loading for PyTorch models](/services/fast-loading.md)<br />- [Image caching for optimized deploys](/container-image.md#cache)                                                                                                        |
| Zone-aware scaling and scheduling          | Anyscale services are zone-aware for scaling and scheduling. This improves resilience and availability for your services. See [Enable multiple availability zones for services](#zone-aware).                                                                                                                                                                                                                                          |
| Replica compaction                         | Anyscale monitors nodes and replicas and attempts to migrate replicas to the fewest number of worker nodes that fulfill the needs of your application. See [Save resources with replica compaction](#replica-compaction).                                                                                                                                                                                                              |
| Support for spot instances with preemption | Anyscale services support using spot instances, on-demand instances, or spot instances with fallback to on-demand.When you use spot instances with fallback to on-demand, Anyscale reacts to the 2 minute spot preemption warning from the cloud provider by attempting to spin up and migrate replicas to on-demand instances, resulting in little to no downtime while benefitting from cost savings associated with spot instances. |

## Best practices for replica configuration[​](#best-practices "Direct link to Best practices for replica configuration")

Anyscale provides the following recommendations and best practices for configuring production services for resiliency, latency, performance, and cost efficiency. Each Ray Serve application is unique, so your specific requirements might differ from general recommendations. Contact [Anyscale support](mailto:support@anyscale.com) for assistance with configuring or troubleshooting your Anyscale services.

| Recommendation                            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Use autoscaling                           | Autoscaling allows you to dynamically scale your service to relieve backpressure on application endpoints. To enable autoscaling, do the following:- Configure your Ray Serve application to [autoscale replicas](#replica-scaling).<br />- Configure your Anyscale service to [autoscale worker nodes](#worker-scaling).                                                                                                                                                                                                                                                                 |
| Set a lower bound for autoscaling         | Specify a minimum number of replicas needed for each endpoint based on your traffic and latency requirements.- Set this value to `0` to shut down an endpoint during periods of low traffic. Don't use scale-to-zero on ingress deployments if you're using high-throughput serving. See [High-throughput serving](/runtime/serve.md#high-throughput).<br />- Set this value to `2` or more to ensure the endpoint always has a fallback.You must also configure autoscaling for your worker nodes to downscale your cluster. Cluster downscaling respects the requirements for replicas. |
| Spread replicas across nodes              | Having replicas on multiple nodes reduces the likelihood of endpoint downtime due to node failure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Spread replicas across availability zones | Anyscale attempts to scale worker nodes and replicas across all availability zones, making your service resilient to zone outages.Not all compute types are available in all zones, especially for GPU resources. Consider using machine pools and capacity reservations to ensure resource availability for GPU-intensive applications.                                                                                                                                                                                                                                                  |
| Use spot instances when available         | Spot instances provide significant savings in cloud provider costs. Anyscale's optimization for deploying worker nodes allows your application to use spot instances when available and fallback to on-demand compute without service downtime.                                                                                                                                                                                                                                                                                                                                           |
| Customize autoscaling thresholds          | You can configure all aspects of Ray Serve autoscaling to control upscaling and downscaling behaviors for your applications.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

## What is Anyscale service autoscaling?[​](#autoscaling "Direct link to What is Anyscale service autoscaling?")

Services use request based autoscaling to dynamically scale the number of replicas in your deployments up or down in response to incoming traffic. This allows your models to upscale to handle variable traffic loads and downscale to save costs by removing idle compute resources from your cluster.

Service autoscaling occurs in two phases:

* Anyscale scales replicas for deployments up or down based on the number of requests enqueued across replicas compared to the target threshold set for your deployment.
* Anyscale scales worker nodes based on the configured CPU and GPU requirements configured for each replica.

You must configure autoscaling in both your Ray Serve application and your compute config.

note

For multi-version services, each version scales independently based on its own service configuration and traffic. See [Deploy multiple versions of an Anyscale service](/services/versions.md).

## Configure replica autoscaling for a deployment[​](#replica-scaling "Direct link to Configure replica autoscaling for a deployment")

Anyscale recommends configuring the following options for every deployment in your service application with autoscaling enabled:

| Option                    | Description                                                                                                                                                                                                                                              | Default |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| `min_replicas`            | The lower bound for autoscaling. Set this value to the minimum threshold required to support requests during low traffic periods.                                                                                                                        | `1`     |
| `max_replicas`            | The upper bound for autoscaling. Prevents your application from scaling uncontrollably. Must be higher than `min_replicas`.                                                                                                                              | `1`     |
| `target_ongoing_requests` | The desired number of requests assigned to a replica. Ongoing requests include active requests and enqueued requests.When active requests exceed this threshold, replicas scale up. When active requests don't meet this threshold, replicas scale down. | `2`     |
| `max_ongoing_requests`    | The upper limit for how many requests a replica can have assigned. Set this value relative to `target_ongoing_requests`.When requests exceed the `max_ongoing_requests`, the service rejects new requests and sends a `503` HTTP message.                | `5`     |

The following syntax examples sets these options:

```
from ray import serve

@serve.deployment(
    max_ongoing_requests: 10,
    autoscaling_config={
        "min_replicas": 2,
        "max_replicas": 5,
        "target_ongoing_requests": 5,
    },
)
class MLModel:
    ...
```

note

You can't set an integer value for `num_replicas` when configuring autoscaling.

For a minimum autoscaling configuration, set `max_replicas` to a value higher than `1`.

You can specify additional options to control how aggressively scaling events trigger due to changes in traffic. See the [Ray Serve docs on autoscaling](https://docs.ray.io/en/latest/serve/advanced-guides/advanced-autoscaling.html).

## Enable worker group autoscaling in the compute config[​](#worker-scaling "Direct link to Enable worker group autoscaling in the compute config")

You must enable autoscaling for your worker node groups in your compute config for Anyscale services to autoscale properly. See [Worker nodes scaling config](/configuration/compute.md#scaling).

note

Anyscale uses machine pools to manage cloud capacity reservations and share fixed resources across jobs, services, and workspaces. You can use machine pools with Anyscale services and autoscaling to help control costs and leverage fixed-cost infrastructure. See [Share compute resources with Anyscale machine pools](/machine-pools.md).

Anyscale recommends setting thresholds in your compute config that allow the autoscaling configurations for your deployments to control scaling behaviors. This means the following:

* Configure the minimum number of nodes for each worker group to be less than global minimum for CPUs or GPUs required when all replicas in your service have fully scaled down. Setting this value to `0` for all worker groups provides your service the greatest flexibility in downscaling.
* Configure the maximum number of nodes for each worker group to be greater than the global maximum for CPUs or GPUs required when all replicas in your service have fully scaled up.

## Spread replicas across nodes[​](#spread-replicas "Direct link to Spread replicas across nodes")

Anyscale recommends configuring your services to have at least two replicas for each deployment and that each deployment has replicas on at least two worker nodes. This redundancy prevents failure due to a worker node crashing.

To avoid scheduling replicas to the same node, use the `max_replicas_per_node` option. The following syntax example shows a configuration that guarantees at least two replicas deployed on different nodes:

```
from ray import serve

@serve.deployment(
    autoscaling_config={
        "min_replicas": 2,
        "max_replicas": 5,
    },
    max_replicas_per_node=1,
)
class MyApp:
    ...

app = MyApp.bind()
```

## Enable multiple availability zones for services[​](#zone-aware "Direct link to Enable multiple availability zones for services")

note

Anyscale clouds backed by Kubernetes deploy all replicas to the same zone.

For Anyscale clouds configured on virtual machines, Anyscale automatically spreads replicas across zones if you have multiple zones enabled for your service. The following describes behavior during scaling and scheduling:

* During auto-scaling events, replicas attempt to scale across all zones allowed by your compute config.
  <!-- -->
  * If the replica requires more compute resources, the replica can scale to add additional worker nodes in the same availability zone.
* When routing requests between replicas, Anyscale prefers replicas in the same zone to minimize network costs.

## Save resources with replica compaction[​](#replica-compaction "Direct link to Save resources with replica compaction")

As your service scales up and down, downscaled replicas can leave empty compute resources on worker nodes. To save costs, Anyscale periodically checks for opportunities to compact replicas down to a smaller number of nodes.

Replication compaction uses a start-then-stop model, where existing replicas don't stop serving traffic until the new replicas are fully operational. The following describes this behavior:

* The head node monitors the cluster for idle compute resources.

* When the head node detects enough idle CPU or GPU capacity to remove a worker node, the following occurs:

  <!-- -->

  * The head node identifies a candidate worker node to remove.
  * For each replica running on the worker node, a new replica initializes on a different node in the cluster.
  * New requests route to the new replicas.
  * The head node terminates all replicas on the candidate node.
  * Anyscale remove the worker node from the cluster.

Anyscale uses replica compaction by default. To turn it off, add the following environment variable to your container image: `RAY_SERVE_USE_COMPACT_SCHEDULING_STRATEGY=0`.

## Specify a fixed replica size[​](#fixed "Direct link to Specify a fixed replica size")

You can optionally specify a fixed replica size for each deployment in your service. This can be useful to control costs during development and testing.

note

For most production use cases, Anyscale recommends using replica autoscaling. Set a `min_replicas` threshold greater than `0` to maintain uptime for your deployment, and set a `max_replicas` threshold to prevent runaway scaling events and unexpected costs.

Specify a fixed size by setting the `num_replicas` option to a positive integer. This disables replica autoscaling for the deployment. The default value for `num_replicas` is `1`. Setting `num_replicas` with any `autoscaling_config` options results in failure.

The following syntax example configures this to `2`:

```
from ray import serve

@serve.deployment(num_replicas=2)
class MLModel:
    ...
```

You can manually scale your service by increasing or decreasing the value `num_replicas` in your deployment. The Anyscale services config is a superset of the Ray Serve config. You can override replica configurations when updating your service with `anyscale service deploy` by specifying configurations for the deployment in the `applications` section of your service config. See [Update an Anyscale service](/services/update.md).
