# Source: https://docs.anyscale.com/machine-pools/config-ref.md

# Machine pool configuration file reference

[View Markdown](/machine-pools/config-ref.md)

# Machine pool configuration file reference

This page provides a reference for the fields and configuration options available in machine pool specification files.

Machine pool spec files use YAML format to define instance types, capacity reservation information, priorities, and quotas. Machine pools use Kubernetes-style selector syntax for setting rules. See [Scheduling rules](/machine-pools/global-resource-scheduler.md#selector).

info

Machine pools and the global resource scheduler are in beta release.

## Top-level fields[​](#top-level-fields "Direct link to Top-level fields")

| Field           | Type                                   | Description                                                                                                                                                                                                                               |
| --------------- | -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `kind`          | String, required                       | The type of machine pool. Valid values:- `ANYSCALE_MANAGED`: Anyscale dynamically creates and terminates cloud instances.<br />- `CUSTOMER_MANAGED`: You register on-premises machines into the pool using the `anyscalemachine` command. |
| `machine_types` | Array, required for `ANYSCALE_MANAGED` | List of machine type configurations. Each entry defines launch templates, partitions, and recycle policies. Omit this field for `CUSTOMER_MANAGED` pools.                                                                                 |

important

Anyscale has deprecated customer-managed machine pools. For legacy documentation, see [Customer-managed on-prem machine pools (legacy)](/archive/customer-managed-machine-pools.md).

## Machine type fields[​](#machine-type-fields "Direct link to Machine type fields")

Each entry in the `machine_types` array supports the following fields:

| Field              | Type                                   | Description                                                                                                                                                                                                                                   |
| ------------------ | -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `machine_type`     | String, required                       | The resource identifier for this machine type, such as `RES-8CPU-32GB` or `1xA100-80G`. Names set for the `machine_type` field appear in the UI dropdown menu for compute configs.                                                            |
| `launch_templates` | Array, required for `ANYSCALE_MANAGED` | List of cloud-specific instance configurations. Each template specifies instance type, market type, and optional advanced configurations. Only relevant for Anyscale-managed machines. See [Launch template fields](#launch-template-fields). |
| `recycle_policy`   | Object, optional                       | Configures instance rotation for Anyscale-managed machine pools on virtual machines (VMs). For machine pools on Kubernetes, pods rotate after each workload. See [Recycle policy fields](#recycle-policy-fields).                             |
| `partitions`       | Array, required                        | List of resource allocation groups. Each partition defines a set of machines with specific scheduling rules and quotas. See [Partition fields](#partition-fields).                                                                            |

## Launch template fields[​](#launch-template-fields "Direct link to Launch template fields")

note

You can define multiple `launch_templates` arrays under a `machine_type`, but all underlying instance types should have the same number and size of CPUs, GPUs, and accelerators. Anyscale assumes that all instance types defined for a `machine_type` are interchangeable.

Each entry in the `launch_templates` array supports the following fields:

| Field                      | Type             | Description                                                                                                                                                                                                                                                                                                                                                                       |
| -------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `instance_type`            | String, required | The cloud provider instance type, such as `m5.2xlarge` for AWS.If using Kubernetes, use user-defined instance types defined in your Helm chart.                                                                                                                                                                                                                                   |
| `market_type`              | String, required | The market type for instance provisioning. Valid values:- `ON_DEMAND`: Use on-demand instances.<br />- `SPOT`: Use spot instances.                                                                                                                                                                                                                                                |
| `advanced_instance_config` | Object, optional | Cloud-specific configuration options passed to the cloud provider when launching instances.- Use this field to configure capacity reservations. See [Capacity reservation config](#capacity-reservation).<br />- See [Compute configurations for AWS](/configuration/compute/aws.md).<br />- See [Compute configuration options for Google Cloud](/configuration/compute/gcp.md). |
| `zones`                    | Array, optional  | List of availability zones to use when launching instances for this launch template, such as `us-west-2a` or `us-west-2b`. If not specified, the scheduler uses the allowed zones from the workload's compute config.                                                                                                                                                             |

### Capacity reservation config[​](#capacity-reservation "Direct link to Capacity reservation config")

Set capacity reservations under the `advanced_instance_config` object alongside other cloud-provider-specific configurations.

* AWS
* Google Cloud

For AWS capacity reservations, use the following structure:

```
CapacityReservationSpecification:
  CapacityReservationTarget:
    CapacityReservationId: <capacity-reservation-id>
```

Replace `<capacity-reservation-id>` with the ID of your AWS capacity reservation.

For Google Cloud capacity reservations, use the following structure:

```
instanceProperties:
  reservationAffinity:
    consumeReservationType: SPECIFIC_RESERVATION
    key: compute.googleapis.com/reservation-name
    values: [<capacity-reservation-name>]
```

Replace `<capacity-reservation-name>` with the name of your Google Cloud capacity reservation, such as `projects/my-project/reservations/shared-a100`.

## Recycle policy fields[​](#recycle-policy-fields "Direct link to Recycle policy fields")

Use the `recycle_policy` object to control how frequently the global resource scheduler rotates instances. The following settings only apply to Anyscale-managed machine pools running on VMs:

| Field               | Type               | Description                                                                                                                                                                            |
| ------------------- | ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `max_workloads`     | Integer, optional  | Rotate instances after this many workloads have run on them. For example, `10` rotates instances after 10 workloads.                                                                   |
| `rotation_interval` | Duration, optional | Rotate instances after this interval has passed since creation. Rotation only happens when workloads complete. Use duration format such as `60m` for 60 minutes or `24h` for 24 hours. |
| `max_idle_duration` | Duration, optional | Terminate idle instances after this duration has passed. Use duration format such as `10m` for 10 minutes.                                                                             |

## Partition fields[​](#partition-fields "Direct link to Partition fields")

Each entry in the `partitions` array supports the following fields:

| Field   | Type              | Description                                                                                                                                                                                                                                      |
| ------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `name`  | String, required  | A unique identifier for the partition, such as `job` or `workspace`. Partition names must be unique within a machine type.                                                                                                                       |
| `size`  | Integer, required | The total number of machines this partition can acquire.Anyscale recommends setting this value to the quota you have for the machine type in your cloud provider account. Anyscale only adds machines to the pool when requested for scheduling. |
| `rules` | Array, required   | List of scheduling rules that apply to this partition. The scheduler evaluates rules in order and uses the first rule that matches. See [Rule fields](#rules).                                                                                   |

### Rule fields[​](#rules "Direct link to Rule fields")

Each entry in the `rules` array supports the following fields:

| Field      | Type              | Description                                                                                                                                                                                                                                                                                                                                                                       |
| ---------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `selector` | String, required  | Kubernetes-style label selector that this rule applies to. Selectors follow the [Kubernetes label selector syntax](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/). For example, `workload-type in (job)` matches workloads with the label `workload-type` set to `job`. See [Scheduling rules](/machine-pools/global-resource-scheduler.md#selector). |
| `priority` | Integer, optional | The priority for workloads matching this rule. Higher values indicate higher priority. If not specified or no rules match a workload, the priority value defaults to `0`. Workloads with a priority value of `0` can't use resources in the partition.                                                                                                                            |
| `quota`    | Integer, optional | The maximum number of machines the scheduler can allocate to workloads matching this rule. Set to `0` to prevent the scheduler from assigning machines in this partition to workloads that match the selector. If not specified, workloads receive unlimited quota.                                                                                                               |

## Example machine pool configuration file[​](#example-machine-pool-configuration-file "Direct link to Example machine pool configuration file")

The following example shows a complete machine pool spec file with capacity reservations:

```
kind: ANYSCALE_MANAGED
machine_types:
  - machine_type: RES-8CPU-32GB
    recycle_policy:
      max_workloads: 10
      rotation_interval: 60m
      max_idle_duration: 10m
    launch_templates:
      - instance_type: "p4de.24xlarge"
        market_type: ON_DEMAND
        advanced_instance_config:
          CapacityReservationSpecification:
            CapacityReservationTarget:
              CapacityReservationId: <your-capacity-reservation-id>
        zones:
          - us-west-2a
          - us-west-2b
    partitions:
      - name: job
        size: 6
        rules:
          - selector: workload-type in (job)
            priority: 20
          - selector: workload-type in (workspace)
            priority: 10
            quota: 3
      - name: workspace
        size: 4
        rules:
          - selector: workload-type in (workspace)
            priority: 20
```
