# Source: https://docs.datadoghq.com/security/default_rules/def-000-2su.md

---
title: Auth0 suspicious IP throttling disabled
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Auth0 suspicious IP throttling disabled
---

# Auth0 suspicious IP throttling disabled
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when Auth0 [suspicious IP throttling](https://auth0.com/docs/secure/attack-protection/suspicious-ip-throttling) is disabled.

## Strategy{% #strategy %}

This rule allows you to monitor Auth0 logs and detect when Auth0 suspicious IP throttling is disabled. Suspicious IP throttling blocks traffic from any IP address that rapidly attempts too many logins or signups. This helps protect your applications from high-velocity attacks that target multiple accounts. Disabling this feature will degrade the security posture of your application, leaving it vulnerable to credential-based attacks like brute force attacks, credential stuffing, or bulk account creation.

## Triage and response{% #triage-and-response %}

1. Investigate the client id `{{@data.client_id}}` to understand if this is an expected operation.
1. Work with your tenant administrator to identify the owner of the application.
1. Speak with the owner of the application to understand if this operation is expected and approved.
1. If the owner of the application is unaware of this operation:
   - Disable the application credentials if possible.
   - Investigate any further activity from the IP `{{@network.client.ip}}` or the client id `{{@data.client_id}}`.
   - Begin your organization's incident response process and investigate.
