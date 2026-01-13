# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codeartifact_domain.dataset.md

---
title: CodeArtifact Domain
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeArtifact Domain
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.codeartifact_domain.dataset/index.html
---

# CodeArtifact Domain

CodeArtifact Domain in AWS is a top-level container for storing and managing package repositories. It allows you to group multiple repositories under a single domain, enabling centralized access control, efficient package sharing, and version management across teams and projects. Domains help reduce duplication by allowing repositories to reuse packages stored in the same domain.

```
aws.codeartifact_domain
```

## Fields

| Title            | ID   | Type      | Data Type                                                                                                  | Description |
| ---------------- | ---- | --------- | ---------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string    |
| account_id       | core | string    |
| arn              | core | string    | The Amazon Resource Name (ARN) of the domain.                                                              |
| asset_size_bytes | core | int64     | The total size of all assets in the domain.                                                                |
| created_time     | core | timestamp | A timestamp that represents the date and time the domain was created.                                      |
| name             | core | string    | The name of the domain.                                                                                    |
| owner            | core | string    | The Amazon Web Services account ID that owns the domain.                                                   |
| repository_count | core | int64     | The number of repositories in the domain.                                                                  |
| s3_bucket_arn    | core | string    | The Amazon Resource Name (ARN) of the Amazon S3 bucket that is used to store package assets in the domain. |
| status           | core | string    | The current status of a domain.                                                                            |
| tags             | core | hstore    |
