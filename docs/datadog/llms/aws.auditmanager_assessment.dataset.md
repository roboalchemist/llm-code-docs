# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.auditmanager_assessment.dataset.md

---
title: Audit Manager Assessment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Audit Manager Assessment
---

# Audit Manager Assessment

Audit Manager Assessment in AWS is a resource that represents an evaluation created within AWS Audit Manager. It helps organizations assess their compliance with regulations and industry standards by collecting evidence from AWS services and accounts. An assessment defines the scope, framework, and controls to be tested, enabling automated evidence collection and reporting. This resource provides details about the assessment, including its status, scope, and related metadata, supporting continuous compliance monitoring and audit readiness.

```
aws.auditmanager_assessment
```

## Fields

| Title      | ID   | Type       | Data Type                                                                                                                                                      | Description |
| ---------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| assessment | core | json       | An entity that defines the scope of audit evidence collected by Audit Manager. An Audit Manager assessment is an implementation of an Audit Manager framework. |
| tags       | core | hstore_csv |
| user_role  | core | json       | The wrapper that contains the Audit Manager role information of the current user. This includes the role type and IAM Amazon Resource Name (ARN).              |
