# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.codeartifact_package_group.dataset.md

---
title: CodeArtifact Package Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > CodeArtifact Package Group
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.codeartifact_package_group.dataset/index.html
---

# CodeArtifact Package Group

An AWS CodeArtifact Package Group is a logical grouping of related packages within a CodeArtifact domain. It helps organize and manage multiple packages under a single group, making it easier to apply consistent access controls, policies, and workflows. This allows teams to streamline dependency management and maintain better structure across their software artifacts.

```
aws.codeartifact_package_group
```

## Fields

| Title                | ID   | Type      | Data Type                                                                                                                  | Description |
| -------------------- | ---- | --------- | -------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string    |
| account_id           | core | string    |
| arn                  | core | string    | The ARN of the package group.                                                                                              |
| contact_info         | core | string    | The contact information of the package group.                                                                              |
| created_time         | core | timestamp | A timestamp that represents the date and time the package group was created.                                               |
| description          | core | string    | The description of the package group.                                                                                      |
| domain_name          | core | string    | The name of the domain that contains the package group.                                                                    |
| domain_owner         | core | string    | The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces. |
| origin_configuration | core | json      | The package group origin configuration that determines how package versions can enter repositories.                        |
| parent               | core | json      | The direct parent package group of the package group.                                                                      |
| pattern              | core | string    | The pattern of the package group. The pattern determines which packages are associated with the package group.             |
| tags                 | core | hstore    |
