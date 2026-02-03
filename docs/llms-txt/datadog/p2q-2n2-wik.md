# Source: https://docs.datadoghq.com/security/default_rules/p2q-2n2-wik.md

---
title: Windows firewall disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows firewall disabled
---

# Windows firewall disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when the Windows firewall is disabled.

## Strategy{% #strategy %}

Monitor the Windows event logs where `@evt.id` is `4950` and the `@Event.EventData.Data.SettingValue:No`.

## Triage and response{% #triage-and-response %}

Verify if `{{@Event.System.Computer}}` has a legitimate reason for having the Windows firewall disabled.

## Changelog{% #changelog %}

- 24 September 2025 - Updated severity.
