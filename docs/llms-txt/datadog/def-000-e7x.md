# Source: https://docs.datadoghq.com/security/default_rules/def-000-e7x.md

---
title: AWS EC2 security group events observed with a suspicious naming convention
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS EC2 security group events observed
  with a suspicious naming convention
---

# AWS EC2 security group events observed with a suspicious naming convention
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when an AWS security group has been modified by a long-term access key that has a suspicious group naming convention.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when an AWS security group has been created or modified with one of the following API calls:

- [AuthorizeSecurityGroupIngress](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AuthorizeSecurityGroupIngress.html)
- [CreateSecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateSecurityGroup.html)

Datadog's security research team has observed security group naming conventions that include a common noun followed by a string of alphanumeric characters. The attack pattern can indicate that the long term access key used has been compromised, `{{@userIdentity.accessKeyId}}`.

## Triage and response{% #triage-and-response %}

1. Determine who was the user who made this API call.
1. Contact the user and confirm this was an API call that they made.
1. If the API call was not made by the user:
   - Rotate the user credentials and investigate what other API calls were made.
   - Determine what other API calls made by that user were not actually initiated directly by that user.
