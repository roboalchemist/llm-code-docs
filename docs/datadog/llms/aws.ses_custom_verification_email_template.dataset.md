# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_custom_verification_email_template.dataset.md

---
title: SES Custom Verification Email Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > SES Custom Verification Email
  Template
---

# SES Custom Verification Email Template

An SES Custom Verification Email Template in AWS is a reusable template that defines the content and layout of custom verification emails sent through Amazon Simple Email Service. It allows you to personalize the subject line, sender information, and message body when requesting email address verification, providing a branded and consistent experience for recipients.

```
aws.ses_custom_verification_email_template
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                           | Description |
| ----------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| failure_redirection_url | core | string     | The URL that the recipient of the verification email is sent to if his or her address is not successfully verified. |
| from_email_address      | core | string     | The email address that the custom verification email is sent from.                                                  |
| success_redirection_url | core | string     | The URL that the recipient of the verification email is sent to if his or her address is successfully verified.     |
| tags                    | core | hstore_csv |
| template_content        | core | string     | The content of the custom verification email.                                                                       |
| template_name           | core | string     | The name of the custom verification email template.                                                                 |
| template_subject        | core | string     | The subject line of the custom verification email.                                                                  |
