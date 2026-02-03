# Source: https://docs.datadoghq.com/security/default_rules/def-000-zza.md

---
title: Windows system environment variables modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows system environment variables
  modified
---

# Windows system environment variables modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1112-modify-registry](https://attack.mitre.org/techniques/T1112) 
## Goal{% #goal %}

Detect modifications of the Windows system environment variables registry key.

## Strategy{% #strategy %}

Various compliance frameworks, including PCI DSS, SOC, and CIS, require monitoring of critical system and configuration files. Microsoft recommends monitoring the system environment variables registry key located at 'HKEY_LOCAL_MACHINE\System\CurrentControlSet\Control\Session Manager\Environment', based on known attack patterns.

## Triage and response{% #triage-and-response %}

1. Identify which user or process modified the registry key.
1. If these changes were not authorized, and you cannot confirm the safety of the changes, roll back the host to an acceptable configuration.

*Requires Agent version 7.52 or later*
