# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotwireless_device_profile.dataset.md

---
title: IoT Wireless Device Profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Wireless Device Profile
---

# IoT Wireless Device Profile

An IoT Wireless Device Profile in AWS defines configuration settings for wireless devices that connect through AWS IoT Core for LoRaWAN. It specifies parameters such as supported data rates, regional frequency settings, and other technical details that determine how a device communicates within the network. This profile helps standardize device behavior and ensures compatibility with the LoRaWAN network server, simplifying device onboarding and management.

```
aws.iotwireless_device_profile
```

## Fields

| Title      | ID   | Type       | Data Type                                                        | Description |
| ---------- | ---- | ---------- | ---------------------------------------------------------------- | ----------- |
| _key       | core | string     |
| account_id | core | string     |
| arn        | core | string     | The Amazon Resource Name of the resource.                        |
| id         | core | string     | The ID of the device profile.                                    |
| lo_ra_wan  | core | json       | Information about the device profile.                            |
| name       | core | string     | The name of the resource.                                        |
| sidewalk   | core | json       | Information about the Sidewalk parameters in the device profile. |
| tags       | core | hstore_csv |
