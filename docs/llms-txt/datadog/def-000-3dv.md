# Source: https://docs.datadoghq.com/security/default_rules/def-000-3dv.md

---
title: Windows MSSQL XPCmdshell change
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows MSSQL XPCmdshell change
---

# Windows MSSQL XPCmdshell change

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1059-command-and-scripting-interpreter](https://attack.mitre.org/techniques/T1059) 
## Goal{% #goal %}

Detects a modification to the `xp_cmdshell` configuration in Microsoft SQL Server.

## Strategy{% #strategy %}

This detection monitors Windows event logs for Event ID 15457 from the MSSQLSERVER provider, which indicates configuration changes to the `xp_cmdshell` feature. The detection specifically looks for events containing "xp_cmdshell" while excluding changes where the configuration remains disabled (0 to 0) or is being disabled (1 to 0), focusing instead on cases where the feature is being enabled.

The `xp_cmdshell` extended stored procedure allows SQL queries to execute operating system commands using the SQL Server service account's privileges. When enabled, it can be abused by attackers to run arbitrary commands on the host system, potentially leading to privilege escalation, lateral movement, and data exfiltration.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` SQL Server instance where the `xp_cmdshell` configuration was modified.
- Determine the user who made the modification by examining the SQL Server audit logs.
- Verify if the user who enabled `xp_cmdshell` has legitimate administrative authority over the SQL Server instance.
- Review SQL Server logs for subsequent commands executed via `xp_cmdshell` to identify potential malicious activity.
- Check for unauthorized SQL logins or privileged account usage around the time of the configuration change.
- Examine network connections from the SQL Server to unknown external hosts.
- Disable `xp_cmdshell` immediately if the activity is deemed suspicious or unauthorized.
- Reset credentials for any potentially compromised SQL Server login accounts.
- Review SQL agent jobs and scheduled tasks that might have been created for persistence.
