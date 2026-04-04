# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.savings_plan_rate.dataset.md

---
title: Savings Plan Rate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Savings Plan Rate
---

# Savings Plan Rate

This table represents the Savings Plan Rate resource from Amazon Web Services.

```
aws.savings_plan_rate
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                           | Description |
| --------------------- | ---- | ---------- | ----------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| currency              | core | string     | The currency.                                                                       |
| operation             | core | string     | The specific Amazon Web Services operation for the line item in the billing report. |
| product_type          | core | string     | The product type.                                                                   |
| properties            | core | json       | The properties.                                                                     |
| rate                  | core | string     | The rate.                                                                           |
| savings_plan_id       | core | string     |
| savings_plan_rate_arn | core | string     |
| service_code          | core | string     | The service.                                                                        |
| tags                  | core | hstore_csv |
| unit                  | core | string     | The unit.                                                                           |
| usage_type            | core | string     | The usage details of the line item in the billing report.                           |
