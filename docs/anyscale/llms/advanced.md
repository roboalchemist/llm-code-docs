# Source: https://docs.anyscale.com/configuration/compute/advanced.md

# Advanced settings for compute configs on Anyscale

[View Markdown](/configuration/compute/advanced.md)

# Advanced settings for compute configs on Anyscale

This page provides an overview of advanced features for compute configs on Anyscale. These options are common to all Anyscale resource configurations.

Some compute config settings are cloud-specific. See the following pages:

* [Compute configurations for AWS](/configuration/compute/aws.md)
* [Compute configuration options for Google Cloud](/configuration/compute/gcp.md)
* [Compute configuration options for Kubernetes](/configuration/compute/kubernetes.md)

## Configure threshold for checking for spot instances[​](#fallback-threshold "Direct link to Configure threshold for checking for spot instances")

When you configure worker nodes to prefer spot instances but fall back to on-demand virtual machines, you can customize how quickly Anyscale checks for spot instance availability after falling back to on-demand instances. By default, Anyscale sets this value to 60 minutes. Set a lower value to instruct Anyscale to preempt on-demand worker nodes in your cluster when spot instances become available.

Use the `replacement_threshold` setting to override this default behavior. You can configure this setting for your entire cluster or for a group of worker nodes. Valid time units are `s` (seconds), `m` (minutes), and `h` (hours).

The following example sets this threshold to 15 minutes:

```
{
  "replacement_threshold": "15m"
}
```

You also use this setting to configure node replacement groups. See [Configure node replacement](#node-replacement).

## Adjustable downscaling[​](#adjustable-downscaling "Direct link to Adjustable downscaling")

The Anyscale platform automatically downscales worker nodes that have been idle for a given period. By default, the timeout period ranges from 30 seconds to 4 minutes and is dynamically adjusted for each node group based on the workload. For example, short, bursty workloads have shorter timeouts and more aggressive downscaling. Adjustable downscaling allows users to adjust this timeout value at the cluster-level based on their workload needs.

* Anyscale console
* CLI

To adjust the timeout value from the Anyscale console, use the **Advanced features** tab under the **Advanced settings** for the cluster. This example sets the timeout to 60 seconds for all nodes in the cluster.

```
{
  "idle_termination_seconds": 60
}
```

To adjust the timeout value from the Anyscale CLI, use the `flags` field. This example YAML sets the timeout value to 60 seconds for all nodes in the cluster.

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_WORKER
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
flags:
  idle_termination_seconds: 30
```

## Cross-zone scaling[​](#cross-zone "Direct link to Cross-zone scaling")

Cross-zone scaling is a feature that allows Anyscale to launch your Ray cluster across multiple availability zones. By default, all worker nodes are launched in the same availability zone. With cross-zone scaling enabled, Anyscale first attempts to launch worker nodes in existing zones, but if that fails, then tries the next-best zone (based on availability).

Use this feature if:

* You want to maximize the chances of provisioning desired instance types.
* You want to spread Serve app replicas across multiple zones for better resilience and availability.
* Your workloads have no heavy inter-node communication or the incurred inter-availability zone cost is acceptable.

- Anyscale console
- CLI

To enable or disable this feature from the Anyscale console, use the "Enable cross-zone scaling" checkbox under the **Advanced settings** for the cluster.

To enable or disable this feature from the Anyscale CLI, use the `enable_cross_zone_scaling` field. This example YAML enables cross-zone scaling for all nodes in the cluster.

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_WORKER
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
enable_cross_zone_scaling: true
```

## Resource limits[​](#resource-limits "Direct link to Resource limits")

Cluster-wide resource limits allow you to define minimum and maximum values for any resource across all nodes in the cluster. There are two common use cases for this feature:

1. Specifying the maximum number of GPUs to avoid unintentionally launching a large number of expensive instances.
2. Specifying a custom resource for specific worker nodes and using that custom resource value to limit the number of nodes of those types.

* Anyscale console
* CLI

To set the maximum number of CPUs and GPUs in a cluster from the Anyscale console, use the "Maximum CPUs" and "Maximum GPUs" fields under the **Advanced settings** for the cluster.

To set other resource limits, use the **Advanced features** tab under the **Advanced settings** for the cluster. To add a custom resource to a node group, use the **Ray config** tab under the **Advanced config** section for that node group.

This example limits the minimum resources to 1 GPU and 1 `CUSTOM_RESOURCE` and limits the maximum resources to 5 `CUSTOM_RESOURCE`.

```
{
  "min_resources": {
    "GPU": 1,
    "CUSTOM_RESOURCE": 1
  },
  "max_resources": {
    "CUSTOM_RESOURCE": 5,
  }
}
```

To set resource limits for a cluster from the Anyscale CLI, use the `min_resources` and `max_resources` fields. This example YAML adds a custom resource to a worker node, limits the minimum resources to 8 CPU and 1 `CUSTOM_RESOURCE`, and limits the maximum resources to 1 GPU and 5 `CUSTOM_RESOURCE`.

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_WORKER
    resources:
      CUSTOM_RESOURCE: 1
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
min_resources:
  CPU: 8
  CUSTOM_RESOURCE: 1
max_resources:
  GPU: 1
  CUSTOM_RESOURCE: 5
```

## Workload starting and recovering timeouts[​](#timeouts "Direct link to Workload starting and recovering timeouts")

The workload starting timeout allows you to configure how long a workload should attempt to acquire the minimum resources when it first starts, before Anyscale terminates it.

After a workload is running, it may enter the `RECOVERING` state if it's attempting to recover the minimum resources, for example, due to spot preemption. The workload recovering timeout allows you to configure how long a workload may remain in the `RECOVERING` state, to avoid the cost of idling existing nodes.

By default, Anyscale sets both timeouts to 25 minutes.

info

These timeouts only apply to jobs and workspaces, not services.

* Anyscale console
* CLI

To configure the workload starting and recovering timeouts from the Anyscale console, use the **Advanced features** tab under the **Advanced settings** for the cluster. This example increases the workload starting timeout to 1 hour and decreases the workload recovering timeout to 10 minutes.

Valid time units are: `s`, `m`, and `h`. For example, `1h30m`.

```
{
  "workload_starting_timeout": "1h",
  "workload_recovering_timeout": "10m"
}
```

To configure the workload starting and recovering timeouts from the Anyscale CLI, use the `flags` field. This example increases the workload starting timeout to 1 hour and decreases the workload recovering timeout to 10 minutes.

Valid time units are: `s`, `m`, and `h`. For example, `1h30m`.

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_WORKER
flags:
  workload_starting_timeout: 1h
  workload_recovering_timeout: 10m
```

## Zonal startup timeout[​](#zonal-timeout "Direct link to Zonal startup timeout")

Anyscale attempts to pack cluster and worker group nodes into the same zone to improve cluster communication performance and minimize cross zone data transfer.

However, machines may not always be available because of capacity constraints, IP addresses, or other reasons. If Anyscale is unable to get the requested minimum resources, Anyscale terminates any existing nodes and sequentially tries the request in a different zone within the cloud deployment.

By default, Anyscale sets the zonal startup timeout to 10 minutes.

* Anyscale console
* CLI

To configure the workload zonal startup timeout from the Anyscale console, use the **Advanced features** tab under the **Advanced settings** for the cluster. This example decreases the workload zonal startup timeout to 5 minutes.

Valid time units are: `s`, `m`, and `h`. For example, `1h30m`.

```
{
  "zone_starting_timeout": "5m"
}
```

To configure the workload zonal startup timeout from the Anyscale CLI, use the `flags` field. This example decreases the workload zonal startup timeout to 5 minutes.

Valid time units are: `s`, `m`, and `h`. For example, `1h30m`.

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_WORKER
flags:
  zone_starting_timeout: 5m
```

## Configure instance ranking and replacement[​](#rank "Direct link to Configure instance ranking and replacement")

You can configure custom worker group ranking, selection strategy, and replacement behavior.

Anyscale uses the following defaults when adding nodes to your Ray cluster:

* Use the smallest node feasible for the workload.
* Don't add GPU worker nodes for CPU-only workloads.
* Prioritize CPU-only worker groups over GPU worker groups.
* Prioritize spot instance over on-demand.
* Prioritize available instance types.

The following sections describe customizing this behavior.

### Instance selection strategy[​](#instance-selection "Direct link to Instance selection strategy")

Set the `instance_selection_strategy` parameter to `relaxed` to override default behavior to prefer smaller nodes.

* Anyscale console
* CLI

To configure the instance ranking strategy from the Anyscale console, use the **Advanced features** tab under the **Advanced settings** for the cluster.

```
{
  "instance_selection_strategy": "force_smallest_fit" | "relaxed",
}
```

To configure the instance ranking strategy from the Anyscale CLI, use the `flags` field when defining a compute config YAML:

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_WORKER
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
flags:
  instance_selection_strategy: force_smallest_fit | relaxed
```

### Price-based ranking strategy[​](#price "Direct link to Price-based ranking strategy")

You can use instance prices to determine ranking for worker groups.

important

This feature is in beta release and only available for Anyscale clouds on AWS using virtual machines.

When you enable price-based ranking, Anyscale makes ranking decisions for worker selection based on pricing details provided by AWS. You can optionally add pricing weights to instances types in your worker group configurations. Anyscale applies pricing weights by dividing the cost by the pricing weight, meaning that higher pricing weights increase the priority for an instance type.

note

Anyscale doesn't refresh prices from AWS in real-time. Spot prices refresh asynchronously every three hours, while on-demand prices refresh at least monthly.

Price-based ranking treats capacity reservations and machine pool instances as having no price, meaning these instances have the highest priority. Price-based ranking uses the `relaxed` instance selection strategy, meaning that Anyscale might deploy larger instance types if they have a lower price.

You enable price-based ranking for the entire cluster using the following syntax:

* Anyscale console
* CLI

In the Anyscale console, use the **Advanced features** tab under the **Advanced settings** for the cluster.

```
{
  "instance_ranking_strategy": [
    {"ranker_type": "price"}
  ]
}
```

In the Anyscale CLI, use the `flags` field.

```
flags:
  instance_ranking_strategy:
    - ranker_type: price
```

You enable pricing weights for instance types using the following syntax:

* Anyscale console
* CLI

In the Anyscale console, use the **Advanced config > Flags** section for each worker node.

```
{"pricing_weight": 2}
```

In the Anyscale CLI, use the `flags` field for each worker node.

```
worker_nodes:
  - instance_type: m5.2xlarge
    market_type: SPOT
    flags:
      pricing_weight: 2
  - instance_type: m5.4xlarge
    market_type: SPOT
    flags:
      pricing_weight: 4
```

important

You can use price-based ranking alongside worker group ranking, including pricing weights. Anyscale applies ranking strategies in the order specified.

For example, add `price` after `custom_group_order` to use pricing information to rank instances within a ranking group, as in the following example:

```
"ranker_type": ["custom_group_order", "price"]
```

### Worker group ranking[​](#worker-ranking "Direct link to Worker group ranking")

Use worker group ranking to set custom prioritization rules for worker groups. This allows you to specify rules that allow for less-preferred instances for fallback or large scaling events while still using your preferred instance types when possible. For example, you could configure a workload to prefer reserved capacity instances, then spot instances, and then on-demand instances.

You specify rules in order of ranking preference, with higher-ranked worker groups listed first. Node replacement also respects worker group ranking, allowing you to automatically replace lower-ranked nodes with higher-ranked node when they become available. See [Configure node replacement](#node-replacement).

The following example demonstrates configuring group ranking for three worker groups named `spot-worker-1`, `spot-worker-2`, and `on-demand-worker`. In this example, Anyscale prioritizes the spot groups over the on-demand group, but the two spot groups have equal priority.

* Anyscale console
* CLI

Specify worker group ranking in the **Advanced features** tab under the **Advanced settings**:

```
{
  "instance_ranking_strategy": [
    {
      "ranker_type": "custom_group_order",
      "ranker_config": {
        "group_order": [
          ["spot-worker-1", "spot-worker-2"],
          "on-demand-worker"
        ]
      }
    },
  ]
}
```

Specify worker group ranking using the `flags` field at the top level of your compute config YAML:

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - name: spot-worker-1
    instance_type: INSTANCE_TYPE_WORKER_1
    market_type: SPOT
  - name: spot-worker-2
    instance_type: INSTANCE_TYPE_WORKER_2
    market_type: SPOT
  - name: on-demand-worker
    instance_type: INSTANCE_TYPE_WORKER_3
    market_type: ON_DEMAND
flags:
  instance_ranking_strategy:
    - ranker_type: custom_group_order
      ranker_config:
        group_order:
          - - spot-worker-1
            - spot-worker-2
          - on-demand-worker
```

### Configure node replacement[​](#node-replacement "Direct link to Configure node replacement")

info

The node replacement feature is in beta release.

Node replacement works alongside custom worker group ranking to automatically replace nodes launched from less-preferred worker groups when resources become available in a higher-ranking worker group. See [Worker group ranking](#worker-ranking).

Anyscale only attempts to launch a replacement node that's at least as large as the existing node, taking into account CPUs, GPUs, memory, accelerator type, and any user-defined custom resources, to ensure that any workload running on the existing node is able to run on the replacement node. You can configure the replacement threshold, the duration a worker node must run for before Anyscale can replace it, to match your workload checkpointing.

One common use case for this feature is for prioritizing multiple spot worker groups over on-demand worker groups.

The following example compute config contains two spot instance worker groups and two on-demand worker groups. It sets a replacement threshold of 30 minutes. Anyscale attempts to launch the spot workers before the on-demand workers, and attempts to replace any on-demand workers with spot workers after 30 minutes. Anyscale doesn't replace the spot workers with each other, or replace the on-demand workers with each other either.

* Anyscale console
* CLI

To configure node replacement from the Anyscale console, specify a custom group order with `enable_replacement` set to `true` and the `replacement_threshold`, using the **Advanced features** tab under the **Advanced settings** for the cluster.

Valid time units for the replacement threshold are: `s`, `m`, and `h`. For example, `1h30m`.

```
{
  "replacement_threshold": "30m",
  "instance_ranking_strategy": [
    {
      "ranker_type": "custom_group_order",
      "ranker_config": {
        "enable_replacement": true,
        "group_order": [
          ["worker-1/spot", "worker-2/spot"],
          ["worker-1/on-demand", "worker-2/on-demand"]
        ]
      }
    },
  ]
}
```

To configure node replacement from the Anyscale CLI, specify a custom group order with `enable_replacement` set to `true` and the `replacement_threshold`, using the `flags` field.

Valid time units for the replacement threshold are: `s`, `m`, and `h`. For example, `1h30m`.

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - name: worker-1
    instance_type: INSTANCE_TYPE_WORKER_1
    market_type: PREFER_SPOT
  - name: worker-2
    instance_type: INSTANCE_TYPE_WORKER_2
    market_type: PREFER_SPOT
flags:
  replacement_threshold: 30m
  instance_ranking_strategy:
    - ranker_type: custom_group_order
      ranker_config:
        enable_replacement: true
        group_order:
          - - worker-1/spot
            - worker-2/spot
          - - worker-1/on-demand
            - worker-2/on-demand
```

## Disable NFS mounts[​](#disable-nfs "Direct link to Disable NFS mounts")

Anyscale clouds deployed with NFS use NFS mounts for shared storage locations.

NFS can lead to issues in large jobs or services because of resource limits for concurrent connections enforced by cloud providers.

note

Anyscale clouds deployed after July 14, 2025, use cloud object storage for shared storage locations by default. All cloud deployments can optionally configure NFS.

You can use the CLI command `anyscale cloud get` to see if your Anyscale cloud has NFS configured.

* Anyscale console
* CLI

To disable NFS mounts from the Anyscale console, use the **Advanced features** tab under the **Advanced settings** for the cluster.

```
{
  "disable_nfs_mount": true,
}
```

To disable NFS mounts from the Anyscale CLI, use the `flags` field.

```
cloud: CLOUD_NAME
head_node:
  instance_type: INSTANCE_TYPE_HEAD
worker_nodes:
  - instance_type: INSTANCE_TYPE_WORKER
    min_nodes: MIN_NODES
    max_nodes: MAX_NODES
flags:
  disable_nfs_mount: true
```

## Control head node scheduling[​](#head-node "Direct link to Control head node scheduling")

Anyscale turns off head node scheduling by default for multi-node clusters. This protects the Ray cluster from instability, as the head node contains important system processes such as the global control service, the Ray driver process, and the API server.

Anyscale recommends against scheduling on the head node. Scheduling on the head node can lead to the following under heavy load:

* The actors and tasks running on the head node contend for resources and interrupt the operation of these system components.
* The Ray cluster becomes unstable and unable to recover from failures properly.

Anyscale schedules to the head node in the following configurations:

* You define logical resources in the **Advanced config > Ray config** for the head node of your Anyscale cluster.
* You configure a single-node cluster by only defining a head node and no worker nodes.

The following table shows examples of several compute configs and describes cluster shape and head node scheduling:

| Cluster shape                                 | Config YAML                                                                                                                                                 | Description                                                                                                                                                          |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Single-node cluster                           | ```
head_node:
    - instance_type: m5.2xlarge
auto_select_worker_config: false
```                                                                             | Single-node clusters only define the head node. In this configuration, all compute runs on the head node.                                                            |
| Multi-node cluster with auto-selected workers | ```
head_node:
    instance_type: m5.2xlarge
auto_select_worker_config: true
```                                                                                | Define a head node and specify `auto_select_worker_nodes` to allow Anyscale to automatically select worker nodes for your cluster. All compute runs on worker nodes. |
| Multi-node cluster with defined workers       | ```
head_node:
    instance_type: m5.2xlarge
worker_nodes:
    - name: gpu-group
      instance_type: p4de.24xlarge
```                                           | If you manually specify worker nodes, all compute runs on worker nodes.                                                                                              |
| Multi-node cluster with head scheduling       | ```
head_node:
    instance_type: m5.2xlarge
    resources:
        CPU: 8
        GPU: 0
worker_nodes:
    - name: gpu-group
      instance_type: p4de.24xlarge
``` | In a multi-node cluster, specify CPU resources on the head node to enable scheduling on the head node.                                                               |

## Use labels to control scheduling[​](#labels "Direct link to Use labels to control scheduling")

In Ray 2.49.0 or later, you can use labels to control scheduling.

important

This feature is in beta release.

Don't use this feature with node replacement, as node replacement doesn't respect labels when evaluating ranks. This can result in attempting to assign an actor or task to a node in a worker group that doesn't have the correct labels.

Anyscale supports labels for all configured cloud resources. All labels are string values.

The following table describes the default labels set for each node in your cluster:

| Label                      | Description                                                                                                                                                                                                                 |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ray.io/node-id`           | A unique ID generated for the node.                                                                                                                                                                                         |
| `ray.io/accelerator-type`  | The accelerator type of the node, for example `L4`. CPU-only machines don't have the label.                                                                                                                                 |
| `ray.io/market-type`       | Indicates whether the node uses `spot` instances or `on-demand` instances.                                                                                                                                                  |
| `ray.io/node-group`        | The name of the node worker group or `head` for the head node. Invalid character in worker group names are replaced by underscores (`_`). For example, the Anyscale default name `1xT4:4CPU-16GB` becomes `1xT4_4CPU-16GB`. |
| `ray.io/region`            | The cloud region of the node.                                                                                                                                                                                               |
| `ray.io/availability-zone` | The availability zone of the node.                                                                                                                                                                                          |

You can add custom labels to your nodes using the Anyscale console, CLI, or SDK. You specify labels as JSON-formatted key-value pairs.

In the Anyscale console, you can find the field for defining labels by navigating to **Advanced config > Ray config > Labels** for the head node or worker node group when creating or versioning a compute config. See [Create or version a compute config](/configuration/compute/create.md).

You use labels by adding them to your Ray code with the following syntax:

```
@ray.remote(label_selector={"label_key": "label_value"})
    pass
```

For example, use the following to force a function to only schedule to instances with Nvidia L4 GPU:

```
@ray.remote(label_selector={"ray.io/accelerator-type": "L4"})
def f():
    pass
```

### Example: Schedule Ray code to a specific worker group on Anyscale[​](#example-schedule-ray-code-to-a-specific-worker-group-on-anyscale "Direct link to Example: Schedule Ray code to a specific worker group on Anyscale")

This example demonstrates how you can use custom labels to directly specify a worker group for scheduling Ray code. Here the pattern controls scheduling Ray code to worker groups with CPU-only machines.

When defining a Ray cluster, add the following custom label to the configuration for each worker group with CPU-only machines:

```
{
  "cpu-only": "True"
}
```

In your Ray code, specify the custom label and value using the `label_selector` option for `@ray.remote()`, as in the following example:

```
import ray

@ray.remote(label_selector={"cpu-only": "True"})
def hello_world():
   return "Hello World!"

result = ray.get(hello_world.remote())
print(result)
```

This patterns ensures that Ray always schedules the `hello_world` function to nodes in a worker group with the `cpu-only` label set to `True`.
