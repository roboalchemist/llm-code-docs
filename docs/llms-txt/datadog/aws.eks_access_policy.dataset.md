# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eks_access_policy.dataset.md

---
title: EKS Access Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EKS Access Policy
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.eks_access_policy.dataset/index.html
---

# EKS Access Policy

This table represents the EKS Access Policy resource from Amazon Web Services.

```
aws.eks_access_policy
```

## Fields

| Title         | ID   | Type      | Data Type                                                                                        | Description |
| ------------- | ---- | --------- | ------------------------------------------------------------------------------------------------ | ----------- |
| _key          | core | string    |
| access_scope  | core | json      | The scope of the access policy.                                                                  |
| account_id    | core | string    |
| associated_at | core | timestamp | The date and time the <code>AccessPolicy</code> was associated with an <code>AccessEntry</code>. |
| modified_at   | core | timestamp | The Unix epoch timestamp for the last modification to the object.                                |
| policy_arn    | core | string    | The ARN of the <code>AccessPolicy</code>.                                                        |
| tags          | core | hstore    |
