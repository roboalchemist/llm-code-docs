# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.dms_event_subscription.dataset.md

---
title: DMS Event Subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DMS Event Subscription
---

# DMS Event Subscription

DMS Event Subscription in AWS Database Migration Service allows you to receive notifications about important events related to your migration tasks and replication instances. By creating a subscription, you can specify which event categories to monitor and which Amazon SNS topic to use for delivering notifications. This helps you stay informed about status changes, errors, or other significant activities during database migrations.

```
aws.dms_event_subscription
```

## Fields

| Title                      | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                          | Description |
| -------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                       | core | string        |
| account_id                 | core | string        |
| cust_subscription_id       | core | string        | The DMS event notification subscription Id.                                                                                                                                                                                                                                                                                                                                        |
| customer_aws_id            | core | string        | The Amazon Web Services customer account associated with the DMS event notification subscription.                                                                                                                                                                                                                                                                                  |
| enabled                    | core | bool          | Boolean value that indicates if the event subscription is enabled.                                                                                                                                                                                                                                                                                                                 |
| event_categories_list      | core | array<string> | A lists of event categories.                                                                                                                                                                                                                                                                                                                                                       |
| sns_topic_arn              | core | string        | The topic ARN of the DMS event notification subscription.                                                                                                                                                                                                                                                                                                                          |
| source_ids_list            | core | array<string> | A list of source Ids for the event subscription.                                                                                                                                                                                                                                                                                                                                   |
| source_type                | core | string        | The type of DMS resource that generates events. Valid values: replication-instance | replication-server | security-group | replication-task                                                                                                                                                                                                                                        |
| status                     | core | string        | The status of the DMS event notification subscription. Constraints: Can be one of the following: creating | modifying | deleting | active | no-permission | topic-not-exist The status "no-permission" indicates that DMS no longer has permission to post to the SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created. |
| subscription_creation_time | core | string        | The time the DMS event notification subscription was created.                                                                                                                                                                                                                                                                                                                      |
| tags                       | core | hstore_csv    |
