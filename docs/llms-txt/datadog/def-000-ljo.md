# Source: https://docs.datadoghq.com/security/default_rules/def-000-ljo.md

---
title: Windows OpenSSH brute force attempt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Windows OpenSSH brute force attempt
---

# Windows OpenSSH brute force attempt

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detects brute force attacks targeting Windows OpenSSH server through multiple invalid user authentication attempts.

## Strategy{% #strategy %}

This rule monitors Windows OpenSSH server events where `@evt.id` is `4` from the `sshd` process when `@Event.EventData.Data.payload` contains `Invalid user` messages. The detection triggers when more than three distinct invalid user attempts occur, indicating potential credential stuffing or brute force attacks. OpenSSH servers log failed authentication attempts when attackers try to authenticate with non-existent usernames, providing a reliable indicator of reconnaissance and brute force activity targeting the SSH service.

## Triage and response{% #triage-and-response %}

- Examine the source IP addresses attempting SSH connections to `{{host}}` and determine if they represent legitimate user locations or suspicious external sources.
- Review the specific invalid usernames being attempted to understand the attacker's reconnaissance methodology and target identification.
- Check for any successful SSH authentication attempts from the same source addresses following the invalid user attempts.
- Analyze network logs to identify the scope of the brute force campaign and other systems that may be targeted.
- Consider implementing SSH access controls, fail2ban rules, or network-level blocking to prevent continued brute force attempts.
