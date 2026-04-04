# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_event_tracker.dataset.md

---
title: Personalize Event Tracker
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Event Tracker
---

# Personalize Event Tracker

Personalize Event Tracker in AWS is a resource that captures real-time user interaction events, such as clicks or views, and sends them to Amazon Personalize. These events are used to train and update recommendation models, enabling more accurate and personalized recommendations. It provides an event tracker ID and an endpoint for recording events.

```
aws.personalize_event_tracker
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                    | Description |
| ---------------------- | ---- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     | The Amazon Web Services account that owns the event tracker.                                                                                                                                 |
| creation_date_time     | core | timestamp  | The date and time (in Unix format) that the event tracker was created.                                                                                                                       |
| dataset_group_arn      | core | string     | The Amazon Resource Name (ARN) of the dataset group that receives the event data.                                                                                                            |
| event_tracker_arn      | core | string     | The ARN of the event tracker.                                                                                                                                                                |
| last_updated_date_time | core | timestamp  | The date and time (in Unix time) that the event tracker was last updated.                                                                                                                    |
| name                   | core | string     | The name of the event tracker.                                                                                                                                                               |
| status                 | core | string     | The status of the event tracker. An event tracker can be in one of the following states: CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED DELETE PENDING > DELETE IN_PROGRESS |
| tags                   | core | hstore_csv |
| tracking_id            | core | string     | The ID of the event tracker. Include this ID in requests to the PutEvents API.                                                                                                               |
