# Source: https://docs.datadoghq.com/security/default_rules/def-000-vzv.md

---
title: Windows WinPwn execution patterns
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows WinPwn execution patterns
---

# Windows WinPwn execution patterns

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1555-credentials-from-password-stores](https://attack.mitre.org/techniques/T1555) 
## Goal{% #goal %}

Detects execution of WinPwn, a PowerShell-based penetration testing and offensive security framework used for Windows system enumeration and exploitation.

## Strategy{% #strategy %}

This rule monitors Windows event logs for PowerShell script block text containing specific WinPwn execution patterns. The detection looks for script blocks that include references to `Offline_WinPwn`, `WinPwn`, `WinPwn.exe`, or `WinPwn.ps1`. WinPwn is a PowerShell-based security toolkit primarily used for offensive security testing that combines various functions for reconnaissance, local privilege escalation, credential extraction, and network lateral movement. The presence of WinPwn execution is highly suspicious in most environments as it is typically used by attackers or red teams during post-exploitation phases rather than for regular system administration.

## Triage & Response{% #triage--response %}

- Analyze the full PowerShell script block content to understand which specific WinPwn functions or modules were executed on `{{host}}`.
- Identify the user account that ran the WinPwn commands and determine if they are authorized to perform security testing.
- Examine the process tree to understand how WinPwn was initiated and what other processes it may have spawned.
- Review system logs for evidence of successful credential extraction, privilege escalation, or lateral movement following WinPwn execution.
- Check for data exfiltration attempts by reviewing network logs for unusual outbound connections.
