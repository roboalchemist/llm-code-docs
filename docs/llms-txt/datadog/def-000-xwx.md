# Source: https://docs.datadoghq.com/security/default_rules/def-000-xwx.md

---
title: Windows boot registry key modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows boot registry key modified
---

# Windows boot registry key modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1112-modify-registry](https://attack.mitre.org/techniques/T1112)
## What happened{% #what-happened %}

The Windows registry key `{{ @registry.key_name }}` was modified by `{{ @process.executable.name }}`, potentially to establish persistence.

## Goal{% #goal %}

Detect modifications of Windows boot registry keys.

## Strategy{% #strategy %}

Various compliance frameworks, including PCI DSS, SOC, and CIS require monitoring of critical system and configuration files. On Windows, a key configurations for how the operating system boots can be found in 'HKEY_LOCAL_MACHINE\Software\Microsoft\Windows NT\CurrentVersion\IniFileMapping\system.ini\boot'.

## Triage and response{% #triage-and-response %}

1. Identify which user or process modified the registry key.
1. If these changes were not authorized, and you cannot confirm the safety of the changes, roll back the host in question to an acceptable configuration.

*Requires Agent version 7.52 or later*
