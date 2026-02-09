# Source: https://docs.datadoghq.com/security/default_rules/def-000-wmq.md

---
title: Ensure All Accounts on the System Have Unique User IDs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure All Accounts on the System Have
  Unique User IDs
---

# Ensure All Accounts on the System Have Unique User IDs
 
## Description{% #description %}

Change user IDs (UIDs), or delete accounts, so each has a unique name.

## Rationale{% #rationale %}

To assure accountability and prevent unauthenticated access, interactive users must be identified and authenticated to prevent potential misuse and compromise of the system.

## Warning{% #warning %}

Automatic remediation of this control is not available due to unique requirements of each system.
