# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.smsvoice_configuration_set.dataset.md

---
title: Pinpoint SMS and Voice Configuration Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Pinpoint SMS and Voice Configuration
  Set
---

# Pinpoint SMS and Voice Configuration Set

A Pinpoint SMS and Voice Configuration Set in AWS is a collection of rules that define how messages are sent and tracked. It allows you to manage settings such as event destinations, message delivery options, and compliance requirements. Configuration sets help you monitor performance, control costs, and ensure consistent behavior across your SMS and voice messaging campaigns.

```
aws.smsvoice_configuration_set
```

## Fields

| Title                            | ID   | Type       | Data Type                                                                                                                                                                 | Description |
| -------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string     |
| account_id                       | core | string     |
| configuration_set_arn            | core | string     | The Resource Name (ARN) of the ConfigurationSet.                                                                                                                          |
| configuration_set_name           | core | string     | The name of the ConfigurationSet.                                                                                                                                         |
| created_timestamp                | core | timestamp  | The time when the ConfigurationSet was created, in UNIX epoch time format.                                                                                                |
| default_message_feedback_enabled | core | bool       | True if message feedback is enabled.                                                                                                                                      |
| default_message_type             | core | string     | The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive. |
| default_sender_id                | core | string     | The default sender ID used by the ConfigurationSet.                                                                                                                       |
| event_destinations               | core | json       | An array of EventDestination objects that describe any events to log and where to log them.                                                                               |
| protect_configuration_id         | core | string     | The unique identifier for the protect configuration.                                                                                                                      |
| tags                             | core | hstore_csv |
