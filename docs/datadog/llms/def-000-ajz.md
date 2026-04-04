# Source: https://docs.datadoghq.com/security/default_rules/def-000-ajz.md

---
title: BigQuery data sets should specify a default customer-managed encryption key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > BigQuery data sets should specify a
  default customer-managed encryption key
---

# BigQuery data sets should specify a default customer-managed encryption key

## Description{% #description %}

By default, BigQuery uses envelope encryption with Google-managed cryptographic keys to encrypt the data at rest. The data is encrypted using *data encryption keys*, and the data encryption keys themselves are further encrypted using *key encryption keys*. This is seamless and does not require any additional input from the user. For greater control, *customer-managed encryption keys* (CMEKs) can be used as an encryption key management solution for BigQuery datasets.

### Default Value{% #default-value %}

Google-managed keys are used as key encryption keys.

## Rationale{% #rationale %}

By default, BigQuery uses envelope encryption with Google-managed cryptographic keys to encrypt the data at rest. The data is encrypted using *data encryption keys*, and the data encryption keys themselves are further encrypted using *key encryption keys*. This is seamless and does not require any additional input from the user.

For greater control, CMEKs can be used as an encryption key management solution for BigQuery datasets. Setting a default CMEK for a dataset ensures that any tables created in the future will use the specified CMEK, if no others are provided.

## Impact{% #impact %}

Using CMEKs incurs an additional labor-hour investment to create, protect, and manage the keys.

**Note**: Google does not store your keys on its servers and cannot access your protected data unless you provide the key. This also means that if you forget or lose your key, there is no way for Google to recover the key or to recover any data encrypted with the lost key.

# Remediation{% #remediation %}

To update the default CMEK for existing data sets, specify the default key in the `EncryptionConfiguration.kmsKeyName` field when calling the `datasets.insert` or `datasets.patch` methods.

## References{% #references %}

1. [https://cloud.google.com/bigquery/docs/customer-managed-encryption](https://cloud.google.com/bigquery/docs/customer-managed-encryption)
