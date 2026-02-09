# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.networkmanager_global_network.dataset.md

---
title: Global Network
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Global Network
---

# Global Network

Global Network in AWS Network Manager is a top-level resource that represents a single, private global network spanning multiple regions and accounts. It provides a central framework to manage, monitor, and visualize your global connectivity, including transit gateways, site-to-site VPNs, and on-premises locations.

```
aws.networkmanager_global_network
```

## Fields

| Title              | ID   | Type       | Data Type                                              | Description |
| ------------------ | ---- | ---------- | ------------------------------------------------------ | ----------- |
| _key               | core | string     |
| account_id         | core | string     |
| created_at         | core | timestamp  | The date and time that the global network was created. |
| description        | core | string     | The description of the global network.                 |
| global_network_arn | core | string     | The Amazon Resource Name (ARN) of the global network.  |
| global_network_id  | core | string     | The ID of the global network.                          |
| state              | core | string     | The state of the global network.                       |
| tags               | core | hstore_csv |
