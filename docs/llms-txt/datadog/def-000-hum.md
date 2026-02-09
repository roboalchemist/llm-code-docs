# Source: https://docs.datadoghq.com/security/default_rules/def-000-hum.md

---
title: Windows PowerShell scripts installed as services
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows PowerShell scripts installed as
  services
---

# Windows PowerShell scripts installed as services

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1569-system-services](https://attack.mitre.org/techniques/T1569) 
## Goal{% #goal %}

Detects PowerShell scripts being installed as Windows services, which can be used for persistence and privilege escalation.

## Strategy{% #strategy %}

This rule monitors Windows event logs for service installation events that reference PowerShell. It specifically looks for Windows Event ID `4697` (Service Installation) where the service name contains PowerShell-identifiable strings. Installing PowerShell scripts as services is uncommon in legitimate administrative scenarios and is often used by attackers as a persistence mechanism.

## Triage & Response{% #triage--response %}

- Examine the service details on `{{host}}` to verify the PowerShell service installation and identify the exact command or script being executed.
- Identify the user account that installed the service and determine if this was an authorized administrative action.
- Review the content of the PowerShell script being executed by the service to understand its functionality and intent.
- Check if the service was installed remotely, which would be a stronger indicator of malicious activity.
- Analyze any network connections established by the PowerShell service for potential command and control activities.
- Reset credentials for any accounts involved in installing unauthorized services.
