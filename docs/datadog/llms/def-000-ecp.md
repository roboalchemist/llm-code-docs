# Source: https://docs.datadoghq.com/security/default_rules/def-000-ecp.md

---
title: Ensure All Groups on the System Have Unique Group ID
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure All Groups on the System Have
  Unique Group ID
---

# Ensure All Groups on the System Have Unique Group ID

## Description{% #description %}

Change the group name or delete groups, so each has a unique id.

## Rationale{% #rationale %}

To assure accountability and prevent unauthenticated access, groups must be identified uniquely to prevent potential misuse and compromise of the system.

## Warning{% #warning %}

Automatic remediation of this control is not available due to the unique requirements of each system.
