# Source: https://docs.anyscale.com/machine-pools.md

# Share compute resources with Anyscale machine pools

[View Markdown](/machine-pools.md)

# Share compute resources with Anyscale machine pools

This page provides an overview of configuring machine pools to share virtual machines across Anyscale jobs, services, and workspaces. Anyscale supports configuring machine pools using capacity reservations, spot instances, and on-demand virtual machines.

Anyscale uses the global resource scheduler to manage resources in machine pools. See [What is the global resource scheduler?](/machine-pools/global-resource-scheduler.md).

info

Machine pools and the global resource scheduler are in beta release.

For an example, see [Tutorial: Create and use an Anyscale-managed machine pool](/machine-pools/tutorial.md).

note

You can also configure machine pools for cloud resources backed by Kubernetes, including on-prem Kubernetes clusters. Contact [Anyscale Support](mailto:support@anyscale.com) to configure machine pools on Kubernetes.

## What are machine pools?[​](#what-are-machine-pools "Direct link to What are machine pools?")

A machine pool defines a fixed-size group of provisioned compute resources. Anyscale recommends using machine pools to leverage compute reservations in your cloud provider account. You can optionally configure machine pools to also manage spot and on-demand instances, allowing for intelligent scheduling and fallback across capacity reservations, spot instances, and on-demand instances. Because of the limited supply of GPUs in many cloud regions, Anyscale recommends reserving GPUs and configuring machine pools to share them across your GPU workloads.

Anyscale manages all compute resources in a machine pool as a warm pool of common resources. This reduces startup time associated with acquiring virtual machines from the cloud provider. Using machine pools allows the global resource scheduler to preempt resources from lower-priority workloads for scheduling higher-priority workloads.

## Configure an Anyscale-managed machine pool[​](#configure "Direct link to Configure an Anyscale-managed machine pool")

You configure Anyscale-managed machine pools using the Anyscale CLI. You must have an Anyscale cloud deployed on AWS or Google Cloud to use machine pools. See [Machine pool configuration file reference](/machine-pools/config-ref.md).

important

All machine pools require that the head node for your cluster uses an on-demand virtual machine in your Anyscale cloud. The driver and Anyscale control plane must communicate with all nodes in your machine pool.

The following machine pool configuration shows an example of configuring a machine pool to manage A100s.

note

Machine pools define resource scheduling rules using `partitions` objects. You can define multiple partitions for a machine type, then define rules for each partition to control what types of workloads can use those instances. Use the `size` field to specify the maximum number of instances allowed in the machine pool partition. Anyscale recommends setting `size` to the quota in your cloud provider account for the given machine type. See [Rule fields](/machine-pools/config-ref.md#rules).

* AWS
* Google Cloud

```
kind: ANYSCALE_MANAGED
machine_types:   
  - machine_type: reserved-a100
    launch_templates:
      - instance_type: p4de.24xlarge
        market_type: ON_DEMAND
        advanced_instance_config:
          CapacityReservationSpecification:
            CapacityReservationTarget:
              CapacityReservationId: cr-xxx
    partitions:
      - name: any
        size: 2
  - machine_type: spot-a100
    launch_templates:
      - instance_type: p4de.24xlarge
        market_type: SPOT
    partitions:
      - name: any
        size: 2
  - machine_type: ondemand-a100
    launch_templates:
      - instance_type: p4de.24xlarge
        market_type: ON_DEMAND
    partitions:
      - name: any
        size: 2
```

```
kind: ANYSCALE_MANAGED
machine_types:   
  - machine_type: reserved-a100
    launch_templates:
      - instance_type: a2-highgpu-8g
        market_type: ON_DEMAND
        advanced_instance_config:
          instanceProperties:
            reservationAffinity:
              consumeReservationType: SPECIFIC_RESERVATION
              key: compute.googleapis.com/reservation-name
              values: [projects/my-project/reservations/shared-a100]
    partitions:
      - name: any
        size: 2
  - machine_type: spot-a100
    launch_templates:
      - instance_type: a2-highgpu-8g
        market_type: SPOT
    partitions:
      - name: any
        size: 2
  - machine_type: ondemand-a100
    launch_templates:
      - instance_type: a2-highgpu-8g
        market_type: ON_DEMAND
    partitions:
      - name: any
        size: 2
```

## Configure compute to use machine pools[​](#configure-compute-to-use-machine-pools "Direct link to Configure compute to use machine pools")

You use machine pools by defining worker nodes in your compute config. The `instance_type` field maps to the `machine_type` name in your machine pool configuration. You add an additional configuration to specify the machine pool by name for each instance type.

The following example YAML configures worker nodes using GPUs configured in a machine pool named `demo-machine-pool` with the following scheduling priority:

* Capacity reservation
* Spot instances
* On-demand

- AWS
- Google Cloud

```
head_node:
  instance_type: m5.2xlarge
worker_nodes:
  - instance_type: reserved-a100
    flags:
      cloud_deployment:
        machine_pool: demo-machine-pool
  - instance_type: spot-a100
    flags:
      cloud_deployment:
        machine_pool: demo-machine-pool
  - instance_type: ondemand-a100
    flags:
      cloud_deployment:
        machine_pool: demo-machine-pool
flags:
  replacement_threshold: 1m
  instance_ranking_strategy:
    - ranker_type: custom_group_order
      ranker_config:
        enable_replacement: true
        group_order:
          - reserved-a100
          - spot-a100
          - ondemand-a100
```

```
head_node:
  instance_type: n2-standard-8
worker_nodes:
  - instance_type: reserved-a100
    flags:
      cloud_deployment:
        machine_pool: demo-machine-pool
  - instance_type: spot-a100
    flags:
      cloud_deployment:
        machine_pool: demo-machine-pool
  - instance_type: ondemand-a100
    flags:
      cloud_deployment:
        machine_pool: demo-machine-pool
flags:
  replacement_threshold: 1m
  instance_ranking_strategy:
    - ranker_type: custom_group_order
      ranker_config:
        enable_replacement: true
        group_order:
          - reserved-a100
          - spot-a100
          - ondemand-a100
```
