# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.sql_server.dataset.md

---
title: SQL Server
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > SQL Server
---

# SQL Server

This table represents the SQL Server resource from Microsoft Azure.

```
azure.sql_server
```

## Fields

| Title                              | ID   | Type       | Data Type                                                                                                                             | Description |
| ---------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                               | core | string     |
| active_directory_administrators    | core | json       |
| administrator_login                | core | string     | Administrator username for the server. Once created it cannot be changed.                                                             |
| administrator_login_password       | core | string     | The administrator login password (required for server creation).                                                                      |
| administrators                     | core | json       | The Azure Active Directory identity of the server.                                                                                    |
| advanced_threat_protection_setting | core | json       |
| alert_policies                     | core | json       |
| audit_setting                      | core | json       |
| encryption_protector               | core | json       |
| firewall_rules                     | core | json       |
| fully_qualified_domain_name        | core | string     | The fully qualified domain name of the server.                                                                                        |
| id                                 | core | string     | Resource ID.                                                                                                                          |
| identity                           | core | json       | The Azure Active Directory identity of the server.                                                                                    |
| key_id                             | core | string     | A CMK URI of the key to use for encryption.                                                                                           |
| kind                               | core | string     | Kind of sql server. This is metadata used for the Azure portal experience.                                                            |
| location                           | core | string     | Resource location.                                                                                                                    |
| minimal_tls_version                | core | string     | Minimal TLS version. Allowed values: '1.0', '1.1', '1.2'                                                                              |
| name                               | core | string     | Resource name.                                                                                                                        |
| primary_user_assigned_identity_id  | core | string     | The resource id of a user assigned identity to be used by default.                                                                    |
| private_endpoint_connections       | core | json       | List of private endpoint connections on a server                                                                                      |
| public_network_access              | core | string     | Whether or not public endpoint access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled' |
| resource_group                     | core | string     |
| state                              | core | string     | The state of the server.                                                                                                              |
| subscription_id                    | core | string     |
| subscription_name                  | core | string     |
| tags                               | core | hstore_csv |
| type                               | core | string     | Resource type.                                                                                                                        |
| version                            | core | string     | The version of the server.                                                                                                            |
| vulnerability_assessments          | core | json       |
| workspace_feature                  | core | string     | Whether or not existing server has a workspace created and if it allows connection from workspace                                     |
