# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eks_fargateprofile.dataset.md

---
title: EKS Fargate Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EKS Fargate Profile
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.eks_fargateprofile.dataset/index.html
---

# EKS Fargate Profile

This table represents the EKS Fargate Profile resource from Amazon Web Services.

```
aws.eks_fargateprofile
```

## Fields

| Title                  | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                       | Description |
| ---------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string        |
| account_id             | core | string        |
| cluster_name           | core | string        | The name of your cluster.                                                                                                                                                                                                                                                                                                                       |
| created_at             | core | timestamp     | The Unix epoch timestamp at object creation.                                                                                                                                                                                                                                                                                                    |
| fargate_profile_arn    | core | string        | The full Amazon Resource Name (ARN) of the Fargate profile.                                                                                                                                                                                                                                                                                     |
| fargate_profile_name   | core | string        | The name of the Fargate profile.                                                                                                                                                                                                                                                                                                                |
| health                 | core | json          | The health status of the Fargate profile. If there are issues with your Fargate profile's health, they are listed here.                                                                                                                                                                                                                         |
| pod_execution_role_arn | core | string        | The Amazon Resource Name (ARN) of the <code>Pod</code> execution role to use for any <code>Pod</code> that matches the selectors in the Fargate profile. For more information, see <a href="https://docs.aws.amazon.com/eks/latest/userguide/pod-execution-role.html"> <code>Pod</code> execution role</a> in the <i>Amazon EKS User Guide</i>. |
| selectors              | core | json          | The selectors to match for a <code>Pod</code> to use this Fargate profile.                                                                                                                                                                                                                                                                      |
| status                 | core | string        | The current status of the Fargate profile.                                                                                                                                                                                                                                                                                                      |
| subnets                | core | array<string> | The IDs of subnets to launch a <code>Pod</code> into.                                                                                                                                                                                                                                                                                           |
| tags                   | core | hstore        |
