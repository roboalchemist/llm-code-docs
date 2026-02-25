# Source: https://docs.datadoghq.com/security/default_rules/def-000-id9.md

---
title: Windows security essentials executable modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows security essentials executable
  modified
---

# Windows security essentials executable modified
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1036-masquerading](https://attack.mitre.org/techniques/T1036)
## What happened{% #what-happened %}

`{{ @process.executable.name }}` modified the Windows Security Essentials executable `{{ @file.path }}`.

## Goal{% #goal %}

Detect modifications of the Windows security essentials executable.

## Strategy{% #strategy %}

Various compliance frameworks, including PCI DSS, SOC, and CIS, require monitoring of critical system and configuration files. Microsoft recommends the monioring of the Windows security essentials executable located at 'C:\Program Files\Microsoft Security Client\msseces.exe' based on known attack patterns.

## Triage and response{% #triage-and-response %}

1. Identify which user or process modified the registry key.
1. If these changes were not authorized, and you cannot confirm the safety of the changes, roll back the host to an acceptable configuration.

*Requires Agent version 7.54 or later*
