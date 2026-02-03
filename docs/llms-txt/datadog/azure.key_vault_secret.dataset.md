# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.key_vault_secret.dataset.md

---
title: Key Vault Secret
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Key Vault Secret
---

# Key Vault Secret

This table represents the Key Vault Secret resource from Microsoft Azure.

```
azure.key_vault_secret
```

## Fields

| Title                   | ID   | Type       | Data Type                                                                                                                                                                                                                                      | Description |
| ----------------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                    | core | string     |
| attributes              | core | json       | The attributes of the secret.                                                                                                                                                                                                                  |
| content_type            | core | string     | The content type of the secret.                                                                                                                                                                                                                |
| id                      | core | string     | Fully qualified identifier of the key vault resource.                                                                                                                                                                                          |
| location                | core | string     | Azure location of the key vault resource.                                                                                                                                                                                                      |
| name                    | core | string     | Name of the key vault resource.                                                                                                                                                                                                                |
| resource_group          | core | string     |
| secret_uri              | core | string     | The URI to retrieve the current version of the secret.                                                                                                                                                                                         |
| secret_uri_with_version | core | string     | The URI to retrieve the specific version of the secret.                                                                                                                                                                                        |
| subscription_id         | core | string     |
| subscription_name       | core | string     |
| tags                    | core | hstore_csv |
| type                    | core | string     | Resource type of the key vault resource.                                                                                                                                                                                                       |
| value                   | core | string     | The value of the secret. NOTE: 'value' will never be returned from the service, as APIs using this model are is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets. |
