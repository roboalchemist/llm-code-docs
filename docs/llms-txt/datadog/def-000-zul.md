# Source: https://docs.datadoghq.com/security/default_rules/def-000-zul.md

---
title: Windows MSSQL SPProcoption set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows MSSQL SPProcoption set
---

# Windows MSSQL SPProcoption set

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1505-server-software-component](https://attack.mitre.org/techniques/T1505)
## Goal{% #goal %}

Detects the use of "sp_procoption" in Microsoft SQL Server, which can be used by attackers to establish persistence by marking stored procedures to automatically execute on server startup.

## Strategy{% #strategy %}

This rule monitors Windows event logs for SQL Server audit events with ID `33205` that capture the execution of the "sp_procoption" system stored procedure. The detection specifically looks for SQL statements containing `EXEC` and where the object_name is `sp_procoption`. The sp_procoption stored procedure is used to mark other stored procedures with the "startup" option, which causes SQL Server to automatically execute them when the database service starts. This is a powerful persistence mechanism that attackers can abuse to maintain access or execute malicious code with the privileges of the SQL Server service account. Such activity is rare in most environments and typically only used for legitimate database maintenance that has been thoroughly reviewed.

## Triage & Response{% #triage--response %}

- Analyze the full SQL statement to identify which stored procedure was configured to run at startup on `{{host}}`.
- Examine the content of the affected stored procedure to understand what actions it performs.
- Verify whether this configuration change was authorized through proper change management channels.
- Check who executed the sp_procoption command by reviewing the associated SQL Server authentication logs.
- Review the stored procedure to determine if it contains malicious code such as commands to interact with the operating system.
