# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.cleanrooms_collaboration.dataset.md

---
title: AWS Clean Rooms Collaboration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS Clean Rooms Collaboration
---

# AWS Clean Rooms Collaboration

AWS Clean Rooms Collaboration is a resource that represents a secure data collaboration environment within AWS Clean Rooms. It allows multiple parties to analyze and query their combined datasets without sharing or revealing raw data. This resource provides details about the collaboration, including participants, configurations, and access controls, enabling privacy-preserving analytics across organizations.

```
aws.cleanrooms_collaboration
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                                                                                                                                                                                              | Description |
| ------------------------ | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| analytics_engine         | core | string     | The analytics engine for the collaboration. After July 16, 2025, the CLEAN_ROOMS_SQL parameter will no longer be available.                                                                                                                                            |
| arn                      | core | string     | The unique ARN for the collaboration.                                                                                                                                                                                                                                  |
| create_time              | core | timestamp  | The time when the collaboration was created.                                                                                                                                                                                                                           |
| creator_account_id       | core | string     | The identifier used to reference members of the collaboration. Currently only supports Amazon Web Services account ID.                                                                                                                                                 |
| creator_display_name     | core | string     | A display name of the collaboration creator.                                                                                                                                                                                                                           |
| data_encryption_metadata | core | json       | The settings for client-side encryption for cryptographic computing.                                                                                                                                                                                                   |
| description              | core | string     | A description of the collaboration provided by the collaboration owner.                                                                                                                                                                                                |
| id                       | core | string     | The unique ID for the collaboration.                                                                                                                                                                                                                                   |
| job_log_status           | core | string     | An indicator as to whether job logging has been enabled or disabled for the collaboration. When ENABLED, Clean Rooms logs details about jobs run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is DISABLED.      |
| member_status            | core | string     | The status of a member in a collaboration.                                                                                                                                                                                                                             |
| membership_arn           | core | string     | The unique ARN for your membership within the collaboration.                                                                                                                                                                                                           |
| membership_id            | core | string     | The unique ID for your membership within the collaboration.                                                                                                                                                                                                            |
| name                     | core | string     | A human-readable identifier provided by the collaboration owner. Display names are not unique.                                                                                                                                                                         |
| query_log_status         | core | string     | An indicator as to whether query logging has been enabled or disabled for the collaboration. When ENABLED, Clean Rooms logs details about queries run within this collaboration and those logs can be viewed in Amazon CloudWatch Logs. The default value is DISABLED. |
| tags                     | core | hstore_csv |
| update_time              | core | timestamp  | The time the collaboration metadata was last updated.                                                                                                                                                                                                                  |
