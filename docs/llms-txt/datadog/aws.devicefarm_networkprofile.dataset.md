# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.devicefarm_networkprofile.dataset.md

---
title: Devicefarm Networkprofile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Devicefarm Networkprofile
---

# Devicefarm Networkprofile

This table represents the devicefarm_networkprofile resource from Amazon Web Services.

```
aws.devicefarm_networkprofile
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                     | Description |
| ----------------------- | ---- | ---------- | --------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| arn                     | core | string     | The Amazon Resource Name (ARN) of the network profile.                                        |
| description             | core | string     | The description of the network profile.                                                       |
| downlink_bandwidth_bits | core | int64      | The data throughput rate in bits per second, as an integer from 0 to 104857600.               |
| downlink_delay_ms       | core | int64      | Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.       |
| downlink_jitter_ms      | core | int64      | Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000. |
| downlink_loss_percent   | core | int64      | Proportion of received packets that fail to arrive from 0 to 100 percent.                     |
| name                    | core | string     | The name of the network profile.                                                              |
| tags                    | core | hstore_csv |
| type                    | core | string     | The type of network profile. Valid values are listed here.                                    |
| uplink_bandwidth_bits   | core | int64      | The data throughput rate in bits per second, as an integer from 0 to 104857600.               |
| uplink_delay_ms         | core | int64      | Delay time for all packets to destination in milliseconds as an integer from 0 to 2000.       |
| uplink_jitter_ms        | core | int64      | Time variation in the delay of received packets in milliseconds as an integer from 0 to 2000. |
| uplink_loss_percent     | core | int64      | Proportion of transmitted packets that fail to arrive from 0 to 100 percent.                  |
