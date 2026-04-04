# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_thingtype.dataset.md

---
title: Iot Thingtype
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iot Thingtype
---

# Iot Thingtype

This table represents the iot_thingtype resource from Amazon Web Services.

```
aws.iot_thingtype
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                                                                                                                                                          | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                  | core | string     |
| account_id            | core | string     |
| tags                  | core | hstore_csv |
| thing_type_arn        | core | string     | The thing type ARN.                                                                                                                                                                                                |
| thing_type_id         | core | string     | The thing type ID.                                                                                                                                                                                                 |
| thing_type_metadata   | core | json       | The ThingTypeMetadata contains additional information about the thing type including: creation date and time, a value indicating whether the thing type is deprecated, and a date and time when it was deprecated. |
| thing_type_name       | core | string     | The name of the thing type.                                                                                                                                                                                        |
| thing_type_properties | core | json       | The ThingTypeProperties contains information about the thing type including description, a list of searchable thing attribute names, and MQTT5 configuration.                                                      |
