# Source: https://docs.datadoghq.com/security/default_rules/def-007-b8k.md

---
title: Windows CobaltStrike service installations
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows CobaltStrike service
  installations
---

# Windows CobaltStrike service installations

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0008-lateral-movement](https://attack.mitre.org/tactics/TA0008)Technique:[T1569-system-services](https://attack.mitre.org/techniques/T1569) 
## Goal{% #goal %}

Detects instances where a Cobalt Strike beacon is installed as a Windows service.

## Strategy{% #strategy %}

This detection monitors Windows System event logs for Event ID 7045 (A new service was installed in the system), focused on service installation patterns common to Cobalt Strike deployments.

Cobalt Strike is a commercial penetration testing tool that is frequently abused by threat actors for post-exploitation activities. Its beacons often use specific patterns when installed as services, including encoded PowerShell commands, suspicious paths, and network communication techniques.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` system where the suspicious service was installed.
- Review the service details, including service name, path, and account under which it's configured to run.
- Extract the binary path from the event logs and check if it points to a non-standard location.
- Identify the user or process that installed the service by correlating with Event ID 4697.
- Verify if the service is running with SYSTEM privileges or an unexpected user account.
- Analyze the service binary using file reputation services or malware analysis tools.
- Correlate with other suspicious activity by examining PowerShell logs, process creation events, and network connections.
- Look for related indicators such as new user account creation or users added to admin groups.
- Stop and disable the service using the Service Control Manager if malicious activity is confirmed.
- Remove the service binary and check for additional persistence mechanisms.
- Investigate potential lateral movement by reviewing network share access and logon events.
- Isolate the affected system until remediation is complete to prevent further lateral movement.
