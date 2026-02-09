# Source: https://docs.datadoghq.com/security/default_rules/def-000-ue8.md

---
title: Windows replay attack detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows replay attack detected
---

# Windows replay attack detected

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1558-steal-or-forge-kerberos-tickets](https://attack.mitre.org/techniques/T1558) 
## Goal{% #goal %}

Detects when a Windows replay attack is identified by the system.

## Strategy{% #strategy %}

This detection monitors Windows event logs for Event ID 4649, which specifically indicates that a replay attack was detected by the security system. The event is generated when Windows identifies an authentication attempt using previously captured credentials or tickets.

A replay attack occurs when an attacker captures authentication traffic and later reuses (or "replays") it to authenticate as the legitimate user, without needing to know their actual credentials. Windows systems can detect such attacks when timestamps or other indicators in the authentication data reveal that the information has been captured and replayed. This technique is commonly used in attempts to forge or reuse Kerberos tickets for unauthorized access.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` where the replay attack was detected.
- Review the event details to determine the targeted user account and source of the attack.
- Check for successful authentication events following the replay attack.
- Examine network logs to identify the source IP address and correlate with other suspicious activities.
- Look for evidence of lateral movement from potentially compromised accounts.
- Verify if the affected user account was involved in other suspicious activities.
- Reset credentials for the targeted account if compromise is confirmed.
- Review Kerberos security settings on domain controllers, particularly ticket lifetime and encryption.
