# Source: https://docs.datadoghq.com/security/default_rules/def-000-y5o.md

---
title: All keys in RBAC Azure Key Vault should have an expiration time set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > All keys in RBAC Azure Key Vault should
  have an expiration time set
---

# All keys in RBAC Azure Key Vault should have an expiration time set
 
## Description{% #description %}

Ensure that all keys in Role Based Access Control (RBAC) Azure Key Vaults have an expiration date set. The **exp** (expiration date) attribute identifies the expiration date on or after which the key **must not** be used for encryption of new data, wrapping of new keys, or signing. By default, keys never expire. It is thus recommended that keys be rotated in the key vault and assigned an explicit expiration date for all keys to help enforce the key rotation. This encourages rotation and ensures that the keys cannot be used indefinitely in the event of a leak.

## Remediation{% #remediation %}

To add an expiration date to an [Azure Key Vault](https://learn.microsoft.com/en-us/azure/key-vault/), follow these steps:

1. Go to **Key vaults**.
1. For each Key vault, click **Keys**.
1. In the main pane, ensure that an appropriate **Expiration date** is set for any keys that are **Enabled**.
