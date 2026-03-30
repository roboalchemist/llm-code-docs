# Source: https://docs.anyscale.com/monitoring/task-dashboard.md

# Anyscale task dashboard

[View Markdown](/monitoring/task-dashboard.md)

# Anyscale task dashboard

This page provides details on using the Anyscale task dashboard for monitoring Ray tasks in your Anyscale jobs and workspaces.

important

This feature is in beta release. Using this feature has [cost](/admin/cloud/system-cluster.md#costs) implications.

The Anyscale task dashboard persists task details beyond the lifetime of the cluster for easy offline debugging. Anyscale uses compute and storage in your cloud provider account for the task dashboard, serving the dashboard to the Anyscale console without passing task details through the Anyscale control plane.

Anyscale has tested support for the task dashboard with millions of tasks. If you encounter limitations due to task count, contact [Anyscale support](mailto:support@anyscale.com).

## Use the Anyscale task dashboard[​](#use-the-anyscale-task-dashboard "Direct link to Use the Anyscale task dashboard")

The Anyscale task dashboard updates in near real-time and provides filtering and aggregate counts for tasks based on the following states:

| State                | Description                                             |
| -------------------- | ------------------------------------------------------- |
| Finished             | Finished tasks.                                         |
| Failed               | Failed tasks.                                           |
| Running              | Tasks actively running on your cluster.                 |
| Pending dependencies | Tasks waiting for dependent tasks to complete.          |
| Pending scheduling   | Submitted tasks waiting for scheduling on your cluster. |

The following table describes the information in each component of the task dashboard.

| Dashboard component | Description                                                                  |
| ------------------- | ---------------------------------------------------------------------------- |
| Task summary        | A count of all tasks and tasks aggregated by state.                          |
| Tasks by function   | A view of all tasks by function name.                                        |
| Tasks by errors     | A view of all errors raised by tasks.                                        |
| Tasks by jobs       | A view of tasks by job ID.                                                   |
| Task table          | A detailed view of all tasks that includes options for filtering and search. |

The **Tasks by function**, **Tasks by errors**, and **Tasks by jobs** components include summary metrics on total tasks and max, min, and average time. For all time metrics, the reported value measures the time elapsed between when the Ray application requests scheduling for a task and when the task completes.

The **Task table** displays details for each task using the following fields. Use the search and filter to limit displayed tasks.

| Field              | Description                                                                                                                                                                                              |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                 | The unique ID for each task.                                                                                                                                                                             |
| Function name      | The name of the function that triggered the task.                                                                                                                                                        |
| State              | The state of the task.This is the main field used for filtering the task table.                                                                                                                          |
| State details      | Additional details about the state of the task.For most task states, you can click the **More details** link under **State details** in the **Task table** to show error messages or cluster event logs. |
| Duration           | The amount of time elapsed between when the Ray application requests scheduling for a task and when the task completes.                                                                                  |
| Start time         | The date and time the Ray application enqueued the task for scheduling.                                                                                                                                  |
| End time           | The date and time the task finished.                                                                                                                                                                     |
| Required resources | The type and amount of resources required for the task.                                                                                                                                                  |
| Node ID            | The unique ID for the node where the task ran.                                                                                                                                                           |
| Worker PID         | The ID of the Ray worker process.                                                                                                                                                                        |
| Worker ID          | The ID of the worker that ran the task.                                                                                                                                                                  |
| Attempt no.        | Indicates the count of retry attempts.`0` for tasks that succeed on the initial attempt.                                                                                                                 |
| Session            | The session in which the task ran.                                                                                                                                                                       |
| Job ID             | The ID of the job where the task ran.Workspaces assign job IDs when you run code that triggers compute on your Ray cluster.                                                                              |
| Type               | Indicates whether the task ran on an actor.                                                                                                                                                              |

## Requirements and limitations[​](#limitations "Direct link to Requirements and limitations")

The task dashboard requires the [system cluster](/admin/cloud/system-cluster.md) to be enabled for your Anyscale cloud. An organization admin must enable the system cluster. See [Enable the system cluster](/admin/cloud/system-cluster.md#enable).

The following requirements and limitations exist:

* The task dashboard is available on Anyscale clouds deployed to AWS or Google Cloud that use virtual machines.
  <!-- -->
  * The task dashboard isn't available for any clouds deployed using Kubernetes, including AKS, EKS, and GKE.
* The task dashboard reports metrics for jobs and workspaces that use Ray 2.49.0 or later.
* The task dashboard only captures metrics when the system cluster is enabled. Jobs or workspaces launched before you enable the system cluster don't report metrics, even if you enable the system cluster while they're running.

note

Anyscale recommends using Ray 2.51.0 or later when enabling the task dashboard. In earlier Ray versions, overhead from reporting task metrics might cause performance degradation.

## Access the task dashboard[​](#access-the-task-dashboard "Direct link to Access the task dashboard")

You can view the task dashboard in the Anyscale console for any job or workspace.

Complete the following steps to access the Anyscale task dashboard:

1. Log in to the Anyscale console.
2. Click **Workspaces** or **Jobs**.
3. Click the name of a workspace or job.
4. Click **Ray Workloads**.
5. Click **Tasks**. The task dashboard appears.

important

Anyscale deploys a system cluster to power the task dashboard. If your cloud doesn't have an active system cluster running, a screen with the message **Observability service is launching** appears as the system cluster starts.
