# Source: https://docs.datadoghq.com/security/default_rules/def-000-abi.md

---
title: Windows PowerShell create volume shadow copy
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell create volume shadow
  copy
---

# Windows PowerShell create volume shadow copy

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003)
## Goal{% #goal %}

Detects PowerShell commands that create Volume Shadow Copies (VSS).

## Strategy{% #strategy %}

This rule monitors PowerShell script block logging for commands that create Volume Shadow Copies. VSS is a legitimate Windows feature that creates point-in-time snapshots of volumes, primarily for backup purposes.

The query searches the `@Event.EventData.Data.ScriptBlockText` field for PowerShell script blocks that contain the terms `Win32_ShadowCopy`, `Create`, and `ClientAccessible`. This combination indicates PowerShell code that's using WMI to create a shadow copy that can be accessed by the client.

While VSS is a legitimate Windows feature, its use through PowerShell is uncommon in routine operations. Attackers frequently abuse this functionality to access locked system files like `NTDS.dit` (Active Directory database) and registry hives containing credential information. By creating shadow copies, attackers can bypass file locks and access sensitive files that would otherwise be unavailable for reading.

## Triage & Response{% #triage--response %}

- Identify the user account that executed the PowerShell shadow copy command on `{{host}}`.
- Determine if the account has legitimate administrative permissions to perform this action.
- Review access logs to domain controllers if Active Directory database access is suspected.
- Check for subsequent file access or copy operations targeting the shadow copy.
- Examine additional PowerShell commands executed before and after the shadow copy creation.
- Look for evidence of access to sensitive files like `NTDS.dit`, `SAM`, or `SYSTEM` registry hives.
- Verify if any data exfiltration occurred following the shadow copy creation.
- Assess whether the shadow copy creation was part of authorized system administration or backup procedures.
- Reset credentials for any accounts involved if unauthorized activity is confirmed.
