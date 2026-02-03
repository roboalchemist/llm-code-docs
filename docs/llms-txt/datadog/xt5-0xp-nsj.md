# Source: https://docs.datadoghq.com/security/default_rules/xt5-0xp-nsj.md

---
title: Critical system binary modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Critical system binary modified
---

# Critical system binary modified
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1036-masquerading](https://attack.mitre.org/techniques/T1036)Framework:pciControl:11.5 
## What happened{% #what-happened %}

The system file `{{ @file.path }}` was modified by the process `{{ @process.comm }}`.

## Goal{% #goal %}

Detect modifications of critical system binaries.

## Strategy{% #strategy %}

PCI-DSS is the payment-card industry's compliance framework. Any systems that handle credit card data and transactions from the major credit card companies must be PCI-DSS compliance. Control 11.5 of the PCI-DSS framework states that organizations must "alert personnel to unauthorized modifications (including changes, additions, and deletions) of critical system files, configuration files, or content files". On Linux, critical system binaries are typically stored in `/bin/`, `/sbin/`, or `/usr/sbin/`. This rule tracks any modifications to those directories.

## Triage and response{% #triage-and-response %}

1. Identify which user or process changed the critical system binaries.
1. If these changes were not authorized, and you cannot confirm the safety of the changes, roll back the host or container in question to an acceptable configuration.

*Requires Agent version 7.27 or greater*
