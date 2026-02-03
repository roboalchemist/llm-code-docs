# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.networkconnectivity_hub.dataset.md

---
title: Network Connectivity Hub
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Connectivity Hub
---

# Network Connectivity Hub

Network Connectivity Hub in Google Cloud is a central management resource for connecting and organizing multiple network services. It provides a unified way to manage spokes, such as VPNs, interconnects, and VPC networks, through a hub-and-spoke model. This simplifies network topology, improves visibility, and enables consistent policy enforcement across hybrid and multi-cloud environments.

```
gcp.networkconnectivity_hub
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The time the hub was created.                                                                                                                                                                                                                                                                                                               |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. An optional description of the hub.                                                                                                                                                                                                                                                                                                            |
| export_psc           | core | bool          | Optional. Whether Private Service Connect connection propagation is enabled for the hub. If true, Private Service Connect endpoints in VPC spokes attached to the hub are made accessible to other VPC spokes attached to the hub. The default value is false.                                                                                           |
| labels               | core | array<string> | Optional labels in key-value pair format. For more information about labels, see [Requirements for labels](https://cloud.google.com/resource-manager/docs/creating-managing-labels#requirements).                                                                                                                                                        |
| name                 | core | string        | Immutable. The name of the hub. Hub names must be unique. They use the following form: `projects/{project_number}/locations/global/hubs/{hub_id}`                                                                                                                                                                                                        |
| organization_id      | core | string        |
| parent               | core | string        |
| policy_mode          | core | string        | Optional. The policy mode of this hub. This field can be either PRESET or CUSTOM. If unspecified, the policy_mode defaults to PRESET.                                                                                                                                                                                                                    |
| preset_topology      | core | string        | Optional. The topology implemented in this hub. Currently, this field is only used when policy_mode = PRESET. The available preset topologies are MESH and STAR. If preset_topology is unspecified and policy_mode = PRESET, the preset_topology defaults to MESH. When policy_mode = CUSTOM, the preset_topology is set to PRESET_TOPOLOGY_UNSPECIFIED. |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| route_tables         | core | array<string> | Output only. The route tables that belong to this hub. They use the following form: `projects/{project_number}/locations/global/hubs/{hub_id}/routeTables/{route_table_id}` This field is read-only. Network Connectivity Center automatically populates it based on the route tables nested under the hub.                                              |
| routing_vpcs         | core | json          | Output only. The VPC networks associated with this hub's spokes. This field is read-only. Network Connectivity Center automatically populates it based on the set of spokes attached to the hub.                                                                                                                                                         |
| spoke_summary        | core | json          | Output only. A summary of the spokes associated with a hub. The summary includes a count of spokes according to type and according to state. If any spokes are inactive, the summary also lists the reasons they are inactive, including a count for each reason.                                                                                        |
| state                | core | string        | Output only. The current lifecycle state of this hub.                                                                                                                                                                                                                                                                                                    |
| tags                 | core | hstore_csv    |
| unique_id            | core | string        | Output only. The Google-generated UUID for the hub. This value is unique across all hub resources. If a hub is deleted and another with the same name is created, the new hub is assigned a different unique_id.                                                                                                                                         |
| update_time          | core | timestamp     | Output only. The time the hub was last updated.                                                                                                                                                                                                                                                                                                          |
| zone_id              | core | string        |
