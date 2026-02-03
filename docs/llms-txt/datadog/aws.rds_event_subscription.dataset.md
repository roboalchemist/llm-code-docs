# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_event_subscription.dataset.md

---
title: RDS Event Subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Event Subscription
---

# RDS Event Subscription

An RDS Event Subscription in AWS allows you to receive notifications about specific events related to your RDS resources, such as database instance changes, security group modifications, or backup completions. You can configure subscriptions to send alerts through Amazon SNS, enabling real-time monitoring and faster response to operational changes or issues.

```
aws.rds_event_subscription
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                          | Description |
| -------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string        |
| account_id                 | core | string        |
| cust_subscription_id       | core | string        | The RDS event notification subscription Id.                                                                                                                                                                                                                                                                                                                                        |
| customer_aws_id            | core | string        | The Amazon Web Services customer account associated with the RDS event notification subscription.                                                                                                                                                                                                                                                                                  |
| enabled                    | core | bool          | Specifies whether the subscription is enabled. True indicates the subscription is enabled.                                                                                                                                                                                                                                                                                         |
| event_categories_list      | core | array<string> | A list of event categories for the RDS event notification subscription.                                                                                                                                                                                                                                                                                                            |
| event_subscription_arn     | core | string        | The Amazon Resource Name (ARN) for the event subscription.                                                                                                                                                                                                                                                                                                                         |
| sns_topic_arn              | core | string        | The topic ARN of the RDS event notification subscription.                                                                                                                                                                                                                                                                                                                          |
| source_ids_list            | core | array<string> | A list of source IDs for the RDS event notification subscription.                                                                                                                                                                                                                                                                                                                  |
| source_type                | core | string        | The source type for the RDS event notification subscription.                                                                                                                                                                                                                                                                                                                       |
| status                     | core | string        | The status of the RDS event notification subscription. Constraints: Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist The status "no-permission" indicates that RDS no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created. |
| subscription_creation_time | core | string        | The time the RDS event notification subscription was created.                                                                                                                                                                                                                                                                                                                      |
| tags                       | core | hstore_csv    |
