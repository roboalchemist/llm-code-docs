# Source: https://docs.anyscale.com/machine-pools/console.md

# Monitor and observe machine pools in the Anyscale console

[View Markdown](/machine-pools/console.md)

# Monitor and observe machine pools in the Anyscale console

The Anyscale console provides a UI for monitoring and observing machine pools in your Anyscale organization.

This page provides an overview of the fields and metrics available in the Anyscale console for machine pools.

You create and configure machine pools using the Anyscale CLI. See [Machine Pool API Reference](/reference/machine-pool.md).

You manage machine pools at the Anyscale organization level, but attach them to Anyscale clouds.

info

Machine pools are in beta release.

## View details for a machine pool[​](#view-details "Direct link to View details for a machine pool")

To view the details for a machine pool, complete the following steps:

1. Log in to the [Anyscale console](https://console.anyscale.com/).
2. Click **Advanced > Machine pools**.
3. Click the name of a machine pool.

The overview for the machine pool displays.

## Machine pool utilization[​](#utilization "Direct link to Machine pool utilization")

The **Total utilization** dashboard shows the overall utilization of machines in your machine pool as a percentage.

See the utilization for each partition in your machine pool under **Partition utilization**.

## Running workloads[​](#running "Direct link to Running workloads")

Each workload assigned to a machine in your machine pool displays under **Running workloads** with the following fields:

| Field           | Description                                                      |
| --------------- | ---------------------------------------------------------------- |
| Workload        | The name of the workspace, job, or service.                      |
| Status          | The current status for the workload in the queue.                |
| Partitions      | The partitions where the workload is running.                    |
| Total machines  | The number of machines in use from each partition.               |
| Priority        | The priority ranking for the workload in each partition.         |
| Cloud / Project | The cloud and project containing the workspace, job, or service. |
| Created at      | The creation timestamp for the workload.                         |
| Created by      | The user or service account that created the workload.           |

## Queued requests[​](#queued "Direct link to Queued requests")

Use the details under **Queued requests** to view workloads in the queue waiting machine pool resources.

The following table describes the fields present for monitoring queued workloads:

| Field                 | Description                                                                       |
| --------------------- | --------------------------------------------------------------------------------- |
| Workload              | The name of the workspace, job, or service.                                       |
| Status                | The current status for the workload in the queue.                                 |
| Partitions & priority | The partition and priority for the workload based on machine pool configurations. |
| Requested machines    | The number of machines required to deploy worker nodes.                           |
| Cloud / Project       | The cloud and project containing the workspace, job, or service.                  |
| Created at            | The creation timestamp for the workload.                                          |
| Created by            | The user or service account that created the workload.                            |

## Machines[​](#machines "Direct link to Machines")

Click the **Machines** tab to view the following information for all machines in your machine pool:

| Field                    | Description                                                                             |
| ------------------------ | --------------------------------------------------------------------------------------- |
| Machine type             | The name of the machine type specified in the machine pool configuration.               |
| Machine state            | The state of the machine, either `Available`, `Allocated`, `Migrating`, or `Restoring`. |
| Partition                | The partition of the machine pool containing the machine.                               |
| Cloud Instance ID        | The unique identifier for the cloud resource in the cloud provider account.             |
| Workload details         | The name of the workspace, job, or service running on the machine.                      |
| Workload Cloud / Project | The cloud and project containing the workload running on the machine.                   |

## Configuration[​](#configuration "Direct link to Configuration")

Click the **Configuration** tab to view the configuration YAML for the machine pool.

You can't modify a machine pool configuration with the UI, but you can copy and modify the provided configuration YAML and use the machine pool API to update your machine pool. See [Machine Pool API Reference](/reference/machine-pool.md).
