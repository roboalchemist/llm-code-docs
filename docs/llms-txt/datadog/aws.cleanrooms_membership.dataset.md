# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cleanrooms_membership.dataset.md

---
title: AWS Clean Rooms Membership
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS Clean Rooms Membership
---

# AWS Clean Rooms Membership

AWS Clean Rooms Membership represents a participant's association within an AWS Clean Rooms collaboration. It contains details about the member account, collaboration identifiers, membership status, and configuration settings that define how data is accessed and used securely. This resource enables organizations to collaborate on shared datasets without exposing underlying raw data, ensuring privacy and compliance while allowing joint analysis.

```
aws.cleanrooms_membership
```

## Fields

| Title                              | ID   | Type          | Data Type                                                                                                                                                                                                                                                           | Description |
| ---------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string        |
| account_id                         | core | string        |
| arn                                | core | string        | The unique ARN for the membership.                                                                                                                                                                                                                                  |
| collaboration_arn                  | core | string        | The unique ARN for the membership's associated collaboration.                                                                                                                                                                                                       |
| collaboration_creator_account_id   | core | string        | The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.                                                                                                                                              |
| collaboration_creator_display_name | core | string        | The display name of the collaboration creator.                                                                                                                                                                                                                      |
| collaboration_id                   | core | string        | The unique ID for the membership's collaboration.                                                                                                                                                                                                                   |
| collaboration_name                 | core | string        | The name of the membership's collaboration.                                                                                                                                                                                                                         |
| create_time                        | core | timestamp     | The time when the membership was created.                                                                                                                                                                                                                           |
| default_job_result_configuration   | core | json          | The default job result configuration for the membership.                                                                                                                                                                                                            |
| default_result_configuration       | core | json          | The default protected query result configuration as specified by the member who can receive results.                                                                                                                                                                |
| id                                 | core | string        | The unique ID of the membership.                                                                                                                                                                                                                                    |
| job_log_status                     | core | string        | An indicator as to whether job logging has been enabled or disabled for the collaboration. When ENABLED, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is DISABLED.   |
| member_abilities                   | core | array<string> | The abilities granted to the collaboration member.                                                                                                                                                                                                                  |
| ml_member_abilities                | core | json          | Specifies the ML member abilities that are granted to a collaboration member.                                                                                                                                                                                       |
| payment_configuration              | core | json          | The payment responsibilities accepted by the collaboration member.                                                                                                                                                                                                  |
| query_log_status                   | core | string        | An indicator as to whether query logging has been enabled or disabled for the membership. When ENABLED, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is DISABLED. |
| status                             | core | string        | The status of the membership.                                                                                                                                                                                                                                       |
| tags                               | core | hstore_csv    |
| update_time                        | core | timestamp     | The time the membership metadata was last updated.                                                                                                                                                                                                                  |
