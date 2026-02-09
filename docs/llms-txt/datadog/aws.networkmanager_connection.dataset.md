# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.networkmanager_connection.dataset.md

---
title: Network Manager Connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Manager Connection
---

# Network Manager Connection

Network Manager Connection in AWS represents a link between two devices or sites within AWS Network Manager. It helps define and manage the connectivity between customer gateways, transit gateways, or core network edges, enabling centralized control of global network topologies. This resource is used to model and monitor the logical connections that form part of a global network managed through AWS Network Manager.

```
aws.networkmanager_connection
```

## Fields

| Title               | ID   | Type       | Data Type                                                   | Description |
| ------------------- | ---- | ---------- | ----------------------------------------------------------- | ----------- |
| _key                | core | string     |
| account_id          | core | string     |
| connected_device_id | core | string     | The ID of the second device in the connection.              |
| connected_link_id   | core | string     | The ID of the link for the second device in the connection. |
| connection_arn      | core | string     | The Amazon Resource Name (ARN) of the connection.           |
| connection_id       | core | string     | The ID of the connection.                                   |
| created_at          | core | timestamp  | The date and time that the connection was created.          |
| description         | core | string     | The description of the connection.                          |
| device_id           | core | string     | The ID of the first device in the connection.               |
| global_network_id   | core | string     | The ID of the global network.                               |
| link_id             | core | string     | The ID of the link for the first device in the connection.  |
| state               | core | string     | The state of the connection.                                |
| tags                | core | hstore_csv |
