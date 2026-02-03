# Source: https://docs.datadoghq.com/security/default_rules/def-000-zzz.md

---
title: Process memory dumped using the minidump functions of comsvcs.dll
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Process memory dumped using the
  minidump functions of comsvcs.dll
---

# Process memory dumped using the minidump functions of comsvcs.dll
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003) 
## What happened{% #what-happened %}

Process memory was dumped using the `comsvcs.dll MiniDump` function.

## Goal{% #goal %}

Detect the minidump function of comsvcs.dll being used to dump process memory.

## Strategy{% #strategy %}

Threat actors are known to utilize tools found natively in a victim's environment to accomplish their objectives. Comsvcs.dll, a legitimate Windows dll, has been abused by malicious actors in the past to dump process memory, notably from LSASS in an attempt to extract credentials.

## Triage and response{% #triage-and-response %}

1. Identify what process is being dumped, and confirm if authorized or expected.
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.50.0 or greater.*
