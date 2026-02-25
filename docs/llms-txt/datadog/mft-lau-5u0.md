# Source: https://docs.datadoghq.com/security/default_rules/mft-lau-5u0.md

---
title: Okta administrator role assigned to user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta administrator role assigned to
  user
---

# Okta administrator role assigned to user
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## Goal{% #goal %}

Detect when administrative privileges (`Super Administrator` or `Organization Administrator` roles) are provisioned to an Okta user.

## Strategy{% #strategy %}

This rule lets you monitor the following Okta event to detect when administrative privileges are provisioned:

- `user.account.privilege.grant`

## Triage and response{% #triage-and-response %}

1. Examine the event details to confirm the exact role in `{{@debugContext.debugData.privilegeGranted}}` and identify the target account receiving the role.
1. Identify the actor who performed the grant and validate an approved request or change ticket exists for this assignment.
1. Review recent authentication activity for both the actor and target accounts, including MFA usage, new device or geoâlocation signals, and failed login attempts.
1. Check the source IP `{{@network.client.ip}}` and geoâlocation for the actor and determine whether they align with expected administrative patterns.
1. If user activity is suspicious, begin your organization's incident response process and investigate for any account takeovers.

## Changelog{% #changelog %}

- 11 December 2025 - Updated query to filter on super and organization administrator roles.
