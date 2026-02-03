# Source: https://docs.datadoghq.com/security/default_rules/a8d-afd-la9.md

---
title: New Amazon EC2 Instance type
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > New Amazon EC2 Instance type
---

# New Amazon EC2 Instance type
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1204-user-execution](https://attack.mitre.org/techniques/T1204) 
## Goal{% #goal %}

Detect when an attacker spawns an instance for malicious purposes.

## Strategy{% #strategy %}

This rule lets you monitor this CloudTrail API call to detect when a new instance type (`@responseElements.instancesSet.items.instanceType`) is spawned:

- [RunInstances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html)

It does this by inspecting the AWS Instance types each AWS account are seen over a 7-day window. Newly detected instance types after this 7-day window till generate security signals.

## Triage and response{% #triage-and-response %}

1. Determine whether the instance type `{{@responseElements.instancesSet.items.instanceType}}` is expected to be used in your AWS account by checking the [Datadog Infrastructure List](https://app.datadoghq.com/infrastructure?tab=details&tags=instance-type%3A%7b%7b@responseElements.instancesSet.items.instanceType%7d%7d).
1. If not, determine who spawned this instance and ask the user whether their activity was legitimate or whether their credentials were compromised and this instance is being used by an attacker.

## Changelog{% #changelog %}

7 April 2022 - Updated rule query.
