# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_reserved_instance.dataset.md

---
title: RDS Reserved Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Reserved Instance
---

# RDS Reserved Instance

This table represents the RDS Reserved Instance resource from Amazon Web Services.

```
aws.rds_reserved_instance
```

## Fields

| Title                             | ID   | Type       | Data Type                                                                                                                                                                                           | Description |
| --------------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| currency_code                     | core | string     | The currency code for the reserved DB instance.                                                                                                                                                     |
| db_instance_class                 | core | string     | The DB instance class for the reserved DB instance.                                                                                                                                                 |
| db_instance_count                 | core | int64      | The number of reserved DB instances.                                                                                                                                                                |
| duration                          | core | int64      | The duration of the reservation in seconds.                                                                                                                                                         |
| fixed_price                       | core | float64    | The fixed price charged for this reserved DB instance.                                                                                                                                              |
| lease_id                          | core | string     | The unique identifier for the lease associated with the reserved DB instance. <note> Amazon Web Services Support might request the lease ID for an issue related to a reserved DB instance. </note> |
| multi_az                          | core | bool       | Indicates whether the reservation applies to Multi-AZ deployments.                                                                                                                                  |
| offering_type                     | core | string     | The offering type of this reserved DB instance.                                                                                                                                                     |
| product_description               | core | string     | The description of the reserved DB instance.                                                                                                                                                        |
| recurring_charges                 | core | json       | The recurring price charged to run this reserved DB instance.                                                                                                                                       |
| reserved_db_instance_arn          | core | string     | The Amazon Resource Name (ARN) for the reserved DB instance.                                                                                                                                        |
| reserved_db_instance_id           | core | string     | The unique identifier for the reservation.                                                                                                                                                          |
| reserved_db_instances_offering_id | core | string     | The offering identifier.                                                                                                                                                                            |
| start_time                        | core | timestamp  | The time the reservation started.                                                                                                                                                                   |
| state                             | core | string     | The state of the reserved DB instance.                                                                                                                                                              |
| tags                              | core | hstore_csv |
| usage_price                       | core | float64    | The hourly price charged for this reserved DB instance.                                                                                                                                             |
