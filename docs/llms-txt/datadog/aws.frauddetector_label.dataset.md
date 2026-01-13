# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_label.dataset.md

---
title: Fraud Detector Label
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector Label
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.frauddetector_label.dataset/index.html
---

# Fraud Detector Label

Fraud Detector Label in AWS is a resource used to categorize outcomes for fraud detection models. Labels represent the classification of events, such as marking a transaction as fraudulent or legitimate. They are essential for training and evaluating machine learning models in Amazon Fraud Detector, helping the service learn patterns and improve accuracy in detecting suspicious activity.

```
aws.frauddetector_label
```

## Fields

| Title             | ID   | Type   | Data Type                                     | Description |
| ----------------- | ---- | ------ | --------------------------------------------- | ----------- |
| _key              | core | string |
| account_id        | core | string |
| arn               | core | string | The label ARN.                                |
| created_time      | core | string | Timestamp of when the event type was created. |
| description       | core | string | The label description.                        |
| last_updated_time | core | string | Timestamp of when the label was last updated. |
| name              | core | string | The label name.                               |
| tags              | core | hstore |
