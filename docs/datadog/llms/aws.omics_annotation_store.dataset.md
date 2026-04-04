# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.omics_annotation_store.dataset.md

---
title: AWS HealthOmics Annotation Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS HealthOmics Annotation Store
---

# AWS HealthOmics Annotation Store

AWS HealthOmics Annotation Store is a managed service that allows users to store, manage, and query genomic annotation data at scale. It supports efficient retrieval and integration of biological metadata, enabling researchers to link genomic variants with functional information. The service is designed for bioinformatics workflows that require secure, high-performance access to large annotation datasets.

```
aws.omics_annotation_store
```

## Fields

| Title            | ID   | Type       | Data Type                                                             | Description |
| ---------------- | ---- | ---------- | --------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| creation_time    | core | timestamp  | When the store was created.                                           |
| description      | core | string     | The store's description.                                              |
| id               | core | string     | The store's ID.                                                       |
| name             | core | string     | The store's name.                                                     |
| num_versions     | core | int64      | An integer indicating how many versions of an annotation store exist. |
| reference        | core | json       | The store's genome reference.                                         |
| sse_config       | core | json       | The store's server-side encryption (SSE) settings.                    |
| status           | core | string     | The store's status.                                                   |
| status_message   | core | string     | A status message.                                                     |
| store_arn        | core | string     | The store's ARN.                                                      |
| store_format     | core | string     | The store's annotation file format.                                   |
| store_options    | core | json       | The store's parsing options.                                          |
| store_size_bytes | core | int64      | The store's size in bytes.                                            |
| tags             | core | hstore_csv |
| update_time      | core | timestamp  | When the store was updated.                                           |
