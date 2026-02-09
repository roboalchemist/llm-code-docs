# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ses_template.dataset.md

---
title: SES Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SES Template
---

# SES Template

An SES Template in AWS Simple Email Service is a reusable email layout that defines the subject line, text body, and HTML body of an email. It allows you to standardize and personalize messages by inserting dynamic content at send time. Templates simplify managing consistent email formats across campaigns and notifications.

```
aws.ses_template
```

## Fields

| Title         | ID   | Type       | Data Type                                                                                                                          | Description |
| ------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| html_part     | core | string     | The HTML body of the email.                                                                                                        |
| subject_part  | core | string     | The subject line of the email.                                                                                                     |
| tags          | core | hstore_csv |
| template_name | core | string     | The name of the template. You use this name when you send email using the SendTemplatedEmail or SendBulkTemplatedEmail operations. |
| text_part     | core | string     | The email body that is visible to recipients whose email clients do not display HTML content.                                      |
