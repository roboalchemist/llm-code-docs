# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotwireless_service_profile.dataset.md

---
title: IoT Wireless Service Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Wireless Service Profile
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iotwireless_service_profile.dataset/index.html
---

# IoT Wireless Service Profile

An IoT Wireless Service Profile in AWS defines the LoRaWAN service settings that control how devices communicate with the network. It specifies parameters such as data rates, frequency handling, and other network behaviors that determine device connectivity and performance. This profile helps manage wireless device interactions without requiring custom configuration for each device.

```
aws.iotwireless_service_profile
```

## Fields

| Title      | ID   | Type   | Data Type                                 | Description |
| ---------- | ---- | ------ | ----------------------------------------- | ----------- |
| _key       | core | string |
| account_id | core | string |
| arn        | core | string | The Amazon Resource Name of the resource. |
| id         | core | string | The ID of the service profile.            |
| lo_ra_wan  | core | json   | Information about the service profile.    |
| name       | core | string | The name of the resource.                 |
| tags       | core | hstore |
