# Source: https://docs.datadoghq.com/security/default_rules/dhz-27i-ani.md

---
title: AWS GuardDuty threat intel set deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS GuardDuty threat intel set deleted
---

# AWS GuardDuty threat intel set deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when an attacker is trying to evade defenses by deleting a GuardDuty ThreatIntelSet.

## Strategy{% #strategy %}

This rule lets you monitor this CloudTrail API call to detect if an attacker is deleting a GuardDuty ThreatIntelSet:

- [DeleteThreatIntelSet](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DeleteThreatIntelSet.html)

## Triage and response{% #triage-and-response %}

1. Determine if user: `{{@userIdentity.arn}}` should have made a `{{@evt.name}}` API call.
1. If the API call was not made by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
- Replace ThreatIntelSets deleted by the user with the `aws-cli` command [create-threat-intel-set](https://docs.aws.amazon.com/cli/latest/reference/guardduty/create-threat-intel-set.html) or use the [AWS Console](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_upload-lists.html).
If the API call was made by the user:
- Determine if the user should be performing this API call and if it was an authorized change.
- If No, see if other API calls were made by the user and determine if they warrant further investigation.
