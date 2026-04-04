# Source: https://docs.datadoghq.com/security/default_rules/def-000-we4.md

---
title: Tailscale device approval configuration disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Tailscale device approval configuration
  disabled
---

# Tailscale device approval configuration disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a [device approval](https://tailscale.com/kb/1099/device-approval/) configuration has been disabled in Tailscale.

## Strategy{% #strategy %}

This rule monitors Tailscale logs for when a device approval configuration has been disabled in Tailscale. The device approval feature allows Tailscale network administrators to review and approve new devices before they can join the network. This is to ensure that only trusted devices, such as workplace-managed laptops and phones, can access a network. An attacker disabling this could be an attempt to impair defenses.

## Triage and response{% #triage-and-response %}

1. Investigate the user `{{@usr.email}}` that disabled device approval within your Tailscale configuration.
1. If the activity is deemed malicious:
   - Begin your organization's incident response process and investigate.
