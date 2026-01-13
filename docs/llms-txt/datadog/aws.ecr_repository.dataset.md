# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ecr_repository.dataset.md

---
title: Elastic Container Registry Repository
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Elastic Container Registry
  Repository
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ecr_repository.dataset/index.html
---

# Elastic Container Registry Repository

An Elastic Container Registry (ECR) Repository in AWS is a managed container image storage service that allows you to securely store, manage, and retrieve Docker and OCI images. It integrates with AWS Identity and Access Management for fine-grained access control and works seamlessly with services like Amazon ECS, EKS, and AWS Lambda to simplify container-based application deployment.

```
aws.ecr_repository
```

## Fields

| Title                        | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                                                  | Description |
| ---------------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                         | core | string    |
| account_id                   | core | string    |
| created_at                   | core | timestamp | The date and time, in JavaScript date format, when the repository was created.                                                                                                                                                                                                                                                             |
| encryption_configuration     | core | json      | The encryption configuration for the repository. This determines how the contents of your repository are encrypted at rest.                                                                                                                                                                                                                |
| image_scanning_configuration | core | json      | The image scanning configuration for a repository.                                                                                                                                                                                                                                                                                         |
| image_tag_mutability         | core | string    | The tag mutability setting for the repository.                                                                                                                                                                                                                                                                                             |
| last_evaluated_at            | core | timestamp | The time stamp of the last time that the lifecycle policy was run.                                                                                                                                                                                                                                                                         |
| lifecycle_policy_text        | core | string    | The JSON lifecycle policy text.                                                                                                                                                                                                                                                                                                            |
| policies                     | core | json      |
| policy_text                  | core | string    | The JSON repository policy text associated with the repository.                                                                                                                                                                                                                                                                            |
| registry_id                  | core | string    | The Amazon Web Services account ID associated with the registry that contains the repository.                                                                                                                                                                                                                                              |
| repository_arn               | core | string    | The Amazon Resource Name (ARN) that identifies the repository. The ARN contains the arn:aws:ecr namespace, followed by the region of the repository, Amazon Web Services account ID of the repository owner, repository namespace, and repository name. For example, arn:aws:ecr:region:012345678910:repository-namespace/repository-name. |
| repository_name              | core | string    | The name of the repository.                                                                                                                                                                                                                                                                                                                |
| repository_uri               | core | string    | The URI for the repository. You can use this URI for container image push and pull operations.                                                                                                                                                                                                                                             |
| tags                         | core | hstore    |
