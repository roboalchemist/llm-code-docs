# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.vmmigration_image_import.dataset.md

---
title: VM Migration Image Import
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VM Migration Image Import
---

# VM Migration Image Import

VM Migration Image Import in Google Cloud is a service that helps migrate virtual machine images from on-premises or other cloud environments into Google Cloud. It automates the process of importing, converting, and preparing images for use as Compute Engine instances, ensuring compatibility and reducing manual effort during migration.

```
gcp.vmmigration_image_import
```

## Fields

| Title                         | ID   | Type          | Data Type                                                                                                                                  | Description |
| ----------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                          | core | string        |
| ancestors                     | core | array<string> |
| cloud_storage_uri             | core | string        | Immutable. The path to the Cloud Storage file from which the image should be imported.                                                     |
| create_time                   | core | timestamp     | Output only. The time the image import was created.                                                                                        |
| datadog_display_name          | core | string        |
| disk_image_target_defaults    | core | json          | Immutable. Target details for importing a disk image, will be used by ImageImportJob.                                                      |
| encryption                    | core | json          | Immutable. The encryption details used by the image import process during the image adaptation for Compute Engine.                         |
| labels                        | core | array<string> |
| machine_image_target_defaults | core | json          | Immutable. Target details for importing a machine image, will be used by ImageImportJob.                                                   |
| name                          | core | string        | Output only. The resource path of the ImageImport.                                                                                         |
| organization_id               | core | string        |
| parent                        | core | string        |
| project_id                    | core | string        |
| project_number                | core | string        |
| recent_image_import_jobs      | core | json          | Output only. The result of the most recent runs for this ImageImport. All jobs for this ImageImport can be listed via ListImageImportJobs. |
| region_id                     | core | string        |
| resource_name                 | core | string        |
| tags                          | core | hstore_csv    |
| zone_id                       | core | string        |
