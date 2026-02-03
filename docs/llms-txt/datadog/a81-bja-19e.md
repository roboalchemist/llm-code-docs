# Source: https://docs.datadoghq.com/security/default_rules/a81-bja-19e.md

---
title: SELinux enforcement disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > SELinux enforcement disabled
---

# SELinux enforcement disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## What happened{% #what-happened %}

SELinux was disabled, potentially by an attacker to disable defenses.

## Goal{% #goal %}

Detect when SELinux enforcement is disabled.

## Strategy{% #strategy %}

This detection monitors the change of SELinux enforcing mode.

## Triage & Response{% #triage--response %}

1. Check which user or process disabled SELinux enforcing mode.
1. If the change is not expected, roll back to enable SELinux enforcing mode.
1. Investigate security signals (if present) occurring around the time of the event to establish an attack path.
1. Find and repair the root cause of the attack.

*Requires Agent version 7.30 or greater*
