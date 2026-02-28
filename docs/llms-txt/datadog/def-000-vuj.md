# Source: https://docs.datadoghq.com/security/default_rules/def-000-vuj.md

---
title: Windows PowerShell Disable-WindowsOptionalFeature command
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell
  Disable-WindowsOptionalFeature command
---

# Windows PowerShell Disable-WindowsOptionalFeature command

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detects attempts to disable Windows Defender components using PowerShell's Disable-WindowsOptionalFeature cmdlet.

## Strategy{% #strategy %}

This rule monitors Windows event logs for PowerShell script block execution that includes the `Disable-WindowsOptionalFeature` cmdlet with specific parameters that target Windows Defender components. The detection looks for command executions that include the `-Online` and `-FeatureName` parameters along with specific Windows Defender component names such as `Windows-Defender-Gui`, `Windows-Defender-Features`, `Windows-Defender`, or `Windows-Defender-ApplicationGuard`. This activity is concerning because it represents an attempt to disable security controls that protect the system. Attackers often try to disable Windows Defender components to evade detection and reduce the risk of being caught.

## Triage & Response{% #triage--response %}

- Review the complete PowerShell script block content to understand exactly which Windows Defender features were targeted on `{{host}}`.
- Determine the user account that executed the PowerShell command and verify if they should have permission to modify security settings.
- Verify the current status of Windows Defender components to confirm if the disablement was successful.
- Examine surrounding PowerShell commands and system activity for other suspicious behavior.
- If unauthorized, immediately re-enable the Windows Defender components using Enable-WindowsOptionalFeature.
- Scan the system with an alternative antivirus solution to identify potential malware that may have been installed.
