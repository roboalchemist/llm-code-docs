# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.qbusiness_subscription.dataset.md

---
title: Q Business Subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Q Business Subscription
---

# Q Business Subscription

Q Business Subscription in AWS represents a subscription resource for Amazon Q Business, a managed generative AI service designed to provide business-focused conversational experiences. This resource tracks subscription details, enabling organizations to manage access, usage, and billing for Q Business features. It helps businesses integrate AI-driven assistants into workflows while maintaining control over service entitlements and configurations.

```
aws.qbusiness_subscription
```

## Fields

| Title                | ID   | Type       | Data Type                                                                                                                                        | Description |
| -------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| current_subscription | core | json       | The type of your current Amazon Q Business subscription.                                                                                         |
| next_subscription    | core | json       | The type of the Amazon Q Business subscription for the next month.                                                                               |
| principal            | core | json       | The IAM Identity Center UserId or GroupId of a user or group in the IAM Identity Center instance connected to the Amazon Q Business application. |
| subscription_arn     | core | string     | The Amazon Resource Name (ARN) of the Amazon Q Business subscription that was updated.                                                           |
| subscription_id      | core | string     | The identifier of the Amazon Q Business subscription to be updated.                                                                              |
| tags                 | core | hstore_csv |
