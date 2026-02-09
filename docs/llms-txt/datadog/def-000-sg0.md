# Source: https://docs.datadoghq.com/security/default_rules/def-000-sg0.md

---
title: Ensure ufw Default Deny Firewall Policy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure ufw Default Deny Firewall Policy
---

# Ensure ufw Default Deny Firewall Policy
 
## Description{% #description %}

A default deny policy on connections ensures that any unconfigured network usage will be rejected. Note: Any port or protocol without a explicit allow before the default deny will be blocked.

## Rationale{% #rationale %}

With a default accept policy the firewall will accept any packet that is not configured to be denied. It is easier to allow acceptable usage than to block unacceptable usage.

## Warning{% #warning %}

Changing firewall settings while connected over network can result in being locked out of the system.
