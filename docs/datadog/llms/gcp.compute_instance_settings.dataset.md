# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.compute_instance_settings.dataset.md

---
title: Compute Instance Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Compute Instance Settings
---

# Compute Instance Settings

Compute Instance Settings in GCP define the configuration parameters for virtual machine instances, including machine type, CPU, memory, disk, network, and metadata options. These settings determine the performance, cost, and behavior of the instance. They can be customized to match workload requirements and are used when creating or managing Compute Engine instances.

```
gcp.compute_instance_settings
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| kind                 | core | string        | Output only. [Output Only] Type of the resource. Alwayscompute#instance_settings for instance settings.                                                                               |
| labels               | core | array<string> |
| metadata             | core | json          | The metadata key/value pairs assigned to all the instances in the corresponding scope.                                                                                                |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone                 | core | string        | Output only. [Output Only] URL of the zone where the resource resides You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body. |
| zone_id              | core | string        |
