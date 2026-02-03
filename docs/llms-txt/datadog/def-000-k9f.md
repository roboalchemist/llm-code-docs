# Source: https://docs.datadoghq.com/security/default_rules/def-000-k9f.md

---
title: Scheduled task created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Scheduled task created
---

# Scheduled task created
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1053-scheduled-task-or-job](https://attack.mitre.org/techniques/T1053) 
## What happened{% #what-happened %}

A scheduled task was created, potentially to establish persistence.

## Goal{% #goal %}

Detect the creation of scheduled tasks.

## Strategy{% #strategy %}

This rule generates a signal when a scheduled task is created. Threat actors often use scheduled tasks as a persistence mechanism.

## Triage and response{% #triage-and-response %}

1. Identify what the scheduled task is executing and determine if it's authorized.
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.50.0 or greater.*
