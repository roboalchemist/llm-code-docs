# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.billingconductor_customlineitem.dataset.md

---
title: Billingconductor Customlineitem
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Billingconductor Customlineitem
---

# Billingconductor Customlineitem

This table represents the billingconductor_customlineitem resource from Amazon Web Services.

```
aws.billingconductor_customlineitem
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                 | Description |
| ------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The Amazon Resource Names (ARNs) for custom line items.                                                   |
| association_size   | core | int64      | The number of resources that are associated to the custom line item.                                      |
| billing_group_arn  | core | string     | The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.   |
| charge_details     | core | json       | A <code>ListCustomLineItemChargeDetails</code> that describes the charge details of a custom line item.   |
| creation_time      | core | int64      | The time created.                                                                                         |
| currency_code      | core | string     | The custom line item's charge value currency. Only one of the valid values can be used.                   |
| description        | core | string     | The custom line item's description. This is shown on the Bills page in association with the charge value. |
| last_modified_time | core | int64      | The most recent time when the custom line item was modified.                                              |
| name               | core | string     | The custom line item's name.                                                                              |
| product_code       | core | string     | The product code that's associated with the custom line item.                                             |
| tags               | core | hstore_csv |
