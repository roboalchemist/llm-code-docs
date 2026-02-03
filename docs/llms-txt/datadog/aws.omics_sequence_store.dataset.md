# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.omics_sequence_store.dataset.md

---
title: AWS HealthOmics Sequence Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS HealthOmics Sequence Store
---

# AWS HealthOmics Sequence Store

AWS HealthOmics Sequence Store is a managed service that allows users to store, manage, and retrieve genomic sequence data at scale. It provides secure, high-performance storage optimized for omics data, enabling efficient access and integration with analysis workflows. The service supports metadata management, versioning, and compliance features to help researchers and healthcare organizations handle sensitive biological data effectively.

```
aws.omics_sequence_store
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                     | Description |
| ------------------------- | ---- | ------------- | --------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| account_id                | core | string        |
| arn                       | core | string        | The store's ARN.                                                                              |
| creation_time             | core | timestamp     | When the store was created.                                                                   |
| description               | core | string        | The store's description.                                                                      |
| e_tag_algorithm_family    | core | string        | The algorithm family of the ETag.                                                             |
| fallback_location         | core | string        | An S3 location that is used to store files that have failed a direct upload.                  |
| id                        | core | string        | The store's ID.                                                                               |
| name                      | core | string        | The store's name.                                                                             |
| propagated_set_level_tags | core | array<string> | The tags keys to propagate to the S3 objects associated with read sets in the sequence store. |
| s3_access                 | core | json          | The S3 metadata of a sequence store, including the ARN and S3 URI of the S3 bucket.           |
| sse_config                | core | json          | The store's server-side encryption (SSE) settings.                                            |
| status                    | core | string        | The status of the sequence store.                                                             |
| status_message            | core | string        | The status message of the sequence store.                                                     |
| tags                      | core | hstore_csv    |
| update_time               | core | timestamp     | The last-updated time of the sequence store.                                                  |
