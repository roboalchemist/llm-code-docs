# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.sns_platform_application.dataset.md

---
title: SNS Platform Application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SNS Platform Application
---

# SNS Platform Application

An SNS Platform Application in AWS represents a mobile app that can send push notifications through Amazon Simple Notification Service. It acts as a container for credentials and settings required to connect with push notification services like APNs, FCM, or ADM. By creating a platform application, you can register device endpoints and deliver messages directly to mobile devices.

```
aws.sns_platform_application
```

## Fields

| Title                    | ID   | Type       | Data Type                                               | Description |
| ------------------------ | ---- | ---------- | ------------------------------------------------------- | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| attributes               | core | hstore     | Attributes for platform application object.             |
| platform_application_arn | core | string     | PlatformApplicationArn for platform application object. |
| tags                     | core | hstore_csv |
