# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iam_group.dataset.md

---
title: IAM Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IAM Group
---

# IAM Group

An IAM Group in AWS is a collection of IAM users that simplifies permission management. Instead of assigning policies to individual users, you can attach policies to the group, and all members inherit those permissions. This makes it easier to manage access control for teams of users with similar roles.

```
aws.iam_group
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                        | Description |
| ----------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| arn               | core | string     | The Amazon Resource Name (ARN) specifying the group. For more information about ARNs and how to use them in policies, see IAM identifiers in the IAM User Guide. |
| attached_policies | core | json       | A list of the attached policies.                                                                                                                                 |
| create_date       | core | timestamp  | The date and time, in ISO 8601 date-time format, when the group was created.                                                                                     |
| group_id          | core | string     | The stable and unique string identifying the group. For more information about IDs, see IAM identifiers in the IAM User Guide.                                   |
| group_name        | core | string     | The friendly name that identifies the group.                                                                                                                     |
| path              | core | string     | The path to the group. For more information about paths, see IAM identifiers in the IAM User Guide.                                                              |
| tags              | core | hstore_csv |
