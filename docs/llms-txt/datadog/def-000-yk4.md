# Source: https://docs.datadoghq.com/security/default_rules/def-000-yk4.md

---
title: Credential Stuffing attack
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Credential Stuffing attack
---

# Credential Stuffing attack
Tactic:[TA0042-resource_development](https://attack.mitre.org/tactics/TA0042)Technique:[T1586-compromise-accounts](https://attack.mitre.org/techniques/T1586) 
### Goal{% #goal %}

Detect Account Takeover (ATO) attempts on services. ATO attempts include [brute force](https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-007_Credential_Cracking.html), dictionary, and distributed [credential stuffing](https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-008_Credential_Stuffing.html) attacks.

This detection rule is designed to detect credential stuffing campaigns, where an IP attempts to log in to different accounts using stolen password lists, often trying a single password per account.

### Required business logic events{% #required-business-logic-events %}

Datadog auto-instruments many event types. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events. This detection requires the following instrumented events:

- `users.login.failure`
- `users.login.success`

### Strategy{% #strategy %}

Monitor login events and track failed logins. Generate a `Low` severity signal when an IP address exceeds the threshold of 30 failed logins (or 15 if the IP has a poor reputation), and in which more than 5 different user accounts were attacked. A fallback is also present in case the instrumentation doesn't provide a `usr.login` when the user doesn't exist.The signal severity is increased to `Critical` when the IP address has a successful login, and the compromised account is highlighted.

### Triage and response{% #triage-and-response %}

1. Consider [blocking](https://docs.datadoghq.com/security/application_security/threats/#slow-down-attacks%5D) the attacking IP addresses temporarily to slow attacks.
1. Check compromised accounts, suspend account access temporarily, and force password change.
1. Implement and enable MFA (multi-factor authentication) when possible.
