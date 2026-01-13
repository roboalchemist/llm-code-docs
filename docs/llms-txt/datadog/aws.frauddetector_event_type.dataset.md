# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_event_type.dataset.md

---
title: Fraud Detector Event Type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector Event Type
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.frauddetector_event_type.dataset/index.html
---

# Fraud Detector Event Type

Fraud Detector Event Type in AWS defines the structure of events that you want to evaluate for potential fraud. It specifies the variables, entity types, and labels associated with an event, such as a transaction or account registration. By creating an event type, you provide the foundation for building fraud detection models and rules that analyze incoming data to identify suspicious activity.

```
aws.frauddetector_event_type
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                                                                                                                                                  | Description |
| ------------------------- | ---- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| account_id                | core | string        |
| arn                       | core | string        | The entity type ARN.                                                                                                                                                                                                                                                       |
| created_time              | core | string        | Timestamp of when the event type was created.                                                                                                                                                                                                                              |
| description               | core | string        | The event type description.                                                                                                                                                                                                                                                |
| entity_types              | core | array<string> | The event type entity types.                                                                                                                                                                                                                                               |
| event_ingestion           | core | string        | If Enabled, Amazon Fraud Detector stores event data when you generate a prediction and uses that data to update calculated variables in near real-time. Amazon Fraud Detector uses this data, known as INGESTED_EVENTS, to train your model and improve fraud predictions. |
| event_orchestration       | core | json          | The event orchestration status.                                                                                                                                                                                                                                            |
| event_variables           | core | array<string> | The event type event variables.                                                                                                                                                                                                                                            |
| ingested_event_statistics | core | json          | Data about the stored events.                                                                                                                                                                                                                                              |
| labels                    | core | array<string> | The event type labels.                                                                                                                                                                                                                                                     |
| last_updated_time         | core | string        | Timestamp of when the event type was last updated.                                                                                                                                                                                                                         |
| name                      | core | string        | The event type name.                                                                                                                                                                                                                                                       |
| tags                      | core | hstore        |
