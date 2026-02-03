# Source: https://docs.datadoghq.com/security/default_rules/def-000-ggb.md

---
title: Windows PowerShell disable ETW trace
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows PowerShell disable ETW trace
---

# Windows PowerShell disable ETW trace

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detects attempts to disable Event Tracing for Windows (ETW) using PowerShell commands.

## Strategy{% #strategy %}

This rule monitors Windows event logs for PowerShell script block execution that attempts to disable Event Tracing for Windows (ETW). It specifically looks for PowerShell commands that use `Remove-EtwTraceProvider`, or `Set-EtwTraceProvider` with the hexadecimal value `0x11`, which disables trace logging. ETW is a critical logging mechanism in Windows that provides telemetry and is heavily used for security monitoring and forensics. Attackers often attempt to disable ETW to evade detection, prevent logging of their activities, and impair defense mechanisms.

## Triage & Response{% #triage--response %}

- Examine the PowerShell script block content on `{{host}}` to verify the ETW trace disabling attempt and understand the full context of the execution.
- Identify the user account that executed the PowerShell command and determine if this activity was authorized.
- Review authentication logs to determine if the account used was compromised or if this was a legitimate administrative action.
- Verify current ETW status on the system to determine if trace providers were successfully modified.
- Implement privileged access management to restrict who can modify ETW settings.
