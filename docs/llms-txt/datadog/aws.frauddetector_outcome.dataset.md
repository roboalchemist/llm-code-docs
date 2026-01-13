# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_outcome.dataset.md

---
title: Fraud Detector Outcome
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector Outcome
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.frauddetector_outcome.dataset/index.html
---

# Fraud Detector Outcome

Fraud Detector Outcome in AWS represents the result of a fraud detection evaluation. It defines the business action to take when a specific condition is met, such as approving, reviewing, or denying a transaction. Outcomes are used in rules within a detector to guide decision-making and automate responses to potential fraudulent activity.

```
aws.frauddetector_outcome
```

## Fields

| Title             | ID   | Type   | Data Type                                        | Description |
| ----------------- | ---- | ------ | ------------------------------------------------ | ----------- |
| _key              | core | string |
| account_id        | core | string |
| arn               | core | string | The outcome ARN.                                 |
| created_time      | core | string | The timestamp when the outcome was created.      |
| description       | core | string | The outcome description.                         |
| last_updated_time | core | string | The timestamp when the outcome was last updated. |
| name              | core | string | The outcome name.                                |
| tags              | core | hstore |
