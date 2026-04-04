# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.pinpoint_channel.dataset.md

---
title: Pinpoint Channel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Pinpoint Channel
---

# Pinpoint Channel

An Amazon Pinpoint Channel represents a communication pathway that you can enable to send messages to your users, such as email, SMS, push notifications, or voice. Each channel has its own configuration settings, including credentials, permissions, and delivery options. By managing channels, you control how your application engages with customers across different platforms.

```
aws.pinpoint_channel
```

## Fields

| Title              | ID   | Type       | Data Type                                                                                              | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| application_id     | core | string     | The unique identifier for the application.                                                             |
| creation_date      | core | string     | The date and time, in ISO 8601 format, when the channel was enabled.                                   |
| enabled            | core | bool       | Specifies whether the channel is enabled for the application.                                          |
| has_credential     | core | bool       | (Not used) This property is retained only for backward compatibility.                                  |
| id                 | core | string     | (Deprecated) An identifier for the channel. This property is retained only for backward compatibility. |
| is_archived        | core | bool       | Specifies whether the channel is archived.                                                             |
| last_modified_by   | core | string     | The user who last modified the channel.                                                                |
| last_modified_date | core | string     | The date and time, in ISO 8601 format, when the channel was last modified.                             |
| tags               | core | hstore_csv |
| version            | core | int64      | The current version of the channel.                                                                    |
