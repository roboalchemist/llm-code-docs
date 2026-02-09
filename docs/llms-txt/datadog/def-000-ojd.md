# Source: https://docs.datadoghq.com/security/default_rules/def-000-ojd.md

---
title: Google Security Command Center finding muted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Security Command Center finding
  muted
---

# Google Security Command Center finding muted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1578-modify-cloud-compute-infrastructure](https://attack.mitre.org/techniques/T1578) 
## Goal{% #goal %}

Detect when a [Google Security Command Center](https://cloud.google.com/security-command-center/docs) muteconfigs rule was created.

## Strategy{% #strategy %}

Google Security Command Center helps you strengthen your security posture by evaluating your security and data attack surface; providing asset inventory and discovery; identifying misconfigurations, vulnerabilities and threats; and helping you mitigate and remediate risks.

This detection rule detects when a user creates a [rule to mute future findings or mute multiple existing findings](https://cloud.google.com/security-command-center/docs/how-to-mute-findings). This could indicate an attacker attempting to hide malicious activity.

## Triage and response{% #triage-and-response %}

1. Investigate the finding to determine if the action was expected.
1. If the finding is deemed malicious, follow the [investigation and remediation guidance](https://cloud.google.com/security-command-center/docs/how-to-investigate-threats) provided by Google and also any internal incident response processes.
