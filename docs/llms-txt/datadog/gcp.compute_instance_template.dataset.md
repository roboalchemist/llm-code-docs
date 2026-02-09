# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_instance_template.dataset.md

---
title: Compute Engine Instance Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Compute Engine Instance Template
---

# Compute Engine Instance Template

A Compute Engine Instance Template in Google Cloud is a reusable configuration that defines settings for virtual machine instances, such as machine type, disk image, network, and metadata. It allows you to create multiple instances with consistent configurations, simplifying scaling and deployment.

```
gcp.compute_instance_template
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ---------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| ancestors              | core | array<string> |
| creation_timestamp     | core | timestamp     | Output only. [Output Only] The creation timestamp for this instance template inRFC3339 text format.                                                                                                                                                                                                                                                                                                                                                 |
| datadog_display_name   | core | string        |
| description            | core | string        | An optional description of this resource. Provide this property when you create the resource.                                                                                                                                                                                                                                                                                                                                                       |
| id                     | core | string        | Output only. [Output Only] A unique identifier for this instance template. The server defines this identifier.                                                                                                                                                                                                                                                                                                                                      |
| kind                   | core | string        | Output only. [Output Only] The resource type, which is alwayscompute#instanceTemplate for instance templates.                                                                                                                                                                                                                                                                                                                                       |
| labels                 | core | array<string> |
| name                   | core | string        | Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply withRFC1035. Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash. |
| organization_id        | core | string        |
| parent                 | core | string        |
| project_id             | core | string        |
| project_number         | core | string        |
| properties             | core | json          | The instance properties for this instance template.                                                                                                                                                                                                                                                                                                                                                                                                 |
| region                 | core | string        | Output only. [Output Only] URL of the region where the instance template resides. Only applicable for regional resources.                                                                                                                                                                                                                                                                                                                           |
| region_id              | core | string        |
| resource_name          | core | string        |
| self_link              | core | string        | Output only. [Output Only] The URL for this instance template. The server defines this URL.                                                                                                                                                                                                                                                                                                                                                         |
| source_instance        | core | string        | The source instance used to create the template. You can provide this as a partial or full URL to the resource. For example, the following are valid values: - https://www.googleapis.com/compute/v1/projects/project/zones/zone/instances/instance - projects/project/zones/zone/instances/instance                                                                                                                                                |
| source_instance_params | core | json          | The source instance params to use to create this instance template.                                                                                                                                                                                                                                                                                                                                                                                 |
| tags                   | core | hstore_csv    |
| zone_id                | core | string        |
