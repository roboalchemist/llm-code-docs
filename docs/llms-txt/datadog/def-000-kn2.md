# Source: https://docs.datadoghq.com/security/default_rules/def-000-kn2.md

---
title: Memfd object created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Memfd object created
---

# Memfd object created
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1620-reflective-code-loading](https://attack.mitre.org/techniques/T1620) 
## What happened{% #what-happened %}

The memfd object `{{ @process.executable.name }}` was executed, potentially by fileless malware.

## Goal{% #goal %}

Detect the creation of memfd objects. Memfd objects may allow fileless process execution.

## Strategy{% #strategy %}

Adversaries may leverage the creation of memory backed objects to conceal the execution of malicious payloads. Executing payloads directly in memory avoids creating files or other artifacts on disk.

## Triage and response{% #triage-and-response %}

1. Review the memfd object and parent process.
1. If the object is unexpected, determine the scope, identify enabling conditions, and gather incident indicators.
1. Declare an incident once it is determined the event meets organizational criteria for notification and reporting.
1. Attempt to contain the compromise. Containment actions may include isolation of the affected workload, disabling functions, or termination. The actions may vary depending on the severity of the incident and and the risk tolerance of your organization.

*Requires Agent version 7.42 or greater*
