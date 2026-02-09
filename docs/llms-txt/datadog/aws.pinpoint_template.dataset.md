# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.pinpoint_template.dataset.md

---
title: Pinpoint Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Pinpoint Template
---

# Pinpoint Template

An AWS Pinpoint Template is a reusable message configuration that defines the content and settings for communications such as email, SMS, or push notifications. It allows you to standardize messaging across campaigns, ensuring consistency and saving time by avoiding repetitive setup. Templates can include personalization features, making it easier to deliver targeted and engaging messages to users.

```
aws.pinpoint_template
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                             | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| arn                   | core | string     | The Amazon Resource Name (ARN) of the message template. This value isn't included in a TemplateResponse object. To retrieve the ARN of a template, use the GetEmailTemplate, GetPushTemplate, GetSmsTemplate, or GetVoiceTemplate operation, depending on the type of template that you want to retrieve the ARN for.                                                                 |
| creation_date         | core | string     | The date, in ISO 8601 format, when the message template was created.                                                                                                                                                                                                                                                                                                                  |
| default_substitutions | core | string     | The JSON object that specifies the default values that are used for message variables in the message template. This object isn't included in a TemplateResponse object. To retrieve this object for a template, use the GetEmailTemplate, GetPushTemplate, GetSmsTemplate, or GetVoiceTemplate operation, depending on the type of template that you want to retrieve the object for. |
| last_modified_date    | core | string     | The date, in ISO 8601 format, when the message template was last modified.                                                                                                                                                                                                                                                                                                            |
| tags                  | core | hstore_csv |
| template_description  | core | string     | The custom description of the message template. This value isn't included in a TemplateResponse object. To retrieve the description of a template, use the GetEmailTemplate, GetPushTemplate, GetSmsTemplate, or GetVoiceTemplate operation, depending on the type of template that you want to retrieve the description for.                                                         |
| template_name         | core | string     | The name of the message template.                                                                                                                                                                                                                                                                                                                                                     |
| template_type         | core | string     | The type of channel that the message template is designed for. Possible values are: EMAIL, PUSH, SMS, INAPP, and VOICE.                                                                                                                                                                                                                                                               |
| version               | core | string     | The unique identifier, as an integer, for the active version of the message template.                                                                                                                                                                                                                                                                                                 |
