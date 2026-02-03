# Source: https://docs.datadoghq.com/security/default_rules/def-000-gzt.md

---
title: Windows PowerShell Invoke-Mimikatz script
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell Invoke-Mimikatz
  script
---

# Windows PowerShell Invoke-Mimikatz script

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003) 
## Goal{% #goal %}

Detects execution of Mimikatz credential dumping tool through PowerShell scripts.

## Strategy{% #strategy %}

This rule monitors Windows event logs for PowerShell script block execution containing known Mimikatz commands and functions. It triggers when detecting PowerShell commands containing specific function names and command patterns commonly associated with Mimikatz operations. Mimikatz is a well-known credential dumping tool that extracts plaintext passwords, hashes, PIN codes, and Kerberos tickets from memory. The tool is commonly used by attackers after gaining initial access to extract credentials for lateral movement, privilege escalation, and persistence. Detection of these script patterns indicates an active attempt to harvest credentials from the system.

## Triage & Response{% #triage--response %}

- Examine the PowerShell script block content on `{{host}}` to verify the Mimikatz execution attempt and understand its full context.
- Identify the user account that executed the PowerShell script and determine how the account may have been compromised.
- Review authentication logs prior to the Mimikatz execution to identify how the attacker gained initial access.
- Check for lateral movement attempts from the affected host to other systems in the environment.
- Search for evidence of data exfiltration or other post-exploitation activities.
- Force password resets for domain admin accounts and other privileged accounts even if not directly observed in the attack.
- Scan the system for additional malware and backdoors that may have been installed.
- Review PowerShell logging configurations across the environment and ensure Script Block Logging is enabled.
