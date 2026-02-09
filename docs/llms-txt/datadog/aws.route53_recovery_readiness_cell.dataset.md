# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.route53_recovery_readiness_cell.dataset.md

---
title: Route 53 Recovery Readiness Cell
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Route 53 Recovery Readiness Cell
---

# Route 53 Recovery Readiness Cell

This table represents the Route 53 Recovery Readiness Cell resource from Amazon Web Services.

```
aws.route53_recovery_readiness_cell
```

## Fields

| Title                   | ID   | Type          | Data Type                                                                                                                                                         | Description |
| ----------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string        |
| account_id              | core | string        |
| cell_arn                | core | string        | The Amazon Resource Name (ARN) for the cell.                                                                                                                      |
| cell_name               | core | string        | The name of the cell.                                                                                                                                             |
| cells                   | core | array<string> | A list of cell ARNs.                                                                                                                                              |
| parent_readiness_scopes | core | array<string> | The readiness scope for the cell, which can be a cell Amazon Resource Name (ARN) or a recovery group ARN. This is a list but currently can have only one element. |
| tags                    | core | hstore_csv    |
