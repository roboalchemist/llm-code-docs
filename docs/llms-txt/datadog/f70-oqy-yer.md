# Source: https://docs.datadoghq.com/security/default_rules/f70-oqy-yer.md

---
title: An AWS account attempted to leave the AWS Organization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > An AWS account attempted to leave the
  AWS Organization
---

# An AWS account attempted to leave the AWS Organization
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)
## Goal{% #goal %}

Detect an AWS account attempting to leave an AWS organization.

## Strategy{% #strategy %}

This rule allows you to monitor CloudTrail and detect if an attacker has attempted to have an AWS account leave an AWS organization using the [LeaveOrganization](https://docs.aws.amazon.com/organizations/latest/APIReference/API_LeaveOrganization.html) API call.

An attacker may attempt this API call for several reasons, such as:

- Target security configurations that are often defined at the organization level. Leaving an organization can disrupt or disable these controls.
- Perform a denial of service (DoS) attack on the victim's account that prevents the victim's organization to access it.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` should have made the `{{@evt.name}}` API call.
1. If the API call was not made by the user:

- Rotate user credentials.
- Determine what other API calls were made by the user.
- Initiate your company's incident response (IR) process.
If the API call was made legitimately by the user:
- Communicate with the user to understand if this was a planned action.
- If No, see if other API calls were made by the user and determine if they warrant further investigation.
- Initiate your company's incident response (IR) process.
