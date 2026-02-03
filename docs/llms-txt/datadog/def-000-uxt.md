# Source: https://docs.datadoghq.com/security/default_rules/def-000-uxt.md

---
title: Crypto miner environment variables observed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Crypto miner environment variables
  observed
---

# Crypto miner environment variables observed
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496) 
## What happened{% #what-happened %}

The process `{{ @process.comm }}` was identified as a crypto miner based on its environment variables.

## Goal{% #goal %}

Detect when a process launches with environment variables associated with cryptocurrency miners.

## Strategy{% #strategy %}

Some cryptocurrency miners support environment variables such as `POOL_USER` or `POOL_URL` to define configuration settings. This can be used to identify suspicious processes with high confidence.

## Triage and response{% #triage-and-response %}

1. Isolate the workload.
1. Use host metrics to verify if cryptocurrency mining is taking place. This is indicated by an increase in CPU usage.
1. Review the process tree and related signals to determine the initial entry point.

*Requires Agent version 7.27 or later.*
