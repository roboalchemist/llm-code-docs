# Source: https://docs.datadoghq.com/security/default_rules/def-000-0fl.md

---
title: Ensure One Logging Service Is In Use
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure One Logging Service Is In Use
---

# Ensure One Logging Service Is In Use

## Description{% #description %}

Ensure that a logging system is active and in use.

```

systemctl is-active rsyslog systemd-journald
```

The command should return at least one `active`.

## Rationale{% #rationale %}

The system should have one active logging service to avoid conflicts and ensure consistency.

## Warning{% #warning %}

This rule does not come with a remediation. There are specific rules for enabling each logging service which should be enabled instead.
