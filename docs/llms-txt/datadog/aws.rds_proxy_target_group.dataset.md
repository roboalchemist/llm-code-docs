# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rds_proxy_target_group.dataset.md

---
title: RDS Proxy Target Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > RDS Proxy Target Group
---

# RDS Proxy Target Group

This table represents the RDS Proxy Target Group resource from Amazon Web Services.

```
aws.rds_proxy_target_group
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                       | Description |
| ---------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| connection_pool_config | core | json       | The settings that determine the size and behavior of the connection pool for the target group.                                                                                                                                                                  |
| created_date           | core | timestamp  | The date and time when the target group was first created.                                                                                                                                                                                                      |
| db_proxy_name          | core | string     | The identifier for the RDS proxy associated with this target group.                                                                                                                                                                                             |
| is_default             | core | bool       | Indicates whether this target group is the first one used for connection requests by the associated proxy. Because each proxy is currently associated with a single target group, currently this setting is always <code>true</code>.                           |
| status                 | core | string     | The current status of this target group. A status of <code>available</code> means the target group is correctly associated with a database. Other values indicate that you must wait for the target group to be ready, or take some action to resolve an issue. |
| tags                   | core | hstore_csv |
| target_group_arn       | core | string     | The Amazon Resource Name (ARN) representing the target group.                                                                                                                                                                                                   |
| target_group_name      | core | string     | The identifier for the target group. This name must be unique for all target groups owned by your Amazon Web Services account in the specified Amazon Web Services Region.                                                                                      |
| targets                | core | json       | An arbitrary number of <code>DBProxyTarget</code> objects, containing details of the corresponding targets.                                                                                                                                                     |
| updated_date           | core | timestamp  | The date and time when the target group was last updated.                                                                                                                                                                                                       |
