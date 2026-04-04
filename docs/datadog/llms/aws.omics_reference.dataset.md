# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.omics_reference.dataset.md

---
title: AWS HealthOmics Reference Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS HealthOmics Reference Store
---

# AWS HealthOmics Reference Store

AWS HealthOmics Reference Store is a managed service that allows users to store, manage, and share reference genomic data used in bioinformatics workflows. It provides a secure and scalable repository for reference files such as genome assemblies and annotation data, enabling consistent and efficient access across analysis pipelines.

```
aws.omics_reference
```

## Fields

| Title              | ID   | Type       | Data Type                       | Description |
| ------------------ | ---- | ---------- | ------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The reference's ARN.            |
| creation_time      | core | timestamp  | When the reference was created. |
| description        | core | string     | The reference's description.    |
| id                 | core | string     | The reference's ID.             |
| md5                | core | string     | The reference's MD5 checksum.   |
| name               | core | string     | The reference's name.           |
| reference_store_id | core | string     | The reference's store ID.       |
| status             | core | string     | The reference's status.         |
| tags               | core | hstore_csv |
| update_time        | core | timestamp  | When the reference was updated. |
