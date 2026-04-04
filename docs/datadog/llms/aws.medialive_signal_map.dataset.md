# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.medialive_signal_map.dataset.md

---
title: Elemental MediaLive Signal Map
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaLive Signal Map
---

# Elemental MediaLive Signal Map

Elemental MediaLive Signal Map provides a visual representation of input signal health and flow within AWS Elemental MediaLive channels. It helps monitor the status of input sources, detect issues in real time, and ensure reliable live video streaming by showing the state of signals across different channel components.

```gdscript3
aws.medialive_signal_map
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                                         | Description |
| ------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| arn                       | core | string     | A signal map's ARN (Amazon Resource Name)                                                         |
| created_at                | core | timestamp  | Placeholder documentation for __timestampIso8601                                                  |
| description               | core | string     | A resource's optional description.                                                                |
| id                        | core | string     | A signal map's id.                                                                                |
| modified_at               | core | timestamp  | Placeholder documentation for __timestampIso8601                                                  |
| monitor_deployment_status | core | string     | A signal map's monitor deployment status.                                                         |
| name                      | core | string     | A resource's name. Names must be unique within the scope of a resource type in a specific region. |
| status                    | core | string     | A signal map's current status which is dependent on its lifecycle actions or associated jobs.     |
| tags                      | core | hstore_csv |
