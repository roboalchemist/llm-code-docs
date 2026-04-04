# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dlp_inspect_template.dataset.md

---
title: InspectTemplate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > InspectTemplate
---

# InspectTemplate

InspectTemplate in Google Cloud is a reusable configuration for Data Loss Prevention (DLP) inspections. It defines what types of sensitive data to look for, such as personally identifiable information, and how to inspect content. By using an InspectTemplate, you can standardize and simplify DLP jobs or API calls across multiple projects or data sources.

```
gcp.dlp_inspect_template
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                | Description |
| -------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The creation timestamp of an inspectTemplate.                                                                                                                                               |
| datadog_display_name | core | string        |
| description          | core | string        | Short description (max 256 chars).                                                                                                                                                                       |
| gcp_display_name     | core | string        | Display name (max 256 chars).                                                                                                                                                                            |
| inspect_config       | core | json          | The core content of the template. Configuration of the scanning process.                                                                                                                                 |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The template name. The template will have one of the following formats: `projects/PROJECT_ID/inspectTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/inspectTemplates/TEMPLATE_ID`; |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The last update timestamp of an inspectTemplate.                                                                                                                                            |
| zone_id              | core | string        |
