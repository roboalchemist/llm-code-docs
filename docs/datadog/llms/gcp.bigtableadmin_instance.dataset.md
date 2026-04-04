# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.bigtableadmin_instance.dataset.md

---
title: Cloud Bigtable Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Bigtable Instance
---

# Cloud Bigtable Instance

Cloud Bigtable Instance is a scalable NoSQL database resource in Google Cloud designed for high-throughput and low-latency workloads. It is ideal for time-series data, analytics, and operational applications that require massive scalability. An instance defines the configuration for clusters, storage type, and replication, serving as the foundation for managing Bigtable tables and workloads.

```
gcp.bigtableadmin_instance
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. A commit timestamp representing when this Instance was created. For instances created before this field was added (August 2021), this value is `seconds: 0, nanos: 1`.                                                                                                                                                                                                                                                                                                                                                                                                                           |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | Required. The descriptive name for this instance as it appears in UIs. Can be changed at any time, but should be kept globally unique to avoid confusion.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| labels               | core | array<string> | Labels are a flexible and lightweight mechanism for organizing cloud resources into groups that reflect a customer's organizational needs and deployment strategies. They can be used to filter resources and aggregate metrics. * Label keys must be between 1 and 63 characters long and must conform to the regular expression: `\p{Ll}\p{Lo}{0,62}`. * Label values must be between 0 and 63 characters long and must conform to the regular expression: `[\p{Ll}\p{Lo}\p{N}_-]{0,63}`. * No more than 64 labels can be associated with a given resource. * Keys and values must both be under 128 bytes. |
| name                 | core | string        | The unique name of the instance. Values are of the form `projects/{project}/instances/a-z+[a-z0-9]`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| state                | core | string        | Output only. The current state of the instance.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| tags                 | core | hstore_csv    |
| type                 | core | string        | The type of the instance. Defaults to `PRODUCTION`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| zone_id              | core | string        |
