# Source: https://docs.datadoghq.com/security/default_rules/def-000-pn2.md

---
title: AWS VPC Flow Log deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS VPC Flow Log deleted
---

# AWS VPC Flow Log deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect when one or more AWS VPC Flow Log are deleted.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when AWS VPC FLow Logs are deleted by calling the [DeleteFlowLogs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFlowLogs.html) API.

## Triage and response{% #triage-and-response %}

1. Determine if the API call: `{{@evt.name}}` should have occurred.
1. If the action was legitimate, consider allowing the invoking service: `{{@userIdentity.invokedBy}}`, user: `{{@userIdentity.arn}}`, or other appropriate attribute through a [suppression list](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise).
1. If it shouldn't have been made:
   - Contact the user: {{@userIdentity.arn}} and see if they made the API call.
1. If the API call was not made by the user:
   - Rotate the user credentials.
   - Determine what other API calls were made with the old credentials that were not made by the user.
