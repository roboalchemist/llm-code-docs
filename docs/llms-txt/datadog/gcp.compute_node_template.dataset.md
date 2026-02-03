# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_node_template.dataset.md

---
title: Compute Node Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Compute Node Template
---

# Compute Node Template

A Compute Node Template in Google Cloud is a resource that defines the configuration for sole-tenant nodes. It specifies properties such as machine type, CPU platform, and node affinity labels, which are then used to create node groups. This allows workloads to run on dedicated physical servers for isolation, compliance, or licensing requirements.

```
gcp.compute_node_template
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| --------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string        |
| accelerators          | core | json          |
| ancestors             | core | array<string> |
| cpu_overcommit_type   | core | string        | CPU overcommit.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| creation_timestamp    | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                                     |
| datadog_display_name  | core | string        |
| description           | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                                            |
| disks                 | core | json          |
| gcp_status            | core | string        | [Output Only] The status of the node template. One of the following values: CREATING, READY, and DELETING. Possible values: ['CREATING', 'DELETING', 'INVALID', 'READY']. Values descriptions: ['Resources are being allocated.', 'The node template is currently being deleted.', 'Invalid status.', 'The node template is ready.']                                                                                                                                     |
| id                    | core | string        | Output only. [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                                             |
| kind                  | core | string        | Output only. [Output Only] The type of the resource. Alwayscompute#nodeTemplate for node templates.                                                                                                                                                                                                                                                                                                                                                                      |
| labels                | core | array<string> |
| name                  | core | string        | The name of the resource, provided by the client when initially creating the resource. The resource name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| node_type             | core | string        | The node type to use for nodes group that are created from this template.                                                                                                                                                                                                                                                                                                                                                                                                |
| node_type_flexibility | core | json          | Do not use. Instead, use the node_type property.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region                | core | string        | Output only. [Output Only] The name of the region where the node template resides, such as us-central1.                                                                                                                                                                                                                                                                                                                                                                  |
| region_id             | core | string        |
| resource_name         | core | string        |
| self_link             | core | string        | Output only. [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                                          |
| server_binding        | core | json          | Sets the binding properties for the physical server. Valid values include: - *[Default]* RESTART_NODE_ON_ANY_SERVER: Restarts VMs on any available physical server - RESTART_NODE_ON_MINIMAL_SERVER: Restarts VMs on the same physical server whenever possible See Sole-tenant node options for more information.                                                                                                                                                       |
| status_message        | core | string        | Output only. [Output Only] An optional, human-readable explanation of the status.                                                                                                                                                                                                                                                                                                                                                                                        |
| tags                  | core | hstore_csv    |
| zone_id               | core | string        |
