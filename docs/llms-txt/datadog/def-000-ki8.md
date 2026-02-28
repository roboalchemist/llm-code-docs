# Source: https://docs.datadoghq.com/security/default_rules/def-000-ki8.md

---
title: Windows MSSQL disable audit settings
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows MSSQL disable audit settings
---

# Windows MSSQL disable audit settings

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detects attempts to disable or modify SQL Server audit settings through ALTER or DROP commands.

## Strategy{% #strategy %}

This rule monitors for event ID `33205` which captures SQL Server audit-related commands. The detection focuses on ALTER and DROP operations targeting SERVER AUDIT configurations, which could indicate attempts to disable security monitoring capabilities within the SQL Server environment.

## Triage & Response{% #triage--response %}

- Examine the specific audit configuration changes made to the SQL Server instance on `{{host}}`.
- Verify if the modifications were part of authorized maintenance or change management.
- Check for any concurrent suspicious activities around the time of the audit changes.
- Restrict audit configuration modifications to authorized database administrators.
