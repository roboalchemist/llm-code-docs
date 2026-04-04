# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_dataset_group.dataset.md

---
title: Personalize Dataset Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Dataset Group
---

# Personalize Dataset Group

An Amazon Personalize Dataset Group is a container that holds related datasets for building and managing personalized recommendation models. It organizes datasets such as interactions, items, and users, enabling you to train, evaluate, and deploy recommendation solutions within a single logical grouping.

```
aws.personalize_dataset_group
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                         | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| creation_date_time     | core | timestamp  | The creation date and time (in Unix time) of the dataset group.                                                                                                                                   |
| dataset_group_arn      | core | string     | The Amazon Resource Name (ARN) of the dataset group.                                                                                                                                              |
| domain                 | core | string     | The domain of a Domain dataset group.                                                                                                                                                             |
| failure_reason         | core | string     | If creating a dataset group fails, provides the reason why.                                                                                                                                       |
| kms_key_arn            | core | string     | The Amazon Resource Name (ARN) of the Key Management Service (KMS) key used to encrypt the datasets.                                                                                              |
| last_updated_date_time | core | timestamp  | The last update date and time (in Unix time) of the dataset group.                                                                                                                                |
| name                   | core | string     | The name of the dataset group.                                                                                                                                                                    |
| role_arn               | core | string     | The ARN of the Identity and Access Management (IAM) role that has permissions to access the Key Management Service (KMS) key. Supplying an IAM role is only valid when also specifying a KMS key. |
| status                 | core | string     | The current status of the dataset group. A dataset group can be in one of the following states: CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED DELETE PENDING                    |
| tags                   | core | hstore_csv |
