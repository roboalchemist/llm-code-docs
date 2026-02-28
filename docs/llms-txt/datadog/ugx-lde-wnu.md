# Source: https://docs.datadoghq.com/security/default_rules/ugx-lde-wnu.md

---
title: New user seen executing a command in an ECS task
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > New user seen executing a command in an
  ECS task
---

# New user seen executing a command in an ECS task
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1651-cloud-administration-command](https://attack.mitre.org/techniques/T1651)
## Goal{% #goal %}

Detect when a user executes a command on an ECS container for the first time. An attacker may use this as a technique to escalate their privileges because they can run arbitrary commands on behalf of the container with the role and permissions associated with the container.

## Strategy{% #strategy %}

This rule lets you monitor this CloudTrail API call to detect if a user is executing a command on an ECS container:

- `ExecuteCommand`

## Triage and response{% #triage-and-response %}

1. Investigate the command that the user ({{@userIdentity.arn}}) ran on the container, which is located in the Cloudtrail log at `@requestParameters.container`, if the telemetry exists.
1. Analyze Cloudtrail logs with {{@userIdentity.arn}} that are within the same time frame as this security signal.
1. Review any other security signals generated for this container.
