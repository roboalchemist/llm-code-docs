# Source: https://docs.datadoghq.com/security/default_rules/def-000-krx.md

---
title: Windows DiagTrackEoP default login username
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows DiagTrackEoP default login
  username
---

# Windows DiagTrackEoP default login username

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detects exploitation of the DiagTrack privilege escalation vulnerability using the default username indicator.

## Strategy{% #strategy %}

This rule monitors Windows Security Audit events, where `@evt.id` is `4624` for NewCredentials logon type `9` when `@Event.EventData.Data.TargetOutboundUserName` is set to "thisisnotvaliduser". This specific username is a hardcoded indicator used by proof-of-concept exploits targeting the DiagTrack service privilege escalation vulnerability (CVE-2021-31958). The vulnerability allows local attackers to escalate privileges from low-privileged users to SYSTEM through manipulation of the Connected User Experiences and Telemetry service.

## Triage and response{% #triage-and-response %}

- Examine the source process and user context that triggered the NewCredentials logon with the default exploit username on `{{host}}`.
- Check for signs of successful privilege escalation by reviewing subsequent high-privilege process execution or system-level activities.
- Analyze the system for presence of known DiagTrack exploit tools or suspicious PowerShell activity that may have triggered the vulnerability.
- Review system patching status to determine if the CVE-2021-31958 vulnerability has been properly remediated.
- Investigate the initial access vector that allowed the attacker to execute the privilege escalation exploit on the system.
