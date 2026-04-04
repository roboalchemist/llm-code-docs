# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.logging_log_bucket.dataset.md

---
title: Log Bucket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Log Bucket
---

# Log Bucket

A Log Bucket in Google Cloud is a specialized storage container within Cloud Logging that holds log entries. It allows you to centralize, organize, and retain logs for analysis, compliance, or troubleshooting. You can configure retention policies, set access controls, and route logs from multiple projects or services into a single bucket for easier management.

```
gcp.logging_log_bucket
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                         | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| analytics_enabled    | core | bool          | Optional. Whether log analytics is enabled for this bucket.Once enabled, log analytics features cannot be disabled.                                                                                                                                                                                                                                                               |
| ancestors            | core | array<string> |
| cmek_settings        | core | json          | Optional. The CMEK settings of the log bucket. If present, new log entries written to this log bucket are encrypted using the CMEK key provided in this configuration. If a log bucket has CMEK settings, the CMEK settings cannot be disabled later by updating the log bucket. Changing the KMS key is allowed.                                                                 |
| create_time          | core | timestamp     | Output only. The creation timestamp of the bucket. This is not set for any of the default buckets.                                                                                                                                                                                                                                                                                |
| datadog_display_name | core | string        |
| description          | core | string        | Optional. Describes this bucket.                                                                                                                                                                                                                                                                                                                                                  |
| index_configs        | core | json          | Optional. A list of indexed fields and related configuration data.                                                                                                                                                                                                                                                                                                                |
| labels               | core | array<string> |
| lifecycle_state      | core | string        | Output only. The bucket lifecycle state.                                                                                                                                                                                                                                                                                                                                          |
| locked               | core | bool          | Optional. Whether the bucket is locked.The retention period on a locked bucket cannot be changed. Locked buckets may only be deleted if they are empty.                                                                                                                                                                                                                           |
| name                 | core | string        | Output only. The resource name of the bucket.For example:projects/my-project/locations/global/buckets/my-bucketFor a list of supported locations, see Supported Regions (https://cloud.google.com/logging/docs/region-support)For the location of global it is unspecified where log entries are actually stored.After a bucket has been created, the location cannot be changed. |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| restricted_fields    | core | array<string> | Optional. Log entry field paths that are denied access in this bucket.The following fields and their children are eligible: textPayload, jsonPayload, protoPayload, httpRequest, labels, sourceLocation.Restricting a repeated field will restrict all values. Adding a parent will block all child fields. (e.g. foo.bar will block foo.bar.baz)                                 |
| retention_days       | core | int64         | Optional. Logs will be retained by default for this amount of time, after which they will automatically be deleted. The minimum retention period is 1 day. If this value is set to zero at bucket creation time, the default time of 30 days will be used.                                                                                                                        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The last update timestamp of the bucket.                                                                                                                                                                                                                                                                                                                             |
| zone_id              | core | string        |
