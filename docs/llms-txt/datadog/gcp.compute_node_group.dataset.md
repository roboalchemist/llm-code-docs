# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_node_group.dataset.md

---
title: Node Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Node Group
---

# Node Group

A Node Group in Google Cloud is a collection of virtual machine instances within a single zone that share the same configuration. It is commonly used with managed instance groups or sole-tenant nodes to organize and manage compute resources. Node Groups allow you to control placement, scheduling, and scaling of workloads across nodes, providing flexibility for high availability, performance optimization, and licensing requirements.

```
gcp.compute_node_group
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| autoscaling_policy   | core | json          | Specifies how autoscaling should behave.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| creation_timestamp   | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                                     |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                                            |
| gcp_status           | core | string        |
| id                   | core | string        | Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                                             |
| kind                 | core | string        | Output only. [Output Only] The type of the resource. Alwayscompute#nodeGroup for node group.                                                                                                                                                                                                                                                                                                                                                                             |
| labels               | core | array<string> |
| location_hint        | core | string        | An opaque location hint used to place the Node close to other resources. This field is for use by internal tools that use the public API. The location hint here on the NodeGroup overrides any location_hint present in the NodeTemplate.                                                                                                                                                                                                                               |
| maintenance_interval | core | string        | Specifies the frequency of planned maintenance events. The accepted values are: `AS_NEEDED` and `RECURRENT`.                                                                                                                                                                                                                                                                                                                                                             |
| maintenance_policy   | core | string        | Specifies how to handle instances when a node in the group undergoes maintenance. Set to one of: DEFAULT,RESTART_IN_PLACE, or MIGRATE_WITHIN_NODE_GROUP. The default value is DEFAULT. For more information, see Maintenance policies.                                                                                                                                                                                                                                   |
| maintenance_window   | core | json          |
| name                 | core | string        | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| node_template        | core | string        | URL of the node template to create the node group from.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| self_link            | core | string        | Output only. [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                                          |
| share_settings       | core | json          | Share-settings for the node group                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| size                 | core | int64         | Output only. [Output Only] The total number of nodes in the node group.                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags                 | core | hstore_csv    |
| zone                 | core | string        | Output only. [Output Only] The name of the zone where the node group resides, such as us-central1-a.                                                                                                                                                                                                                                                                                                                                                                     |
| zone_id              | core | string        |
