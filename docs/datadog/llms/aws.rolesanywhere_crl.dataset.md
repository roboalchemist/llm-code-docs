# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.rolesanywhere_crl.dataset.md

---
title: Rolesanywhere Crl
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Rolesanywhere Crl
---

# Rolesanywhere Crl

This table represents the rolesanywhere_crl resource from Amazon Web Services.

```
aws.rolesanywhere_crl
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                     | Description |
| ---------------- | ---- | ---------- | --------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| created_at       | core | timestamp  | The ISO-8601 timestamp when the certificate revocation list (CRL) was created.                |
| crl_arn          | core | string     | The ARN of the certificate revocation list (CRL).                                             |
| crl_id           | core | string     | The unique identifier of the certificate revocation list (CRL).                               |
| enabled          | core | bool       | Indicates whether the certificate revocation list (CRL) is enabled.                           |
| name             | core | string     | The name of the certificate revocation list (CRL).                                            |
| tags             | core | hstore_csv |
| trust_anchor_arn | core | string     | The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for. |
| updated_at       | core | timestamp  | The ISO-8601 timestamp when the certificate revocation list (CRL) was last updated.           |
