# Source: https://docs.datadoghq.com/security/default_rules/wv9-wm3-v0s.md

---
title: AWS GuardDuty publishing destination deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS GuardDuty publishing destination
  deleted
---

# AWS GuardDuty publishing destination deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a user deletes a publishing destination for a detector which will prevent the exporting of findings.

## Strategy{% #strategy %}

This rule lets you monitor this CloudTrail API call to detect if a user has deleted a Guard Duty publishing destination.

- [DeletePublishingDestination](https://docs.aws.amazon.com/fr_fr/guardduty/latest/APIReference/API_DeletePublishingDestination.html)

## Triage and response{% #triage-and-response %}

1. Determine which user in your organization owns the API key that made this API call.
1. Contact the user to see if they intended to make this API call.
1. If the user did not make the API call:
   - Rotate the credentials.
   - Investigate if the same credentials made other unauthorized API calls.
