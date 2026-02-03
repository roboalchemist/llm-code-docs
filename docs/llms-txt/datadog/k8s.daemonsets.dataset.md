# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/k8s/k8s.daemonsets.dataset.md

---
title: Kubernetes DaemonSets
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Kubernetes DaemonSets
---

# Kubernetes DaemonSets

The Kubernetes DaemonSets table provides information about Kubernetes DaemonSets monitored by Datadog across your clusters. Each row represents a Kubernetes DaemonSet and includes metadata about annotations, labels, pod selectors, minimum ready seconds, revision history limits, scheduling status across nodes (current, desired, available, ready, updated, misscheduled), status conditions, and lifecycle timestamps. This table enables you to monitor DaemonSet rollout status, ensure daemon pods are running on all appropriate nodes, track misscheduled pods (running on nodes where they shouldn't), verify update progress across the cluster, monitor availability and readiness of daemon pods, and troubleshoot node-level services. DaemonSets ensure that all (or specific) nodes run a copy of a pod, commonly used for cluster-wide services like log collectors, monitoring agents, or node-level storage daemons. The desired vs current scheduled counts help identify scheduling issues or node constraints.

```
k8s.daemonsets
```

## Fields

| Title                           | ID                              | Type | Data Type | Description                                                                                                           |
| ------------------------------- | ------------------------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| Annotations                     | annotations                     | core | hstore    | Key-value pairs containing annotations attached to the daemonset, stored as hstore.                                   |
| Cluster Name                    | cluster_name                    | core | string    | The name of the Kubernetes cluster where the daemonset is running.                                                    |
| Creation Timestamp              | creation_timestamp              | core | timestamp | The timestamp when the daemonset was created.                                                                         |
| Deletion Timestamp              | deletion_timestamp              | core | timestamp | The timestamp when the daemonset deletion was requested.                                                              |
| Labels                          | labels                          | core | hstore    | Key-value pairs containing labels attached to the daemonset, stored as hstore.                                        |
| DaemonSet Name                  | name                            | core | string    | The name of the daemonset.                                                                                            |
| Namespace                       | namespace                       | core | string    | The Kubernetes namespace where the daemonset is running.                                                              |
| Spec Min Ready Seconds          | spec_min_ready_seconds          | core | int64     | The minimum number of seconds a pod must be ready before it is considered available.                                  |
| Spec Revision History Limit     | spec_revision_history_limit     | core | int64     | The number of old replica sets to retain for rollback.                                                                |
| Spec Selector                   | spec_selector                   | core | json      | The label selector used to select pods for the daemonset, stored as JSON.                                             |
| Status Conditions               | status_conditions               | core | json      | The conditions of the daemonset status, stored as JSON.                                                               |
| Status Current Number Scheduled | status_current_number_scheduled | core | int64     | The number of nodes that are running at least one daemon pod.                                                         |
| Status Desired Number Scheduled | status_desired_number_scheduled | core | int64     | The number of nodes that should be running the daemon pod.                                                            |
| Status Number Available         | status_number_available         | core | int64     | The number of nodes that have at least one available daemon pod.                                                      |
| Status Number Misscheduled      | status_number_misscheduled      | core | int64     | The number of nodes that are running the daemon pod but should not be.                                                |
| Status Number Ready             | status_number_ready             | core | int64     | The number of nodes that have at least one ready daemon pod.                                                          |
| Status Updated Number Scheduled | status_updated_number_scheduled | core | int64     | The number of nodes that are running updated daemon pods.                                                             |
| Resource Tags                   | tags                            | core | hstore    | This field contains tags represented as key-value pairs, used to categorize and provide metadata about the daemonset. |
| UID                             | uid                             | core | string    | The unique identifier of the daemonset.                                                                               |
