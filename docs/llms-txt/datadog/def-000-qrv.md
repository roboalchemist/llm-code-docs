# Source: https://docs.datadoghq.com/security/default_rules/def-000-qrv.md

---
title: Process memory dumped using ProcDump
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Process memory dumped using ProcDump
---

# Process memory dumped using ProcDump

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003)
## Goal{% #goal %}

Detect when ProcDump is used to dump process memory.

## Strategy{% #strategy %}

ProcDump is a Sysinternals tool originally created to help troubleshoot running applications. Threat actors have used it to dump process memory in an attempt to extract credentials, often from the LSASS process.

## Triage and response{% #triage-and-response %}

1. Identify what process is being dumped, and if it is authorized or expected.
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.
