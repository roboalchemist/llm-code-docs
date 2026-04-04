# Source: https://docs.datadoghq.com/security/default_rules/def-000-cju.md

---
title: >-
  BigQuery tables should be encrypted with customer-managed encryption keys
  (CMEK)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > BigQuery tables should be encrypted
  with customer-managed encryption keys (CMEK)
---

# BigQuery tables should be encrypted with customer-managed encryption keys (CMEK)

## Description{% #description %}

By default, BigQuery encrypts data at rest by employing `Envelope Encryption` using Google managed cryptographic keys. The data is encrypted using the `data encryption keys` and data encryption keys themselves are further encrypted using `key encryption keys`. This is done automatically and does not require any additional input from the user. However, if you want to have greater control, customer-managed encryption keys (CMEK) can be used as an encryption key management solution for BigQuery datasets. If CMEK is used, the CMEK is used to encrypt the data encryption keys, instead of using google-managed encryption keys.

### Default Value{% #default-value %}

Google-managed keys are used as `key encryption keys`.

## Rationale{% #rationale %}

For greater control over the encryption, customer-managed encryption keys (CMEK) can be used as encryption key management solution for BigQuery tables. CMEK is used to encrypt the data encryption keys instead of using google-managed encryption keys. BigQuery stores the table and CMEK association. The encryption/decryption is done automatically.

Apply the default customer-managed keys on BigQuery datasets to ensure that all new tables created in the future will be encrypted using CMEK. However, existing tables need to be updated individually to use CMEK.

## Impact{% #impact %}

Using customer-managed encryption keys (CMEK) will incur additional labor-hour investment to create, protect, and manage the keys.

- Note: Google does not store your keys on its servers and cannot access your protected data unless you provide the key. This also means that if you forget or lose your key, there is no way for Google to recover the key or to recover any data encrypted with the lost key.

## Finding Notes{% #finding-notes %}

Google Cloud has published a known bug affecting the ability to access and use the required BigQuery field: [https://issuetracker.google.com/issues/212719457?pli=1](https://issuetracker.google.com/issues/212719457?pli=1). May not generate correct pass findings until this is remediated

### Manual audits may be performed using{% #manual-audits-may-be-performed-using %}

1. Go to `Analytics`.
1. Go to `BigQuery`.
1. Under `SQL Workspace`, select the project.
1. Select Data Set and select the table.
1. Go to the `Details` tab.
1. Under `Table info`, verify `Customer-managed key` is present.
1. Repeat for each table in all data sets for all projects.

## Remediation{% #remediation %}

Currently, there is no way to update the encryption of existing data in the table. The data needs to be copied to either an original table or another table. Either option requires the specification of the customer managed encryption key (CMEK).

### From the command line{% #from-the-command-line %}

Use the following command to copy the data to the original table and encrypt it with the CMEK. The source and the destination needs to be same when copying to the original table.

```
bq cp --destination_kms_key <customer_managed_key> source_dataset.source_table destination_dataset.destination_table
```

## References{% #references %}

1. [https://cloud.google.com/bigquery/docs/customer-managed-encryption](https://cloud.google.com/bigquery/docs/customer-managed-encryption)
