# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.eks_eks_anywhere_subscription.dataset.md

---
title: EKS EKS Anywhere Subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > EKS EKS Anywhere Subscription
---

# EKS EKS Anywhere Subscription

This table represents the EKS EKS Anywhere Subscription resource from Amazon Web Services.

```
aws.eks_eks_anywhere_subscription
```

## Fields

| Title            | ID   | Type          | Data Type                                                                                                                                                                | Description |
| ---------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key             | core | string        |
| account_id       | core | string        |
| arn              | core | string        | The Amazon Resource Name (ARN) for the subscription.                                                                                                                     |
| auto_renew       | core | bool          | A boolean indicating whether or not a subscription will auto renew when it expires.                                                                                      |
| created_at       | core | timestamp     | The Unix timestamp in seconds for when the subscription was created.                                                                                                     |
| effective_date   | core | timestamp     | The Unix timestamp in seconds for when the subscription is effective.                                                                                                    |
| expiration_date  | core | timestamp     | The Unix timestamp in seconds for when the subscription will expire or auto renew, depending on the auto renew configuration of the subscription object.                 |
| id               | core | string        | UUID identifying a subscription.                                                                                                                                         |
| license_arns     | core | array<string> | Amazon Web Services License Manager ARN associated with the subscription.                                                                                                |
| license_quantity | core | int64         | The number of licenses included in a subscription. Valid values are between 1 and 100.                                                                                   |
| license_type     | core | string        | The type of licenses included in the subscription. Valid value is CLUSTER. With the CLUSTER license type, each license covers support for a single EKS Anywhere cluster. |
| licenses         | core | json          | Includes all of the claims in the license token necessary to validate the license for extended support.                                                                  |
| status           | core | string        | The status of a subscription.                                                                                                                                            |
| tags             | core | hstore_csv    |
| term             | core | json          | An EksAnywhereSubscriptionTerm object.                                                                                                                                   |
