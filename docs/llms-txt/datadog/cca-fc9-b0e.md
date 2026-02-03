# Source: https://docs.datadoghq.com/security/default_rules/cca-fc9-b0e.md

---
title: AWS security group created, modified or deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS security group created, modified or
  deleted
---

# AWS security group created, modified or deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when an AWS security group has been modified.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when an AWS security group has been created or modified with one of the following API calls:

- [AuthorizeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html)
- [AuthorizeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupEgress.html)
- [RevokeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupIngress.html)
- [RevokeSecurityGroupEgress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RevokeSecurityGroupEgress.html)
- [CreateSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html)
- [DeleteSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSecurityGroup.html)

**Note:** There is a separate rule to detect AWS Security Group Open to the World.

## Triage and response{% #triage-and-response %}

1. Determine who the user was who made this API call.
1. Contact the user and see if this was an API call which was made by the user.
1. If the API call was not made by the user:
   - Rotate the user credentials and investigate what other API calls.
   - Determine what other API calls the user made which were not made by the user.

## Changelog{% #changelog %}

18 March 2022 - Updated severity, split query into multiple queries, and split the single case into multiple cases.
