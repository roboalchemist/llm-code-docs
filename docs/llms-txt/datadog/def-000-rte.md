# Source: https://docs.datadoghq.com/security/default_rules/def-000-rte.md

---
title: Suspicious named pipe created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Suspicious named pipe created
---

# Suspicious named pipe created
Classification:attackTactic:[TA0008-lateral-movement](https://attack.mitre.org/tactics/TA0008)Technique:[T1021-remote-services](https://attack.mitre.org/techniques/T1021)
## Goal{% #goal %}

Detects when a suspicious remote named pipe is observed, which could indicate lateral movement or remote execution attempts by malicious actors.

## Strategy{% #strategy %}

Monitoring of Windows event logs where `@evt.id` is `5145` and grouping by `@Event.System.Computer`, where a network share object was checked to see whether client can be granted desired access. The value that was observed was unusual, which made it suspicious.

## Triage & Response{% #triage--response %}

Verify if the execution of the suspicious pipe on `{{@@Event.System.Computer}}` is expected. If the execution was not intended isolate the system.
