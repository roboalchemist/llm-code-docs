# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_recovery_readiness_readiness_check.dataset.md

---
title: Route 53 Recovery Readiness Readiness Check
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Route 53 Recovery Readiness
  Readiness Check
---

# Route 53 Recovery Readiness Readiness Check

This table represents the Route 53 Recovery Readiness Readiness Check resource from Amazon Web Services.

```
aws.route53_recovery_readiness_readiness_check
```

## Fields

| Title                | ID   | Type       | Data Type                                                         | Description |
| -------------------- | ---- | ---------- | ----------------------------------------------------------------- | ----------- |
| _key                 | core | string     |
| account_id           | core | string     |
| readiness_check_arn  | core | string     | The Amazon Resource Name (ARN) associated with a readiness check. |
| readiness_check_name | core | string     | Name of a readiness check.                                        |
| resource_set         | core | string     | Name of the resource set to be checked.                           |
| tags                 | core | hstore_csv |
