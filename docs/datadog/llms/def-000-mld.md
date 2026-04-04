# Source: https://docs.datadoghq.com/security/default_rules/def-000-mld.md

---
title: Windows credential dumping tools service execution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows credential dumping tools
  service execution
---

# Windows credential dumping tools service execution

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1569-system-services](https://attack.mitre.org/techniques/T1569)
## Goal{% #goal %}

Detects execution of known credential dumping tools registered as a Windows service.

## Strategy{% #strategy %}

This rule monitors Windows Security event logs for service installation events involving known credential dumping utilities. It specifically watches for Windows Event ID `4697` (Service Installation) where the ServiceFileName contains strings associated with credential dumping tools. These tools are designed to extract credentials from the operating system and are commonly used by attackers after gaining initial access to extract passwords, hashes, or tickets for lateral movement and privilege escalation. The installation of these tools as services provides persistence and enables attackers to harvest credentials from the compromised system.

## Triage & Response{% #triage--response %}

- Examine the service details on `{{host}}` to verify the suspicious service installation event.
- Review process execution history leading up to the service installation for additional context.
- Investigate network connections established by the host during and after the service installation.
- Search for other systems in the environment with similar service installations.
- Reset credentials for all accounts that were logged on to the compromised system.
- Scan the system for additional malware and persistence mechanisms.
- Review authentication logs for suspicious logon activities that might indicate how the attacker gained access.
