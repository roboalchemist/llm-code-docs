# Source: https://docs.datadoghq.com/security/default_rules/def-000-azr.md

---
title: Distributed Credential Stuffing campaign (attempt count)
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Distributed Credential Stuffing
  campaign (attempt count)
---

# Distributed Credential Stuffing campaign (attempt count)
Tactic:[TA0042-resource_development](https://attack.mitre.org/tactics/TA0042)Technique:[T1586-compromise-accounts](https://attack.mitre.org/techniques/T1586) 
### Goal{% #goal %}

Detect Account Takeover (ATO) attempts on services. ATO attempts include [brute force](https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-007_Credential_Cracking.html), dictionary, and distributed [credential stuffing](https://owasp.org/www-project-automated-threats-to-web-applications/assets/oats/EN/OAT-008_Credential_Stuffing.html) attacks.

This detection rule is designed to detect distributed credential stuffing campaigns, where an attacker uses many IP addresses to attempt to log into different accounts using stolen password lists. The attacker will often try a single password per account, and may make a few login attempts with each individual IP address.

### Required business logic events{% #required-business-logic-events %}

Datadog auto-instruments many event types. [Review](https://app.datadoghq.com/security/appsec/business-logic) your instrumented business logic events. This detection requires the following instrumented events: `users.login.failure` with `usr.login` populated.

### Strategy{% #strategy %}

Monitor login events and track the number of failed login attempts. Generate a `Low` severity signal when the rate of login failures deviate from historical trends. Datadog requires a number of users to be logged in and associated with multiple IP addresses to be attempting logins. This helps deduplicate any non-distributed signals (such as brute force and credential stuffing) that may appear.

The monitored login attempts exclude local IP addresses to help reduce false positives.

### Triage and response{% #triage-and-response %}

1. Review the attacker clusters in the "Attacker Attributes" section to identify the attacker. You may see a mix of legitimate and malicious activity. Confirm that the activity from the cluster correlates with the rise in login failures without legitimate activity so real users are not accidentally blocked.
1. Create a custom WAF rule to block on those attributes if possible.
1. Review any successful logins from the cluster. Those accounts may be compromised and should be blocked until the passwords are reset.
