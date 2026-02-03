# Source: https://docs.datadoghq.com/security/default_rules/def-000-msc.md

---
title: GitHub secret scanning disabled or bypassed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub secret scanning disabled or
  bypassed
---

# GitHub secret scanning disabled or bypassed
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when a GitHub secret scanning setting has been disabled.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a secret scanning setting has been disabled. GitHub scans repositories for known types of secrets to prevent fraudulent use of secrets that were committed accidentally. Disabling these settings could lead to a degradation in the organization's security posture.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.

## Changelog{% #changelog %}

- 21 February 2024 - Updated detection rule name.
- 4 September 2024 - Updated detection rule name.
- 3 January 2025 - update detection rule severity from High to Medium for several cases.
