# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.composer_environment.dataset.md

---
title: Cloud Composer Environment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Composer Environment
---

# Cloud Composer Environment

Cloud Composer Environment in GCP is a fully managed workflow orchestration service built on Apache Airflow. It allows you to author, schedule, and monitor complex data pipelines across cloud and on-premises environments. Composer handles infrastructure, scaling, and Airflow upgrades, so you can focus on building workflows instead of managing servers.

```
gcp.composer_environment
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                      | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| config               | core | json          | Optional. Configuration parameters for this environment.                                                                                                                                                                                                                                                                                                                                       |
| create_time          | core | timestamp     | Output only. The time at which this environment was created.                                                                                                                                                                                                                                                                                                                                   |
| datadog_display_name | core | string        |
| labels               | core | array<string> | Optional. User-defined labels for this environment. The labels map can contain no more than 64 entries. Entries of the labels map are UTF8 strings that comply with the following restrictions: * Keys must conform to regexp: \p{Ll}\p{Lo}{0,62} * Values must conform to regexp: [\p{Ll}\p{Lo}\p{N}_-]{0,63} * Both keys and values are additionally constrained to be <= 128 bytes in size. |
| name                 | core | string        | Identifier. The resource name of the environment, in the form: "projects/{projectId}/locations/{locationId}/environments/{environmentId}" EnvironmentId must start with a lowercase letter followed by up to 63 lowercase letters, numbers, or hyphens, and cannot end with a hyphen.                                                                                                          |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| satisfies_pzi        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                                                                                                                                                                          |
| satisfies_pzs        | core | bool          | Output only. Reserved for future use.                                                                                                                                                                                                                                                                                                                                                          |
| state                | core | string        | The current state of the environment.                                                                                                                                                                                                                                                                                                                                                          |
| storage_config       | core | json          | Optional. Storage configuration for this environment.                                                                                                                                                                                                                                                                                                                                          |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The time at which this environment was last modified.                                                                                                                                                                                                                                                                                                                             |
| uuid                 | core | string        | Output only. The UUID (Universally Unique IDentifier) associated with this environment. This value is generated when the environment is created.                                                                                                                                                                                                                                               |
| zone_id              | core | string        |
