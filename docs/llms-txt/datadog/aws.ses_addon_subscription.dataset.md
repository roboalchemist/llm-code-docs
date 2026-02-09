# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_addon_subscription.dataset.md

---
title: SES Addon Subscription
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Addon Subscription
---

# SES Addon Subscription

This table represents the SES Addon Subscription resource from Amazon Web Services.

```
aws.ses_addon_subscription
```

## Fields

| Title                  | ID   | Type       | Data Type                                                  | Description |
| ---------------------- | ---- | ---------- | ---------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| addon_name             | core | string     | The name of the Add On.                                    |
| addon_subscription_arn | core | string     | The Amazon Resource Name (ARN) of the Add On subscription. |
| addon_subscription_id  | core | string     | The unique ID of the Add On subscription.                  |
| created_timestamp      | core | timestamp  | The timestamp of when the Add On subscription was created. |
| tags                   | core | hstore_csv |
