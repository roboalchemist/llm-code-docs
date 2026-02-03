# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ec2_transitgatewayconnectpeer.dataset.md

---
title: Ec2 Transitgatewayconnectpeer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ec2 Transitgatewayconnectpeer
---

# Ec2 Transitgatewayconnectpeer

This table represents the ec2_transitgatewayconnectpeer resource from Amazon Web Services.

```
aws.ec2_transitgatewayconnectpeer
```

## Fields

| Title                           | ID   | Type       | Data Type                         | Description |
| ------------------------------- | ---- | ---------- | --------------------------------- | ----------- |
| _key                            | core | string     |
| account_id                      | core | string     |
| connect_peer_configuration      | core | json       | The Connect peer details.         |
| creation_time                   | core | timestamp  | The creation time.                |
| state                           | core | string     | The state of the Connect peer.    |
| tags                            | core | hstore_csv |
| transit_gateway_attachment_id   | core | string     | The ID of the Connect attachment. |
| transit_gateway_connect_peer_id | core | string     | The ID of the Connect peer.       |
