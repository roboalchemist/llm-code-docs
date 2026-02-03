# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotfleetwise_state_template.dataset.md

---
title: IoT FleetWise State Template
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT FleetWise State Template
---

# IoT FleetWise State Template

IoT FleetWise State Template in AWS represents the response structure for retrieving a state template. It provides details about the configuration and state management of vehicle data collection and processing within IoT FleetWise. This resource helps define how vehicle signals and data are organized, enabling consistent data handling across fleets.

```
aws.iotfleetwise_state_template
```

## Fields

| Title                     | ID   | Type          | Data Type                                                                                                                                            | Description |
| ------------------------- | ---- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                      | core | string        |
| account_id                | core | string        |
| arn                       | core | string        | The Amazon Resource Name (ARN) of the state template.                                                                                                |
| creation_time             | core | timestamp     | The time the state template was created in seconds since epoch (January 1, 1970 at midnight UTC time).                                               |
| data_extra_dimensions     | core | array<string> | A list of vehicle attributes associated with the payload published on the state template's MQTT topic. Default: An empty array                       |
| description               | core | string        | A brief description of the state template.                                                                                                           |
| id                        | core | string        | The unique ID of the state template.                                                                                                                 |
| last_modification_time    | core | timestamp     | The time the state template was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).                                          |
| metadata_extra_dimensions | core | array<string> | A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. Default: An empty array |
| name                      | core | string        | The name of the state template.                                                                                                                      |
| signal_catalog_arn        | core | string        | The ARN of the signal catalog associated with the state template.                                                                                    |
| state_template_properties | core | array<string> | A list of signals from which data is collected. The state template properties contain the fully qualified names of the signals.                      |
| tags                      | core | hstore_csv    |
