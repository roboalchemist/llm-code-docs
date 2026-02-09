# Source: https://docs.datadoghq.com/security/default_rules/def-000-b8k.md

---
title: Windows PurpleSharp execution
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows PurpleSharp execution
---

# Windows PurpleSharp execution

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0042-resource-development](https://attack.mitre.org/tactics/TA0042)Technique:[T1587-develop-capabilities](https://attack.mitre.org/techniques/T1587) 
## Goal{% #goal %}

Detects execution of PurpleSharp, an adversary simulation tool designed to help security teams test detection capabilities.

## Strategy{% #strategy %}

This detection monitors Windows event logs for process execution events containing indicators of PurpleSharp usage. The detection uses two approaches: looking for process names containing "PurpleSharp.exe" or "purplesharp" in the `NewProcessName` field, and checking command lines containing "PurpleSharp" or "xyz123456.exe" (a common test filename used by the tool) in the `ProcessCommandLine` field.

PurpleSharp is a legitimate security testing tool that simulates common attack techniques to evaluate detection capabilities. While it has legitimate uses for security teams, unauthorized presence of this tool could indicate either rogue security testing, or potentially an attacker using it to test evasion techniques before launching actual attacks. The tool is designed to emulate various MITRE ATT&CK techniques, making it important to identify when it's being used in your environment.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` where PurpleSharp execution was detected.
- Determine if there is an authorized penetration test or purple team exercise currently in progress.
- Look for evidence of data collection or exfiltration that may indicate a real attack.
- Identify the user account that executed PurpleSharp by reviewing process creation events.
- Examine the specific command line arguments used, to understand which attack techniques were simulated.
- Review login events prior to the PurpleSharp execution, to identify how access was gained.
- Contain the affected system and revoke access if the activity is unauthorized.
- Verify if additional systems have been targeted by checking for lateral movement indicators.
