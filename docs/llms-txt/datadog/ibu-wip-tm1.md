# Source: https://docs.datadoghq.com/security/default_rules/ibu-wip-tm1.md

---
title: DNS lookup for cryptocurrency mining pool
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > DNS lookup for cryptocurrency mining
  pool
---

# DNS lookup for cryptocurrency mining pool
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496) 
## What happened{% #what-happened %}

The process `{{ @process.comm }}` was identified as a cryptocurrency miner because it made a DNS lookup for the mining pool `{{ @dns.question.name }}`.

## Goal{% #goal %}

Attackers often use compromised cloud infrastructure to mine cryptocurrency.

## Strategy{% #strategy %}

Detect when a process performs a DNS lookup for a domain related to cryptomining.

## Triage and response{% #triage-and-response %}

`{{@process.executable.name}}` performed a DNS lookup for `{{@dns.question.name}}`

**Note:** Cryptocurrency mining is often a symptom of a greater issue. It is imperative to determine the initial entry point such as through compromised cloud credentials or an application that is vulnerable to remote code execution (RCE).

1. Isolate the host or container and roll back to a known secure configuration.
1. Use host metrics to verify that cryptocurrency mining is taking place. This will be indicated by an increase in CPU usage.
1. Review the process tree, related signals, and related logs to determine the initial entry point.

*Requires Agent version 7.36 or later*
