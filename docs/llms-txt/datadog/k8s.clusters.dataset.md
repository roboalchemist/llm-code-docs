# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/k8s/k8s.clusters.dataset.md

---
title: Kubernetes Clusters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Kubernetes Clusters
---

# Kubernetes Clusters

The Kubernetes Clusters table provides comprehensive information about Kubernetes clusters monitored by Datadog. Each row represents a Kubernetes cluster and includes metadata about API server versions, kubelet versions running across nodes, total resource capacity and allocatable resources (CPU, memory, pods), node counts, and creation timestamps. This table enables you to get a high-level overview of your Kubernetes infrastructure, track cluster resource allocation and utilization, monitor version distribution across control plane and worker nodes, ensure cluster capacity meets demand, and correlate cluster-level metrics with workload performance. Datadog supports monitoring for all major Kubernetes distributions including AWS EKS, Azure AKS, Google GKE, Red Hat OpenShift, Rancher, and Oracle OKE.

```
k8s.clusters
```

## Fields

| Title               | ID                  | Type | Data Type | Description                                                                                                         |
| ------------------- | ------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------- |
| Key                 | _key                | core | string    | The unique identifier for the cluster.                                                                              |
| API Server Versions | api_server_versions | core | hstore    | A map of API server versions running in the cluster, stored as key-value pairs.                                     |
| Cluster ID          | cluster_id          | core | string    | The unique identifier of the Kubernetes cluster.                                                                    |
| Cluster Name        | name                | core | string    | The name of the Kubernetes cluster.                                                                                 |
| CPU Allocatable     | cpu_allocatable     | core | string    | The total allocatable CPU resources across all nodes in the cluster.                                                |
| CPU Capacity        | cpu_capacity        | core | string    | The total CPU capacity across all nodes in the cluster.                                                             |
| Creation Timestamp  | creation_timestamp  | core | timestamp | The timestamp when the cluster was created.                                                                         |
| Kubelet Versions    | kubelet_versions    | core | hstore    | A map of kubelet versions running on nodes in the cluster, stored as key-value pairs.                               |
| Memory Allocatable  | memory_allocatable  | core | string    | The total allocatable memory resources across all nodes in the cluster.                                             |
| Memory Capacity     | memory_capacity     | core | string    | The total memory capacity across all nodes in the cluster.                                                          |
| Node Count          | node_count          | core | int64     | The number of nodes in the cluster.                                                                                 |
| Pod Allocatable     | pod_allocatable     | core | int64     | The total number of allocatable pod slots across all nodes in the cluster.                                          |
| Pod Capacity        | pod_capacity        | core | int64     | The total pod capacity across all nodes in the cluster.                                                             |
| Resource Tags       | tags                | core | hstore    | This field contains tags represented as key-value pairs, used to categorize and provide metadata about the cluster. |
