# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_model.dataset.md

---
title: Fraud Detector Model
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector Model
---

# Fraud Detector Model

Fraud Detector Model in AWS is a machine learning resource that helps identify potentially fraudulent activities in real time. It allows you to build, train, and deploy models using historical data and predefined variables without requiring deep ML expertise. The model can be integrated into applications to evaluate events such as online transactions, account registrations, or payments, providing a fraud risk score that supports automated decision-making.

```
aws.frauddetector_model
```

## Fields

| Title             | ID   | Type       | Data Type                                     | Description |
| ----------------- | ---- | ---------- | --------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| arn               | core | string     | The ARN of the model.                         |
| created_time      | core | string     | Timestamp of when the model was created.      |
| description       | core | string     | The model description.                        |
| event_type_name   | core | string     | The name of the event type.                   |
| last_updated_time | core | string     | Timestamp of last time the model was updated. |
| model_id          | core | string     | The model ID.                                 |
| model_type        | core | string     | The model type.                               |
| tags              | core | hstore_csv |
