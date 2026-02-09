# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_service_setting.dataset.md

---
title: Systems Manager Service Setting
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Systems Manager Service Setting
---

# Systems Manager Service Setting

Systems Manager Service Setting is an AWS resource that lets you configure global settings for AWS Systems Manager. These settings control how Systems Manager features behave across your account, such as enabling or disabling specific capabilities. It provides centralized management of service-level configurations without needing to adjust individual resources.

```
aws.ssm_service_setting
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                           | Description |
| ------------------ | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The ARN of the service setting.                                                                                                                                                                                                                                                                                                                                                                     |
| last_modified_date | core | timestamp  | The last time the service setting was modified.                                                                                                                                                                                                                                                                                                                                                     |
| last_modified_user | core | string     | The ARN of the last modified user. This field is populated only if the setting value was overwritten.                                                                                                                                                                                                                                                                                               |
| setting_id         | core | string     | The ID of the service setting.                                                                                                                                                                                                                                                                                                                                                                      |
| setting_value      | core | string     | The value of the service setting.                                                                                                                                                                                                                                                                                                                                                                   |
| status             | core | string     | The status of the service setting. The value can be Default, Customized or PendingUpdate. Default: The current setting uses a default value provisioned by the Amazon Web Services service team. Customized: The current setting use a custom value specified by the customer. PendingUpdate: The current setting uses a default or custom value, but a setting change request is pending approval. |
| tags               | core | hstore_csv |
