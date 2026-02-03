# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.proton_repository.dataset.md

---
title: Proton Repository
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Proton Repository
---

# Proton Repository

An AWS Proton Repository represents a registered source code repository, such as one in AWS CodeCommit, GitHub, or Bitbucket, that Proton can use to store and manage infrastructure and service templates. It allows Proton to pull template files directly from version-controlled repositories, enabling automated deployments and consistent environment provisioning.

```
aws.proton_repository
```

## Fields

| Title          | ID   | Type       | Data Type                                                                                                                | Description |
| -------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key           | core | string     |
| account_id     | core | string     |
| arn            | core | string     | The Amazon Resource Name (ARN) of the linked repository.                                                                 |
| connection_arn | core | string     | The Amazon Resource Name (ARN) of your AWS CodeStar connection that connects Proton to your repository provider account. |
| name           | core | string     | The repository name.                                                                                                     |
| provider       | core | string     | The repository provider.                                                                                                 |
| tags           | core | hstore_csv |
