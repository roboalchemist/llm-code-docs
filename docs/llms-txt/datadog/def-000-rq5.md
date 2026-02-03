# Source: https://docs.datadoghq.com/security/default_rules/def-000-rq5.md

---
title: >-
  'Allow storage account key access' setting for Azure Storage Accounts should
  be disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > 'Allow storage account key access'
  setting for Azure Storage Accounts should be disabled
---

# 'Allow storage account key access' setting for Azure Storage Accounts should be disabled
 
## Description{% #description %}

Disable shared key access for Azure Storage Accounts.

## Remediation{% #remediation %}

Disable shared key access in the Storage Account Configuration settings. See [Azure shared key access](https://learn.microsoft.com/en-us/azure/storage/common/storage-account-keys-manage?tabs=azure-portal#disable-shared-key-access) for more information.
