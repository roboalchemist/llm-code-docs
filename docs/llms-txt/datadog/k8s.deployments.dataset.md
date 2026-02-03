# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/k8s/k8s.deployments.dataset.md

---
title: Kubernetes Deployments
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Kubernetes Deployments
---

# Kubernetes Deployments

The Kubernetes Deployments table provides information about Kubernetes deployments monitored by Datadog across your clusters. Each row represents a Kubernetes deployment and includes metadata about annotations, labels, desired replica counts (spec_replicas), actual replica status (replicas, available, ready, unavailable, updated), deployment strategy (RollingUpdate, Recreate), status conditions, and lifecycle timestamps. This table enables you to monitor deployment health and rollout status, track replica availability and readiness, compare desired vs actual replica counts to detect issues, alert on unavailable replicas, analyze deployment strategies and configurations, and correlate deployments with pod and container performance. Datadog collects kube_deployment_spec_replicas (desired) and kube_deployment_status_replicas (actual) metrics - these numbers should match unless you're in the midst of a deployment or experiencing issues. You can filter and view resources by kube_deployment tag in Datadog.

```
k8s.deployments
```

## Fields

| Title                       | ID                          | Type | Data Type | Description                                                                                                            |
| --------------------------- | --------------------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------- |
| Annotations                 | annotations                 | core | hstore    | Key-value pairs containing annotations attached to the deployment, stored as hstore.                                   |
| Cluster Name                | cluster_name                | core | string    | The name of the Kubernetes cluster where the deployment is running.                                                    |
| Creation Timestamp          | creation_timestamp          | core | timestamp | The timestamp when the deployment was created.                                                                         |
| Deletion Timestamp          | deletion_timestamp          | core | timestamp | The timestamp when the deployment deletion was requested.                                                              |
| Labels                      | labels                      | core | hstore    | Key-value pairs containing labels attached to the deployment, stored as hstore.                                        |
| Deployment Name             | name                        | core | string    | The name of the deployment.                                                                                            |
| Namespace                   | namespace                   | core | string    | The Kubernetes namespace where the deployment is running.                                                              |
| Spec Replicas               | spec_replicas               | core | int64     | The desired number of replicas for the deployment.                                                                     |
| Spec Strategy               | spec_strategy               | core | string    | The deployment strategy used (e.g., RollingUpdate, Recreate).                                                          |
| Status Available Replicas   | status_available_replicas   | core | int64     | The number of available replicas in the deployment.                                                                    |
| Status Conditions           | status_conditions           | core | json      | The conditions of the deployment status, stored as JSON.                                                               |
| Status Ready Replicas       | status_ready_replicas       | core | int64     | The number of ready replicas in the deployment.                                                                        |
| Status Replicas             | status_replicas             | core | int64     | The total number of replicas in the deployment.                                                                        |
| Status Unavailable Replicas | status_unavailable_replicas | core | int64     | The number of unavailable replicas in the deployment.                                                                  |
| Status Updated Replicas     | status_updated_replicas     | core | int64     | The number of updated replicas in the deployment.                                                                      |
| Resource Tags               | tags                        | core | hstore    | This field contains tags represented as key-value pairs, used to categorize and provide metadata about the deployment. |
| UID                         | uid                         | core | string    | The unique identifier of the deployment.                                                                               |
