# Source: https://docs.datadoghq.com/security/default_rules/def-000-f3x.md

---
title: >-
  Storage account encryption scopes should use customer-managed keys to encrypt
  data at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Storage account encryption scopes
  should use customer-managed keys to encrypt data at rest
---

# Storage account encryption scopes should use customer-managed keys to encrypt data at rest

## Description{% #description %}

This rule checks whether storage account encryption scopes are using customer-managed keys to encrypt data at rest. It is important to use customer-managed keys for encryption to ensure better control and security of data at rest.

## Remediation{% #remediation %}

To ensure storage account encryption scopes use customer-managed keys, update the encryption settings to use customer-managed keys. For instructions on how to do this, see: [Azure Documentation](https://docs.microsoft.com/en-us/azure/storage/common/customer-managed-keys-overview)
