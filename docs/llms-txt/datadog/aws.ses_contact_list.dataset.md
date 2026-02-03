# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_contact_list.dataset.md

---
title: SES Contact List
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Contact List
---

# SES Contact List

This table represents the SES Contact List resource from Amazon Web Services.

```
aws.ses_contact_list
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                  | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------ | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| contact_list_name      | core | string     | The name of the contact list.                                                              |
| created_timestamp      | core | timestamp  | A timestamp noting when the contact list was created.                                      |
| description            | core | string     | A description of what the contact list is about.                                           |
| last_updated_timestamp | core | timestamp  | A timestamp noting the last time the contact list was updated.                             |
| tags                   | core | hstore_csv |
| topics                 | core | json       | An interest group, theme, or label within a list. A contact list can have multiple topics. |
