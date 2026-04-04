# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.integrations_integration.dataset.md

---
title: Integration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Integration
---

# Integration

Integration in Google Cloud refers to a managed service that connects and automates workflows across different Google Cloud and external systems. It enables users to design, deploy, and manage integrations using prebuilt connectors, triggers, and transformations. This resource helps streamline data exchange, event handling, and process orchestration between applications and services without requiring extensive custom code.

```
gcp.integrations_integration
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                    | Description |
| -------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| active               | core | bool          | Required. If any integration version is published.                                                                           |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Required. Output only. Auto-generated.                                                                                       |
| creator_email        | core | string        | Output only. The creator's email address. Generated based on the End User Credentials/LOAS role of the user making the call. |
| datadog_display_name | core | string        |
| description          | core | string        | Optional.                                                                                                                    |
| labels               | core | array<string> |
| last_modifier_email  | core | string        | Required. The last modifier of this integration                                                                              |
| name                 | core | string        | Required. The resource name of the integration.                                                                              |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. Auto-generated.                                                                                                 |
| zone_id              | core | string        |
