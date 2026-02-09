# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.livestream_pool.dataset.md

---
title: Livestream Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Livestream Pool
---

# Livestream Pool

Livestream Pool in Google Cloud is a managed resource that handles live video streaming workloads. It manages a group of streaming instances that process, package, and deliver live video content efficiently. The pool automatically scales resources based on demand, ensuring low latency and high availability for live broadcasts. It integrates with other Google Cloud media services for encoding, storage, and content delivery.

```
gcp.livestream_pool
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The creation time.                                                                          |
| datadog_display_name | core | string        |
| labels               | core | array<string> | User-defined key/value metadata.                                                                         |
| name                 | core | string        | The resource name of the pool, in the form of: `projects/{project}/locations/{location}/pools/{poolId}`. |
| network_config       | core | json          | Network configuration for the pool.                                                                      |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The update time.                                                                            |
| zone_id              | core | string        |
