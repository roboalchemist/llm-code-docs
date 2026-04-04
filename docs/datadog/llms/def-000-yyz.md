# Source: https://docs.datadoghq.com/security/default_rules/def-000-yyz.md

---
title: WMI used to remotely execute content
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > WMI used to remotely execute content
---

# WMI used to remotely execute content
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1047-windows-management-instrumentation](https://attack.mitre.org/techniques/T1047)
## What happened{% #what-happened %}

`{{ @process.executable.name }}` spawned from Windows Management Instrumentation (WMI), which could indicate lateral movement from another compromised host.

## Goal{% #goal %}

Detects when WMI spawns a shell to execute content.

## Strategy{% #strategy %}

Threat actors are known to utilize tools found natively in a victim's environment to accomplish their objectives. Windows Management Instrumentation, a legitimate Windows capability, has been abused by malicious actors in the past to execute content on remote systems.

## Triage and response{% #triage-and-response %}

1. Identify what is being executed, and if it is authorized.
1. Identify account used to remotely authenticate to the host.
1. If it's not authorized, isolate the host from the network, and lock down potentially compromised account.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.50.0 or greater.*
