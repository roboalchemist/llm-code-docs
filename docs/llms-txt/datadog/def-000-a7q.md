# Source: https://docs.datadoghq.com/security/default_rules/def-000-a7q.md

---
title: Okta Active Directory environment linked
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta Active Directory environment
  linked
---

# Okta Active Directory environment linked
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## Goal{% #goal %}

Detect the creation and linking of an on-premises Active Directory environment to Okta via an authorized agent.

## Strategy{% #strategy %}

This rule monitors Okta system events for Active Directory environment onboarding through the Okta agent. It correlates `system.agent.ad.create` or `system.agent.ad.connect` events with a `app.oauth2.token.grant.access_token_success` event, indicating an access token was provided. An attacker can link a new Active Directory environment in order to import compromised user accounts to an Okta instance.

Okta system events can populate with `system@okta.com` as the user name and `Active Directory Agent` in the user agent field. The rule is grouped by the IP address that took the two actions.

## Triage & Response{% #triage--response %}

- Examine the timeline of `system.agent.ad.create` or `system.agent.ad.connect` around the alert to confirm it matches a planned integration.
- Identify other behavior occurring from the user and source IP address, `{{@network.client.ip}}`.
- Verify the activity is consistent with known user behaviors.
- Review activity for the import of users from new Active Directory environment.
- If the creation of an Active Directory integration is unexpected or resulted in new user creation, initiate your incident response plan.
