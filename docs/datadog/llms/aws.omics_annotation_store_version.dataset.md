# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.omics_annotation_store_version.dataset.md

---
title: AWS HealthOmics Annotation Store Version
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > AWS HealthOmics Annotation Store
  Version
---

# AWS HealthOmics Annotation Store Version

Represents a specific version of an annotation store in AWS HealthOmics. It provides details about the versioned annotation data, including metadata, status, and related information used for managing and retrieving genomic annotations within the HealthOmics service.

```
aws.omics_annotation_store_version
```

## Fields

| Title              | ID   | Type       | Data Type                                                                    | Description |
| ------------------ | ---- | ---------- | ---------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| creation_time      | core | timestamp  | The time stamp for when an annotation store version was created.             |
| description        | core | string     | The description for an annotation store version.                             |
| id                 | core | string     | The annotation store version ID.                                             |
| name               | core | string     | The name of the annotation store.                                            |
| status             | core | string     | The status of an annotation store version.                                   |
| status_message     | core | string     | The status of an annotation store version.                                   |
| store_id           | core | string     | The store ID for annotation store version.                                   |
| tags               | core | hstore_csv |
| update_time        | core | timestamp  | The time stamp for when an annotation store version was updated.             |
| version_arn        | core | string     | The Arn for the annotation store.                                            |
| version_name       | core | string     | The name given to an annotation store version to distinguish it from others. |
| version_options    | core | json       | The options for an annotation store version.                                 |
| version_size_bytes | core | int64      | The size of the annotation store version in Bytes.                           |
