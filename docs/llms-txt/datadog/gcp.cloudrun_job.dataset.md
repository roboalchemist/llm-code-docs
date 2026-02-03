# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudrun_job.dataset.md

---
title: Cloudrun Job
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloudrun Job
---

# Cloudrun Job

This table represents the Cloudrun Job resource from Google Cloud Platform.

```
gcp.cloudrun_job
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                          | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| api_version          | core | string        | Optional. APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. |
| datadog_display_name | core | string        |
| gcp_status           | core | json          | Output only. Current status of a job.                                                                                                                                                              |
| kind                 | core | string        | Optional. Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase.  |
| labels               | core | array<string> |
| metadata             | core | json          | Optional. Standard object's metadata.                                                                                                                                                              |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| spec                 | core | json          | Optional. Specification of the desired behavior of a job.                                                                                                                                          |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
