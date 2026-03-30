# Source: https://docs.datadoghq.com/security/default_rules/def-000-pew.md

---
title: Invitation sent to account to join AWS organization
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Invitation sent to account to join AWS
  organization
---

# Invitation sent to account to join AWS organization
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1535-unused-or-unsupported-cloud-regions](https://attack.mitre.org/techniques/T1535)
## Goal{% #goal %}

Detect when there is an attempt to invite an AWS account to an AWS organization.

## Strategy{% #strategy %}

This rule allows you to monitor CloudTrail and detect if an attacker has attempted to invite an AWS account to an AWS organization. An attacker may attempt add an attacker controlled AWS account to a compromised AWS organization to evade the existing defenses of the organization.

This [operation](https://docs.aws.amazon.com/organizations/latest/APIReference/API_InviteAccountToOrganization.html) can be called only from the organization's management account.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` should have made a `{{@evt.name}}` API call.
   - Refer to `@requestParameters.target.id` to retrieve the account invited. This maybe in the form of an AWS account ID or email address.
   - Attempt to confirm the action either with the identity making the change or search for a ticket associated with the change.
   - Investigate other activities performed by the identity `{{@userIdentity.arn}}` using the Cloud SIEM - User Investigation dashboard.
1. If the API call does not appear to be legitimate, begin your organization's incident response process and investigate.
   - Follow [AWS recommendations](https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/technique-access-containment.html) for containing the potentially compromised identity, if appropriate.
   - [Remove the potentially malicious account](https://docs.aws.amazon.com/organizations/latest/APIReference/API_RemoveAccountFromOrganization.html) from your AWS organization.
