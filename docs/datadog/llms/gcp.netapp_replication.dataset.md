# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.netapp_replication.dataset.md

---
title: NetApp Volumes Replication
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > NetApp Volumes Replication
---

# NetApp Volumes Replication

NetApp Volumes Replication in Google Cloud enables data replication between NetApp volumes for disaster recovery, backup, and high availability. It allows asynchronous replication of data across regions or zones, ensuring business continuity and data protection. This service helps maintain consistent copies of critical data with minimal management overhead.

```
gcp.netapp_replication
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                                                                                                                                                               | Description |
| ----------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string        |
| ancestors                     | core | array<string> |
| cluster_location              | core | string        | Optional. Location of the user cluster.                                                                                                                                                                                                                                                 |
| create_time                   | core | timestamp     | Output only. Replication create time.                                                                                                                                                                                                                                                   |
| datadog_display_name          | core | string        |
| description                   | core | string        | A description about this replication relationship.                                                                                                                                                                                                                                      |
| destination_volume            | core | string        | Output only. Full name of destination volume resource. Example : "projects/{project}/locations/{location}/volumes/{volume_id}"                                                                                                                                                          |
| destination_volume_parameters | core | json          | Required. Input only. Destination volume parameters                                                                                                                                                                                                                                     |
| healthy                       | core | bool          | Output only. Condition of the relationship. Can be one of the following: - true: The replication relationship is healthy. It has not missed the most recent scheduled transfer. - false: The replication relationship is not healthy. It has missed the most recent scheduled transfer. |
| hybrid_peering_details        | core | json          | Output only. Hybrid peering details.                                                                                                                                                                                                                                                    |
| hybrid_replication_type       | core | string        | Output only. Type of the hybrid replication.                                                                                                                                                                                                                                            |
| labels                        | core | array<string> | Resource labels to represent user provided metadata.                                                                                                                                                                                                                                    |
| mirror_state                  | core | string        | Output only. Indicates the state of mirroring.                                                                                                                                                                                                                                          |
| name                          | core | string        | Identifier. The resource name of the Replication. Format: `projects/{project_id}/locations/{location}/volumes/{volume_id}/replications/{replication_id}`.                                                                                                                               |
| organization_id               | core | string        |
| parent                        | core | string        |
| project_id                    | core | string        |
| project_number                | core | string        |
| region_id                     | core | string        |
| replication_schedule          | core | string        | Required. Indicates the schedule for replication.                                                                                                                                                                                                                                       |
| resource_name                 | core | string        |
| role                          | core | string        | Output only. Indicates whether this points to source or destination.                                                                                                                                                                                                                    |
| source_volume                 | core | string        | Output only. Full name of source volume resource. Example : "projects/{project}/locations/{location}/volumes/{volume_id}"                                                                                                                                                               |
| state                         | core | string        | Output only. State of the replication.                                                                                                                                                                                                                                                  |
| state_details                 | core | string        | Output only. State details of the replication.                                                                                                                                                                                                                                          |
| tags                          | core | hstore_csv    |
| transfer_stats                | core | json          | Output only. Replication transfer statistics.                                                                                                                                                                                                                                           |
| zone_id                       | core | string        |
