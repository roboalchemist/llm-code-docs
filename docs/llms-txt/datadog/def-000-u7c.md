# Source: https://docs.datadoghq.com/security/default_rules/def-000-u7c.md

---
title: Windows MSSQL XPCmdshell suspicious execution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows MSSQL XPCmdshell suspicious
  execution
---

# Windows MSSQL XPCmdshell suspicious execution
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1059-command-and-scripting-interpreter](https://attack.mitre.org/techniques/T1059)
## Goal{% #goal %}

Detects suspicious execution of xp_cmdshell in Microsoft SQL Server to run system commands.

## Strategy{% #strategy %}

This rule monitors Windows event logs for Microsoft SQL Server audit events related to xp_cmdshell usage. It specifically looks for event ID `33205` from MSSQL providers where logs contain both "xp_cmdshell" and "EXEC" strings. The xp_cmdshell extended stored procedure allows SQL Server to execute operating system commands through the SQL Server service account, which is frequently abused by attackers who have gained access to SQL Server instances. This functionality allows attackers to run arbitrary commands on the database server, potentially leading to full system compromise, data theft, or lateral movement through the environment.

## Triage & Response{% #triage--response %}

- Examine the SQL Server logs on `{{host}}` to verify the xp_cmdshell execution and identify the specific commands executed.
- Determine which SQL account executed the xp_cmdshell command and check if it was an authorized action.
- Review the authentication events preceding the xp_cmdshell execution to identify how the account gained access.
- Check for any new files, processes, or network connections created after the suspicious activity.
- Verify if xp_cmdshell was recently enabled, as it's typically disabled by default in secure configurations.
- Disable the xp_cmdshell extended stored procedure if not legitimately required.
- Reset credentials for the SQL Server service account and any compromised database user accounts.
- Review SQL Server audit settings to ensure comprehensive monitoring of privileged operations.
