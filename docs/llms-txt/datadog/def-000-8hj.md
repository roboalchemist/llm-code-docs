# Source: https://docs.datadoghq.com/security/default_rules/def-000-8hj.md

---
title: Auth0 brute-force protection disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Auth0 brute-force protection disabled
---

# Auth0 brute-force protection disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when Auth0 [brute-force protection](https://auth0.com/docs/secure/attack-protection/brute-force-protection) is disabled.

## Strategy{% #strategy %}

This rule allows you to monitor Auth0 logs and detect when Auth0 brute-force protection is disabled. Brute-force protection safeguards against a single IP address attacking a single user account. For example, when a given IP address tries and fails multiple times to log in as the same user. Disabling this feature will degrade the security posture of your application, leaving it vulnerable to credential-based attacks like brute force attacks.

## Triage and response{% #triage-and-response %}

1. Investigate the client id `{{@data.client_id}}` to understand if this is an expected operation.
1. Work with your tenant administrator to identify the owner of the application.
1. Speak with the owner of the application to understand if this operation is expected and approved.
1. If the owner of the application is unaware of this operation:
   - Disable the application credentials if possible.
   - Investigate any further activity from the IP `{{@network.client.ip}}` or the client id `{{@data.client_id}}`.
   - Begin your organization's incident response process and investigate.
