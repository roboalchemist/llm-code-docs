# Source: https://docs.datadoghq.com/security/default_rules/def-000-wjt.md

---
title: Windows service installed by suspicious client
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows service installed by suspicious
  client
---

# Windows service installed by suspicious client

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1543-create-or-modify-system-process](https://attack.mitre.org/techniques/T1543) 
## Goal{% #goal %}

Detects the installation of Windows services by suspicious or unusual client processes.

## Strategy{% #strategy %}

This detection monitors Windows event logs through two separate queries targeting different log sources. The first query examines Security Event logs for Event ID 4697 (A service was installed in the system) where either the ClientProcessId or ParentProcessId is 0, excluding known legitimate services. The second query looks at System Event logs for Event ID 7045 (A new service was installed) with ProcessID 0 from the "Service Control Manager" provider.

Windows services provide a way to execute code with SYSTEM privileges and persist across reboots, making them attractive targets for attackers seeking to maintain access to compromised systems. The detection excludes known legitimate services from vendors like PDQ and Ivanti to reduce false positives.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` system where the suspicious service installation occurred.
- Examine the service details, including name, description, path, and start type from the event data.
- Look for unusual service names, random strings, or execution from non-standard directories.
- Determine which account was used to install the service by reviewing the Security event logs.
- Extract the binary path from service details and verify if it points to legitimate software.
- Check if the service is configured to run under SYSTEM or an unexpected user account.
- Examine the binary file's metadata, certificate, and reputation with security tools.
- Stop and disable the service if it appears suspicious.
- Investigate the service binary through malware analysis if needed.
- Identify any lateral movement attempts from the system with the suspicious service.

## Changelog{% #changelog %}

- 24 September 2025 - Updated severity.
