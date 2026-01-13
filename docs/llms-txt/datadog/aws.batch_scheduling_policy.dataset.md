# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.batch_scheduling_policy.dataset.md

---
title: Batch Scheduling Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Batch Scheduling Policy
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.batch_scheduling_policy.dataset/index.html
---

# Batch Scheduling Policy

An AWS Batch Scheduling Policy defines how jobs are prioritized and ordered within a compute environment. It allows you to configure fair-share scheduling, job prioritization, and resource allocation strategies to ensure workloads are distributed efficiently. This helps balance compute usage across multiple users or teams while optimizing throughput and cost.

```
aws.batch_scheduling_policy
```

## Fields

| Title            | ID   | Type   | Data Type                                                                                                                                    | Description |
| ---------------- | ---- | ------ | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string |
| account_id       | core | string |
| arn              | core | string | The Amazon Resource Name (ARN) of the scheduling policy. An example is arn:aws:batch:us-east-1:123456789012:scheduling-policy/HighPriority . |
| fairshare_policy | core | json   | The fair-share scheduling policy details.                                                                                                    |
| name             | core | string | The name of the fair-share scheduling policy.                                                                                                |
| tags             | core | hstore |
