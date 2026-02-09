# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.macie2_settings.dataset.md

---
title: Macie Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Macie Settings
---

# Macie Settings

This table represents the Macie Settings resource from Amazon Web Services.

```
aws.macie2_settings
```

## Fields

| Title                        | ID   | Type       | Data Type                                                                                                                                                                                                                                                       | Description |
| ---------------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string     |
| account_id                   | core | string     |
| created_at                   | core | timestamp  | The date and time, in UTC and extended ISO 8601 format, when the Amazon Macie account was created.                                                                                                                                                              |
| finding_publishing_frequency | core | string     | The frequency with which Amazon Macie publishes updates to policy findings for the account. This includes publishing updates to Security Hub and Amazon EventBridge (formerly Amazon CloudWatch Events).                                                        |
| service_role                 | core | string     | The Amazon Resource Name (ARN) of the service-linked role that allows Amazon Macie to monitor and analyze data in Amazon Web Services resources for the account.                                                                                                |
| status                       | core | string     | The current status of the Amazon Macie account. Possible values are: PAUSED, the account is enabled but all Macie activities are suspended (paused) for the account; and, ENABLED, the account is enabled and all Macie activities are enabled for the account. |
| tags                         | core | hstore_csv |
| updated_at                   | core | timestamp  | The date and time, in UTC and extended ISO 8601 format, of the most recent change to the status or configuration settings for the Amazon Macie account.                                                                                                         |
