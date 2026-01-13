# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.ivs_public_key.dataset.md

---
title: Ivs Public Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Ivs Public Key
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.ivs_public_key.dataset/index.html
---

# Ivs Public Key

This table represents the ivs_public_key resource from Amazon Web Services.

```
aws.ivs_public_key
```

## Fields

| Title               | ID   | Type   | Data Type                                                                                  | Description |
| ------------------- | ---- | ------ | ------------------------------------------------------------------------------------------ | ----------- |
| _key                | core | string |
| account_id          | core | string |
| arn                 | core | string | Public key ARN.                                                                            |
| fingerprint         | core | string | The public key fingerprint, a short string used to identify or verify the full public key. |
| name                | core | string | Public key name.                                                                           |
| public_key_material | core | string | Public key material.                                                                       |
| tags                | core | hstore |
