# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.apphub_service_project_attachment.dataset.md

---
title: Service Project Attachment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Service Project Attachment
---

# Service Project Attachment

A Service Project Attachment in Google Cloud links a service project to a host project within a Shared VPC setup. It allows the service project to use network resources, such as subnets and firewalls, that are centrally managed in the host project. This setup helps enforce consistent network policies and simplifies resource management across multiple projects.

```
gcp.apphub_service_project_attachment
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                               | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. Create time.                                                                                                                                                                                               |
| datadog_display_name | core | string        |
| labels               | core | array<string> |
| name                 | core | string        | Identifier. The resource name of a ServiceProjectAttachment. Format: `"projects/{host-project-id}/locations/global/serviceProjectAttachments/{service-project-id}."`                                                    |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| service_project      | core | string        | Required. Immutable. Service project name in the format: `"projects/abc"` or `"projects/123"`. As input, project name with either project id or number are accepted. As output, this field will contain project number. |
| state                | core | string        | Output only. ServiceProjectAttachment state.                                                                                                                                                                            |
| tags                 | core | hstore_csv    |
| uid                  | core | string        | Output only. A globally unique identifier (in UUID4 format) for the `ServiceProjectAttachment`.                                                                                                                         |
| zone_id              | core | string        |
