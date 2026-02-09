# Source: https://docs.datadoghq.com/security/default_rules/def-000-oc4.md

---
title: Windows PowerShell disable command history
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell disable command
  history
---

# Windows PowerShell disable command history

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1070-indicator-removal](https://attack.mitre.org/techniques/T1070) 
## Goal{% #goal %}

Detects attempts to disable PowerShell command history by removing the PSReadLine module.

## Strategy{% #strategy %}

This rule monitors PowerShell script block logging for commands that remove the PSReadLine module. The PSReadLine module provides command history functionality in PowerShell, storing a record of executed commands that can be accessed via the arrow keys or the Get-History cmdlet.

The query looks for script blocks containing `Remove-Module` and `psreadline` in the `@Event.EventData.Data.ScriptBlockText` field. When attackers execute PowerShell commands for malicious purposes, they often attempt to cover their tracks by disabling command history to prevent forensic analysis of their activities.

Removing the PSReadLine module is a rare operation in normal administrative activity, as command history provides valuable functionality for legitimate users. The deliberate removal of this module indicates an attempt to hide command execution and is a common anti-forensic technique.

## Triage & Response{% #triage--response %}

- Identify the user account that executed the PowerShell command on `{{host}}` to disable command history.
- Review all PowerShell commands executed before and after the `PSReadLine` module removal.
- Examine other event logs on `{{host}}` for signs of lateral movement or privilege escalation attempts such as Event ID `4624` (logons from new IPs), `4672` (admin privileges.granted), `4688` (suspicious process creations), or `4697` (service installations).
- Look for other anti-forensic techniques such as event log clearing or scheduled task creation.
- Determine if the command was executed locally or via remote access methods.
- Check for unauthorized access to the account that disabled the command history.
- Capture and preserve any remaining forensic artifacts from `{{host}}` such as memory dumps or system logs.
- Reset the affected user account's credentials if compromised.
