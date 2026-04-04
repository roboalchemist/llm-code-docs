# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.license_manager_license_configuration.dataset.md

---
title: License Manager License Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > License Manager License
  Configuration
---

# License Manager License Configuration

This table represents the license_manager_license_configuration resource from Amazon Web Services.

```
aws.license_manager_license_configuration
```

## Fields

| Title                           | ID   | Type          | Data Type                                                         | Description |
| ------------------------------- | ---- | ------------- | ----------------------------------------------------------------- | ----------- |
| _key                            | core | string        |
| account_id                      | core | string        |
| automated_discovery_information | core | json          | Automated discovery information.                                  |
| consumed_license_summary_list   | core | json          | Summaries for licenses consumed by various resources.             |
| consumed_licenses               | core | int64         | Number of licenses consumed.                                      |
| description                     | core | string        | Description of the license configuration.                         |
| disassociate_when_not_found     | core | bool          | When true, disassociates a resource when software is uninstalled. |
| license_configuration_arn       | core | string        | Amazon Resource Name (ARN) of the license configuration.          |
| license_configuration_id        | core | string        | Unique ID of the license configuration.                           |
| license_count                   | core | int64         | Number of licenses managed by the license configuration.          |
| license_count_hard_limit        | core | bool          | Number of available licenses as a hard limit.                     |
| license_counting_type           | core | string        | Dimension to use to track the license inventory.                  |
| license_rules                   | core | array<string> | License rules.                                                    |
| managed_resource_summary_list   | core | json          | Summaries for managed resources.                                  |
| name                            | core | string        | Name of the license configuration.                                |
| owner_account_id                | core | string        | Account ID of the license configuration's owner.                  |
| product_information_list        | core | json          | Product information.                                              |
| status                          | core | string        | Status of the license configuration.                              |
| tags                            | core | hstore_csv    |
