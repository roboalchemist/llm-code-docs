# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotevents_detector_model.dataset.md

---
title: IoT Events Detector Model
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Events Detector Model
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iotevents_detector_model.dataset/index.html
---

# IoT Events Detector Model

AWS IoT Events Detector Model is a resource that defines how IoT devices and systems detect and respond to specific events. It allows you to model input signals, set conditions, and trigger actions such as alerts or device updates when certain patterns occur. This helps automate responses to real-time events across IoT applications.

```
aws.iotevents_detector_model
```

## Fields

| Title                        | ID   | Type   | Data Type                                         | Description |
| ---------------------------- | ---- | ------ | ------------------------------------------------- | ----------- |
| _key                         | core | string |
| account_id                   | core | string |
| detector_model_configuration | core | json   | Information about how the detector is configured. |
| detector_model_definition    | core | json   | Information that defines how a detector operates. |
| tags                         | core | hstore |
