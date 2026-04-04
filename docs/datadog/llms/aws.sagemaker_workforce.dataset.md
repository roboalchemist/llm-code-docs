# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sagemaker_workforce.dataset.md

---
title: SageMaker Workforce
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SageMaker Workforce
---

# SageMaker Workforce

SageMaker Workforce in AWS is a managed resource that defines a group of human labelers who can perform data labeling tasks for machine learning. It allows you to set up and manage workforces from your own employees, third-party vendors, or Amazon Mechanical Turk. This resource is used to organize, secure, and monitor labeling teams for tasks such as image classification, text annotation, and other supervised learning workflows.

```
aws.sagemaker_workforce
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                                  | Description |
| -------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| cognito_config       | core | json       | The configuration of an Amazon Cognito workforce. A single Cognito workforce is created using and corresponds to a single Amazon Cognito user pool.        |
| create_date          | core | timestamp  | The date that the workforce is created.                                                                                                                    |
| failure_reason       | core | string     | The reason your workforce failed.                                                                                                                          |
| last_updated_date    | core | timestamp  | The most recent date that UpdateWorkforce was used to successfully add one or more IP address ranges (CIDRs) to a private workforce's allow list.          |
| oidc_config          | core | json       | The configuration of an OIDC Identity Provider (IdP) private workforce.                                                                                    |
| source_ip_config     | core | json       | A list of one to ten IP address ranges (CIDRs) to be added to the workforce allow list. By default, a workforce isn't restricted to specific IP addresses. |
| status               | core | string     | The status of your workforce.                                                                                                                              |
| sub_domain           | core | string     | The subdomain for your OIDC Identity Provider.                                                                                                             |
| tags                 | core | hstore_csv |
| workforce_arn        | core | string     | The Amazon Resource Name (ARN) of the private workforce.                                                                                                   |
| workforce_name       | core | string     | The name of the private workforce.                                                                                                                         |
| workforce_vpc_config | core | json       | The configuration of a VPC workforce.                                                                                                                      |
