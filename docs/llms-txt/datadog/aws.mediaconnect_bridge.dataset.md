# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediaconnect_bridge.dataset.md

---
title: Elemental MediaConnect Bridge
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Elemental MediaConnect Bridge
---

# Elemental MediaConnect Bridge

Elemental MediaConnect Bridge in AWS is a resource that enables the transport of live video between different AWS Regions or between AWS and on-premises networks. It acts as a connection point for video workflows, allowing you to send or receive live video streams securely and with low latency. This helps broadcasters and media companies extend their video distribution, support hybrid workflows, and improve reliability by bridging video across environments.

```
aws.mediaconnect_bridge
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                             | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| bridge_arn             | core | string     | The Amazon Resource Number (ARN) of the bridge.                                                                                       |
| bridge_messages        | core | json       | Messages with details about the bridge.                                                                                               |
| bridge_state           | core | string     | The state of the bridge.                                                                                                              |
| egress_gateway_bridge  | core | json       | An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises. |
| ingress_gateway_bridge | core | json       | An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.                 |
| name                   | core | string     | The name of the bridge.                                                                                                               |
| outputs                | core | json       | The outputs on this bridge.                                                                                                           |
| placement_arn          | core | string     | The placement Amazon Resource Number (ARN) of the bridge.                                                                             |
| source_failover_config | core | json       | The settings for source failover.                                                                                                     |
| sources                | core | json       | The sources on this bridge.                                                                                                           |
| tags                   | core | hstore_csv |
