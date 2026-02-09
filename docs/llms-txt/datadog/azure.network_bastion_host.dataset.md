# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.network_bastion_host.dataset.md

---
title: Azure Bastion
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Azure Bastion
---

# Azure Bastion

Azure Bastion is a fully managed service that provides secure and seamless RDP and SSH connectivity to virtual machines directly through the Azure portal. It eliminates the need for public IP addresses on VMs, reducing exposure to threats. Azure Bastion is deployed inside a virtual network and provides browser-based access, ensuring traffic remains within the Azure network for enhanced security and simplified management.

```
azure.network_bastion_host
```

## Fields

| Title                 | ID   | Type       | Data Type                                                                | Description |
| --------------------- | ---- | ---------- | ------------------------------------------------------------------------ | ----------- |
| _key                  | core | string     |
| disable_copy_paste    | core | bool       | Enable/Disable Copy/Paste feature of the Bastion Host resource.          |
| dns_name              | core | string     | FQDN for the endpoint on which bastion host is accessible.               |
| enable_file_copy      | core | bool       | Enable/Disable File Copy feature of the Bastion Host resource.           |
| enable_ip_connect     | core | bool       | Enable/Disable IP Connect feature of the Bastion Host resource.          |
| enable_shareable_link | core | bool       | Enable/Disable Shareable Link of the Bastion Host resource.              |
| enable_tunneling      | core | bool       | Enable/Disable Tunneling feature of the Bastion Host resource.           |
| etag                  | core | string     | A unique read-only string that changes whenever the resource is updated. |
| id                    | core | string     | Resource ID.                                                             |
| ip_configurations     | core | json       | IP configuration of the Bastion Host resource.                           |
| location              | core | string     | Resource location.                                                       |
| name                  | core | string     | Resource name.                                                           |
| provisioning_state    | core | string     | The current provisioning state.                                          |
| resource_group        | core | string     |
| scale_units           | core | int64      | The scale units for the Bastion Host resource.                           |
| sku                   | core | json       | The sku of this Bastion Host.                                            |
| subscription_id       | core | string     |
| subscription_name     | core | string     |
| tags                  | core | hstore_csv |
| type                  | core | string     | Resource type.                                                           |
