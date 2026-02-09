# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.securitycenter_notification_config.dataset.md

---
title: Security Command Center NotificationConfig
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Security Command Center
  NotificationConfig
---

# Security Command Center NotificationConfig

Security Command Center NotificationConfig in Google Cloud defines how and where to send notifications about security findings and events. It allows you to configure notification channels such as Pub/Sub topics to receive alerts in real time when new findings are detected or existing ones change. This helps automate security monitoring and response workflows.

```
gcp.securitycenter_notification_config
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                         | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| description          | core | string        | The description of the notification config (max of 1024 characters).                                                                                                                                                                                                                                                                                              |
| labels               | core | array<string> |
| name                 | core | string        | The relative resource name of this notification config. See: https://cloud.google.com/apis/design/resource_names#relative_resource_name Example: "organizations/{organization_id}/notificationConfigs/notify_public_bucket", "folders/{folder_id}/notificationConfigs/notify_public_bucket", or "projects/{project_id}/notificationConfigs/notify_public_bucket". |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| pubsub_topic         | core | string        | The Pub/Sub topic to send notifications to. Its format is "projects/[project_id]/topics/[topic]".                                                                                                                                                                                                                                                                 |
| region_id            | core | string        |
| resource_name        | core | string        |
| service_account      | core | string        | Output only. The service account that needs "pubsub.topics.publish" permission to publish to the Pub/Sub topic.                                                                                                                                                                                                                                                   |
| streaming_config     | core | json          | The config for triggering streaming-based notifications.                                                                                                                                                                                                                                                                                                          |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
