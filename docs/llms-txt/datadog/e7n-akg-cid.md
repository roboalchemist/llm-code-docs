# Source: https://docs.datadoghq.com/security/default_rules/e7n-akg-cid.md

---
title: User ran a command on Azure Compute
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > User ran a command on Azure Compute
---

# User ran a command on Azure Compute
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1651-cloud-administration-command](https://attack.mitre.org/techniques/T1651) 
## Goal{% #goal %}

Detect when a user runs a command on an Azure Virtual Machine through the Azure CLI or Portal.

## Strategy{% #strategy %}

Monitor Azure Compute logs for `MICROSOFT.COMPUTE/VIRTUALMACHINES/RUNCOMMAND/ACTION` events that have `@evt.outcome` of `Success`.

## Triage and response{% #triage-and-response %}

Reach out to the user to determine if the activity is legitimate.
