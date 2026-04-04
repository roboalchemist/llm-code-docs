# Source: https://docs.datadoghq.com/security/default_rules/def-000-bbp.md

---
title: Verify All Account Password Hashes are Shadowed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify All Account Password Hashes are
  Shadowed
---

# Verify All Account Password Hashes are Shadowed

## Description{% #description %}

If any password hashes are stored in `/etc/passwd` (in the second field, instead of an `x` or `*`), the cause of this misconfiguration should be investigated. The account should have its password reset and the hash should be properly stored, or the account should be deleted entirely.

## Rationale{% #rationale %}

The hashes for all user account passwords should be stored in the file `/etc/shadow` and never in `/etc/passwd`, which is readable by all users.
