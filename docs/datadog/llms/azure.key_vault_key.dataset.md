# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/azure/azure.key_vault_key.dataset.md

---
title: Key Vault Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Key Vault Key
---

# Key Vault Key

This table represents the Key Vault Key resource from Microsoft Azure.

```
azure.key_vault_key
```

## Fields

| Title                | ID   | Type          | Data Type                                                           | Description |
| -------------------- | ---- | ------------- | ------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| attributes           | core | json          | The attributes of the key.                                          |
| curve_name           | core | string        | The elliptic curve name. For valid values, see JsonWebKeyCurveName. |
| id                   | core | string        | Fully qualified identifier of the key vault resource.               |
| key_ops              | core | array<string> |
| key_size             | core | int64         | The key size in bits. For example: 2048, 3072, or 4096 for RSA.     |
| key_uri              | core | string        | The URI to retrieve the current version of the key.                 |
| key_uri_with_version | core | string        | The URI to retrieve the specific version of the key.                |
| kty                  | core | string        | The type of the key. For valid values, see JsonWebKeyType.          |
| location             | core | string        | Azure location of the key vault resource.                           |
| name                 | core | string        | Name of the key vault resource.                                     |
| resource_group       | core | string        |
| subscription_id      | core | string        |
| subscription_name    | core | string        |
| tags                 | core | hstore_csv    |
| type                 | core | string        | Resource type of the key vault resource.                            |
