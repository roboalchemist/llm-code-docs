# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_addon_instance.dataset.md

---
title: SES Addon Instance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Addon Instance
---

# SES Addon Instance

This table represents the SES Addon Instance resource from Amazon Web Services.

```
aws.ses_addon_instance
```

## Fields

| Title                 | ID   | Type       | Data Type                                              | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------ | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| addon_instance_arn    | core | string     | The Amazon Resource Name (ARN) of the Add On instance. |
| addon_instance_id     | core | string     | The unique ID of the Add On instance.                  |
| addon_name            | core | string     | The name of the Add On for the instance.               |
| addon_subscription_id | core | string     | The subscription ID for the instance.                  |
| created_timestamp     | core | timestamp  | The timestamp of when the Add On instance was created. |
| tags                  | core | hstore_csv |
