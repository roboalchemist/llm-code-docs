# Source: https://docs.datadoghq.com/security/default_rules/def-000-www.md

---
title: Windows moriya rootkit
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows moriya rootkit
---

# Windows moriya rootkit

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1543-create-or-modify-system-process](https://attack.mitre.org/techniques/T1543) 
## Goal{% #goal %}

Detects installation of the Moriya rootkit, a sophisticated kernel-mode backdoor used in targeted attacks.

## Strategy{% #strategy %}

This detection monitors Windows event logs for service installation events where Event ID 7045 is recorded with specific characteristics known to be associated with the Moriya rootkit. The detection specifically looks for the service name "ZzNetSvc" being registered through the Service Control Manager.

Moriya is a sophisticated kernel-mode rootkit that operates as a passive backdoor, allowing attackers to maintain persistent access while evading detection. It operates by registering a Windows service using specific identifiers, which this detection targets. The rootkit intercepts network traffic and can execute arbitrary commands with kernel-level privileges, making it an extremely dangerous threat when deployed.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` where the Moriya rootkit service was installed.
- Determine which user account or process initiated the service installation by reviewing related logs.
- Examine the binary file path used for the ZzNetSvc service to confirm the presence of the rootkit.
- Check for additional persistence mechanisms that may have been established.
- Look for evidence of lateral movement from the infected system.
- Analyze memory dumps and disk images for hidden components of the rootkit if possible.
- Immediately isolate the affected system from the network to prevent further command and control communications.
- Consider rebuilding the affected system rather than attempting remediation.
- Review network logs to identify potential command and control servers.
