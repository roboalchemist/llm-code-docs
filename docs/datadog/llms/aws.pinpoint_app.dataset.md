# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.pinpoint_app.dataset.md

---
title: Pinpoint App
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Pinpoint App
---

# Pinpoint App

This table represents the pinpoint_app resource from Amazon Web Services.

```
aws.pinpoint_app
```

## Fields

| Title         | ID   | Type       | Data Type                                                                                                                        | Description |
| ------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key          | core | string     |
| account_id    | core | string     |
| arn           | core | string     | The Amazon Resource Name (ARN) of the application.                                                                               |
| creation_date | core | string     | The date and time when the Application was created.                                                                              |
| event_stream  | core | json       |
| id            | core | string     | The unique identifier for the application. This identifier is displayed as the <b>Project ID</b> on the Amazon Pinpoint console. |
| name          | core | string     | The display name of the application. This name is displayed as the <b>Project name</b> on the Amazon Pinpoint console.           |
| tags          | core | hstore_csv |
