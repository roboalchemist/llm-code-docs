# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_workteam.dataset.md

---
title: SageMaker Workteam
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Workteam
---

# SageMaker Workteam

SageMaker Workteam is an Amazon SageMaker resource that defines a group of people who can perform data labeling tasks for machine learning. A workteam can consist of internal employees, contractors, or members of Amazon Mechanical Turk or vendor-managed workforces. It provides a way to manage and organize human labelers, assign labeling jobs, and control access to datasets.

```
aws.sagemaker_workteam
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                             | Description |
| --------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| account_id                  | core | string        |
| create_date                 | core | timestamp     | The date and time that the work team was created (timestamp).                                                                                                                                                                                                                                                                                                                         |
| description                 | core | string        | A description of the work team.                                                                                                                                                                                                                                                                                                                                                       |
| last_updated_date           | core | timestamp     | The date and time that the work team was last updated (timestamp).                                                                                                                                                                                                                                                                                                                    |
| member_definitions          | core | json          | A list of MemberDefinition objects that contains objects that identify the workers that make up the work team. Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (IdP). For private workforces created using Amazon Cognito use CognitoMemberDefinition. For workforces created using your own OIDC identity provider (IdP) use OidcMemberDefinition. |
| notification_configuration  | core | json          | Configures SNS notifications of available or expiring work items for work teams.                                                                                                                                                                                                                                                                                                      |
| product_listing_ids         | core | array<string> | The Amazon Marketplace identifier for a vendor's work team.                                                                                                                                                                                                                                                                                                                           |
| sub_domain                  | core | string        | The URI of the labeling job's user interface. Workers open this URI to start labeling your data objects.                                                                                                                                                                                                                                                                              |
| tags                        | core | hstore_csv    |
| worker_access_configuration | core | json          | Describes any access constraints that have been defined for Amazon S3 resources.                                                                                                                                                                                                                                                                                                      |
| workforce_arn               | core | string        | The Amazon Resource Name (ARN) of the workforce.                                                                                                                                                                                                                                                                                                                                      |
| workteam_arn                | core | string        | The Amazon Resource Name (ARN) that identifies the work team.                                                                                                                                                                                                                                                                                                                         |
| workteam_name               | core | string        | The name of the work team.                                                                                                                                                                                                                                                                                                                                                            |
