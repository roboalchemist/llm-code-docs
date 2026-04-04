# Source: https://docs.datadoghq.com/security/default_rules/def-000-hvl.md

---
title: Azure Blob Storage versioning should be enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure Blob Storage versioning should be
  enabled
---

# Azure Blob Storage versioning should be enabled

## Description{% #description %}

Enable versioning for Azure Blob Storage to maintain previous versions of blobs and protect against accidental modifications or deletions.

## Remediation{% #remediation %}

Enable versioning in the Storage Account Blob service settings. See [Azure Blob Storage versioning](https://docs.microsoft.com/en-us/azure/storage/blobs/versioning-overview) for more information.
