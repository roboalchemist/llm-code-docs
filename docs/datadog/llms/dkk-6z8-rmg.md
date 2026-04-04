# Source: https://docs.datadoghq.com/security/default_rules/dkk-6z8-rmg.md

---
title: AWS CloudWatch rule disabled or deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS CloudWatch rule disabled or deleted
---

# AWS CloudWatch rule disabled or deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a CloudWatch rule has been disabled or deleted.

## Strategy{% #strategy %}

This rule lets you monitor CloudTrail and detect if a [`DisableRule`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteRule.html) or [`DeleteRule`](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DisableRule.html) API call has occurred. An attacker may delete rules in an attempt to evade defenses.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` should have made the `{{@evt.name}}` API call.
1. If the API call was **not** made legitimately by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
- Enable or create a rule using the `aws-cli` commands [`enable-rule`](https://docs.aws.amazon.com/cli/latest/reference/events/enable-rule.html) or [`put-rule`](https://docs.aws.amazon.com/cli/latest/reference/events/put-rule.html), or reference the [AWS documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) to revert the rules back to the last known good state.
If the API call was made legitimately by the user:
- Determine if the user was authorized to make that change.
- If **Yes**, consider including the EventBus name in a [suppression list](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise): `{{@requestParameters.eventBusName}}`.
- If **No**, enable or create a rule using the `aws-cli` commands [`enable-rule`](https://docs.aws.amazon.com/cli/latest/reference/events/enable-rule.html) or [`put-rule`](https://docs.aws.amazon.com/cli/latest/reference/events/put-rule.html), respectively, or reference the [AWS documentation](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) to revert the rules back to the last known good state.
  - Begin your company's IR process and investigate.

## Changelog{% #changelog %}

- 4 October 2022 - Updated severity
