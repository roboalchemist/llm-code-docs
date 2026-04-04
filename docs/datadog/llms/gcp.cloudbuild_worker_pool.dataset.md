# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.cloudbuild_worker_pool.dataset.md

---
title: Cloud Build Worker Pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Build Worker Pool
---

# Cloud Build Worker Pool

A Cloud Build Worker Pool in Google Cloud is a private pool of workers used to run Cloud Build jobs on dedicated infrastructure. It allows you to isolate builds from the public pool, control network access, and customize machine types for performance or security needs. This helps ensure consistent build environments and compliance with organizational policies.

```
gcp.cloudbuild_worker_pool
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                             | Description |
| ---------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| ancestors              | core | array<string> |
| annotations            | core | hstore        | User specified annotations. See https://google.aip.dev/128#annotations for more details such as format and size limitations.                                                                                                                                                                          |
| create_time            | core | timestamp     | Output only. Time at which the request to create the `WorkerPool` was received.                                                                                                                                                                                                                       |
| datadog_display_name   | core | string        |
| delete_time            | core | timestamp     | Output only. Time at which the request to delete the `WorkerPool` was received.                                                                                                                                                                                                                       |
| etag                   | core | string        | Output only. Checksum computed by the server. May be sent on update and delete requests to ensure that the client has an up-to-date value before proceeding.                                                                                                                                          |
| gcp_display_name       | core | string        | A user-specified, human-readable name for the `WorkerPool`. If provided, this value must be 1-63 characters.                                                                                                                                                                                          |
| labels                 | core | array<string> |
| name                   | core | string        | Output only. The resource name of the `WorkerPool`, with format `projects/{project}/locations/{location}/workerPools/{worker_pool}`. The value of `{worker_pool}` is provided by `worker_pool_id` in `CreateWorkerPool` request and the value of `{location}` is determined by the endpoint accessed. |
| organization_id        | core | string        |
| parent                 | core | string        |
| private_pool_v1_config | core | json          | Private Pool configuration.                                                                                                                                                                                                                                                                           |
| project_id             | core | string        |
| project_number         | core | string        |
| region_id              | core | string        |
| resource_name          | core | string        |
| state                  | core | string        | Output only. `WorkerPool` state.                                                                                                                                                                                                                                                                      |
| tags                   | core | hstore_csv    |
| uid                    | core | string        | Output only. A unique identifier for the `WorkerPool`.                                                                                                                                                                                                                                                |
| update_time            | core | timestamp     | Output only. Time at which the request to update the `WorkerPool` was received.                                                                                                                                                                                                                       |
| zone_id                | core | string        |
