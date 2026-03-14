# Source: https://docs.anyscale.com/monitoring/actor-dashboard.md

# Anyscale actor dashboard

[View Markdown](/monitoring/actor-dashboard.md)

# Anyscale actor dashboard

This page provides details on using the Anyscale actor dashboard for monitoring Ray actors in your Anyscale jobs and workspaces.

important

This feature is in beta release. Using this feature has [cost](/admin/cloud/system-cluster.md#costs) implications.

The Anyscale actor dashboard persists actor details beyond the lifetime of the cluster for easy offline debugging. Anyscale uses compute and storage in your cloud provider account for the actor dashboard, serving the dashboard to the Anyscale console without passing actor details through the Anyscale control plane.

## Use the Anyscale actor dashboard[​](#use-the-anyscale-actor-dashboard "Direct link to Use the Anyscale actor dashboard")

The Anyscale actor dashboard updates in near real-time and provides filtering and aggregate counts for actors based on the following states:

| State                | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| Alive                | Actors that are currently running.                          |
| Dead                 | Actors that have died and won't be restarted.               |
| Restarting           | Actors that have died and that are now restarting.          |
| Pending dependencies | Actors waiting for dependent actors or resources.           |
| Pending creation     | Actors waiting for creation and scheduling on your cluster. |

The following table describes the information in each component of the actor dashboard.

| Dashboard component   | Description                                                                   |
| --------------------- | ----------------------------------------------------------------------------- |
| Actor summary         | A count of all actors and actors aggregated by state.                         |
| Actors by name        | A view of all actors grouped by actor name or class name.                     |
| Actors by exit detail | A view of all actor death reasons and error messages.                         |
| Actors by jobs        | A view of actors grouped by job ID.                                           |
| Actor table           | A detailed view of all actors that includes options for filtering and search. |

The **Actors by name**, **Actors by exit detail**, and **Actors by jobs** components include summary metrics on total actors and counts for each state. Click any count to filter the actor table to that specific group and state.

The **Actor table** displays details for each actor using the following fields. Use the search and filter to limit displayed actors.

| Field               | Description                                                                                                                                                               |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ID                  | The unique ID for each actor. Click to view the actor detail page.                                                                                                        |
| Name                | The name of the actor. This is the class name unless a custom name was set when creating the actor.                                                                       |
| State               | The state of the actor.This is the main field used for filtering the actor table.                                                                                         |
| CPU                 | Live CPU utilization percentage for the actor. Only available for alive actors in the current session.                                                                    |
| Memory              | Live memory utilization for the actor, showing used memory out of total available. Only available for alive actors in the current session.                                |
| GPU                 | Live GPU utilization for the actor. Only available for alive actors in the current session.                                                                               |
| GRAM                | Live GPU memory utilization for the actor. Only available for alive actors in the current session.                                                                        |
| Actions             | Profiling options for the actor, including CPU flame graph, CPU stack trace, GPU profiling, and memory profiling. Only available for alive actors in the current session. |
| Timestamp           | The date and time of the last state transition for the actor.                                                                                                             |
| Death reason        | The error message or cause of death for dead actors.                                                                                                                      |
| Required resources  | The type and amount of resources required for the actor.                                                                                                                  |
| Runtime environment | The runtime environment configuration for the actor.                                                                                                                      |
| Node ID             | The unique ID for the node where the actor runs or ran.                                                                                                                   |
| Worker ID           | The ID of the Ray worker process running the actor.                                                                                                                       |
| Placement group ID  | The ID of the placement group, if the actor is part of one.                                                                                                               |
| Label selector      | The label selector configuration for node scheduling.                                                                                                                     |
| Session             | The Ray session in which the actor ran.                                                                                                                                   |
| Job ID              | The ID of the job that created the actor.                                                                                                                                 |

### Actor detail page[​](#actor-detail-page "Direct link to Actor detail page")

Click any actor ID in the actor table to view the actor detail page. The actor detail page provides additional information about a specific actor:

| Section        | Description                                                                                                                                                                                                  |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Actor metadata | Displays detailed metadata including ID, Job ID, function and class name, required resources, Worker ID, Node ID, Node IP, runtime environment, placement group ID, label selector, session, and start time. |
| Actor events   | Displays the lifecycle events with the timestamp of the state transition for the actor.                                                                                                                      |
| Actor logs     | Displays logs for the actor. Requires the node containing the actor is running.                                                                                                                              |
| Actor tasks    | For actors that have run tasks, displays a filtered view of the tasks dashboard. See [Anyscale task dashboard](/monitoring/task-dashboard.md).                                                               |

## Requirements and limitations[​](#limitations "Direct link to Requirements and limitations")

The actor dashboard requires the [system cluster](/admin/cloud/system-cluster.md) to be enabled for your Anyscale cloud. An organization admin must enable the system cluster. See [Enable the system cluster](/admin/cloud/system-cluster.md#enable).

The following requirements and limitations exist:

* The actor dashboard is available on Anyscale clouds deployed to AWS or Google Cloud that use virtual machines.
  <!-- -->
  * The actor dashboard isn't available for any clouds deployed using Kubernetes, including AKS, EKS, and GKE.

* The actor dashboard reports metrics for jobs and workspaces that use Ray 2.50.0 or later.

* The actor dashboard only captures metrics when the system cluster is enabled. Jobs or workspaces launched before you enable the system cluster don't report metrics, even if you enable the system cluster while they're running.

* Metrics displayed depend on the state of the actor and nodes:

  <!-- -->

  * Only live actors in the current session support profiling actions and display live metrics such as CPU, Memory, GPU, and GRAM.
  * You can view logs for all actors scheduled on running nodes.
  * Actors from past sessions display historical state information only.

## Access the actor dashboard[​](#access-the-actor-dashboard "Direct link to Access the actor dashboard")

You can view the actor dashboard in the Anyscale console for any job or workspace.

Complete the following steps to access the Anyscale actor dashboard:

1. Log in to the Anyscale console.
2. Click **Workspaces** or **Jobs**.
3. Click the name of a workspace or job.
4. Click **Ray Workloads**.
5. Click **Actors**. The actor dashboard appears.

important

Anyscale deploys a system cluster to power the actor dashboard. If your cloud doesn't have an active system cluster running, a screen with the message **System workload cluster is launching. This may take a minute** appears as the system cluster starts.
