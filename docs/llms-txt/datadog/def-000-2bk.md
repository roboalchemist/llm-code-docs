# Source: https://docs.datadoghq.com/security/default_rules/def-000-2bk.md

---
title: Ensure Authentication Required for Single User Mode
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure Authentication Required for
  Single User Mode
---

# Ensure Authentication Required for Single User Mode

## Description{% #description %}

Single user mode is used for recovery when the system detects an issue during boot or by manual selection from the bootloader.

## Rationale{% #rationale %}

Requiring authentication in single user mode prevents an unauthorized user from rebooting the system into single user to gain root privileges without credentials.
