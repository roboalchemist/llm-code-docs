# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_thing.dataset.md

---
title: IoT Thing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Thing
source_url: https://docs.datadoghq.com/data_directory/aws/aws.iot_thing.dataset/index.html
---

# IoT Thing

An IoT Thing in AWS represents a digital identity for a physical device within AWS IoT Core. It allows you to manage, monitor, and interact with connected devices by defining attributes, metadata, and configurations. This resource is central to organizing devices, enabling secure communication, and integrating with IoT rules and policies.

```
aws.iot_thing
```

## Fields

| Title              | ID   | Type   | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| ------------------ | ---- | ------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key               | core | string |
| account_id         | core | string |
| attributes         | core | hstore | The thing attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| billing_group_name | core | string | The name of the billing group the thing belongs to.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| default_client_id  | core | string | The default MQTT client ID. For a typical device, the thing name is also used as the default MQTT client ID. Although we don't require a mapping between a thing's registry name and its use of MQTT client IDs, certificates, or shadow state, we recommend that you choose a thing name and use it as the MQTT client ID for the registry and the Device Shadow service. This lets you better organize your IoT fleet without removing the flexibility of the underlying device certificate model or shadows. |
| tags               | core | hstore |
| thing_arn          | core | string | The ARN of the thing to describe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| thing_id           | core | string | The ID of the thing to describe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| thing_name         | core | string | The name of the thing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| thing_type_name    | core | string | The thing type name.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| version            | core | int64  | The current version of the thing record in the registry. To avoid unintentional changes to the information in the registry, you can pass the version information in the expectedVersion parameter of the UpdateThing and DeleteThing calls.                                                                                                                                                                                                                                                                     |
