# Source: https://docs.datadoghq.com/security/default_rules/def-000-rrr.md

---
title: NTDS file referenced in command line
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > NTDS file referenced in command line
---

# NTDS file referenced in command line
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003) 
## What happened{% #what-happened %}

The process `{{ @process.executable.name }}` referenced the `NTDS.dit` file in its command line arguments, potentially attempting to extract Active Directory data.

## Goal{% #goal %}

Detect references to NTDS.dit file in command line

## Strategy{% #strategy %}

All data in Active Directory is stored within the file ntds.dit. Typically located on the domain controller, there are a variety of methods available for a threat actor to extract this file, with the most common being utilization of the ntdsutil command or extracting it from a shadow copy or backup of the domain controller. This detection looks to identify when process arguments are referencing the ntds.dit file, as it could be evidence of a threat actor attempting to exfiltrate the file.

## Triage and response{% #triage-and-response %}

1. Identify what is being executed and if it is actually accessing the ntds.dit file.
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.50.0 or greater.*
