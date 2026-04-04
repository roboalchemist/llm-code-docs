# Source: https://docs.anyscale.com/monitoring/cluster-dashboard.md

# Anyscale cluster dashboard

[View Markdown](/monitoring/cluster-dashboard.md)

# Anyscale cluster dashboard

This page provides details on using the Anyscale cluster dashboard for monitoring your Ray cluster nodes in your Anyscale jobs and workspaces.

important

This feature is in beta release and requires Ray 2.50.0 or later.

The Anyscale cluster dashboard persists node details beyond the lifetime of the cluster for offline debugging. It provides a scoped view of metrics and Ray entities per node, which allows you to observe how your Ray workload uses cluster resources. Other Anyscale dashboards link to the cluster dashboard to provide details about a specific node.

## Access the cluster dashboard[​](#access-the-cluster-dashboard "Direct link to Access the cluster dashboard")

You can view the cluster dashboard in the Anyscale console for any job or workspace.

Complete the following steps to access the Anyscale cluster dashboard:

1. Log in to the Anyscale console.
2. Click **Workspaces** or **Jobs**.
3. Click the name of a workspace or job.
4. Click **Ray Workloads**.
5. Click **Cluster**. The cluster dashboard appears.

note

By default, the cluster dashboard displays the current running session or most recently terminated session. You can view up to the last ten Ray sessions using the dropdown in the top right corner.

## Cluster overview[​](#cluster-overview "Direct link to Cluster overview")

The **Overview** tab contains a list of all nodes in a cluster, including dead nodes. You can expand each node row using the expand button on the left to view the live workers running on that node.

The following table describes the fields in the node overview:

| Field               | Description                                                                                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Node                | The name of the node in the format `Instance type (truncated_node_id)`.                                                                                      |
| State               | The state of the node:- `ALIVE`: Node is alive.<br />- `DRAINING`: Node is alive but starting shutdown processing to terminate.<br />- `DEAD`: Node is dead. |
| IP                  | The IP address of the node.                                                                                                                                  |
| ID                  | The ID of the node.                                                                                                                                          |
| CPU                 | The live CPU utilization of the node.                                                                                                                        |
| Memory              | The live memory utilization of the node.                                                                                                                     |
| GPU                 | The live GPU utilization of the node.                                                                                                                        |
| GRAM                | The live GPU memory utilization of the node.                                                                                                                 |
| Object store memory | The live object store memory utilization of the node.                                                                                                        |
| Disk                | The live disk usage of the node.                                                                                                                             |
| Network sent        | The live network bytes sent per second for the node.                                                                                                         |
| Network received    | The live network bytes received per second for the node.                                                                                                     |
| Duration            | The total duration of the node.In the case of an ungraceful shutdown, Anyscale may not have captured the end time of the node and this field may be missing. |
| Start time          | The start time of the node.                                                                                                                                  |
| End time            | The end time of the node.In the case of an ungraceful shutdown, Anyscale may not have captured the end time of the node and this field may be missing.       |
| Resources           | The Ray resources configured for the node.                                                                                                                   |
| Labels              | The labels configured for the node.                                                                                                                          |

## Worker details[​](#worker-details "Direct link to Worker details")

Click the chevron next to a node in the overview to see live workers on the node. The following details are available for workers on live nodes:

| Field   | Description                                                                        |
| ------- | ---------------------------------------------------------------------------------- |
| Workers | The command line or process the Ray worker is running.                             |
| State   | The state of the worker:- `ALIVE`: Worker is alive.<br />- `DEAD`: Worker is dead. |
| PID     | The process ID of the Ray worker process.                                          |
| ID      | The ID of the worker.                                                              |
| CPU     | The live CPU utilization of the worker.                                            |
| Memory  | The live memory utilization of the worker.                                         |
| GPU     | The live GPU utilization of the worker.                                            |
| GRAM    | The live GPU memory utilization of the worker.                                     |

## Node detail[​](#node-detail "Direct link to Node detail")

Click the node name to see detailed information for a single node in the cluster.

The **Overview** tab repeats the details from the main cluster dashboard list.

The **Metrics** tab provides a filtered view of the Ray Core metrics dashboard for the node. See [New metrics dashboard experience in Ray 2.50.0 or later](/monitoring/metrics.md#new-metrics).

The **Workers** tab contains the list of live workers running on the node. This tab is only available for live nodes.

The **Tasks** tab contains a list of all tasks run on the node.

important

The tasks tab provides a filtered view of the tasks dashboard. See [Anyscale task dashboard](/monitoring/task-dashboard.md).

Task dashboards require the system cluster, which has an associated cost. See [System cluster](/admin/cloud/system-cluster.md).

All limitations and requirements for the task dashboard apply to the task tab. See [Requirements and limitations](/monitoring/task-dashboard.md#limitations).
