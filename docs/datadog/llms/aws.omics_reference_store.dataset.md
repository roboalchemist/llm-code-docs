# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.omics_reference_store.dataset.md

---
title: Omics Reference Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Omics Reference Store
---

# Omics Reference Store

This table represents the omics_reference_store resource from Amazon Web Services.

```
aws.omics_reference_store
```

## Fields

| Title         | ID   | Type       | Data Type                                          | Description |
| ------------- | ---- | ---------- | -------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| arn           | core | string     | The store's ARN.                                   |
| creation_time | core | timestamp  | When the store was created.                        |
| description   | core | string     | The store's description.                           |
| id            | core | string     | The store's ID.                                    |
| name          | core | string     | The store's name.                                  |
| sse_config    | core | json       | The store's server-side encryption (SSE) settings. |
| tags          | core | hstore_csv |
