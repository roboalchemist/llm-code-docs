# Source: https://docs.datadoghq.com/security/default_rules/def-000-xx1.md

---
title: Bring your own file system (BYOF) tool executed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Bring your own file system (BYOF) tool
  executed
---

# Bring your own file system (BYOF) tool executed
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1105-ingress-tool-transfer](https://attack.mitre.org/techniques/T1105) 
## What happened{% #what-happened %}

A Bring Your Own Filesystem (BYOF) tool was executed, which attackers can abuse to download and access additional utilities.

## Goal{% #goal %}

Detect execution of the BYOF tool `proot`, which attackers may use to download and access additional malicious tools.

## Strategy{% #strategy %}

This rule monitors for execution of the `proot` binary and detects processes spawned from the path `*/freeroot/root.sh`, a file system previously observed in BYOF compromises.

## Triage and response{% #triage-and-response %}

1. Review the process tree to understand what initiated the `proot` execution.
1. Investigate the filesystem and determine if this is authorized activity.
1. If the activity is unauthorized, isolate the affected system and investigate the initial access point.
1. Review related signals and events to establish a timeline of the compromise.

*Requires Agent version 7.27 or greater.*
