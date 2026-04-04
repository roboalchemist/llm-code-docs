# Source: https://docs.datadoghq.com/security/default_rules/def-000-la6.md

---
title: Attempt to create Xlarge EC2 instances in multiple AWS regions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Attempt to create Xlarge EC2 instances
  in multiple AWS regions
---

# Attempt to create Xlarge EC2 instances in multiple AWS regions
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1535-unused-or-unsupported-cloud-regions](https://attack.mitre.org/techniques/T1535)
## Goal{% #goal %}

Detect when there is an attempt to create Xlarge EC2 instances in multiple AWS regions.

## Strategy{% #strategy %}

Monitor CloudTrail and detect when an attempt to create Xlarge EC2 instances in multiple AWS regions occurs. An attacker may use Xlarge EC2 instances as a means of creating easily scalable resources to mine cryptocurrency. To avoid detection and resource service quotas, the attacker may try to create these resources in multiple regions.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` should have carried out this operation.
1. If the API calls were not made by the user:

- Rotate user credentials.
- Remove the newly created instances `{{@@responseElements.instancesSet.items.instanceId}}` if the API call was successful.
- Remove any associated EC2 security groups or key pairs.
- Determine what other API calls were made by the user.
- Begin your organization's incident response process and investigate.
