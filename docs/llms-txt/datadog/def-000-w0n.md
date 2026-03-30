# Source: https://docs.datadoghq.com/security/default_rules/def-000-w0n.md

---
title: Ensure All Groups on the System Have Unique Group Names
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure All Groups on the System Have
  Unique Group Names
---

# Ensure All Groups on the System Have Unique Group Names

## Description{% #description %}

Change the group name or delete groups, so each has a unique name.

## Rationale{% #rationale %}

To assure accountability and prevent unauthenticated access, groups must be identified uniquely to prevent potential misuse and compromise of the system.

## Warning{% #warning %}

Automatic remediation of this control is not available due to the unique requirements of each system.
