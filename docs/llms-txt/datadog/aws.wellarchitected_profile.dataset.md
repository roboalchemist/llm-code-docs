# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.wellarchitected_profile.dataset.md

---
title: AWS Well-Architected Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS Well-Architected Profile
---

# AWS Well-Architected Profile

Provides details about an AWS Well-Architected Profile, which contains information on best practice guidance, review results, and improvement recommendations for workloads. It helps assess and track architecture quality across the AWS Well-Architected Framework pillars.

```
aws.wellarchitected_profile
```

## Fields

| Title               | ID   | Type       | Data Type                                | Description |
| ------------------- | ---- | ---------- | ---------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| created_at          | core | timestamp  | The date and time recorded.              |
| owner               | core | string     | An Amazon Web Services account ID.       |
| profile_arn         | core | string     | The profile ARN.                         |
| profile_description | core | string     | The profile description.                 |
| profile_name        | core | string     | The profile name.                        |
| profile_questions   | core | json       | Profile questions.                       |
| profile_version     | core | string     | The profile version.                     |
| share_invitation_id | core | string     | The ID assigned to the share invitation. |
| tags                | core | hstore_csv |
| updated_at          | core | timestamp  | The date and time recorded.              |
