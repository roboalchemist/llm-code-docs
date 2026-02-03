# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/k8s/k8s.pods.dataset.md

---
title: Kubernetes Pods
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Kubernetes Pods
---

# Kubernetes Pods

The Kubernetes Pods table provides detailed information about Kubernetes pods monitored by Datadog across your clusters. Each row represents a Kubernetes pod and includes metadata about annotations, labels (which can be automatically converted to Datadog tags), namespace, node placement, creation and deletion timestamps, status conditions, container statuses, and current phase (Pending, Running, Succeeded, Failed, Unknown). This table enables you to monitor pod health and lifecycle, track pod scheduling and placement across nodes, use pod annotations for Autodiscovery configuration, correlate pods with their parent deployments or workloads, troubleshoot container failures, and analyze resource usage. The Datadog Agent can automatically assign tags to metrics, traces, and logs emitted by pods based on their labels and annotations. Starting with Agent 7.55.0+, namespace labels can also be used as tags for all pods in that namespace.

```
k8s.pods
```

## Fields

| Title                     | ID                        | Type | Data Type | Description                                                                                                     |
| ------------------------- | ------------------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------- |
| Annotations               | annotations               | core | hstore    | Key-value pairs containing annotations attached to the pod, stored as hstore.                                   |
| Cluster Name              | cluster_name              | core | string    | The name of the Kubernetes cluster where the pod is running.                                                    |
| Creation Timestamp        | creation_timestamp        | core | timestamp | The timestamp when the pod was created.                                                                         |
| Deletion Timestamp        | deletion_timestamp        | core | timestamp | The timestamp when the pod deletion was requested.                                                              |
| Labels                    | labels                    | core | hstore    | Key-value pairs containing labels attached to the pod, stored as hstore.                                        |
| Pod Name                  | name                      | core | string    | The name of the pod.                                                                                            |
| Namespace                 | namespace                 | core | string    | The Kubernetes namespace where the pod is running.                                                              |
| Spec Hostname             | spec_hostname             | core | string    | The hostname specified in the pod specification.                                                                |
| Spec Node Name            | spec_node_name            | core | string    | The name of the node where the pod is scheduled to run.                                                         |
| Status Conditions         | status_conditions         | core | json      | The conditions of the pod status, stored as JSON.                                                               |
| Status Container Statuses | status_container_statuses | core | json      | The status information for containers in the pod, stored as JSON.                                               |
| Status Phase              | status_phase              | core | string    | The current phase of the pod (e.g., Pending, Running, Succeeded, Failed, Unknown).                              |
| Resource Tags             | tags                      | core | hstore    | This field contains tags represented as key-value pairs, used to categorize and provide metadata about the pod. |
| UID                       | uid                       | core | string    | The unique identifier of the pod.                                                                               |
