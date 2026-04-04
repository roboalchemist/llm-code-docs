# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.networkmanager_core_network.dataset.md

---
title: Network Manager Core Network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Network Manager Core Network
---

# Network Manager Core Network

AWS Network Manager Core Network is a global networking resource that enables you to centrally manage, connect, and monitor your multi-region and multi-account networks. It provides a unified core network structure that simplifies building secure, scalable, and consistent connectivity across AWS and on-premises environments.

```
aws.networkmanager_core_network
```

## Fields

| Title                   | ID   | Type       | Data Type                                                         | Description |
| ----------------------- | ---- | ---------- | ----------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| account_id              | core | string     |
| core_network_arn        | core | string     | The ARN of a core network.                                        |
| core_network_id         | core | string     | The ID of a core network.                                         |
| created_at              | core | timestamp  | The timestamp when a core network was created.                    |
| description             | core | string     | The description of a core network.                                |
| edges                   | core | json       | The edges within a core network.                                  |
| global_network_id       | core | string     | The ID of the global network that your core network is a part of. |
| network_function_groups | core | json       | The network function groups associated with a core network.       |
| segments                | core | json       | The segments within a core network.                               |
| state                   | core | string     | The current state of a core network.                              |
| tags                    | core | hstore_csv |
