# Source: https://docs.datadoghq.com/security/default_rules/def-000-y4m.md

---
title: Ensure root account access is controlled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure root account access is
  controlled
---

# Ensure root account access is controlled

## Description{% #description %}

There are a number of methods to access the root account directly. Without a password set any user would be able to gain access and thus control over the entire system.

## Rationale{% #rationale %}

Access to root should be secured at all times.

## Warning{% #warning %}

This rule doesn't come with a remediation, as the exact requirement allows root to either have a password or be locked.
