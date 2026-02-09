# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.license_manager_license.dataset.md

---
title: License Manager License
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > License Manager License
---

# License Manager License

This table represents the license_manager_license resource from Amazon Web Services.

```
aws.license_manager_license
```

## Fields

| Title                     | ID   | Type       | Data Type                                                                     | Description |
| ------------------------- | ---- | ---------- | ----------------------------------------------------------------------------- | ----------- |
| _key                      | core | string     |
| account_id                | core | string     |
| beneficiary               | core | string     | License beneficiary.                                                          |
| consumption_configuration | core | json       | Configuration for consumption of the license.                                 |
| create_time               | core | string     | License creation time.                                                        |
| entitlements              | core | json       | License entitlements.                                                         |
| home_region               | core | string     | Home Region of the license.                                                   |
| issuer                    | core | json       | License issuer.                                                               |
| license_arn               | core | string     | Amazon Resource Name (ARN) of the license.                                    |
| license_metadata          | core | json       | License metadata.                                                             |
| license_name              | core | string     | License name.                                                                 |
| product_name              | core | string     | Product name.                                                                 |
| product_sku               | core | string     | Product SKU.                                                                  |
| status                    | core | string     | License status.                                                               |
| tags                      | core | hstore_csv |
| validity                  | core | json       | Date and time range during which the license is valid, in ISO8601-UTC format. |
| version                   | core | string     | License version.                                                              |
