# Source: https://docs.anyscale.com/services/update.md

# Update an Anyscale service

[View Markdown](/services/update.md)

# Update an Anyscale service

This page provides an overview of the features Anyscale provides for updating services in production.

## Deploy an update to a service[​](#deploy-update "Direct link to Deploy an update to a service")

You update a service by deploying with the same name as an existing service using the CLI or SDK with the following syntax:

* CLI
* SDK

```
anyscale service deploy --config-file <config-file> -n <service-name>
```

```
import anyscale
from anyscale.service.models import ServiceConfig

service_config = ServiceConfig.from_yaml("/path/to/service-config.yaml")
# Ensure the config name matches the existing service.
anyscale.service.deploy(service_config)
```

note

Service names are unique within an Anyscale project. You can have multiple services with the same name in an Anyscale cloud or organization.

Anyscale recommends always identifying your service name, cloud, and project in the service config.

See [Configure and deploy Anyscale services](/services/deploy.md).

## How does Anyscale update services?[​](#how-update "Direct link to How does Anyscale update services?")

Anyscale updates all services using a zero-downtime rollout strategy by default, gradually transitioning traffic to the new version. The following table defines the concepts Anyscale uses to describe the update process:

| Concept         | Definition                                                                                                                                                                                                                                                                                        |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Rollout         | A *rollout* is the process Anyscale uses to incrementally update a service in production.During a rollout, your service has two versions of your Ray Serve applications running on different clusters. Anyscale gradually shifts traffic from the old version of your service to the new version. |
| Primary version | The *primary version* is the current version of a service you have in production.All running services have a primary version.                                                                                                                                                                     |
| Canary version  | The *canary version* is the version of the service you are deploying.A canary version only exists while a rollout is in progress.                                                                                                                                                                 |

When you trigger an update, the following happens:

1. Anyscale starts a new cluster to run the canary version.
2. Anyscale monitors the canary version and waits for all your Ray Serve applications to become healthy.
3. Anyscale begins to gradually shift traffic from your primary version to the canary version.
4. Anyscale terminates the primary version once all traffic has migrated to the canary version.
5. The canary version becomes the primary version.

If the canary version fails to start or becomes unhealthy during the rollout, Anyscale automatically performs a rollback for the service and sends all traffic to the primary version. By default, rollouts that don't complete within 120 minutes timeout and rollback. Contact [Anyscale support](mailto:support@anyscale.com) for help troubleshooting rollouts.

note

When you manually control a service rollout, this overrides default rollout and rollback behavior. See [Manually-controlled rollouts](#manual).

### Rollback a service during a rollout[​](#rollback-a-service-during-a-rollout "Direct link to Rollback a service during a rollout")

You can manually rollback a service during a rollout using the CLI or SDK using the following syntax:

* CLI
* SDK

```
anyscale service rollback -n <service-name>
```

```
import anyscale

anyscale.service.rollback(service_name="<service-name>")
```

See the [service rollback reference](/reference/service-api.md#anyscale-service-rollback).

## Query a specific version during a rollout[​](#query-specific-version "Direct link to Query a specific version during a rollout")

During a rollout, Anyscale automatically splits requests to the service between the primary and canary versions. Route requests to a specific version during a rollout by adding the `X-ANYSCALE-VERSION` HTTP header. Set the header value to `primary` to route to the primary version or `canary` to route to the canary version, as in the following examples:

```
curl -H "Authorization: Bearer <bearer-token>" -H "X-ANYSCALE-VERSION: primary"  <service-url>

curl -H "Authorization: Bearer <bearer-token>" -H "X-ANYSCALE-VERSION: canary" <service-url>
```

## Update a service with constrained resources[​](#resource-constrained "Direct link to Update a service with constrained resources")

By default, Anyscale fully duplicates your service cluster during a rollout. For large service clusters or services that use difficult to acquire instances such as GPUs, this might not be possible due to high costs or instance availability. To overcome these limitations, use the `--max-surge-percent` option to specify a percentage of your total service resources that Anyscale can duplicate during an incremental rollout.

* CLI
* SDK

```
anyscale service deploy --config-file /path/to/service-config.yaml --max-surge-percent=25
```

```
import anyscale
from anyscale.service.models import ServiceConfig

service_config = ServiceConfig.from_yaml("/path/to/service-config.yaml")
anyscale.service.deploy(service_config, max_surge_percent=25)
```

This option limits the total amount of Ray Serve replicas running across the two clusters as a percentage of their steady-state capacity, reducing the total quantity of hardware needed for the update.

note

You should always enable worker group autoscaling with `min_nodes=0` in your compute config when using `--max-surge-percent`. This ensures that the canary version only add worker nodes as necessary and your primary version can remove all worker nodes as replicas incrementally migrate.

For example, configuring `--max-surge-percent=25` has the following outcome:

1. Anyscale starts a canary version cluster.

2. Anyscale deploys 25% of the replicas for all applications and deployments in your service.

   <!-- -->

   * Anyscale deploys at least one replica for all deployments in your applications.
   * If replicas in your workload require specific compute instances, Anyscale deploys these instances.

3. Anyscale shifts 25% of the traffic to the canary version.

4. Anyscale reduces the capacity of the primary version by 25%.

This continues until all traffic has shifted to the canary version and the primary version can terminate, as shown in the following table:

| Canary version replicas | Canary version traffic | Primary version replicas | Primary version traffic |
| ----------------------- | ---------------------- | ------------------------ | ----------------------- |
| 0                       | 0                      | 100                      | 100                     |
| 25                      | 0                      | 100                      | 100                     |
| 25                      | 25                     | 75                       | 75                      |
| 50                      | 25                     | 75                       | 75                      |
| 50                      | 50                     | 50                       | 50                      |
| 75                      | 50                     | 50                       | 50                      |
| 75                      | 75                     | 25                       | 25                      |
| 100                     | 75                     | 25                       | 25                      |
| 100                     | 100                    | 0                        | 0                       |

Anyscale ensures that the percentage of traffic sent to a cluster never exceeds its current capacity and ensures that the total capacity across both clusters never exceeds `100 + max-surge-percent`, in this example 125%.

### How do constrained rollouts interact with replica scaling configurations?[​](#constrained-scaling "Direct link to How do constrained rollouts interact with replica scaling configurations?")

If you use static replica configurations, Anyscale rounds up when calculating the number of replicas to run in the canary version. For example, if you configure a deployment to run seven replicas at full capacity, then four replicas run at 50% capacity.

note

Until 100% of replicas and traffic migrate, at least one replica for each deployment must run in both your primary and canary version.

The percentages apply to all deployments across all applications in your service. For autoscaling deployments, the percentages adjust the `min_replicas` and `max_replicas` bounds, and autoscaling behaves as usual within these adjusted bounds.

For the canary cluster, the percentage also applies to `initial_replicas`. The adjusted `initial_replicas` value is the floor for the number of replicas until the rollout finishes.

### Rollbacks with constrained rollouts[​](#constrained-rollbacks "Direct link to Rollbacks with constrained rollouts")

When a constrained rollout fails and a rollback triggers, Anyscale attempts to return the service to a stable state as quickly as possible.

In a normal incremental rollout, Anyscale doesn't remove replicas from the primary version until all traffic has successfully migrated to the canary version. In a constrained rollout, because Anyscale incrementally removes resources as replicas migrate to the canary version, the primary version might not have sufficient replicas or worker nodes to handle all traffic during a rollback. When a rollback triggers on a constrained rollout, the following rollback behaviors trigger simultaneously:

* Anyscale routes all traffic to the primary version.
* Anyscale activates all replicas on the primary version, adding worker nodes as required.
* Anyscale deactivates all replicas on the canary version and terminates the cluster.

Requests might fail during this rollback, and might fail at a higher percentage if most replicas had already migrated to the canary version. Anyscale recommends configuring retries and timeouts to improve resilience to request failures. See [Manage timeouts and retries for Anyscale services](/services/retries-timeouts.md).

note

If you run a manual rollback with the `anyscale service rollback` command, you can specify the `max-surge-percent` to gradually shift capacity back to the original cluster.

## Manually-controlled rollouts[​](#manual "Direct link to Manually-controlled rollouts")

By default, rollouts proceed automatically and shift traffic using a predefined pattern. To manually control the rollout instead, pass the canary traffic percentage when you deploy. The traffic progression pauses at the specified traffic split until you run another command. To complete the rollout, set the canary percent to 100.

* CLI
* SDK

```
anyscale service deploy --config-file /path/to/service-config.yaml --canary-percent=50
```

To complete the rollout, use the following command:

```
anyscale service deploy --config-file /path/to/service-config.yaml --canary-percent=100
```

```
import anyscale
from anyscale.service.models import ServiceConfig

service_config = ServiceConfig.from_yaml("/path/to/service-config.yaml")
anyscale.service.deploy(service_config, canary_percent=50)
```

To complete the rollout, run `deploy` again with `canary_percent=100`.

note

You can use `--canary-percent` with `--max-surge-percent` to manually control a gradual rollout with constrained resources.

When you use manual rollouts, you must also use manual rollbacks. Setting `--canary-percent` disables automatic rollback behavior.

important

Anyscale has introduced multi-version services as a beta feature. Multi-version services provide a more extensible set of features for controlling traffic between service versions. See [Deploy multiple versions of an Anyscale service](/services/versions.md).

## Update a service in-place[​](#in-place "Direct link to Update a service in-place")

You can override default behavior for incremental rollouts by using the in-place option. This replaces your existing service with the new version. When possible, this update reuses your existing cluster and applies updates without needing to acquire new instances from the cloud provider or restart the cluster.

* CLI
* SDK

```
anyscale service deploy --config-file /path/to/service-config.yaml --in-place
```

```
import anyscale
from anyscale.service.models import ServiceConfig

service_config = ServiceConfig.from_yaml("/path/to/service-config.yaml")
anyscale.service.deploy(service_config, in_place=True)
```

caution

In-place updates don't support automatic rollback on failure. You must monitor the service status to ensure the update is successful. In case of a failed update, redeploy the service with the previous config to rollback.

You can deploy multiple applications in an Anyscale service. Updates to add or remove an application are more resilient when in-place updates fail, as these changes don't impact existing replicas for other applications. When you update existing applications or deployments, failed updates might lead to service degradation or downtime, especially if you have a low number of replicas.

Ray Serve implements in-place updates through two different methods: lightweight updates and heavyweight updates. Lightweight rollouts are generally safe for in-place updates. Heavyweight updates might lead to service downtime, especially if the in-place update fails and you must redeploy your service to rollback.

* Lightweight updates involve changing configuration options that don't affect the replica code. Changing these options doesn't require stopping old replicas and starting new ones. The following configurations are lightweight updates:

  <!-- -->

  * `num_replicas`
  * `autoscaling_config`
  * `user_config`
  * `max_ongoing_requests`
  * `graceful_shutdown_timeout_s`
  * `graceful_shutdown_wait_loop_s`
  * `health_check_period_s`
  * `health_check_timeout_s`

* Heavyweight updates involve modifying other aspects of the Ray Serve configuration that affect the replica code, such as changing code, Ray actor options, or placement groups. These updates require stopping old replicas and starting new ones.

note

You can't update the cloud, image, or compute config of a service using an in-place update.

You can't specify `--canary-percent` and `--max-surge-percent` for in-place updates.

See [Ray Serve in-place update](https://docs.ray.io/en/latest/serve/advanced-guides/inplace-updates.html) for more details.
