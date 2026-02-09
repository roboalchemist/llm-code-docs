# Source: https://docs.datadoghq.com/security/default_rules/def-000-g1q.md

---
title: SQL servers should use customer-managed keys to encrypt data at rest
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SQL servers should use customer-managed
  keys to encrypt data at rest
---

# SQL servers should use customer-managed keys to encrypt data at rest
 
## Description{% #description %}

This rule checks if SQL servers are using customer-managed keys to encrypt data at rest. This is important for ensuring that sensitive data stored on SQL servers is securely encrypted and protected from unauthorized access.

## Remediation{% #remediation %}

To remediate this, configure SQL servers to use customer-managed keys for encrypting data at rest. For instructions on how to do this, see: [Azure SQL documentation](https://docs.microsoft.com/en-us/azure/azure-sql/database/always-encrypted-cmk-overview).
