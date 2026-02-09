# Source: https://docs.datadoghq.com/security/default_rules/def-000-yzz.md

---
title: Process memory dumped using procdump
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Process memory dumped using procdump
---

# Process memory dumped using procdump
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003) 
## What happened{% #what-happened %}

The Sysinternals tool `{{ @process.executable.name }}` was used to dump process memory.

## Goal{% #goal %}

Detect when procdump is used to dump process memory.

## Strategy{% #strategy %}

Procdump is a sysinternals tool originally created to help trouble shoot running applications. Threat actors have used it to dump process memory in an attempt to extract credentials, oftentimes from the lsass process.

## Triage and response{% #triage-and-response %}

1. Identify what process is being dumped, and if it is authorized or expected.
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.50.0 or greater.*
