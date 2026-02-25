# Source: https://docs.datadoghq.com/security/default_rules/f6b-3b4-aef.md

---
title: AWS VPC created or modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS VPC created or modified
---

# AWS VPC created or modified
Classification:complianceTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1485-data-destruction](https://attack.mitre.org/techniques/T1485)Framework:cis-awsControl:4.14
## Goal{% #goal %}

Detect when an attacker is destroying a VPC.

## Strategy{% #strategy %}

This rule lets you monitor this CloudTrail API call to detect if an attacker is deleting a VPC:

- [DeleteVpc](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpc.html)

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` is expected to perform the `{{@evt.name}}` API call on the account: `{{@userIdentity.accountId}}`.
1. Contact the principal owner and see if this was an API call that was made by the user.
1. If the API call was not made by the user, rotate the user credentials and investigate what other APIs were successfully accessed.
   - Rotate the credentials.
   - Investigate if the same credentials made other unauthorized API calls.

## Changelog{% #changelog %}

7 April 2022 - Updated rule query, cases and signal message.
