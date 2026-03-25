# Source: https://docs.anyscale.com/monitoring/workload-debugging.md

# Workload dashboards

[View Markdown](/monitoring/workload-debugging.md)

# Workload dashboards

note

This feature is in a beta release and is in active development. Reach out with any feedback or suggestions.

Workload dashboards are workload-specific dashboards that aid with debugging Ray workloads. They are exclusive to Anyscale. Access them by clicking the **Ray Workloads** tab in the Jobs or Workspaces page.

The **Ray Workloads** tab has multiple sub-tabs, each of which is dedicated to a specific type of workload. To see more information about these dashboards, view the other docs in this section.

## Dashboards[​](#dashboards "Direct link to Dashboards")

* [Data Dashboard](/monitoring/workload-debugging/data-dashboard.md): For debugging Ray Data workloads.
* [Train Dashboard](/monitoring/workload-debugging/train-dashboard.md): For debugging Ray Train workloads.

## Ray sessions[​](#ray-sessions "Direct link to Ray sessions")

Anyscale organizes workload dashboards by the Ray **session** and persists dashboards after cluster termination.

A Ray session is the lifetime of a Ray cluster. Each time a cluster starts, Ray creates a new session using an ID based on the current timestamp.

Use the **Past session** dropdown to select a Ray session. Anyscale supports viewing data from the 10 most recent sessions.

![](/img/workload-debugging/ray_sessions.png)

## Stale data[​](#stale-data "Direct link to Stale data")

If a Ray cluster terminates unexpectedly, the workloads dashboard may show stale data. This behavior occurs because the dashboard persists events received by the Ray cluster and the cluster may not emit a termination event if it terminates unexpectedly. In this case, the dashboard shows the last known state of the cluster.
