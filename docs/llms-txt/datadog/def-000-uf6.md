# Source: https://docs.datadoghq.com/security/default_rules/def-000-uf6.md

---
title: Cryptocurrency miner attempted to boost CPU performance
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cryptocurrency miner attempted to boost
  CPU performance
---

# Cryptocurrency miner attempted to boost CPU performance
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496) 
## What happened{% #what-happened %}

A process modified a setting for model-specific registers (MSRs). This is used by the XMRig cryptocurrency miner to boost CPU performance.

## Goal{% #goal %}

Detect cryptocurrency miners modifying CPU settings to boost performance.

## Strategy{% #strategy %}

Some cryptocurrency miners use [model-specific registers](https://www.intel.com/content/www/us/en/developer/articles/technical/software-security-guidance/best-practices/reading-writing-msrs-in-linux.html) to boost performance, and therefore profit. Legitimate use of this feature is rare.

## Triage and response{% #triage-and-response %}

1. Review the process tree to determine why MSRs were used. The activity is likely malicious if the parent process is not expected.
1. Use host metrics to verify if cryptocurrency mining is taking place. This will be indicated by an increase in CPU usage.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.35 or later*
