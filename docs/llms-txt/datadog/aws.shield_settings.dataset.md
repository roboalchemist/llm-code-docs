# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.shield_settings.dataset.md

---
title: Shield Protection Settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Shield Protection Settings
---

# Shield Protection Settings

Shield Protection Settings in AWS provide details about your AWS Shield Advanced subscription. It includes information on emergency contact settings for incident response, the current subscription details such as protections and features enabled, and the overall subscription state. This resource helps you manage and monitor your Shield Advanced configuration to ensure your applications are protected against DDoS attacks.

```
aws.shield_settings
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                               | Description |
| ---------------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| emergency_contact_list | core | json       | A list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support. |
| subscription           | core | json       | The Shield Advanced subscription details for an account.                                                                                                                                                                |
| subscription_state     | core | string     | The status of the subscription.                                                                                                                                                                                         |
| tags                   | core | hstore_csv |
