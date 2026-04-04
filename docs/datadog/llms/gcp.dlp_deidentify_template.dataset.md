# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dlp_deidentify_template.dataset.md

---
title: Deidentify Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Deidentify Template
---

# Deidentify Template

A Deidentify Template in Google Cloud is a reusable configuration that defines how sensitive data should be transformed or masked to protect privacy. It specifies de-identification methods such as tokenization, masking, or date shifting, and can be applied to multiple data sources through the Data Loss Prevention (DLP) API.

```
gcp.dlp_deidentify_template
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                                     | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The creation timestamp of an inspectTemplate.                                                                                                                                                    |
| datadog_display_name | core | string        |
| deidentify_config    | core | json          | The core content of the template.                                                                                                                                                                             |
| description          | core | string        | Short description (max 256 chars).                                                                                                                                                                            |
| gcp_display_name     | core | string        | Display name (max 256 chars).                                                                                                                                                                                 |
| labels               | core | array<string> |
| name                 | core | string        | Output only. The template name. The template will have one of the following formats: `projects/PROJECT_ID/deidentifyTemplates/TEMPLATE_ID` OR `organizations/ORGANIZATION_ID/deidentifyTemplates/TEMPLATE_ID` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| update_time          | core | timestamp     | Output only. The last update timestamp of an inspectTemplate.                                                                                                                                                 |
| zone_id              | core | string        |
