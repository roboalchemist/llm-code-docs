# Source: https://docs.datadoghq.com/security/default_rules/def-000-mid.md

---
title: Windows PowerShell PSAsyncShell asynchronous TCP reverse shell
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell PSAsyncShell
  asynchronous TCP reverse shell
---

# Windows PowerShell PSAsyncShell asynchronous TCP reverse shell

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071)
## Goal{% #goal %}

Detects execution of PSAsyncShell PowerShell commands used for establishing persistent asynchronous TCP reverse shells.

## Strategy{% #strategy %}

This rule monitors PowerShell script block logging through `@Event.EventData.Data.ScriptBlockText` for PSAsyncShell command patterns. PSAsyncShell is a PowerShell-based asynchronous reverse shell tool that creates persistent command and control channels through outbound TCP connections.

Asynchronous reverse shells maintain command execution capabilities even during intermittent connectivity, making detection and disruption more difficult. These shells typically establish outbound connections that bypass firewall rules that block inbound connections, allowing attackers to maintain persistent access to compromised systems.

## Triage & Response{% #triage--response %}

- Examine the complete PowerShell command and execution context on `{{host}}`.
- Analyze network connections for suspicious outbound TCP traffic to unusual destinations.
- Review PowerShell session history for additional commands executed before and after detection.
- Check startup locations and scheduled tasks for persistence mechanisms.
- Monitor for data transfers occurring through the shell connection.
- Isolate `{{host}}` from the network to prevent command and control communication.
- Reset any potentially compromised account credentials.
