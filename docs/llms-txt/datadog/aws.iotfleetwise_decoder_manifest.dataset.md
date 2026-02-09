# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotfleetwise_decoder_manifest.dataset.md

---
title: IoT FleetWise Decoder Manifest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT FleetWise Decoder Manifest
---

# IoT FleetWise Decoder Manifest

An IoT FleetWise Decoder Manifest in AWS defines how vehicle data signals are interpreted and translated into meaningful information. It specifies the decoding rules for raw vehicle data, such as sensor values or network messages, so that applications can understand and use the data consistently. This resource helps manage and organize decoder configurations across fleets.

```
aws.iotfleetwise_decoder_manifest
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                           | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| arn                    | core | string     | The ARN of a vehicle model (model manifest) associated with the decoder manifest.                                                                                   |
| creation_time          | core | timestamp  | The time the decoder manifest was created in seconds since epoch (January 1, 1970 at midnight UTC time).                                                            |
| description            | core | string     | A brief description of the decoder manifest.                                                                                                                        |
| last_modification_time | core | timestamp  | The time the decoder manifest was last updated in seconds since epoch (January 1, 1970 at midnight UTC time).                                                       |
| message                | core | string     | The detailed message for the decoder manifest. When a decoder manifest is in an INVALID status, the message contains detailed reason and help information.          |
| model_manifest_arn     | core | string     | The ARN of a vehicle model (model manifest) associated with the decoder manifest.                                                                                   |
| name                   | core | string     | The name of the decoder manifest.                                                                                                                                   |
| status                 | core | string     | The state of the decoder manifest. If the status is ACTIVE, the decoder manifest can't be edited. If the status is marked DRAFT, you can edit the decoder manifest. |
| tags                   | core | hstore_csv |
