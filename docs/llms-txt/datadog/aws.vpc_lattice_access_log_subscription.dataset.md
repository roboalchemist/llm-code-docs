# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.vpc_lattice_access_log_subscription.dataset.md

---
title: VPC Lattice Access Log Subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > VPC Lattice Access Log Subscription
---

# VPC Lattice Access Log Subscription

This table represents the VPC Lattice Access Log Subscription resource from Amazon Web Services.

```
aws.vpc_lattice_access_log_subscription
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                | Description |
| ------------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| arn                      | core | string     | The Amazon Resource Name (ARN) of the access log subscription                            |
| created_at               | core | timestamp  | The date and time that the access log subscription was created, in ISO-8601 format.      |
| destination_arn          | core | string     | The Amazon Resource Name (ARN) of the destination.                                       |
| id                       | core | string     | The ID of the access log subscription.                                                   |
| last_updated_at          | core | timestamp  | The date and time that the access log subscription was last updated, in ISO-8601 format. |
| resource_arn             | core | string     | The Amazon Resource Name (ARN) of the service or service network.                        |
| resource_id              | core | string     | The ID of the service or service network.                                                |
| service_network_log_type | core | string     | Log type of the service network.                                                         |
| tags                     | core | hstore_csv |
