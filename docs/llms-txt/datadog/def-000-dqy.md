# Source: https://docs.datadoghq.com/security/default_rules/def-000-dqy.md

---
title: Windows RottenPotato like attack pattern
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows RottenPotato like attack
  pattern
---

# Windows RottenPotato like attack pattern

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1557-adversary-in-the-middle](https://attack.mitre.org/techniques/T1557)
## Goal{% #goal %}

Detects authentication patterns associated with RottenPotato and similar token impersonation attacks used to escalate privileges on Windows systems.

## Strategy{% #strategy %}

This rule monitors Windows event logs for logon events (Event ID `4624`) with specific characteristics that match the authentication pattern used in RottenPotato attacks. The detection looks for logon type 3 (network) authentications coming from the local loopback addresses (127.0.0.1 or ::1) with a blank workstation name ("-") and using the "ANONYMOUS LOGON" account. RottenPotato and similar attacks (such as JuicyPotato and SweetPotato) exploit the Windows token impersonation mechanism by setting up a fake NTLM authentication server locally and performing a man-in-the-middle attack against the system's own NTLM authentication process. This technique allows attackers to capture and impersonate authentication tokens with SYSTEM privileges, effectively elevating their access rights from a lower-privileged account.

## Triage & Response{% #triage--response %}

- Examine the complete logon event details to confirm the RottenPotato attack pattern on `{{host}}`.
- Identify the local user account or process that was active at the time of the suspicious authentication.
- Check process creation logs preceding the event to determine what binary or script might have initiated the attack.
- Review file creation events for indicators that a privilege escalation tool was dropped onto the system.
- Analyze the process tree to understand the full attack chain leading to the token impersonation attempt.
- Remove any malicious binaries related to RottenPotato variants (common filenames include potato.exe, juicypotato.exe, sweetpotato.exe).
