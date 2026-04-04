# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_lineage_group.dataset.md

---
title: SageMaker Lineage Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Lineage Group
---

# SageMaker Lineage Group

SageMaker Lineage Group is an Amazon SageMaker resource that organizes and tracks related machine learning entities such as datasets, models, and experiments. It provides a way to group lineage information, making it easier to trace the origin, relationships, and dependencies of ML artifacts throughout their lifecycle. This helps with reproducibility, auditing, and compliance.

```
aws.sagemaker_lineage_group
```

## Fields

| Title              | ID   | Type       | Data Type                                                                | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| created_by         | core | json       | Information about the user who created or modified a SageMaker resource. |
| creation_time      | core | timestamp  | The creation time of lineage group.                                      |
| description        | core | string     | The description of the lineage group.                                    |
| last_modified_by   | core | json       | Information about the user who created or modified a SageMaker resource. |
| last_modified_time | core | timestamp  | The last modified time of the lineage group.                             |
| lineage_group_arn  | core | string     | The Amazon Resource Name (ARN) of the lineage group.                     |
| lineage_group_name | core | string     | The name of the lineage group.                                           |
| tags               | core | hstore_csv |
