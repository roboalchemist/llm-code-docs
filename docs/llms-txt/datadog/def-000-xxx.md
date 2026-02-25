# Source: https://docs.datadoghq.com/security/default_rules/def-000-xxx.md

---
title: Suspicous ntdsutil usage
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Suspicous ntdsutil usage
---

# Suspicous ntdsutil usage
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003)
## What happened{% #what-happened %}

The utility `{{ @process.executable.name }}` was used to access the `ntds.dit` file, potentially to steal credentials.

## Goal{% #goal %}

Detect when ntdsutil is used in a suspicious manner, typically to access the ntds.dit file

## Strategy{% #strategy %}

Threat actors are known to utilize tools found natively in a victim's environment to accomplish their objectives. Ntdsutil, a legitimate Windows binary, has been abused by malicious actors in the past to gain access to the ntds.dit file.

## Triage and response{% #triage-and-response %}

1. Identify if the usage of ntdsutil is authorized, and confirm if the ntds.dit file was downloaded.
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.50.0 or greater.*
