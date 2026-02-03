# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.aiplatform_specialist_pool.dataset.md

---
title: Specialist Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Specialist Pool
---

# Specialist Pool

Specialist Pool in Google Cloud is a managed group of specialized virtual machine instances designed for specific workloads such as machine learning, data processing, or high-performance computing. It allows users to allocate dedicated compute resources optimized for particular tasks, ensuring consistent performance and scalability.

```
gcp.aiplatform_specialist_pool
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                                                                                               | Description |
| -------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string        |
| ancestors                  | core | array<string> |
| datadog_display_name       | core | string        |
| gcp_display_name           | core | string        | Required. The user-defined name of the SpecialistPool. The name can be up to 128 characters long and can consist of any UTF-8 characters. This field should be unique on project-level. |
| labels                     | core | array<string> |
| name                       | core | string        | Required. The resource name of the SpecialistPool.                                                                                                                                      |
| organization_id            | core | string        |
| parent                     | core | string        |
| pending_data_labeling_jobs | core | array<string> | Output only. The resource name of the pending data labeling jobs.                                                                                                                       |
| project_id                 | core | string        |
| project_number             | core | string        |
| region_id                  | core | string        |
| resource_name              | core | string        |
| specialist_manager_emails  | core | array<string> | The email addresses of the managers in the SpecialistPool.                                                                                                                              |
| specialist_managers_count  | core | int64         | Output only. The number of managers in this SpecialistPool.                                                                                                                             |
| specialist_worker_emails   | core | array<string> | The email addresses of workers in the SpecialistPool.                                                                                                                                   |
| tags                       | core | hstore_csv    |
| zone_id                    | core | string        |
