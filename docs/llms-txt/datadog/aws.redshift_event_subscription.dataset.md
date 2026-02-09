# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshift_event_subscription.dataset.md

---
title: Redshift Event Subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift Event Subscription
---

# Redshift Event Subscription

Redshift Event Subscription in AWS allows you to receive notifications about specific events occurring in your Amazon Redshift clusters, snapshots, security groups, or parameter groups. By creating a subscription, you can choose event categories and delivery options, such as sending notifications through Amazon SNS. This helps you stay informed about important changes, issues, or maintenance activities in your Redshift environment, enabling faster response and improved monitoring.

```
aws.redshift_event_subscription
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string        |
| account_id                      | core | string        |
| cust_subscription_id            | core | string        | The name of the Amazon Redshift event notification subscription.                                                                                                                                                                                                                                                                                                                |
| customer_aws_id                 | core | string        | The Amazon Web Services account associated with the Amazon Redshift event notification subscription.                                                                                                                                                                                                                                                                            |
| enabled                         | core | bool          | A boolean value indicating whether the subscription is enabled; true indicates that the subscription is enabled.                                                                                                                                                                                                                                                                |
| event_categories_list           | core | array<string> | The list of Amazon Redshift event categories specified in the event notification subscription. Values: Configuration, Management, Monitoring, Security, Pending                                                                                                                                                                                                                 |
| redshift_event_subscription_arn | core | string        |
| severity                        | core | string        | The event severity specified in the Amazon Redshift event notification subscription. Values: ERROR, INFO                                                                                                                                                                                                                                                                        |
| sns_topic_arn                   | core | string        | The Amazon Resource Name (ARN) of the Amazon SNS topic used by the event notification subscription.                                                                                                                                                                                                                                                                             |
| source_ids_list                 | core | array<string> | A list of the sources that publish events to the Amazon Redshift event notification subscription.                                                                                                                                                                                                                                                                               |
| source_type                     | core | string        | The source type of the events returned by the Amazon Redshift event notification, such as cluster, cluster-snapshot, cluster-parameter-group, cluster-security-group, or scheduled-action.                                                                                                                                                                                      |
| status                          | core | string        | The status of the Amazon Redshift event notification subscription. Constraints: Can be one of the following: active | no-permission | topic-not-exist The status "no-permission" indicates that Amazon Redshift no longer has permission to post to the Amazon SNS topic. The status "topic-not-exist" indicates that the topic was deleted after the subscription was created. |
| subscription_creation_time      | core | timestamp     | The date and time the Amazon Redshift event notification subscription was created.                                                                                                                                                                                                                                                                                              |
| tags                            | core | hstore_csv    |
