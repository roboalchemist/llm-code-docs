# Source: https://docs.datadoghq.com/security/default_rules/def-000-rhl.md

---
title: Windows PowerShell Veeam backup servers credential dumping script execution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell Veeam backup servers
  credential dumping script execution
---

# Windows PowerShell Veeam backup servers credential dumping script execution

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003)
## Goal{% #goal %}

Detects execution of PowerShell scripts attempting to extract credentials from Veeam Backup servers.

## Strategy{% #strategy %}

This rule monitors PowerShell script block logging for scripts that interact with Veeam Backup's protected storage. The detection identifies scripts accessing `Veeam.Backup.Common.ProtectedStorage`, using `GetLocalString` methods, and executing SQL commands, which are commonly used to extract stored credentials from Veeam Backup and Replication servers.

## Triage & Response{% #triage--response %}

- Analyze the full PowerShell script content executed on `{{host}}` for malicious commands.
- Review the user account that executed the script and verify if they have legitimate access to Veeam servers.
- Examine any data exfiltration attempts from the Veeam backup infrastructure.
- Check for unauthorized access to backup server configurations and credentials.
- Reset compromised Veeam backup server credentials.
- Restrict access to Veeam backup server configuration files.
