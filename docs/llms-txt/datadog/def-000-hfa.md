# Source: https://docs.datadoghq.com/security/default_rules/def-000-hfa.md

---
title: Okta IDP creation followed by failed authentication attempts
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta IDP creation followed by failed
  authentication attempts
---

# Okta IDP creation followed by failed authentication attempts
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## Goal{% #goal %}

Detects creation of a new Okta identity provider followed by repeated failed authentications through that external provider.

## Strategy{% #strategy %}

This rule monitors Okta events for successful identity provider creation, `system.idp.lifecycle.create`, and subsequent authentication failures through that provider, indicated through `user.authentication.auth_via_IDP` events resulting in `FAILURE`. The `target.displayName` represents the new identity provider (IdP) name in the system creation log.

Events are grouped by network provider and Okta account to capture the variety of user sessions.

This behavior can be indicative of a cross-tenant impersonation attempt where an attacker first gains privileged access to an organization's Okta admin console and then sets up a new IdP that allows them to authenticate as any user without knowing their credentials.

## Triage & Response{% #triage--response %}

- Review the `system.idp.lifecycle.create` event details for the administrator who initiated the change and the new IdP name within the `target.displayName` field.
- Identify the failing `user.authentication.auth_via_IDP` events, including the source IPs and ASNs used and the `{{@outcome.reason}}`.
- Check whether failures from `{{@network.client.geoip.as.domain}}` match expected locations, travel, or corporate VPN patterns.
- Review your Okta admin console for information on the registered IdP and associated routing rules.
- If the events are unexpected or resulted in suspicious activities, initiate your incident response plan.
