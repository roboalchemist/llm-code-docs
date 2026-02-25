# Source: https://docs.datadoghq.com/security/default_rules/def-000-q9d.md

---
title: Windows potential powershell reverseshell connection
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows potential powershell
  reverseshell connection
---

# Windows potential powershell reverseshell connection

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1059-command-and-scripting-interpreter](https://attack.mitre.org/techniques/T1059)
## Goal{% #goal %}

Detects PowerShell processes initiating a reverse shell connection, which is a common technique used by attackers to gain remote access and execute commands on a compromised system.

## Strategy{% #strategy %}

This detection monitors Windows event logs for PowerShell executions that contain specific command patterns associated with reverse shells. It looks for the combination of .NET socket programming indicators typical in reverse shells, including `Net.Sockets.TCPClient` (creating a TCP connection), `GetStream()` (accessing the network stream), and `Write()` (sending data over the connection).

PowerShell reverse shells are a common post-exploitation technique that establish outbound connections from a compromised host to an attacker-controlled server.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` system where the suspicious PowerShell reverse shell was detected.
- Examine the full PowerShell command line to understand the exact technique and destination.
- Identify the IP address and port number that PowerShell attempted to connect to.
- Determine which user account executed the PowerShell command and its privilege level.
- Verify which process spawned PowerShell by reviewing process creation logs.
- Check if the PowerShell process successfully established a network connection.
- Identify any data potentially exfiltrated through the reverse shell by reviewing network logs.
- Terminate the active PowerShell process immediately if the activity is confirmed malicious.
- Isolate the affected system to prevent lateral movement.
- Remove any persistence mechanisms such as scheduled tasks or registry auto run keys.
- Reset credentials for accounts used during the time the reverse shell was active.
