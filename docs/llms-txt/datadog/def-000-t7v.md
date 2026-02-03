# Source: https://docs.datadoghq.com/security/default_rules/def-000-t7v.md

---
title: Evidence hidden by deleting system log file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Evidence hidden by deleting system log
  file
---

# Evidence hidden by deleting system log file
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1070-indicator-removal](https://attack.mitre.org/techniques/T1070) 
## What happened{% #what-happened %}

The file `{{ @file.path }}` was deleted by the process `{{ @process.comm }}`. This may have been done to hide evidence.

## Goal{% #goal %}

Detect the removal of system log files in order to hide evidence of malicious activity.

## Strategy{% #strategy %}

Monitor the file system for the deletion of specific system logs.

## Triage and response{% #triage-and-response %}

1. Review the signal to understand how the file `{{ @file.path }}` was deleted.
1. If the activity is malicious, isolate the affected host to prevent further compromise.
1. Use related signals and other logs to find and repair the root cause.

*Requires Agent version 7.27 or later.*
