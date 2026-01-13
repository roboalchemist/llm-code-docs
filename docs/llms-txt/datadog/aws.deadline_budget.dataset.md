# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.deadline_budget.dataset.md

---
title: Deadline Cloud Budget
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Deadline Cloud Budget
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.deadline_budget.dataset/index.html
---

# Deadline Cloud Budget

Deadline Cloud Budget in AWS is part of the Deadline Cloud service, which manages rendering workloads in the cloud. A budget defines the spending limits and cost tracking for rendering projects, helping studios control expenses while running large-scale compute jobs. It provides visibility into usage and costs, ensuring rendering tasks stay within financial constraints.

```
aws.deadline_budget
```

## Fields

| Title                    | ID   | Type      | Data Type                                                                                                                                                                                            | Description |
| ------------------------ | ---- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string    |
| account_id               | core | string    |
| actions                  | core | json      | The budget actions for the budget.                                                                                                                                                                   |
| approximate_dollar_limit | core | float64   | The consumed usage limit for the budget.                                                                                                                                                             |
| budget_id                | core | string    | The budget ID.                                                                                                                                                                                       |
| created_at               | core | timestamp | The date and time the resource was created.                                                                                                                                                          |
| created_by               | core | string    | The user or system that created this resource.                                                                                                                                                       |
| description              | core | string    | The description of the budget. This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field. |
| queue_stopped_at         | core | timestamp | The date and time the queue stopped.                                                                                                                                                                 |
| schedule                 | core | json      | The budget schedule.                                                                                                                                                                                 |
| status                   | core | string    | The status of the budget. ACTIVEâGet a budget being evaluated. INACTIVEâGet an inactive budget. This can include expired, canceled, or deleted statuses.                                             |
| tags                     | core | hstore    |
| updated_at               | core | timestamp | The date and time the resource was updated.                                                                                                                                                          |
| updated_by               | core | string    | The user or system that updated this resource.                                                                                                                                                       |
| usage_tracking_resource  | core | json      | The resource that the budget is tracking usage for.                                                                                                                                                  |
| usages                   | core | json      | The usages of the budget.                                                                                                                                                                            |
