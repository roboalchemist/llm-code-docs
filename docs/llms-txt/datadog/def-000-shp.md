# Source: https://docs.datadoghq.com/security/default_rules/def-000-shp.md

---
title: Azure Blob Storage soft delete should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure Blob Storage soft delete should
  be enabled
---

# Azure Blob Storage soft delete should be enabled
 
## Description{% #description %}

Enable soft delete for Azure Blob Storage to recover deleted blobs within a retention period (1-365 days).

## Remediation{% #remediation %}

Enable soft delete for blobs in the Storage Account Data protection settings. See [Azure Blob Storage soft delete](https://docs.microsoft.com/en-us/azure/storage/blobs/soft-delete-blob-overview) for more information.
