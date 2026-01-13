# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.frauddetector_detector.dataset.md

---
title: Fraud Detector Detector
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Fraud Detector Detector
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.frauddetector_detector.dataset/index.html
---

# Fraud Detector Detector

Fraud Detector Detector in AWS is a resource that defines the core detection logic for identifying potentially fraudulent activities. It combines event data, rules, and machine learning models to evaluate incoming events and determine the likelihood of fraud. This resource acts as the central component in AWS Fraud Detector, enabling you to configure how events are analyzed and what outcomes or actions should be triggered when suspicious behavior is detected.

```
aws.frauddetector_detector
```

## Fields

| Title             | ID   | Type   | Data Type                                        | Description |
| ----------------- | ---- | ------ | ------------------------------------------------ | ----------- |
| _key              | core | string |
| account_id        | core | string |
| arn               | core | string | The detector ARN.                                |
| created_time      | core | string | Timestamp of when the detector was created.      |
| description       | core | string | The detector description.                        |
| detector_id       | core | string | The detector ID.                                 |
| event_type_name   | core | string | The name of the event type.                      |
| last_updated_time | core | string | Timestamp of when the detector was last updated. |
| tags              | core | hstore |
