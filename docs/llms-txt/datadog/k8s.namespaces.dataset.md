# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/k8s/k8s.namespaces.dataset.md

---
title: Kubernetes Namespaces
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Kubernetes Namespaces
---

# Kubernetes Namespaces

The Kubernetes Namespaces table provides information about Kubernetes namespaces monitored by Datadog across your clusters. Each row represents a Kubernetes namespace and includes metadata about annotations, labels (which can be applied as tags to all pods in the namespace), finalizers that must complete before deletion, creation and deletion timestamps, and current phase (Active, Terminating). This table enables you to organize and track workload isolation boundaries, monitor namespace lifecycle and deletion status, use namespace labels as tags for all resources within (Agent 7.55.0+), manage resource quotas and access controls at the namespace level, and correlate namespace-level policies with pod and deployment behavior. Namespaces are a key organizational construct in Kubernetes for dividing cluster resources between multiple users, teams, or applications.

```
k8s.namespaces
```

## Fields

| Title              | ID                 | Type | Data Type     | Description                                                                                                           |
| ------------------ | ------------------ | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------- |
| Annotations        | annotations        | core | hstore        | Key-value pairs containing annotations attached to the namespace, stored as hstore.                                   |
| Cluster Name       | cluster_name       | core | string        | The name of the Kubernetes cluster where the namespace exists.                                                        |
| Creation Timestamp | creation_timestamp | core | timestamp     | The timestamp when the namespace was created.                                                                         |
| Deletion Timestamp | deletion_timestamp | core | timestamp     | The timestamp when the namespace deletion was requested.                                                              |
| Labels             | labels             | core | hstore        | Key-value pairs containing labels attached to the namespace, stored as hstore.                                        |
| Namespace Name     | name               | core | string        | The name of the namespace.                                                                                            |
| Namespace          | namespace          | core | string        | The namespace name (same as name field).                                                                              |
| Spec Finalizers    | spec_finalizers    | core | array<string> | List of finalizers that must be completed before the namespace can be deleted.                                        |
| Status Phase       | status_phase       | core | string        | The current phase of the namespace (e.g., Active, Terminating).                                                       |
| Resource Tags      | tags               | core | hstore        | This field contains tags represented as key-value pairs, used to categorize and provide metadata about the namespace. |
| UID                | uid                | core | string        | The unique identifier of the namespace.                                                                               |
