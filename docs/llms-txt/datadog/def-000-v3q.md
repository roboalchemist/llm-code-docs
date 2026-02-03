# Source: https://docs.datadoghq.com/security/default_rules/def-000-v3q.md

---
title: Windows register new logon process by Rubeus
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows register new logon process by
  Rubeus
---

# Windows register new logon process by Rubeus

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1558-steal-or-forge-kerberos-tickets](https://attack.mitre.org/techniques/T1558) 
## Goal{% #goal %}

Detects registration of suspicious logon processes matching patterns associated with the Rubeus Kerberos manipulation tool.

## Strategy{% #strategy %}

This rule monitors for event ID `4611` which tracks new logon process registrations. The detection specifically looks for logon process names matching `User32LogonProcesss`, a common misspelling used by the Rubeus tool when registering new logon processes for Kerberos ticket manipulation.

## Triage & Response{% #triage--response %}

- Verify the process that registered the new logon process on `{{host}}` and its parent process.
- Examine running processes and loaded modules for signs of Rubeus or other Kerberos exploitation tools.
- Review authentication logs for unusual Kerberos ticket requests or modifications.
- Reset passwords for any potentially compromised accounts.
- Monitor for additional Kerberos ticket manipulation attempts.
