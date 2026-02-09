# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.gkeonprem_bare_metal_node_pool.dataset.md

---
title: Bare Metal Node Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bare Metal Node Pool
---

# Bare Metal Node Pool

A Bare Metal Node Pool in Google Cloud is a collection of physical, non-virtualized servers used to run workloads that require direct access to hardware. It provides high performance, predictable latency, and full control over the underlying infrastructure. This resource is typically used in Google Kubernetes Engine (GKE) on Bare Metal environments to manage and scale clusters efficiently while maintaining the benefits of Kubernetes orchestration.

```
gcp.gkeonprem_bare_metal_node_pool
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| annotations          | core | hstore        | Annotations on the bare metal node pool. This field has the same restrictions as Kubernetes annotations. The total size of all keys and values combined is limited to 256k. Key can have 2 segments: prefix (optional) and name (required), separated by a slash (/). Prefix must be a DNS subdomain. Name must be 63 characters or less, begin and end with alphanumerics, with dashes (-), underscores (_), dots (.), and alphanumerics between. |
| create_time          | core | timestamp     | Output only. The time at which this bare metal node pool was created.                                                                                                                                                                                                                                                                                                                                                                              |
| datadog_display_name | core | string        |
| delete_time          | core | timestamp     | Output only. The time at which this bare metal node pool was deleted. If the resource is not deleted, this must be empty                                                                                                                                                                                                                                                                                                                           |
| etag                 | core | string        | This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding. Allows clients to perform consistent read-modify-writes through optimistic concurrency control.                                                                                                                                                          |
| gcp_display_name     | core | string        | The display name for the bare metal node pool.                                                                                                                                                                                                                                                                                                                                                                                                     |
| gcp_status           | core | json          | Output only. ResourceStatus representing the detailed node pool status.                                                                                                                                                                                                                                                                                                                                                                            |
| labels               | core | array<string> |
| name                 | core | string        | Immutable. The bare metal node pool resource name.                                                                                                                                                                                                                                                                                                                                                                                                 |
| node_pool_config     | core | json          | Required. Node pool configuration.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| reconciling          | core | bool          | Output only. If set, there are currently changes in flight to the bare metal node pool.                                                                                                                                                                                                                                                                                                                                                            |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. The current state of the bare metal node pool.                                                                                                                                                                                                                                                                                                                                                                                        |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. The unique identifier of the bare metal node pool.                                                                                                                                                                                                                                                                                                                                                                                    |
| update_time          | core | timestamp     | Output only. The time at which this bare metal node pool was last updated.                                                                                                                                                                                                                                                                                                                                                                         |
| upgrade_policy       | core | json          | The worker node pool upgrade policy.                                                                                                                                                                                                                                                                                                                                                                                                               |
| zone_id              | core | string        |
