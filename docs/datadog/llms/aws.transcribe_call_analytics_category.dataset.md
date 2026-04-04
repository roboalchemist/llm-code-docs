# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.transcribe_call_analytics_category.dataset.md

---
title: Transcribe Call Analytics Category
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Transcribe Call Analytics Category
---

# Transcribe Call Analytics Category

This table represents the Transcribe Call Analytics Category resource from Amazon Web Services.

```
aws.transcribe_call_analytics_category
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                                                                                                                                                                  | Description |
| ---------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| category_name    | core | string     | The name of the Call Analytics category. Category names are case sensitive and must be unique within an Amazon Web Services account.                                                                                                                       |
| create_time      | core | timestamp  | The date and time the specified Call Analytics category was created. Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-04T12:32:58.761000-07:00</code> represents 12:32 PM UTC-7 on May 4, 2022.      |
| input_type       | core | string     | The input type associated with the specified category. <code>POST_CALL</code> refers to a category that is applied to batch transcriptions; <code>REAL_TIME</code> refers to a category that is applied to streaming transcriptions.                       |
| last_update_time | core | timestamp  | The date and time the specified Call Analytics category was last updated. Timestamps are in the format <code>YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC</code>. For example, <code>2022-05-05T12:45:32.691000-07:00</code> represents 12:45 PM UTC-7 on May 5, 2022. |
| rules            | core | json       | The rules used to define a Call Analytics category. Each category can have between 1 and 20 rules.                                                                                                                                                         |
| tags             | core | hstore_csv |
