# Source: https://docs.datadoghq.com/security/default_rules/def-000-tvg.md

---
title: Multiple failed login attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Multiple failed login attempts
---

# Multiple failed login attempts
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detects when multiple failed logins are seen from the same IP address, indicating a potential brute force attack is occurring.

## Strategy{% #strategy %}

Monitoring of Windows event logs where `@evt.id` is `4625` and grouping by `@network.client.ip`.

## Triage & Response{% #triage--response %}

Verify if `{{@network.client.ip}}` is expected to be attempting to access the network. It is possible for this detection to be triggered by services and applications attempting to authenticate with recently-expired credentials.
