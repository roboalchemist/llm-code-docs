# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.quicksight_account.dataset.md

---
title: QuickSight Account
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > QuickSight Account
---

# QuickSight Account

This table represents the QuickSight Account resource from Amazon Web Services.

```
aws.quicksight_account
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Description |
| ---------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| account_settings | core | json       | The Amazon QuickSight settings for this Amazon Web Services account. This information includes the edition of Amazon Amazon QuickSight that you subscribed to (Standard or Enterprise) and the notification email for the Amazon QuickSight subscription. In the QuickSight console, the Amazon QuickSight subscription is sometimes referred to as a QuickSight "account" even though it's technically not an account by itself. Instead, it's a subscription to the Amazon QuickSight service for your Amazon Web Services account. The edition that you subscribe to applies to Amazon QuickSight in every Amazon Web Services Region where you use it. |
| request_id       | core | string     | The Amazon Web Services request ID for this operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| status           | core | int64      | The HTTP status of the request.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| tags             | core | hstore_csv |
