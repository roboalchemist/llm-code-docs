# Source: https://docs.datadoghq.com/security/default_rules/def-000-vc2.md

---
title: >-
  'Blob public access' should be disabled for storage accounts with blob
  containers
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'Blob public access' should be disabled
  for storage accounts with blob containers
---

# 'Blob public access' should be disabled for storage accounts with blob containers

## Description{% #description %}

Disallowing public access for a storage account overrides the public access settings for individual containers in that storage account.

### Default Value{% #default-value %}

By default, `Public access level` is set to `Private (no anonymous access)` for blob containers and `AllowBlobPublicAccess` is set to `Null` (allow in effect) for storage accounts.

## Rationale{% #rationale %}

It is recommended that you avoid providing anonymous access to blob containers unless necessary. A Shared Access Signature (SAS) token or Azure AD RBAC should be used for providing controlled and timed access to blob containers. If no anonymous access is needed on any container in the storage account, it's recommended to set `allowBlobPublicAccess` to false at the account level, which prevents any container from accepting anonymous access in the future.

### Impact{% #impact %}

Access must be managed using shared access signatures or with Azure AD RBAC.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

**Note**: You must [create a SAS token](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/create-sas-tokens?tabs=Containers) for your blob containers before completing the following remediation steps.

1. Go to **Storage Accounts**.
1. For each storage account, go to **Configuration** in the side panel.
1. Set **Allow Blob public access** to **Disabled**.

### From the command line{% #from-the-command-line %}

First, follow [Microsoft documentation](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/create-sas-tokens?tabs=Containers) and create SAS tokens for your blob containers. Then, follow the steps below:

1. Set **Allow Blob Public Access** to `false` on the storage account.

   ```
   az storage account update --name <storage-account> --resource-group <resource-group> --allow-blob-public-access false
   ```

## References{% #references %}

1. [https://learn.microsoft.com/en-us/azure/storage/common/storage-sas-overview](https://learn.microsoft.com/en-us/azure/cognitive-services/translator/document-translation/create-sas-tokens?tabs=Containers)
1. [https://docs.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-prevent](https://docs.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-prevent)
1. [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-governance-strategy#gs-2-define-and-implement-enterprise-segmentationseparation-of-duties-strategy](https://docs.microsoft.com/en-us/security/benchmark/azure-security-controls-v3-governance-strategy#gs-2-define-and-implement-enterprise-segmentationseparation-of-duties-strategy)
1. [https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-2-secure-cloud-services-with-network-controls](https://docs.microsoft.com/en-us/security/benchmark/azure/security-controls-v3-network-security#ns-2-secure-cloud-services-with-network-controls)
1. [https://docs.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure](https://docs.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure)
1. [https://docs.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access](https://docs.microsoft.com/en-us/azure/storage/blobs/assign-azure-role-data-access)
