# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.smsvoice_sender_id.dataset.md

---
title: Pinpoint SMS and Voice Sender ID
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Pinpoint SMS and Voice Sender ID
---

# Pinpoint SMS and Voice Sender ID

Pinpoint SMS and Voice Sender ID in AWS represents information about a sender ID used for sending SMS messages. A sender ID is the name or number that appears as the message sender on a recipient's device. This resource provides details such as the sender ID string, its registration status, and the countries where it is supported. It helps manage compliance and branding for SMS campaigns by ensuring messages are delivered with a recognizable and approved sender identity.

```
aws.smsvoice_sender_id
```

## Fields

| Title                       | ID   | Type          | Data Type                                                                                                                                                                 | Description |
| --------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                        | core | string        |
| account_id                  | core | string        |
| deletion_protection_enabled | core | bool          | By default this is set to false. When set to true the sender ID can't be deleted.                                                                                         |
| iso_country_code            | core | string        | The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.                                                                                          |
| message_types               | core | array<string> | The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that aren't critical or time-sensitive. |
| monthly_leasing_price       | core | string        | The monthly leasing price, in US dollars.                                                                                                                                 |
| registered                  | core | bool          | True if the sender ID is registered.                                                                                                                                      |
| registration_id             | core | string        | The unique identifier for the registration.                                                                                                                               |
| sender_id                   | core | string        | The alphanumeric sender ID in a specific country that you'd like to describe.                                                                                             |
| sender_id_arn               | core | string        | The Amazon Resource Name (ARN) associated with the SenderId.                                                                                                              |
| tags                        | core | hstore_csv    |
