# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codeartifact_repository.dataset.md

---
title: CodeArtifact Repository
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeArtifact Repository
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.codeartifact_repository.dataset/index.html
---

# CodeArtifact Repository

An AWS CodeArtifact Repository is a fully managed artifact storage and sharing service that makes it easy to securely store, publish, and share software packages used in application development. It supports common package formats like npm, Maven, PyPI, and NuGet, and integrates with build and deployment tools. The repository helps teams centralize dependencies, control access with AWS IAM, and automatically fetch packages from public repositories while caching them for faster, more reliable builds.

```
aws.codeartifact_repository
```

## Fields

| Title                 | ID   | Type      | Data Type                                                                                                                                                                                                                                                                   | Description |
| --------------------- | ---- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string    |
| account_id            | core | string    |
| administrator_account | core | string    | The 12-digit account number of the Amazon Web Services account that manages the repository.                                                                                                                                                                                 |
| arn                   | core | string    | The Amazon Resource Name (ARN) of the repository.                                                                                                                                                                                                                           |
| created_time          | core | timestamp | A timestamp that represents the date and time the repository was created.                                                                                                                                                                                                   |
| description           | core | string    | A text description of the repository.                                                                                                                                                                                                                                       |
| domain_name           | core | string    | The name of the domain that contains the repository.                                                                                                                                                                                                                        |
| domain_owner          | core | string    | The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces.                                                                                                                     |
| external_connections  | core | json      | An array of external connections associated with the repository.                                                                                                                                                                                                            |
| name                  | core | string    | The name of the repository.                                                                                                                                                                                                                                                 |
| tags                  | core | hstore    |
| upstreams             | core | json      | A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when CodeArtifact looks for a requested package version. For more information, see Working with upstream repositories. |
