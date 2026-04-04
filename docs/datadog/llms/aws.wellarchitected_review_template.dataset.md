# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.wellarchitected_review_template.dataset.md

---
title: AWS Well-Architected Review Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > AWS Well-Architected Review Template
---

# AWS Well-Architected Review Template

Provides details about an AWS Well-Architected Review Template, including its structure, metadata, and configuration. It helps users retrieve information about a specific review template used to assess workloads against AWS best practices across the Well-Architected Framework pillars.

```
aws.wellarchitected_review_template
```

## Fields

| Title               | ID   | Type          | Data Type                                                                                                                                                  | Description |
| ------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| answered            | core | int64         |
| description         | core | string        | The review template description.                                                                                                                           |
| lenses              | core | array<string> | The lenses applied to the review template.                                                                                                                 |
| notes               | core | string        | The notes associated with the workload. For a review template, these are the notes that will be associated with the workload when the template is applied. |
| owner               | core | string        | An Amazon Web Services account ID.                                                                                                                         |
| share_invitation_id | core | string        | The ID assigned to the template share invitation.                                                                                                          |
| tags                | core | hstore_csv    |
| template_arn        | core | string        | The review template ARN.                                                                                                                                   |
| template_name       | core | string        | The name of the review template.                                                                                                                           |
| unanswered          | core | int64         |
| update_status       | core | string        | The latest status of a review template.                                                                                                                    |
| updated_at          | core | timestamp     | The date and time recorded.                                                                                                                                |
