# Source: https://docs.datadoghq.com/security/default_rules/def-000-sc1.md

---
title: Okta phishing detection with FastPass origin check
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta phishing detection with FastPass
  origin check
---

# Okta phishing detection with FastPass origin check
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566)
## Goal{% #goal %}

Detect when Okta raises a phishing [detection](https://sec.okta.com/fastpassphishingdetection) with FastPass origin check.

## Strategy{% #strategy %}

This rule monitors Okta for when a phishing detection with FastPass origin check has been raised. Okta provides a platform detection for when a user enrolled in FastPass fails to authenticate via a real-time adversary in the middle (AiTM) phishing proxy.

## Triage and response{% #triage-and-response %}

1. Extract the IP address `{{@network.client.ip}}` and context provided by Okta in `@debugContext.debugData.risk`. The user email will always populate as `system@okta.com` and further log events are required to determine the user account targeted.

1. Review the risk analysis provided in `@debugContext.debugData.risk`. This field may include:

- The application that was attempted to be accessed
- Okta's risk severity rating
- Mismatched request origin detail

If the authentication attempt was to the Okta dashboard directly, the application name will populate as `okta_enduser`. A mismatched request origin can provide insight on AiTM infrastructure if captured by Okta and provided in this log field.
Determine what user account was associated with the failed FastPass attempt by reviewing surrounding Okta logs for evidence of related login attempts, such as:
- `user.session.start`
- `policy.evaluate_sign_on`
- `user.authentication_via_mfa`
- `user.authentication.verify`

The IP address, device hash, or user agent can be helpful fields for further context on the identity triggering the login events.

Investigate if the authentication attempts, from this IP address or user, follows typical behaviors within your environment.

If the behavior appears malicious and authentication occurred successfully following the failed FastPass attempt, [clear related user sessions](https://developer.okta.com/docs/reference/api/users/#clear-current-user-sessions) and [reset user passwords](https://developer.okta.com/docs/reference/api/users/#response-example-32).

Begin your organization's security incident response process and investigate further for any account takeover and lateral movement behavior.

## Changelog{% #changelog %}

- 4 August 2025 - Updated rule query to group by `usr.email`.
- 16 January 2026 - Updated documentation to include additional context.
