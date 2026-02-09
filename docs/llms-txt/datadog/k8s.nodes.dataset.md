# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/k8s/k8s.nodes.dataset.md

---
title: Kubernetes Nodes
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Kubernetes Nodes
---

# Kubernetes Nodes

The Kubernetes Nodes table provides comprehensive information about Kubernetes nodes (worker machines) monitored by Datadog across your clusters. Each row represents a Kubernetes node and includes metadata about annotations, labels, resource capacity and allocatable resources (CPU, memory, pods), pod CIDR blocks for networking (including dual-stack support), cloud provider ID, taints that affect pod scheduling, node conditions (Ready, DiskPressure, MemoryPressure), cached container images, unschedulable status (cordoned nodes), and current phase. This table enables you to monitor node health and availability, track node resource capacity and allocation, identify resource pressure conditions, analyze pod scheduling constraints via taints and tolerations, correlate nodes with cloud provider instances, monitor node status for capacity planning, and troubleshoot pod scheduling issues. Kube-state-metrics provides detailed metrics on node status and capacity that Datadog collects for comprehensive node monitoring.

```
k8s.nodes
```

## Fields

| Title              | ID                 | Type | Data Type     | Description                                                                                                      |
| ------------------ | ------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------- |
| Annotations        | annotations        | core | hstore        | Key-value pairs containing annotations attached to the node, stored as hstore.                                   |
| Cluster Name       | cluster_name       | core | string        | The name of the Kubernetes cluster where the node is running.                                                    |
| Creation Timestamp | creation_timestamp | core | timestamp     | The timestamp when the node was created.                                                                         |
| Deletion Timestamp | deletion_timestamp | core | timestamp     | The timestamp when the node deletion was requested.                                                              |
| Labels             | labels             | core | hstore        | Key-value pairs containing labels attached to the node, stored as hstore.                                        |
| Node Name          | name               | core | string        | The name of the node.                                                                                            |
| Namespace          | namespace          | core | string        | The Kubernetes namespace (typically empty for nodes as they are cluster-scoped).                                 |
| Spec Pod CIDR      | spec_pod_cidr      | core | string        | The pod CIDR block assigned to the node for pod IP addresses.                                                    |
| Spec Pod CIDRs     | spec_pod_cidrs     | core | array<string> | List of pod CIDR blocks assigned to the node (supports dual-stack networking).                                   |
| Spec Provider ID   | spec_provider_id   | core | string        | The cloud provider specific identifier for the node (e.g., AWS instance ID).                                     |
| Spec Taints        | spec_taints        | core | json          | The taints applied to the node that affect pod scheduling, stored as JSON.                                       |
| Spec Unschedulable | spec_unschedulable | core | bool          | Indicates whether the node is marked as unschedulable (cordoned).                                                |
| Status Allocatable | status_allocatable | core | hstore        | The allocatable resources on the node (CPU, memory, pods), stored as hstore.                                     |
| Status Capacity    | status_capacity    | core | hstore        | The total capacity of resources on the node (CPU, memory, pods), stored as hstore.                               |
| Status Conditions  | status_conditions  | core | json          | The conditions of the node status (e.g., Ready, DiskPressure, MemoryPressure), stored as JSON.                   |
| Status Images      | status_images      | core | json          | List of container images cached on the node, stored as JSON.                                                     |
| Status Phase       | status_phase       | core | string        | The current phase of the node.                                                                                   |
| Resource Tags      | tags               | core | hstore        | This field contains tags represented as key-value pairs, used to categorize and provide metadata about the node. |
| UID                | uid                | core | string        | The unique identifier of the node.                                                                               |
