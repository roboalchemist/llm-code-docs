# Source: https://docs.datadoghq.com/security/default_rules/def-000-oac.md

---
title: Okta phone number assigned to multiple users
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Okta phone number assigned to multiple
  users
---

# Okta phone number assigned to multiple users
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detects the reuse of the same phone number across different Okta user accounts during multi-factor enrollment.

## Strategy{% #strategy %}

This rule monitors phone number enrollment verification by SMS within a short period. The reuse of one phone number across users may indicate an attacker's attempt to maintain persistence.

This detection has been adopted from rules published by the [Okta team](https://github.com/okta/customer-detections/).

## Triage & Response{% #triage--response %}

1. Identify the user account who triggered the signal, `{{@actor.alternateId}}`, and all other user accounts associated with `{{@debugContext.debugData.phoneNumber}}`.
1. Confirm whether sharing a number is expected for those accounts within the organization, such as for a service account.
1. Review recent factor enrollment and recovery changes for each user, focusing on additions or resets of factors.
1. Check authentication activity around the verification for each user from source IP `{{@network.client.ip}}` and geoâlocation for anomalies.
1. If user activity is suspicious, begin your organization's incident response process and investigate for any account takeovers.
