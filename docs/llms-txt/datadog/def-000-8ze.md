# Source: https://docs.datadoghq.com/security/default_rules/def-000-8ze.md

---
title: Azure Key Vault should be recoverable
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Azure Key Vault should be recoverable
---

# Azure Key Vault should be recoverable
 
## Description{% #description %}

The key vault contains object keys, secrets, and certificates. If a key vault is made unavailable accidentally, it can cause immediate data loss or loss of security functions supported by the key vault objects. This includes authentication, validation, verification, and non-repudiation. It is recommended that the key vault be made recoverable by enabling the "Do Not Purge" and "Soft Delete" functions. This prevents loss of encrypted data, including storage accounts, SQL databases, and dependent services provided by key vault objects (keys, secrets, certificates, etc.), which may occur due to accidental deletion by a user or from disruptive activity by a malicious user.

**Note**: When a new key vault is created, the `enableSoftDelete` and `enablePurgeProtection` parameters are set to `null` by default, disabling both features.

## Remediation{% #remediation %}

Enable "Do Not Purge" and "Soft Delete" for a key vault.

### From the console{% #from-the-console %}

1. Log in to the [Azure Portal](https://portal.azure.com).
1. Go to **Key Vaults** and click **Properties**.
1. Verify that the status of soft-delete is set to **'Soft delete has been enabled on this key vault'**.
1. At the bottom of the page, click **'Enable Purge Protection'**.
