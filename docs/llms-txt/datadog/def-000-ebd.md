# Source: https://docs.datadoghq.com/security/default_rules/def-000-ebd.md

---
title: Windows PowerShell volume shadow copy deletion
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell volume shadow copy
  deletion
---

# Windows PowerShell volume shadow copy deletion

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1059-command-and-scripting-interpreter](https://attack.mitre.org/techniques/T1059) 
## Goal{% #goal %}

Detects deletion of Windows Volume Shadow Copies through PowerShell and WMI/CIM commands.

## Strategy{% #strategy %}

This rule monitors Windows event logs for PowerShell script block execution that targets Volume Shadow Copies for deletion. It specifically looks for PowerShell commands that use WMI or CIM interfaces to interact with `Win32_ShadowCopy` objects, combined with various deletion methods. Volume Shadow Copy Service (VSS) is a Windows feature that creates backup copies or snapshots of files or volumes, even when they're in use. Attackers commonly delete these shadow copies to prevent recovery of encrypted files during ransomware attacks or to remove forensic evidence. This activity is a strong indicator of an attack designed to inhibit system recovery capabilities.

## Triage & Response{% #triage--response %}

- Examine the PowerShell script block content on `{{host}}` to verify the shadow copy deletion attempt and understand the full context of the command execution.
- Identify the user account that executed the PowerShell commands and determine if this was authorized activity.
- Review authentication events prior to the shadow copy deletion to identify potential account compromise.
- Check for other indicators of ransomware activity, such as unusual file encryption operations or ransom notes.
- Look for evidence of data exfiltration before the shadow copy deletion, which could indicate a multi-stage attack.
- Reset credentials for accounts that executed the suspicious commands if they were compromised.
- Implement PowerShell logging and Script Block Logging across the environment if not already enabled.
