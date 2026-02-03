# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_target_instance.dataset.md

---
title: Target Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Target Instance
---

# Target Instance

A Target Instance in Google Cloud is a single virtual machine instance used as a target for traffic from a forwarding rule in a network load balancing configuration. It allows direct routing of traffic to a specific VM without using an instance group, making it suitable for simple or single-instance load balancing scenarios.

```
gcp.compute_target_instance
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| creation_timestamp   | core | timestamp     | Output only. [Output Only] Creation timestamp inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| description          | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| id                   | core | string        | [Output Only] The unique identifier for the resource. This identifier is defined by the server.                                                                                                                                                                                                                                                                                                                                                     |
| instance             | core | string        | A URL to the virtual machine instance that handles traffic for this target instance. When creating a target instance, you can provide the fully-qualified URL or a valid partial URL to the desired virtual machine. For example, the following are all valid URLs: - https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance - projects/project/zones/zone/instances/instance - zones/zone/instances/instance         |
| kind                 | core | string        | Output only. [Output Only] The type of the resource. Alwayscompute#targetInstance for target instances.                                                                                                                                                                                                                                                                                                                                             |
| labels               | core | array<string> |
| name                 | core | string        | Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| nat_policy           | core | string        | Must have a value of NO_NAT. Protocol forwarding delivers packets while preserving the destination IP address of the forwarding rule referencing the target instance.                                                                                                                                                                                                                                                                               |
| network              | core | string        | The URL of the network this target instance uses to forward traffic. If not specified, the traffic will be forwarded to the network that the default network interface belongs to.                                                                                                                                                                                                                                                                  |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| security_policy      | core | string        | [Output Only] The resource URL for the security policy associated with this target instance.                                                                                                                                                                                                                                                                                                                                                        |
| self_link            | core | string        | [Output Only] Server-defined URL for the resource.                                                                                                                                                                                                                                                                                                                                                                                                  |
| tags                 | core | hstore_csv    |
| zone                 | core | string        | Output only. [Output Only] URL of the zone where the target instance resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.                                                                                                                                                                                                                                                       |
| zone_id              | core | string        |
