# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.clouddeploy_custom_target_type.dataset.md

---
title: Cloud Deploy Custom Target Type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Cloud Deploy Custom Target Type
---

# Cloud Deploy Custom Target Type

Cloud Deploy Custom Target Type in Google Cloud lets you define and manage custom deployment targets beyond the built-in options like GKE or Cloud Run. It allows integration with external systems or environments by specifying custom deployment logic and configurations. This enables flexible, consistent delivery pipelines across diverse infrastructure setups.

```
gcp.clouddeploy_custom_target_type
```

## Fields

| Title                 | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| --------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string        |
| ancestors             | core | array<string> |
| annotations           | core | hstore        | Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See https://google.aip.dev/128#annotations for more details such as format and size limitations.                                                                                                                                                                                                                                                                                                                        |
| create_time           | core | timestamp     | Output only. Time at which the `CustomTargetType` was created.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| custom_actions        | core | json          | Optional. Configures render and deploy for the `CustomTargetType` using Skaffold custom actions.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| custom_target_type_id | core | string        | Output only. Resource id of the `CustomTargetType`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| datadog_display_name  | core | string        |
| description           | core | string        | Optional. Description of the `CustomTargetType`. Max length is 255 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| etag                  | core | string        | Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.                                                                                                                                                                                                                                                                                                                                 |
| labels                | core | array<string> | Optional. Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints: * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. * All characters must use UTF-8 encoding, and international characters are allowed. * Keys must start with a lowercase letter or international character. * Each resource is limited to a maximum of 64 labels. Both keys and values are additionally constrained to be <= 128 bytes. |
| name                  | core | string        | Identifier. Name of the `CustomTargetType`. Format is `projects/{project}/locations/{location}/customTargetTypes/{customTargetType}`. The `customTargetType` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`                                                                                                                                                                                                                                                                                                                 |
| organization_id       | core | string        |
| parent                | core | string        |
| project_id            | core | string        |
| project_number        | core | string        |
| region_id             | core | string        |
| resource_name         | core | string        |
| tags                  | core | hstore_csv    |
| uid                   | core | string        | Output only. Unique identifier of the `CustomTargetType`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| update_time           | core | timestamp     | Output only. Most recent time at which the `CustomTargetType` was updated.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| zone_id               | core | string        |
