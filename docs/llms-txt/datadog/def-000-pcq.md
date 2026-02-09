# Source: https://docs.datadoghq.com/security/default_rules/def-000-pcq.md

---
title: Offensive Kubernetes tool executed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Offensive Kubernetes tool executed
---

# Offensive Kubernetes tool executed
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1613-container-and-resource-discovery](https://attack.mitre.org/techniques/T1613) 
## What happened{% #what-happened %}

The process `{{ @process.comm }}` was executed with the intent of Kubernetes enumeration or privilege escalation.

## Goal{% #goal %}

A known Kubernetes attack tool has been executed.

## Strategy{% #strategy %}

This rule identifies whenever a known tool used during Kubernetes penetration has been executed. These tools are often used to gather information about the Kubernetes environment to facilitate lateral movement and privilege escalation.

## Triage and response{% #triage-and-response %}

1. Determine if the tool usage is authorized or part of an authorized penetration test.
1. If the activity is not authorized, begin to look at activity surrounding the execution of the tool.
1. Usage of many of these tools requires access to the Kubernetes API. Identify and revoke accounts used to execute the command.
1. Begin the incident response process to find and revoke the initial access vector.

*Requires Agent version 7.27 or greater*
