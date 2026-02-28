# Source: https://docs.datadoghq.com/security/default_rules/def-000-bfe.md

---
title: Windows PowerShell Rubeus execution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows PowerShell Rubeus execution
---

# Windows PowerShell Rubeus execution

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0008-lateral-movement](https://attack.mitre.org/tactics/TA0008)Technique:[T1550-use-alternate-authentication-material](https://attack.mitre.org/techniques/T1550)
## Goal{% #goal %}

Detects execution of Rubeus, a Kerberos attack tool used for ticket extraction, modification, forgery, and replay attacks.

## Strategy{% #strategy %}

This rule monitors Windows PowerShell script block logs for commands containing distinct Rubeus command-line arguments. Rubeus is a toolset designed for Kerberos interaction and abuse, commonly used by attackers to extract tickets, perform pass-the-ticket attacks, request and forge tickets, and conduct other Kerberos-based attacks. The presence of these command patterns is highly suspicious as Rubeus is primarily used for offensive security testing or actual attacks and rarely has legitimate use cases in most enterprise environments.

## Triage & Response{% #triage--response %}

- Analyze the full PowerShell script block content to understand which specific Rubeus capabilities were utilized on `{{host}}`.
- Identify the user account that executed the Rubeus commands and determine if they are authorized to perform security testing.
- Check for successful ticket creation, extraction, or manipulation by reviewing associated event logs around the same timeframe.
- Examine authentication events to identify potential lateral movement or privilege escalation following Rubeus execution.
- Review process creation events to identify the source of the Rubeus tool on the system.
