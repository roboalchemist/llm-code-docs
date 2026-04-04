# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.billingconductor_pricingplan.dataset.md

---
title: Billingconductor Pricingplan
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Billingconductor Pricingplan
---

# Billingconductor Pricingplan

This table represents the billingconductor_pricingplan resource from Amazon Web Services.

```
aws.billingconductor_pricingplan
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                           | Description |
| ------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The pricing plan Amazon Resource Names (ARN). This can be used to uniquely identify a pricing plan. |
| creation_time      | core | int64      | The time when the pricing plan was created.                                                         |
| description        | core | string     | The pricing plan description.                                                                       |
| last_modified_time | core | int64      | The most recent time when the pricing plan was modified.                                            |
| name               | core | string     | The name of a pricing plan.                                                                         |
| size               | core | int64      | The pricing rules count that's currently associated with this pricing plan list element.            |
| tags               | core | hstore_csv |
