# Source: https://docs.datadoghq.com/security/default_rules/def-000-xxw.md

---
title: Verify Non-Interactive Accounts Are Locked
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Non-Interactive Accounts Are
  Locked
---

# Verify Non-Interactive Accounts Are Locked

## Description{% #description %}

Accounts meant for non-interactive purposes should be locked to prevent unauthorized access. Accounts with non-standard shells (those not defined in `/etc/shells`) should be locked using `usermod -L`.

## Rationale{% #rationale %}

Locking non-interactive accounts improves security by preventing potential misuse. While many systems configure these accounts with invalid strings, setting the shell field to `nologin` is also suggested

## Warning{% #warning %}

Automatic remediation of this control is not recommended. Locking system accounts could be highly disruptive.
