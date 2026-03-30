# Source: https://docs.datadoghq.com/security/default_rules/fd3-1aa-d7d.md

---
title: AWS Route Table created or modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS Route Table created or modified
---

# AWS Route Table created or modified
Classification:complianceTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)Framework:cis-awsControl:4.13
## Goal{% #goal %}

Detect when an AWS Route Table has been created or modified.

## Strategy{% #strategy %}

This rule lets you monitor CloudTrail and detect when an AWS Route Table has been created or modified with one of the following API calls:

- [CreateRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRoute.html)
- [CreateRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateRouteTable)
- [ReplaceRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceRoute.html)
- [ReplaceRouteTableAssociation](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReplaceRouteTableAssociation)
- [DeleteRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRouteTable.html)
- [DeleteRoute](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteRoute.html)
- [DisassociateRouteTable](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DisassociateRouteTable.html)

## Triage and response{% #triage-and-response %}

1. Determine if {{@userIdentity.arn}} is expected to perform the {{@evt.name}} API call.
1. Contact the principal owner and see if this was an API call which was made by the user.
1. If the API call was not made by the user, rotate the user credentials and investigate what other APIs were successfully accessed.

## Changelog{% #changelog %}

6 April 2022 - Updated signal message, rule query, and case layout.
