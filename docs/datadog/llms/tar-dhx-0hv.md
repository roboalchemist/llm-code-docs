# Source: https://docs.datadoghq.com/security/default_rules/tar-dhx-0hv.md

---
title: AWS Disable Cloudtrail with event selectors
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Disable Cloudtrail with event
  selectors
---

# AWS Disable Cloudtrail with event selectors
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when CloudTrail has been disabled by creating an event selector on the Trail.

## Strategy{% #strategy %}

This rule lets you monitor CloudTrail and detect if an attacker used the [`PutEventSelectors`](https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_PutEventSelectors.html) API call to filter out management events, effectively disabling CloudTrail for the specified Trail.

See the [public Proof of Concept](https://github.com/RhinoSecurityLabs/Cloud-Security-Research/tree/master/AWS/cloudtrail_guardduty_bypass) (PoC) for this attack.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` should have made the `{{@evt.name}}` API call.
1. If the API call was **not** made legitimately by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
- Remove the event selector using the `aws-cli` command [`put-event-selectors`](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/put-event-selectors.html) or use the [AWS console](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-update-a-trail-console.html) to revert the event selector back to the last known good state.
If the API call was made legitimately by the user:
- Determine if the user was authorized to make that change.
- If **Yes**, work with the user to ensure that CloudTrail logs for the affected account `{{@userIdentity.accountId}}` are being sent to the Datadog platform.
- If **No**, remove the event selector using the `aws-cli` command [`put-event-selectors`](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/put-event-selectors.html) or reference the [AWS console documentation](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-update-a-trail-console.html) to revert the event selector back to the last known good state.

## Changelog{% #changelog %}

- 17 October 2022 - Updated tags.
