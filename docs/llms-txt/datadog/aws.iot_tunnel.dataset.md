# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.iot_tunnel.dataset.md

---
title: Iot Tunnel
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Iot Tunnel
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.iot_tunnel.dataset/index.html
---

# Iot Tunnel

This table represents the iot_tunnel resource from Amazon Web Services.

```
aws.iot_tunnel
```

## Fields

| Title                        | ID   | Type      | Data Type                                                                                                                                                                     | Description |
| ---------------------------- | ---- | --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                         | core | string    |
| account_id                   | core | string    |
| created_at                   | core | timestamp | The time when the tunnel was created.                                                                                                                                         |
| description                  | core | string    | A description of the tunnel.                                                                                                                                                  |
| destination_config           | core | json      | The destination configuration that specifies the thing name of the destination device and a service name that the local proxy uses to connect to the destination application. |
| destination_connection_state | core | json      | The connection state of the destination application.                                                                                                                          |
| last_updated_at              | core | timestamp | The last time the tunnel was updated.                                                                                                                                         |
| source_connection_state      | core | json      | The connection state of the source application.                                                                                                                               |
| status                       | core | string    | The status of a tunnel. Valid values are: Open and Closed.                                                                                                                    |
| tags                         | core | hstore    |
| timeout_config               | core | json      | Timeout configuration for the tunnel.                                                                                                                                         |
| tunnel_arn                   | core | string    | The Amazon Resource Name (ARN) of a tunnel.                                                                                                                                   |
| tunnel_id                    | core | string    | A unique alpha-numeric ID that identifies a tunnel.                                                                                                                           |
