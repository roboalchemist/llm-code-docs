# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.socialmessaging_waba.dataset.md

---
title: Social Messaging Waba
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Social Messaging Waba
---

# Social Messaging Waba

This table represents the Social Messaging Waba resource from Amazon Web Services.

```
aws.socialmessaging_waba
```

## Fields

| Title               | ID   | Type       | Data Type                                                                                                        | Description |
| ------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| arn                 | core | string     | The ARN of the linked WhatsApp Business Account.                                                                 |
| event_destinations  | core | json       | The event destinations for the linked WhatsApp Business Account.                                                 |
| id                  | core | string     | The ID of the linked WhatsApp Business Account, formatted as <code>waba-01234567890123456789012345678901</code>. |
| link_date           | core | timestamp  | The date the WhatsApp Business Account was linked.                                                               |
| phone_numbers       | core | json       | The phone numbers associated with the Linked WhatsApp Business Account.                                          |
| registration_status | core | string     | The registration status of the linked WhatsApp Business Account.                                                 |
| tags                | core | hstore_csv |
| waba_id             | core | string     | The WhatsApp Business Account ID from meta.                                                                      |
| waba_name           | core | string     | The name of the linked WhatsApp Business Account.                                                                |
