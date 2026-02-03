# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iotwireless_multicast_group.dataset.md

---
title: IoT Wireless Multicast Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > IoT Wireless Multicast Group
---

# IoT Wireless Multicast Group

An IoT Wireless Multicast Group in AWS enables sending messages to multiple wireless devices simultaneously using LoRaWAN networks. It simplifies communication by grouping devices together, allowing efficient data distribution without sending individual messages to each device. This helps reduce network traffic and improves scalability for IoT applications.

```
aws.iotwireless_multicast_group
```

## Fields

| Title       | ID   | Type       | Data Type                                                                                | Description |
| ----------- | ---- | ---------- | ---------------------------------------------------------------------------------------- | ----------- |
| _key        | core | string     |
| account_id  | core | string     |
| arn         | core | string     | The arn of the multicast group.                                                          |
| created_at  | core | timestamp  | Created at timestamp for the resource.                                                   |
| description | core | string     | The description of the new resource.                                                     |
| id          | core | string     | The ID of the multicast group.                                                           |
| lo_ra_wan   | core | json       | The LoRaWAN information that is to be returned from getting multicast group information. |
| name        | core | string     | The name of the multicast group.                                                         |
| status      | core | string     | The status of the multicast group.                                                       |
| tags        | core | hstore_csv |
