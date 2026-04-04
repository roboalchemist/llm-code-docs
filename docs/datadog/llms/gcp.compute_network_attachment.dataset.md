# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_network_attachment.dataset.md

---
title: Network Attachment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Attachment
---

# Network Attachment

A Network Attachment in Google Cloud is a resource that connects a Virtual Private Cloud (VPC) network to a service producer's network using Private Service Connect. It allows managed services or partner services to be securely accessed through internal IP addresses, enabling private communication without exposing traffic to the public internet.

```
gcp.compute_network_attachment
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| --------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| connection_endpoints  | core | json          | Output only. [Output Only] An array of connections for all the producers connected to this network attachment.                                                                                                                                                                                                                                                                                                                                      |
| connection_preference | core | string        |
| creation_timestamp    | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                |
| datadog_display_name  | core | string        |
| description           | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| id                    | core | string        | Output only. [Output Only] The unique identifier for the resource type. The server generates this identifier.                                                                                                                                                                                                                                                                                                                                       |
| kind                  | core | string        | Output only. [Output Only] Type of the resource.                                                                                                                                                                                                                                                                                                                                                                                                    |
| labels                | core | array<string> |
| name                  | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| network               | core | string        | Output only. [Output Only] The URL of the network which the Network Attachment belongs to. Practically it is inferred by fetching the network of the first subnetwork associated. Because it is required that all the subnetworks must be from the same network, it is assured that the Network Attachment belongs to the same network as all the subnetworks.                                                                                      |
| organization_id       | core | string        |
| parent                | core | string        |
| producer_accept_lists | core | array<string> | Projects that are allowed to connect to this network attachment. The project can be specified using its id or number.                                                                                                                                                                                                                                                                                                                               |
| producer_reject_lists | core | array<string> | Projects that are not allowed to connect to this network attachment. The project can be specified using its id or number.                                                                                                                                                                                                                                                                                                                           |
| project_id            | core | string        |
| project_number        | core | string        |
| region                | core | string        | Output only. [Output Only] URL of the region where the network attachment resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.                                                                                                                                                                                                  |
| region_id             | core | string        |
| resource_name         | core | string        |
| self_link             | core | string        | Output only. [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                     |
| self_link_with_id     | core | string        | Output only. [Output Only] Server-defined URL for this resource's resource id.                                                                                                                                                                                                                                                                                                                                                                      |
| subnetworks           | core | array<string> | An array of URLs where each entry is the URL of a subnet provided by the service consumer to use for endpoints in the producers that connect to this network attachment.                                                                                                                                                                                                                                                                            |
| tags                  | core | hstore_csv    |
| zone_id               | core | string        |
