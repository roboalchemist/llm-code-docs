# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_endpoint_connection_notification.dataset.md

---
title: VPC Endpoint Connection Notification
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Endpoint Connection Notification
---

# VPC Endpoint Connection Notification

This table represents the VPC Endpoint Connection Notification resource from Amazon Web Services.

```
aws.vpc_endpoint_connection_notification
```

## Fields

| Title                                | ID   | Type          | Data Type                                                                                                                                  | Description |
| ------------------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                                 | core | string        |
| account_id                           | core | string        |
| connection_events                    | core | array<string> | The events for the notification. Valid values are <code>Accept</code>, <code>Connect</code>, <code>Delete</code>, and <code>Reject</code>. |
| connection_notification_arn          | core | string        | The ARN of the SNS topic for the notification.                                                                                             |
| connection_notification_id           | core | string        | The ID of the notification.                                                                                                                |
| connection_notification_state        | core | string        | The state of the notification.                                                                                                             |
| connection_notification_type         | core | string        | The type of notification.                                                                                                                  |
| endpoint_connection_notification_arn | core | string        |
| service_id                           | core | string        | The ID of the endpoint service.                                                                                                            |
| service_region                       | core | string        | The Region for the endpoint service.                                                                                                       |
| tags                                 | core | hstore_csv    |
| vpc_endpoint_id                      | core | string        | The ID of the VPC endpoint.                                                                                                                |
