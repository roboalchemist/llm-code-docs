# Source: https://docs.datadoghq.com/security/default_rules/def-000-dr5.md

---
title: Tailscale user approval configuration disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Tailscale user approval configuration
  disabled
---

# Tailscale user approval configuration disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when the TailScale [user approval](https://tailscale.com/kb/1239/user-approval/) configuration has been disabled.

## Strategy{% #strategy %}

This rule monitors Tailscale logs for when the user approval configuration has been disabled. The user approval feature allows Tailscale network administrators to review and approve new users before they can join the network. An attacker disabling this could be an attempt to disable defenses.

## Triage and response{% #triage-and-response %}

1. Investigate the user `{{@usr.email}}` that disabled user approval within your Tailscale configuration.
1. If the activity is deemed malicious:
   - Begin your organization's incident response process and investigate.
