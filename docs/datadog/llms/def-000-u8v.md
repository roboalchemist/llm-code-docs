# Source: https://docs.datadoghq.com/security/default_rules/def-000-u8v.md

---
title: Ensure network interfaces are assigned to appropriate zone
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure network interfaces are assigned
  to appropriate zone
---

# Ensure network interfaces are assigned to appropriate zone

## Description{% #description %}

Firewall zones define the trust level of network connections or interfaces. Note: Changing firewall settings while connected over network can result in being locked out of the system.

## Rationale{% #rationale %}

A network interface not assigned to the appropriate zone can allow unexpected or undesired network traffic to be accepted on the interface.
