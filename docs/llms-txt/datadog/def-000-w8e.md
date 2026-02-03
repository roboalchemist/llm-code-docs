# Source: https://docs.datadoghq.com/security/default_rules/def-000-w8e.md

---
title: PsExec execution detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > PsExec execution detected
---

# PsExec execution detected
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1569-system-services](https://attack.mitre.org/techniques/T1569) 
## Goal{% #goal %}

Detects when the Windows utility PsExec was executed on a system. PsExec is commonly utilized for executing processes remotely on Windows machines, often as part of legitimate system administration activity. This could be evidence of unauthorized remote access by an attcker.

## Strategy{% #strategy %}

Monitoring of Windows event logs where `@evt.id` is `7045` or `4697` and grouping by `@Event.System.Computer`, which detects service psexec service installation on a system./ logs where `@evt.id` is `5145` and grouping by `@Event.System.Computer`, where A network share object was checked to see whether client can be granted desired access by psexec.

## Triage & Response{% #triage--response %}

Verify if the exection of psexec on `{{@@Event.System.Computer}}` is expected. If the execution was not intended isolate the system.
