# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.omics_variant_store.dataset.md

---
title: AWS HealthOmics Variant Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS HealthOmics Variant Store
---

# AWS HealthOmics Variant Store

AWS HealthOmics Variant Store is a managed service that stores, queries, and analyzes genomic variant data at scale. It enables researchers and bioinformaticians to efficiently manage variant datasets, integrate them with other omics data, and perform downstream analysis using AWS analytics and machine learning tools.

```gdscript3
aws.omics_variant_store
```

## Fields

| Title            | ID   | Type       | Data Type                                          | Description |
| ---------------- | ---- | ---------- | -------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| creation_time    | core | timestamp  | When the store was created.                        |
| description      | core | string     | The store's description.                           |
| id               | core | string     | The store's ID.                                    |
| name             | core | string     | The store's name.                                  |
| reference        | core | json       | The store's genome reference.                      |
| sse_config       | core | json       | The store's server-side encryption (SSE) settings. |
| status           | core | string     | The store's status.                                |
| status_message   | core | string     | The store's status message.                        |
| store_arn        | core | string     | The store's ARN.                                   |
| store_size_bytes | core | int64      | The store's size in bytes.                         |
| tags             | core | hstore_csv |
| update_time      | core | timestamp  | When the store was updated.                        |
