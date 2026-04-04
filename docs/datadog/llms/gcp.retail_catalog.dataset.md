# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.retail_catalog.dataset.md

---
title: Catalog
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Catalog
---

# Catalog

Catalog in Google Cloud refers to the Data Catalog service, which provides a fully managed metadata management solution. It helps users discover, understand, and manage data assets across GCP services by offering a unified view of datasets, tables, and other resources. It supports tagging, searching, and policy management for better data governance.

```
gcp.retail_catalog
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                         | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | Required. Immutable. The catalog display name. This field must be a UTF-8 encoded string with a length limit of 128 characters. Otherwise, an INVALID_ARGUMENT error is returned. |
| labels               | core | array<string> |
| name                 | core | string        | Required. Immutable. The fully qualified resource name of the catalog.                                                                                                            |
| organization_id      | core | string        |
| parent               | core | string        |
| product_level_config | core | json          | Required. The product level configuration.                                                                                                                                        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
