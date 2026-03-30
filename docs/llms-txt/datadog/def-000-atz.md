# Source: https://docs.datadoghq.com/security/default_rules/def-000-atz.md

---
title: Default network access rule for storage accounts should be set to deny
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Default network access rule for storage
  accounts should be set to deny
---

# Default network access rule for storage accounts should be set to deny

## Description{% #description %}

Ensure default network access rule for storage accounts is set to deny to prevent unauthorized access.

## Remediation{% #remediation %}

Configure the default network access rule to deny in the Storage Account Networking settings. See [Azure Storage Account Network Rules](https://docs.microsoft.com/en-us/azure/storage/common/storage-network-security) for more information.
