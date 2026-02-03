# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.networkmanager_connect_peer.dataset.md

---
title: Network Manager Connect Peer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Manager Connect Peer
---

# Network Manager Connect Peer

Network Manager Connect Peer in AWS represents the configuration details of a peer connection within AWS Network Manager. It provides information about the connection between a core network and an external peer, such as edge devices or third-party networks. This resource helps manage and monitor connectivity, routing, and status of peer links to ensure secure and reliable communication across distributed networks.

```
aws.networkmanager_connect_peer
```

## Fields

| Title                    | ID   | Type       | Data Type                                                                                  | Description |
| ------------------------ | ---- | ---------- | ------------------------------------------------------------------------------------------ | ----------- |
| _key                     | core | string     |
| account_id               | core | string     |
| configuration            | core | json       | The configuration of the Connect peer.                                                     |
| connect_attachment_id    | core | string     | The ID of the attachment to connect.                                                       |
| connect_peer_id          | core | string     | The ID of the Connect peer.                                                                |
| core_network_id          | core | string     | The ID of a core network.                                                                  |
| created_at               | core | timestamp  | The timestamp when the Connect peer was created.                                           |
| edge_location            | core | string     | The Connect peer Regions where edges are located.                                          |
| last_modification_errors | core | json       | Describes the error associated with the attachment request.                                |
| state                    | core | string     | The state of the Connect peer.                                                             |
| subnet_arn               | core | string     | The subnet ARN for the Connect peer. This only applies only when the protocol is NO_ENCAP. |
| tags                     | core | hstore_csv |
