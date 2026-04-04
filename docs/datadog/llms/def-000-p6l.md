# Source: https://docs.datadoghq.com/security/default_rules/def-000-p6l.md

---
title: Azure Storage should have soft delete enabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Azure Storage should have soft delete
  enabled
---

# Azure Storage should have soft delete enabled

## Description{% #description %}

Azure Storage blobs may contain sensitive data such as ePHI, financial information, secrets, or personal data. Accidental modifications or deletions by applications or users can result in data loss or unavailability. To mitigate this risk, it is recommended to enable soft delete configuration in Azure Storage. This allows for the saving and recovery of data when blobs or blob snapshots are deleted. By enabling recoverable blobs configuration, even if data is deleted from the storage account, it remains recoverable within the specified retention policy timeframe, which can range from 7 to 365 days.

## Remediation{% #remediation %}

### From the console{% #from-the-console %}

1. Go to **Storage Accounts**.
1. For each Storage Account, navigate to **Data protection** in the left scroll column.
1. Check **soft delete** for both blobs and containers. Set the retention period to a sufficient length for your organization.
