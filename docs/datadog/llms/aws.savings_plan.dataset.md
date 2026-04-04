# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.savings_plan.dataset.md

---
title: Savings Plan
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Savings Plan
---

# Savings Plan

This table represents the Savings Plan resource from Amazon Web Services.

```
aws.savings_plan
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                  | Description |
| ------------------------ | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| account_id               | core | string        |
| commitment               | core | string        | The hourly commitment amount in the specified currency.                                                                                                    |
| currency                 | core | string        | The currency.                                                                                                                                              |
| description              | core | string        | The description.                                                                                                                                           |
| ec2_instance_family      | core | string        | The EC2 instance family.                                                                                                                                   |
| end                      | core | string        | The end time.                                                                                                                                              |
| offering_id              | core | string        | The ID of the offering.                                                                                                                                    |
| payment_option           | core | string        | The payment option.                                                                                                                                        |
| product_types            | core | array<string> | The product types.                                                                                                                                         |
| recurring_payment_amount | core | string        | The recurring payment amount.                                                                                                                              |
| region                   | core | string        | The Amazon Web Services Region.                                                                                                                            |
| returnable_until         | core | string        | The time until when a return for the Savings Plan can be requested. If the Savings Plan is not returnable, the field reflects the Savings Plan start time. |
| savings_plan_arn         | core | string        | The Amazon Resource Name (ARN) of the Savings Plan.                                                                                                        |
| savings_plan_id          | core | string        | The ID of the Savings Plan.                                                                                                                                |
| savings_plan_type        | core | string        | The plan type.                                                                                                                                             |
| start                    | core | string        | The start time.                                                                                                                                            |
| state                    | core | string        | The current state.                                                                                                                                         |
| tags                     | core | hstore_csv    |
| term_duration_in_seconds | core | int64         | The duration of the term, in seconds.                                                                                                                      |
| upfront_payment_amount   | core | string        | The up-front payment amount.                                                                                                                               |
