# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.financialservices_instance.dataset.md

---
title: >-
  There is no official Google Cloud resource called
  "gcp_financialservices_instance".
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > There is no official Google Cloud
  resource called "gcp_financialservices_instance".
---

# There is no official Google Cloud resource called "gcp_financialservices_instance".

This table represents the There is no official Google Cloud resource called "gcp_financialservices_instance". resource from Google Cloud Platform.

```
gcp.financialservices_instance
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                               | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Timestamp when the Instance was created. Assigned by the server.                                                           |
| datadog_display_name | core | string        |
| labels               | core | array<string> | Labels                                                                                                                                  |
| name                 | core | string        | Output only. The full path to the Instance resource in this API. format: `projects/{project}/locations/{location}/instances/{instance}` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. State of the instance. Assigned by the server.                                                                             |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Timestamp when the Instance was last updated. Assigned by the server.                                                      |
| zone_id              | core | string        |
