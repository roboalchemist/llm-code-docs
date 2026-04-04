# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.blockchainnodeengine_blockchain_node.dataset.md

---
title: Blockchain Node Engine Blockchain Node
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > Blockchain Node Engine Blockchain
  Node
---

# Blockchain Node Engine Blockchain Node

Blockchain Node Engine Blockchain Node on Google Cloud is a managed service that allows you to deploy, manage, and scale dedicated blockchain nodes without handling the underlying infrastructure. It simplifies running nodes for supported blockchain networks by providing automated provisioning, monitoring, and security features, enabling developers to focus on building decentralized applications instead of node maintenance.

```
gcp.blockchainnodeengine_blockchain_node
```

## Fields

| Title                           | ID   | Type          | Data Type                                                                                                                                                                                                                                             | Description |
| ------------------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                            | core | string        |
| ancestors                       | core | array<string> |
| blockchain_type                 | core | string        | Immutable. The blockchain type of the node.                                                                                                                                                                                                           |
| connection_info                 | core | json          | Output only. The connection information used to interact with a blockchain node.                                                                                                                                                                      |
| create_time                     | core | timestamp     | Output only. The timestamp at which the blockchain node was first created.                                                                                                                                                                            |
| datadog_display_name            | core | string        |
| ethereum_details                | core | json          | Ethereum-specific blockchain node details.                                                                                                                                                                                                            |
| labels                          | core | array<string> | User-provided key-value pairs.                                                                                                                                                                                                                        |
| name                            | core | string        | Output only. The fully qualified name of the blockchain node. e.g. `projects/my-project/locations/us-central1/blockchainNodes/my-node`.                                                                                                               |
| organization_id                 | core | string        |
| parent                          | core | string        |
| private_service_connect_enabled | core | bool          | Optional. When true, the node is only accessible via Private Service Connect; no public endpoints are exposed. Otherwise, the node is only accessible via public endpoints. Warning: These nodes are deprecated, please use public endpoints instead. |
| project_id                      | core | string        |
| project_number                  | core | string        |
| region_id                       | core | string        |
| resource_name                   | core | string        |
| state                           | core | string        | Output only. A status representing the state of the node.                                                                                                                                                                                             |
| tags                            | core | hstore_csv    |
| update_time                     | core | timestamp     | Output only. The timestamp at which the blockchain node was last updated.                                                                                                                                                                             |
| zone_id                         | core | string        |
