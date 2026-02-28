# Source: https://docs.datadoghq.com/security/default_rules/def-000-agx.md

---
title: Windows PowerShell suspicious Get-ADDBAccount usage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell suspicious
  Get-ADDBAccount usage
---

# Windows PowerShell suspicious Get-ADDBAccount usage

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003)
## Goal{% #goal %}

Detects PowerShell commands using `Get-ADDBAccount` with BootKey and DatabasePath parameters to extract Active Directory credential hashes directly from database files.

## Strategy{% #strategy %}

This rule monitors PowerShell module logging through `@Event.EventData.Data.Payload` for commands containing `Get-ADDBAccount` along with `BootKey` and `DatabasePath` parameters. This specific DSInternals PowerShell module cmdlet provides functionality to access Active Directory databases directly.

Direct database credential extraction bypasses normal authentication channels and security controls, potentially compromising the entire domain's credential database. This technique requires privileged access and is rarely used for legitimate administrative purposes.

## Triage & Response{% #triage--response %}

- Examine the complete PowerShell command on `{{host}}` including the targeted database path.
- Validate authorization status for the account executing the command.
- Investigate the source and access path of the `NTDS.dit` file being accessed.
- Check for evidence of credential hash data exfiltration activities.
- Look for additional domain controller compromise indicators.
- Initiate emergency password resets for all domain accounts.
