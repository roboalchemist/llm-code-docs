# Source: https://docs.datadoghq.com/security/default_rules/def-000-bt0.md

---
title: Storage for critical data should be encrypted with Customer Managed Key
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Storage for critical data should be
  encrypted with Customer Managed Key
---

# Storage for critical data should be encrypted with Customer Managed Key
 
## Description{% #description %}

By default all data in Azure storage account, including blobs, disks, files, queues, tables, and object metadata, is encrypted at rest using Microsoft managed keys. You can enhance the security of your sensitive data by opting for customer-managed keys, which allow you to control and manage the encryption key that protects and controls access to your data. You can also choose to automatically update the key version used for Azure Storage encryption whenever a new version is available in the associated key vault.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Open Azure portal at [https://portal.azure.com/](https://portal.azure.com/)
1. Go to your existing storage account.
1. Inside your storage account, choose **Settings** then select **Encryption**.
1. By default, Azure storage is encrypted with Microsoft managed keys. To modify this, opt for **Customer-managed key**.
1. You'll need to specify a key from your already available Key Vault in the **Customer-managed key** settings.
1. Lastly, you can choose to turn on automatic key updates for encryption whenever a new version is available. Locate this setting under the customer-managed key settings and check the box for **Automatic key rotation**.
