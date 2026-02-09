# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.smsvoice_registration_attachment.dataset.md

---
title: SMS/Voice Registration Attachment
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SMS/Voice Registration Attachment
---

# SMS/Voice Registration Attachment

This table represents the SMS/Voice Registration Attachment resource from Amazon Web Services.

```
aws.smsvoice_registration_attachment
```

## Fields

| Title                          | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                               | Description |
| ------------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                           | core | string     |
| account_id                     | core | string     |
| attachment_status              | core | string     | The status of the registration attachment. <ul> <li> <code>UPLOAD_IN_PROGRESS</code> The attachment is being uploaded. </li> <li> <code>UPLOAD_COMPLETE</code> The attachment has been uploaded. </li> <li> <code>UPLOAD_FAILED</code> The attachment failed to uploaded. </li> <li> <code>DELETED</code> The attachment has been deleted.. </li> </ul> |
| attachment_upload_error_reason | core | string     | A description of why the upload didn't successfully complete.                                                                                                                                                                                                                                                                                           |
| created_timestamp              | core | timestamp  | The time when the registration attachment was created, in <a href="https://www.epochconverter.com/">UNIX epoch time</a> format.                                                                                                                                                                                                                         |
| registration_attachment_arn    | core | string     | The Amazon Resource Name (ARN) for the registration attachment.                                                                                                                                                                                                                                                                                         |
| registration_attachment_id     | core | string     | The unique identifier for the registration attachment.                                                                                                                                                                                                                                                                                                  |
| tags                           | core | hstore_csv |
