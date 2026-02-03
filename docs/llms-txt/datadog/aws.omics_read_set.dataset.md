# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.omics_read_set.dataset.md

---
title: AWS HealthOmics Read Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS HealthOmics Read Set
---

# AWS HealthOmics Read Set

An AWS HealthOmics Read Set represents a collection of genomic sequencing reads stored in AWS HealthOmics. It contains metadata and references to the raw sequencing data, enabling efficient management, retrieval, and analysis of genomic information. This resource helps researchers organize and process sequencing data for bioinformatics workflows.

```
aws.omics_read_set
```

## Fields

| Title                | ID   | Type       | Data Type                                                                               | Description |
| -------------------- | ---- | ---------- | --------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| arn                  | core | string     | The read set's ARN.                                                                     |
| creation_time        | core | timestamp  | When the read set was created.                                                          |
| creation_type        | core | string     | The creation type of the read set.                                                      |
| description          | core | string     | The read set's description.                                                             |
| etag                 | core | json       | The entity tag (ETag) is a hash of the object representing its semantic content.        |
| file_type            | core | string     | The read set's file type.                                                               |
| id                   | core | string     | The read set's ID.                                                                      |
| name                 | core | string     | The read set's name.                                                                    |
| reference_arn        | core | string     | The read set's genome reference ARN.                                                    |
| sample_id            | core | string     | The read set's sample ID.                                                               |
| sequence_information | core | json       | Details about a sequence.                                                               |
| sequence_store_id    | core | string     | The read set's sequence store ID.                                                       |
| status               | core | string     | The read set's status.                                                                  |
| status_message       | core | string     | The status for a read set. It provides more detail as to why the read set has a status. |
| subject_id           | core | string     | The read set's subject ID.                                                              |
| tags                 | core | hstore_csv |
