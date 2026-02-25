# Source: https://docs.datadoghq.com/security/default_rules/bif-xha-5if.md

---
title: AWS CloudWatch log group deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS CloudWatch log group deleted
---

# AWS CloudWatch log group deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when a CloudWatch Log Group is deleted.

## Strategy{% #strategy %}

Detect a successful `@evt.name:DeleteLogGroup` event.

## Triage and response{% #triage-and-response %}

1. Ensure that the `{{@requestParameters.logGroupName}}` log group is not used for auditing or security purposes.
1. If it is then:
   - Ensure that the user: `{{@userIdentity.session_name}}` should be making this API call to your `{{env}}` environment.
   - Consider adding to the allowlist the log group name: `{{@requestParameters.logGroupName}}` through a [suppression list](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise).
1. If not, begin your company's IR process and investigate.

## Changelog{% #changelog %}

11 October 2022 - updated severity.
