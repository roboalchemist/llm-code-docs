# Source: https://docs.datadoghq.com/security/default_rules/def-00j-05d.md

---
title: >-
  SQL server's Transparent Data Encryption (TDE) protector should be encrypted
  with a customer-managed key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL server's Transparent Data
  Encryption (TDE) protector should be encrypted with a customer-managed key
---

# SQL server's Transparent Data Encryption (TDE) protector should be encrypted with a customer-managed key

## Description{% #description %}

By default, the TDE protector managed by Microsoft is enabled for a SQL server, but with customer-managed key support, users gain control over Transparent Data Encryption (TDE) encryption keys. This support allows for the encryption of the TDE protector with a key managed by the data owner, providing increased transparency and control. Azure Key Vault, a cloud-based key store, offers central key management and the use of hardware security modules (HSMs) for enhanced security. When deploying customer-managed keys, it is essential to have an automated toolset for key management, including discovery and rotation, and to store the keys in an HSM or hardware-backed keystore. Additionally, it is recommended to check with your cryptographic key provider for any available add-ons or toolsets related to key management.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to **SQL servers**.
1. For your server instance, click **Transparent data encryption**.
1. Set **Transparent data encryption** to **Customer-managed key**.
1. Browse through your key vaults to select an existing key or create a new key in the Azure Key Vault.
1. Check **Make selected key the default TDE protector**.
