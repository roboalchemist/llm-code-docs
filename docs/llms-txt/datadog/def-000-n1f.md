# Source: https://docs.datadoghq.com/security/default_rules/def-000-n1f.md

---
title: Windows eventlog cleared
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows eventlog cleared
---

# Windows eventlog cleared

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detects when critical Windows event logs are cleared.

## Strategy{% #strategy %}

This rule monitors for event ID `104` from the `Microsoft-Windows-Eventlog` provider, which indicates that an event log has been cleared. The query specifically focuses on security-relevant logs including `Security`, `System`, `PowerShell/Operational`, `PowerShellCore/Operational`, `Sysmon/Operational`, and `Windows PowerShell`.

Event logs record crucial system and security activities that are vital for incident response and forensic analysis. The `@Event.EventData.Data.Channel` field identifies the specific log that was cleared. While log clearing can occasionally occur during routine maintenance, the clearing of certain logs is highly suspicious and rarely performed in normal operations.

Attackers frequently clear event logs to remove evidence of their intrusion, lateral movement, privilege escalation, or other malicious activities. This action significantly hampers security investigations and represents a serious attempt to avoid detection.

## Triage & Response{% #triage--response %}

- Identify the specific log that was cleared on `{{host}}` and the user account that performed the action.
- Determine if the account that cleared the logs has legitimate administrative permissions.
- Review any available logs before the clearing event for suspicious activities.
- Examine authentication logs for unusual login patterns or unauthorized access.
- Look for other anti-forensic techniques being used, such as disabling auditing or tampering with other logs.
- Search for process execution events that might indicate the presence of log-clearing tools.
- Assess whether the log clearing was part of documented maintenance procedures.
- Reset credentials for any accounts involved in unauthorized log clearing.
