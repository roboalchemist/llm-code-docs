# Source: https://docs.datadoghq.com/security/default_rules/dvz-4x3-3ws.md

---
title: Credentials file modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Credentials file modified
---

# Credentials file modified
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1003-os-credential-dumping](https://attack.mitre.org/techniques/T1003)
## What happened{% #what-happened %}

The credential file `{{ @file.path }}` was modified by the process `{{ @process.comm }}`.

## Goal{% #goal %}

Detect modifications to sensitive credential files from non-standard processes.

## Strategy{% #strategy %}

Especially in production, all credentials should be either defined as code, or static. Drift and unmonitored changes to these credentials can open up attack vectors for adversaries, and cause your organization to be out of compliance with any frameworks or regulations that you are subject to. This detection watches for the modification of sensitive credential files which should not be changed outside of their definitions as code (or static definitions). The Linux commands `vipw` and `vigr` are the standard way to modify shadow and gshadow files respectively. Other processes interacting with these sensitive credential files is highly suspicious and should be investigated.

## Triage and response{% #triage-and-response %}

1. Identify the user or process that changed the credential file(s).
1. Identify what was changed in the credential files.
1. If these changes are not acceptable, roll back contain the host or container in question to an acceptable configuration.

*Requires Agent version 7.27 or greater*
