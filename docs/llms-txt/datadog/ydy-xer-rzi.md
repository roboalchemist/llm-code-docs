# Source: https://docs.datadoghq.com/security/default_rules/ydy-xer-rzi.md

---
title: Crypto miner process observed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Crypto miner process observed
---

# Crypto miner process observed
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496) 
## What happened{% #what-happened %}

The process `{{ @process.comm }}` was identified as a crypto miner. Cryptocurrency mining monopolizes CPU usage, slowing legitimate services.

## Goal{% #goal %}

Detect when a process launches with arguments associated with cryptocurrency miners.

## Strategy{% #strategy %}

Monitor systems process and analyze command-line arguments to identify specific patterns or arguments commonly associated with cryptocurrency mining software. Miners are often executed with unique arguments such as `--donate-level`.

## Triage and response{% #triage-and-response %}

**Note:** Cryptocurrency mining is often a symptom of a greater issue. It is imperative to determine the initial entry point such as through compromised cloud credentials or an application that is vulnerable to remote code execution (RCE).

1. Use host metrics to verify that cryptocurrency mining is taking place. This is indicated by an increase in CPU usage.
1. Review the process tree, related signals, and related logs to determine the initial entry point.
1. Remediate the affected resources and secure the initial entry point. This may involve patching vulnerabilities or rotating credentials.

## Changelog{% #changelog %}

- 26 September 2024 - Updated rule name and description

*Requires Agent version 7.28 or later*
