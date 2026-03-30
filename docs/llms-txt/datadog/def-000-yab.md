# Source: https://docs.datadoghq.com/security/default_rules/def-000-yab.md

---
title: Okta temporary AWS credentials granted using open source tooling
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta temporary AWS credentials granted
  using open source tooling
---

# Okta temporary AWS credentials granted using open source tooling
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078)
## Goal{% #goal %}

Detects when the open source CLI tool, [gimme-aws-creds](https://github.com/Nike-Inc/gimme-aws-creds), is used to obtain temporary Okta user credentials to AWS.

## Strategy{% #strategy %}

This rule monitors for successful application authentication event, `user.authentication.sso`, events when the user agent includes `gimme-aws-creds`.

When the activity is from a new device or suspicious origin, the severity is increased.

## Triage & Response{% #triage--response %}

- Review the sign-on details for `{{@usr.email}}` and confirm if the user normally uses this tooling to access AWS. The field `{{@target.displayName}}` will include the name of the AWS application instance which was authenticated to through the tooling.
- Check whether the geolocation and source IP `{{@network.client.ip}}` match expected locations, travel, or corporate VPN patterns.
- Examine subsequent AWS actions within CloudTrail logs from the same user after obtaining credentials.
- If the access event is unexpected or resulted in suspicious activities, initiate your incident response plan.
