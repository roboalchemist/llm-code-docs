# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.redshift_hsm_client_certificate.dataset.md

---
title: Redshift HSM Client Certificate
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Redshift HSM Client Certificate
---

# Redshift HSM Client Certificate

An Amazon Redshift HSM Client Certificate is a security resource that stores the public key certificate used to connect Redshift clusters with a hardware security module (HSM). It enables secure communication between Redshift and the HSM for managing encryption keys, ensuring that sensitive data is protected with hardware-based key management.

```
aws.redshift_hsm_client_certificate
```

## Fields

| Title                             | ID   | Type       | Data Type                                     | Description |
| --------------------------------- | ---- | ---------- | --------------------------------------------- | ----------- |
| _key                              | core | string     |
| account_id                        | core | string     |
| hsm_client_certificate_identifier | core | string     | The identifier of the HSM client certificate. |
| tags                              | core | hstore_csv |
