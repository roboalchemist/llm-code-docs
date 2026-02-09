# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_recovery_readiness_recovery_group.dataset.md

---
title: Route 53 Recovery Readiness Recovery Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Route 53 Recovery Readiness Recovery
  Group
---

# Route 53 Recovery Readiness Recovery Group

This table represents the Route 53 Recovery Readiness Recovery Group resource from Amazon Web Services.

```
aws.route53_recovery_readiness_recovery_group
```

## Fields

| Title               | ID   | Type          | Data Type                                              | Description |
| ------------------- | ---- | ------------- | ------------------------------------------------------ | ----------- |
| _key                | core | string        |
| account_id          | core | string        |
| cells               | core | array<string> | A list of a cell's Amazon Resource Names (ARNs).       |
| recovery_group_arn  | core | string        | The Amazon Resource Name (ARN) for the recovery group. |
| recovery_group_name | core | string        | The name of the recovery group.                        |
| tags                | core | hstore_csv    |
