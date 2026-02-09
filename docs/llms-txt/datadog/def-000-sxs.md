# Source: https://docs.datadoghq.com/security/default_rules/def-000-sxs.md

---
title: Okta session hijacking
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Okta session hijacking
---

# Okta session hijacking

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1528-steal-application-access-token](https://attack.mitre.org/techniques/T1528) 
## Goal{% #goal %}

Detect when an active Okta session exhibits unusual changes in its ASN (Autonomous System Number) or user agent, potentially indicating session hijacking. This type of attack may allow unauthorized access to application tokens, posing a security risk.

## Strategy{% #strategy %}

This rule lets you monitor all Okta user-generated events to determine when a user takes an action, except for:

- `user.session.clear`
- `user.authentication.auth_via_mfa`
- `user.mfa.factor.activate`
- `user.session.end`

## Triage and response{% #triage-and-response %}

1. Check the specific Okta session events to confirm ASN or user agent changes for the affected session. Verify if the changes align with known travel or user activity patterns.
1. Inspect the GeoIP information in the logs to identify unusual locations or ASNs associated with the user. Determine if these IPs are from suspicious or untrusted regions.
1. If the user did not make the observed authentication attempts:
   - Rotate user credentials.
   - Confirm that no successful authentication attempts have been made.
   - Investigate the source IP: `{{@network.client.ip}}` using the Cloud SIEM - IP Investigation dashboard to determine if the IP address has taken other actions.

## Changelog{% #changelog %}

- 14 April 2025 - Updated rule query to exclude `user.mfa.factor.activate` events.
