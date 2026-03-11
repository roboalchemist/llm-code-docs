# Source: https://docs.anyscale.com/configuration/compute/declarative.md

# Declarative compute configs

[View Markdown](/configuration/compute/declarative.md)

# Declarative compute configs

This page provides an overview of using the `required_resources` field for declarative compute configuration.

note

This feature is in beta release. Declarative compute configs are available through the CLI and SDK only using version 0.26.88 or later.

Declarative compute configs provide a unified syntax for specifying compute requirements for Anyscale clusters. These configs are highly portable and work across all cloud resources and stacks.

You use the syntax to specify the CPU, memory, GPU, and accelerator resources your workload needs. For Anyscale cloud resources backed by Kubernetes, Anyscale provisions a pod that satisfies these requirements. For cloud resources backed by VMs, Anyscale searches for available VM instance types and selects instances that match your requirements. See [How does Anyscale select VM instances?](#vm-instance-selection).

This new functionality replaces traditional compute configs, where you select from a list of predefined instance types. On Kubernetes, these instance types are pod shapes that a Kubernetes admin defines in the Helm chart. On VMs, these are cloud provider instance types such as `m5.2xlarge` or `n2-standard-8`.

## How declarative compute configs work[​](#how-it-works "Direct link to How declarative compute configs work")

Rather than specifying instance types, you define CPU and accelerator requirements for your workloads.

1. You specify the resources your workload needs using `required_resources`.
2. Optionally, you target specific hardware using `required_labels`.
3. Anyscale provisions nodes that satisfy those requirements.
4. Autoscaling works as usual, adding nodes up to `max_nodes` as needed.

For a given cloud resource to be eligible for scheduling, you must have sufficient quota in the specified region for your cloud provider account. Some Kubernetes offerings can autoprovision and autoscale node pools based on pod shape requirements, while others require that you register all resources as node pools.

important

Each node group must use either `instance_type` or `required_resources`, not both. You can mix approaches in the same compute config. For example, you can use `instance_type` for the head node and `required_resources` for worker groups.

## Define resource requirements[​](#define "Direct link to Define resource requirements")

Define resource requirements in your [compute configuration](/configuration/compute.md) using `required_resources` and, optionally, `required_labels`. For full compute config syntax, see [Compute Config API Reference](/reference/compute-config-api.md).

important

Anyscale support for TPUs requires cloud resources backed by GKE. See [Leverage Cloud TPUs on GKE](/administration/cloud-deployment/leverage-cloud-tpus-on-kubernetes.md).

### required\_resources[​](#required-resources "Direct link to required_resources")

Use `required_resources` to specify CPU, memory, and accelerator requirements for a node group.

| Resource   | Type    | Description                                      | Example        |
| ---------- | ------- | ------------------------------------------------ | -------------- |
| CPU        | Integer | Number of CPU cores.                             | `CPU: 8`       |
| memory     | String  | Memory with unit (Gi, Mi, G, M).                 | `memory: 16Gi` |
| GPU        | Integer | Number of GPUs.                                  | `GPU: 1`       |
| TPU        | Integer | Number of TPU chips.                             | `TPU: 4`       |
| tpu\_hosts | Integer | Number of TPU hosts. Required for TPU workloads. | `tpu_hosts: 1` |

### required\_labels[​](#required-labels "Direct link to required_labels")

Use `required_labels` to target specific hardware such as GPU types or TPU topologies.

| Label                     | Description                               | Example values                                     |
| ------------------------- | ----------------------------------------- | -------------------------------------------------- |
| `ray.io/accelerator-type` | GPU or accelerator type.                  | T4, A10G, A100, L4, H100, TPU-V4, TPU-V5E, TPU-V6E |
| `ray.io/tpu-topology`     | TPU topology. Required for TPU workloads. | 2x2, 2x4, 4x4                                      |

### Other worker group settings[​](#other-worker-group-settings "Direct link to Other worker group settings")

Use the following fields to control upper and lower bounds for autoscaling events and to specify whether to use spot or on-demand instances.

| Field         | Description                                                                                        |
| ------------- | -------------------------------------------------------------------------------------------------- |
| `min_nodes`   | The minimum number of nodes to keep running for this worker group.                                 |
| `max_nodes`   | The maximum number of nodes that the cluster can acquire during autoscaling for this worker group. |
| `market_type` | The type of instances to use. One of the following: `PREFER_SPOT`, `SPOT`, or `ON_DEMAND`.         |

note

Use `PREFER_SPOT` to try to deploy to spot instances but fall back to on-demand if they become unavailable.

## Examples[​](#examples "Direct link to Examples")

The following examples demonstrate declarative compute configs for common workloads.

* Basic CPU
* GPU
* Mixed CPU/GPU
* High memory
* TPU

Request CPU and memory resources for a compute workload.

```
compute_config:
  head_node:
    required_resources:
      CPU: 4
      memory: 8Gi

  worker_nodes:
    - name: cpu-workers
      required_resources:
        CPU: 8
        memory: 16Gi
      min_nodes: 1
      max_nodes: 10
      market_type: PREFER_SPOT
```

Target specific accelerator types using `required_labels`.

```
compute_config:
  head_node:
    required_resources:
      CPU: 4
      memory: 8Gi

  worker_nodes:
    # Single GPU attached to a node
    - name: t4-workers
      required_resources:
        CPU: 7
        memory: 12Gi
        GPU: 1
      required_labels:
        ray.io/accelerator-type: T4
      min_nodes: 1
      max_nodes: 5

    # Multiple GPUs attached to a node
    - name: a100-workers
      required_resources:
        CPU: 30
        memory: 200Gi
        GPU: 4
      required_labels:
        ray.io/accelerator-type: A100
      min_nodes: 1
      max_nodes: 2
```

Combine CPU-only worker groups for preprocessing with GPU workers for training.

```
compute_config:
  head_node:
    required_resources:
      CPU: 4
      memory: 8Gi

  worker_nodes:
    - name: cpu-preprocessors
      required_resources:
        CPU: 16
        memory: 32Gi
      min_nodes: 2
      max_nodes: 10

    - name: gpu-trainers
      required_resources:
        CPU: 8
        memory: 32Gi
        GPU: 1
      required_labels:
        ray.io/accelerator-type: A10G
      min_nodes: 1
      max_nodes: 4
```

Configure high-memory workers for data processing workloads.

```
compute_config:
  head_node:
    required_resources:
      CPU: 2
      memory: 4Gi

  worker_nodes:
    - name: high-memory-workers
      required_resources:
        CPU: 32
        memory: 128Gi
      min_nodes: 4
      max_nodes: 20
```

Configure TPU workers for JAX or TensorFlow workloads. Requires a GKE cluster with TPU node pools.

```
compute_config:
  head_node:
    required_resources:
      CPU: 4
      memory: 16Gi

  worker_nodes:
    - name: tpu-v6e-2x2
      required_resources:
        CPU: 7
        memory: 12Gi
        TPU: 4
        tpu_hosts: 1
      required_labels:
        ray.io/accelerator-type: TPU-V6E
        ray.io/tpu-topology: 2x2
      min_nodes: 1
      max_nodes: 5
      market_type: SPOT

    - name: tpu-v6e-2x4
      required_resources:
        CPU: 14
        memory: 24Gi
        TPU: 8
        tpu_hosts: 1
      required_labels:
        ray.io/accelerator-type: TPU-V6E
        ray.io/tpu-topology: 2x4
      min_nodes: 0
      max_nodes: 2
      market_type: SPOT
```

note

You must set the `tpu_hosts` and `ray.io/tpu-topology` fields for TPU workloads. Ensure your project has sufficient TPU quota and matching node pools.

## How does Anyscale select VM instances?[​](#vm-instance-selection "Direct link to How does Anyscale select VM instances?")

Anyscale chooses VM instance types that satisfy your requirements set in the `required_resources` and `required_labels` fields. Anyscale uses the following criteria to identify candidate instance types.

### 1. Match requirements[​](#1-match-requirements "Direct link to 1. Match requirements")

For each cloud resource available to your workload, Anyscale filters instances in your cloud and region that match what you requested. Anyscale uses fuzzy matching for CPU and memory requirements, but exact matching for GPU requirements, as described in the following table:

| Configuration               | Description                                                                                                                          |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| CPU count                   | Seeks instances that have approximately this many CPUs. Anyscale considers instance types with up to double the specified CPU count. |
| Memory                      | Seeks instances that have approximately this much memory. Anyscale considers instance types with up to double the specified memory.  |
| GPU count                   | Anyscale only considers instances that have exactly the number of GPUs you specify.                                                  |
| GPU type (accelerator type) | Anyscale only considers instances that have the exact GPU type you specify.                                                          |

### 2. Rank by cost efficiency[​](#2-rank-by-cost-efficiency "Direct link to 2. Rank by cost efficiency")

Anyscale ranks instances using a cost-efficiency score tuned to find the best resource fit at lowest cost.

### 3. Select primary and fallback options[​](#3-select-primary-and-fallback-options "Direct link to 3. Select primary and fallback options")

For the head node, Anyscale selects the single best-matching instance type.

note

Some single-node development workloads might be appropriate to run on a single node with GPU enabled. Standard Anyscale clusters with worker nodes don't schedule Ray tasks and actors to the head node, and so don't need GPUs.

Anyscale recommends always using on-demand instances for your head node for workload stability.

For worker nodes, Anyscale selects the most cost-effective instance type by default. Anyscale can select up to the top three matches for a worker group to improve availability when one instance type is capacity-constrained. For workers with multiple instance types, the system creates instance groups that share the same logical worker resource, respecting min and max thresholds set for the worker group and the cluster. Anyscale launches lower-cost options first.

### 4. Spot consideration[​](#4-spot-consideration "Direct link to 4. Spot consideration")

If you specify the `PREFER_SPOT` option for market type for a worker group, Anyscale includes both spot and on-demand instances in the ranking. Anyscale launches spot instances first when available and falls back to on-demand.

## How does Anyscale select pod shapes on Kubernetes?[​](#kubernetes "Direct link to How does Anyscale select pod shapes on Kubernetes?")

On Kubernetes, declarative compute configs bypass the instance types defined in the Helm chart for the Anyscale operator. You don't need to define instance types in the Helm chart for worker groups that use `required_resources`. Anyscale dynamically defines pod shapes from your requirements, so you don't need to patch and redeploy the Helm chart.

Kubernetes schedules pods onto nodes that can satisfy the requested resources. Ensure your Kubernetes cluster has nodes with sufficient capacity and the required accelerators available.

For general Kubernetes compute config options such as tolerations, node selectors, and volume mounts, see [Compute configuration options for Kubernetes](/configuration/compute/kubernetes.md).

## Best practices[​](#best-practices "Direct link to Best practices")

* Profile workloads to understand actual resource needs.
* Leave headroom for Ray overhead (CPU and memory).
* Use meaningful worker group names for observability.
* Test autoscaling with small minimums first.
* Monitor real usage and refine resource specifications over time.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Kubernetes Pods stuck in pending[​](#pods-pending "Direct link to Kubernetes Pods stuck in pending")

* Ensure cluster nodes can satisfy requested resources.
* Verify required labels match node labels.
* Confirm requests don't exceed single-node capacity.

### Nodes not launching (VM-based clouds)[​](#vm-not-launching "Direct link to Nodes not launching (VM-based clouds)")

* Ensure at least one instance type in your cloud and region satisfies your `required_resources`. See [How does Anyscale select VM instances?](#vm-instance-selection).
* Verify you have sufficient quota for the instance types in your cloud provider account.

### Pods or nodes not using expected hardware[​](#wrong-hardware "Direct link to Pods or nodes not using expected hardware")

* Verify accelerator labels on nodes.
* Check label spelling and capitalization.
* Verify `required_resources` and `required_labels`.
* Confirm the instance type exists in your region and that you have quota.

### TPU pods not starting[​](#tpu-not-starting "Direct link to TPU pods not starting")

* Confirm you've set `tpu_hosts` and `ray.io/tpu-topology`.
* Ensure TPU count matches topology.
* Verify TPU quota and node pool configuration.
