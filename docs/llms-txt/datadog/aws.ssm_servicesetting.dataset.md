# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ssm_servicesetting.dataset.md

---
title: Systems Manager Service Setting
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Systems Manager Service Setting
---

# Systems Manager Service Setting

This table represents the Systems Manager Service Setting resource from Amazon Web Services.

```
aws.ssm_servicesetting
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ------------------ | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| arn                | core | string     | The ARN of the service setting.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| last_modified_date | core | timestamp  | The last time the service setting was modified.                                                                                                                                                                                                                                                                                                                                                                                                 |
| last_modified_user | core | string     | The ARN of the last modified user. This field is populated only if the setting value was overwritten.                                                                                                                                                                                                                                                                                                                                           |
| setting_id         | core | string     | The ID of the service setting.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| setting_value      | core | string     | The value of the service setting.                                                                                                                                                                                                                                                                                                                                                                                                               |
| status             | core | string     | The status of the service setting. The value can be Default, Customized or PendingUpdate. <ul> <li> Default: The current setting uses a default value provisioned by the Amazon Web Services service team. </li> <li> Customized: The current setting use a custom value specified by the customer. </li> <li> PendingUpdate: The current setting uses a default or custom value, but a setting change request is pending approval. </li> </ul> |
| tags               | core | hstore_csv |
