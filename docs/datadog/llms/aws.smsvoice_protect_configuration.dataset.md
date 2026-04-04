# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.smsvoice_protect_configuration.dataset.md

---
title: Pinpoint SMS and Voice V2 Protect Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Pinpoint SMS and Voice V2 Protect
  Configuration
---

# Pinpoint SMS and Voice V2 Protect Configuration

Pinpoint SMS and Voice V2 Protect Configuration in AWS defines settings that help safeguard your messaging and voice resources. It provides information about protection configurations, such as rules and controls that limit unwanted traffic, prevent abuse, and ensure compliance with communication policies. This resource is used to manage how messages and calls are filtered or restricted to maintain security and reliability.

```
aws.smsvoice_protect_configuration
```

## Fields

| Title                       | ID   | Type       | Data Type                                                                                                                                          | Description |
| --------------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string     |
| account_default             | core | bool       | This is true if the protect configuration is set as your account default protect configuration.                                                    |
| account_id                  | core | string     |
| created_timestamp           | core | timestamp  | The time when the protect configuration was created, in UNIX epoch time format.                                                                    |
| deletion_protection_enabled | core | bool       | The status of deletion protection for the protect configuration. When set to true deletion protection is enabled. By default this is set to false. |
| protect_configuration_arn   | core | string     | The Amazon Resource Name (ARN) of the protect configuration.                                                                                       |
| protect_configuration_id    | core | string     | The unique identifier for the protect configuration.                                                                                               |
| tags                        | core | hstore_csv |
