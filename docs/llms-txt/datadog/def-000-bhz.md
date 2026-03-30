# Source: https://docs.datadoghq.com/security/default_rules/def-000-bhz.md

---
title: Critical windows file modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Critical windows file modified
---

# Critical windows file modified
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1036-masquerading](https://attack.mitre.org/techniques/T1036)
## What happened{% #what-happened %}

The critical system file `{{ @file.path }}` was modified by the process `{{ @process.executable.name }}`, potentially indicating unauthorized system changes.

## Goal{% #goal %}

Detect modifications of critical Windows system file.

## Strategy{% #strategy %}

Various compliance frameworks, including PCI DSS, SOC, and CIS, require monitoring of critical system files and binaries. On Windows, critical system binaries are typically stored in `C:\Windows\system32`. This rule tracks any modifications to that directory.

## Triage and response{% #triage-and-response %}

1. Identify which user or process changed the critical system binaries.
1. If these changes were not authorized, and you cannot confirm the safety of the changes, roll back the host or container in question to an acceptable configuration.

*Requires Agent version 7.52 or later*
