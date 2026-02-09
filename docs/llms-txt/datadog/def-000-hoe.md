# Source: https://docs.datadoghq.com/security/default_rules/def-000-hoe.md

---
title: Windows credential dumping via WER application error
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows credential dumping via WER
  application error
---

# Windows credential dumping via WER application error

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003) 
## Goal{% #goal %}

Detects Windows Error Reporting events triggered by Local Security Authority Subsystem Service (LSASS) crashes indicative of active credential dumping attempts.

## Strategy{% #strategy %}

This rule monitors Application Error events with event ID `1000` where `@Event.EventData.Data.Application` is `lsass.exe` and `@Event.EventData.Data.ExceptionCode` is `c0000001`.

LSASS stores authentication credentials and security tokens in memory. Credential dumping tools often interact with LSASS memory in ways that cause access violations, resulting in process crashes with specific exception codes.

## Triage & Response{% #triage--response %}

- Examine the Application event logs on `{{host}}` for details about the LSASS crash.
- Review process execution history for credential dumping tools like Mimikatz.
- Check for unauthorized authentication attempts using potentially extracted credentials.
- Identify any lateral movement attempts from `{{host}}`.
- Capture memory dumps if available for forensic analysis.
- Force password resets for all accounts accessed on the affected system.
