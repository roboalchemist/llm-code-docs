# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.smsvoice_opt_out_list.dataset.md

---
title: Pinpoint SMS and Voice Opt-Out List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Pinpoint SMS and Voice Opt-Out List
---

# Pinpoint SMS and Voice Opt-Out List

The Pinpoint SMS and Voice Opt-Out List in AWS stores information about phone numbers that have opted out of receiving SMS messages. It helps ensure compliance with communication preferences by preventing messages from being sent to numbers that no longer wish to receive them. This resource provides details such as the opt-out list name, creation time, and associated metadata.

```
aws.smsvoice_opt_out_list
```

## Fields

| Title             | ID   | Type       | Data Type                                                            | Description |
| ----------------- | ---- | ---------- | -------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| created_timestamp | core | timestamp  | The time when the OutOutList was created, in UNIX epoch time format. |
| opt_out_list_arn  | core | string     | The Amazon Resource Name (ARN) of the OptOutList.                    |
| opt_out_list_name | core | string     | The name of the OptOutList.                                          |
| tags              | core | hstore_csv |
