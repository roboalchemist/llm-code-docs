# Source: https://docs.datadoghq.com/security/default_rules/def-000-hb6.md

---
title: Ensure all users last password change date is in the past
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure all users last password change
  date is in the past
---

# Ensure all users last password change date is in the past
 
## Description{% #description %}

All users should have a password change date in the past.

## Rationale{% #rationale %}

If a user recorded password change date is in the future then they could bypass any set password expiration.

## Warning{% #warning %}

Automatic remediation is not available, in order to avoid any system disruption.
