# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.financialservices_dataset.dataset.md

---
title: Financial Services Dataset
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Financial Services Dataset
---

# Financial Services Dataset

A Financial Services Dataset in Google Cloud is a curated collection of financial data designed to support analytics, machine learning, and research in areas such as banking, insurance, and investment. It provides structured and anonymized data that can be used to build predictive models, assess risk, and gain insights into financial trends while maintaining compliance and data security standards.

```
gcp.financialservices_dataset
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                 | Description |
| -------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| create_time          | core | timestamp     | Output only. The timestamp of creation of this resource.                                                                                                  |
| datadog_display_name | core | string        |
| date_range           | core | json          | Required. Core time window of the dataset. All tables should have complete data covering this period.                                                     |
| labels               | core | array<string> | Optional. Labels                                                                                                                                          |
| name                 | core | string        | Output only. Identifier. The resource name of the Dataset. format: `/projects/{project_num}/locations/{location}/instances/{instance}/datasets/{dataset}` |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| state                | core | string        | Output only. State of the dataset (creating, active, deleting, etc.)                                                                                      |
| tags                 | core | hstore_csv    |
| time_zone            | core | json          | Optional. The timezone of the data, default will act as UTC.                                                                                              |
| update_time          | core | timestamp     | Output only. The timestamp of the most recent update of this resource.                                                                                    |
| zone_id              | core | string        |
