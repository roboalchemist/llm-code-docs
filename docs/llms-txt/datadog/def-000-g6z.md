# Source: https://docs.datadoghq.com/security/default_rules/def-000-g6z.md

---
title: Windows privilege escalation via local kerberos relay over LDAP
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Windows privilege escalation via local
  kerberos relay over LDAP
---

# Windows privilege escalation via local kerberos relay over LDAP

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1548-abuse-elevation-control-mechanism](https://attack.mitre.org/techniques/T1548) 
## Goal{% #goal %}

Detects potential privilege escalation attempts using local Kerberos relay attacks over LDAP.

## Strategy{% #strategy %}

This detection monitors Windows event logs for successful logon events with specific characteristics of Kerberos relay attacks. The detection looks for Event ID 4624 (successful logon) with Kerberos authentication from the loopback address (127.0.0.1) targeting privileged accounts. It specifically filters for logon type 3 (network logon), Kerberos authentication, a non-zero IP port, and a target SID matching the local Administrator account pattern.

The technique exploits Windows authentication mechanisms to relay Kerberos tickets locally, potentially granting attackers elevated privileges. By monitoring for Kerberos authentication from the loopback address that targets administrator accounts, we can identify attempts to leverage this technique for privilege escalation.

## Triage & Response{% #triage--response %}

- Identify the `{{host}}` where the suspicious Kerberos authentication occurred.
- Review the logon events to determine the source process and user context that initiated the authentication.
- Check for other suspicious activities surrounding the event, such as unusual process creations.
- Look for evidence of LDAP-based attacks by examining LDAP query logs or network traffic.
- Verify if there were any recent patches missing for Kerberos or LDAP services.
- Reset credentials for the affected Administrator account if malicious activity is confirmed.
- Check for persistence mechanisms that may have been established using the elevated privileges.
- Implement LDAP signing and channel binding to prevent future relay attacks.
- Review domain controller security settings and patch levels.
