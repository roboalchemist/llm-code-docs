# Source: https://docs.anyscale.com/admin/cloud/system-cluster.md

# System cluster

[View Markdown](/admin/cloud/system-cluster.md)

# System cluster

This page provides details on the system cluster that powers Anyscale observability dashboards, including the [task dashboard](/monitoring/task-dashboard.md) and [actor dashboard](/monitoring/actor-dashboard.md).

## What is the system cluster?[​](#what-is-the-system-cluster "Direct link to What is the system cluster?")

When you access a task or actor dashboard, Anyscale deploys a single node system cluster in your Anyscale cloud. A single system cluster monitors all workloads in all projects for an Anyscale cloud, but each cloud deployment requires a separate system cluster.

Anyscale uses compute and storage in your cloud provider account for the system cluster. The system cluster serves dashboard data to the Anyscale console without passing task or actor details through the Anyscale control plane.

## Requirements and limitations[​](#limitations "Direct link to Requirements and limitations")

The following requirements and limitations exist:

* The system cluster is available on Anyscale clouds deployed to AWS or Google Cloud that use virtual machines.
  <!-- -->
  * The system cluster isn't available for any clouds deployed using Kubernetes, including AKS, EKS, and GKE.
* To terminate the system cluster with the Anyscale CLI or SDK, you must use version 0.26.32 or later.
* The system cluster only captures metrics when enabled. Jobs or workspaces launched before you enable the system cluster don't report metrics, even if you enable the system cluster while they're running.

### Ray version requirements[​](#ray-versions "Direct link to Ray version requirements")

Enabling the system cluster enables both the task and actor dashboards for a cloud. However, Ray version requirements still apply:

| Dashboard       | Ray version         |
| --------------- | ------------------- |
| Task dashboard  | Ray 2.49.0 or later |
| Actor dashboard | Ray 2.50.0 or later |

Metrics only display for workloads running supported Ray versions.

## Costs[​](#costs "Direct link to Costs")

See the [Anyscale pricing page](https://www.anyscale.com/pricing-detail) for details on costs associated with the system cluster.

The following table indicates the instance type for each supported cloud deployment:

| Cloud deployment | Instance type   |
| ---------------- | --------------- |
| AWS              | `m5.2xlarge`    |
| Google Cloud     | `n2-standard-8` |

Anyscale stores the metrics the system cluster collects in the default cloud object storage location configured for your Anyscale cloud deployment. Anyscale doesn't delete data when the system cluster terminates.

## Enable the system cluster[​](#enable "Direct link to Enable the system cluster")

An organization admin must enable the system cluster using the Anyscale CLI. Enabling the system cluster for an Anyscale cloud enables both the task and actor dashboards for that cloud.

To enable the system cluster, run the following command:

```
anyscale cloud config update --cloud-id <cloud-id> --enable-system-cluster
```

To disable the system cluster and turn off the dashboards for a cloud, run the following command:

```
anyscale cloud config update --cloud-id <cloud-id> --disable-system-cluster
```

## Monitor the system cluster[​](#monitor "Direct link to Monitor the system cluster")

You can monitor the system cluster using the Anyscale cloud dashboard. See [Dashboard](/administration/resource-management/telescope-dashboard.md).

## Automatic termination[​](#auto-terminate "Direct link to Automatic termination")

By default, the system cluster terminates after 8 hours if no users are actively viewing a task or actor dashboard in your cloud deployment.

Anyscale automatically restarts the system cluster when a user views a task or actor dashboard.

## Terminate the system cluster[​](#terminate "Direct link to Terminate the system cluster")

Cloud owners can manually terminate the system cluster for a cloud.

Terminating the system cluster shuts down the task and actor dashboards for all clusters in this cloud. This action doesn't delete data and Anyscale continues to export task and actor data for future dashboard usage.

* Anyscale console
* CLI
* SDK

To terminate the system cluster in the Anyscale console, complete the following steps:

1. [Log in to the Anyscale console](https://console.anyscale.com/).
2. Click the user icon.
3. Click **Clouds**.
4. Click the name of your cloud.
5. Click **Settings**.
6. Under **Platform services > System cluster**, click **Terminate cluster**. A confirmation dialog displays.
7. Click **Terminate** to shut down the system cluster.

The following CLI example uses the `wait` option to block return until the system cluster successfully shuts down. If you don't specify the `wait` option, the command returns after initializing termination. Requires CLI version 0.26.32 or later.

```
anyscale cloud terminate-system-cluster --cloud-id <cloud-id> --wait
```

See [`anyscale cloud terminate-system-cluster`](/reference/cloud.md#anyscale-cloud-terminate-system-cluster).

The following SDK example uses the `wait` option to block return until the system cluster successfully shuts down. If you don't specify the `wait` option, the command returns after initializing termination. Requires CLI version 0.26.32 or later.

```
import anyscale
anyscale.cloud.terminate_system_cluster("<cloud-id>", wait=True)
```

See [`anyscale.cloud.terminate_system_cluster`](/reference/cloud.md#anyscalecloudterminate_system_cluster).
