# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotevents_input.dataset.md

---
title: IoT Events Input
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Events Input
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iotevents_input.dataset/index.html
---

# IoT Events Input

IoT Events Input in AWS represents a data entry point for AWS IoT Events. It defines how event data from devices, applications, or other AWS services is ingested into IoT Events for analysis. Inputs can be configured to accept messages in specific formats, enabling the service to detect patterns, trigger actions, and respond to changes in IoT device behavior.

```
aws.iotevents_input
```

## Fields

| Title               | ID   | Type   | Data Type                                        | Description |
| ------------------- | ---- | ------ | ------------------------------------------------ | ----------- |
| _key                | core | string |
| account_id          | core | string |
| input_configuration | core | json   | Information about the configuration of an input. |
| input_definition    | core | json   | The definition of the input.                     |
| tags                | core | hstore |
