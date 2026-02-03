# Source: https://docs.datadoghq.com/security/default_rules/def-000-yiq.md

---
title: Okta admin console activity from new device
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta admin console activity from new
  device
---

# Okta admin console activity from new device
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detects Okta Admin Console sign-in from a new device and geolocation. Using Okta's new device and location enrichment, alerts are triggered from allowed sign-ons to the Okta's administrator console.

## Strategy{% #strategy %}

This rule monitors Okta sign-on evaluation, `policy.evaluate_sign_on`, events for admin console access where `@debugContext.debugData.behaviors` includes a positive flag for new device and geolocation. After a sign-on evaluation action, the `user.session.access_admin_app` event will be logged for the user.

Accessing administrative views and privileges from a new device and location can indicate an account takeover.

## Triage & Response{% #triage--response %}

- Review the sign-on details for `{{@usr.email}}` and confirm the user recognizes the new device.
- Check whether the geolocation and source IP `{{@network.client.ip}}` match expected locations, travel, or corporate VPN patterns.
- Identify preceding authentication events for `{{@usr.email}}` (failed logins, MFA challenges, password resets) near the alert time.
- Determine if strong MFA and device posture controls were required for this account and whether they were satisfied within the policy evaluation log.
- Examine subsequent Okta actions from the same user after accessing the admin portal, such as admin role changes, policy updates, application assignments, or reading of OAuth secrets.
- If the access event is unexpected or resulted in suspicious activities, initiate your incident response plan.
