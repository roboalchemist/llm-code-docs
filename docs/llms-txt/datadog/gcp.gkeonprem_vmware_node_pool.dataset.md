# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkeonprem_vmware_node_pool.dataset.md

---
title: VMware Node Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VMware Node Pool
---

# VMware Node Pool

A VMware Node Pool in Google Cloud is a group of nodes used to run VMware workloads within Google Cloud VMware Engine. It provides a managed cluster of ESXi hosts that deliver compute, storage, and networking resources for virtual machines. The node pool allows scaling, maintenance, and lifecycle management of VMware environments while integrating with Google Cloud services.

```
gcp.gkeonprem_vmware_node_pool
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                               | Description |
| --------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| annotations           | core | hstore        | Annotations on the node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| config                | core | json          | Required. The node configuration of the node pool.                                                                                                                                                                                                                                                                                                                                                                                      |
| create_time           | core | timestamp     | Output only. The time at which this node pool was created.                                                                                                                                                                                                                                                                                                                                                                              |
| datadog_display_name  | core | string        |
| delete_time           | core | timestamp     | Output only. The time at which this node pool was deleted. If the resource is not deleted, this must be empty                                                                                                                                                                                                                                                                                                                           |
| etag                  | core | string        | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.                                                                                                                                               |
| gcp_display_name      | core | string        | The display name for the node pool.                                                                                                                                                                                                                                                                                                                                                                                                     |
| gcp_status            | core | json          | Output only. ResourceStatus representing the detailed VMware node pool state.                                                                                                                                                                                                                                                                                                                                                           |
| labels                | core | array<string> |
| name                  | core | string        | Immutable. The resource name of this node pool.                                                                                                                                                                                                                                                                                                                                                                                         |
| node_pool_autoscaling | core | json          | Node pool autoscaling config for the node pool.                                                                                                                                                                                                                                                                                                                                                                                         |
| on_prem_version       | core | string        | Anthos version for the node pool. Defaults to the user cluster version.                                                                                                                                                                                                                                                                                                                                                                 |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| reconciling           | core | bool          | Output only. If set, there are currently changes in flight to the node pool.                                                                                                                                                                                                                                                                                                                                                            |
| region_id             | core | string        |
| resource_name         | core | string        |
| state                 | core | string        | Output only. The current state of the node pool.                                                                                                                                                                                                                                                                                                                                                                                        |
| tags                  | core | hstore_csv    |
| uid                   | core | string        | Output only. The unique identifier of the node pool.                                                                                                                                                                                                                                                                                                                                                                                    |
| update_time           | core | timestamp     | Output only. The time at which this node pool was last updated.                                                                                                                                                                                                                                                                                                                                                                         |
| zone_id               | core | string        |
