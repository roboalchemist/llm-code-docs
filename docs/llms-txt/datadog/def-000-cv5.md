# Source: https://docs.datadoghq.com/security/default_rules/def-000-cv5.md

---
title: Windows Impacket PsExec execution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows Impacket PsExec execution
---

# Windows Impacket PsExec execution

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0008-lateral-movement](https://attack.mitre.org/tactics/TA0008)Technique:[T1021-remote-services](https://attack.mitre.org/techniques/T1021) 
## Goal{% #goal %}

Detects lateral movement activity using Impacket's PsExec implementation through network share access patterns.

## Strategy{% #strategy %}

This rule monitors Windows network share access events where `@evt.id` is `5145` for access to the `IPC$` administrative share when `@Event.EventData.Data.RelativeTargetName` contains RemCom-related file patterns including `RemCom_stdin`, `RemCom_stdout`, or `RemCom_stderr`. Impacket's PsExec tool uses these specific named pipe files to establish command execution on remote systems. Unlike Microsoft's official PsExec tool, Impacket PsExec creates distinctive file artifacts that can be reliably detected, making this an effective indicator of lateral movement activity commonly used by attackers.

## Triage and response{% #triage-and-response %}

- Examine the source IP address and user account associated with the IPC$ share access to determine the origin of the lateral movement attempt on `{{host}}`.
- Check for corresponding process execution or command activity that may have been executed through the PsExec session.
- Review authentication logs to identify how the attacker obtained credentials necessary for the remote execution.
- Analyze network traffic patterns to identify other systems that may have been targeted by the same lateral movement campaign.
- Investigate the initial compromise vector and determine if the source system is also compromised and requires isolation.
