# Source: https://docs.datadoghq.com/security/default_rules/def-000-qe5.md

---
title: RC scripts modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > RC scripts modified
---

# RC scripts modified
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1037-boot-or-logon-initialization-scripts](https://attack.mitre.org/techniques/T1037)
## What happened{% #what-happened %}

The file `{{ @file.path }}` was modified by the process `{{ @process.comm }}`, potentially to establish persistence.

## Goal{% #goal %}

Detect modifications to RC script files (`rc.local` and `rc.common`).

## Strategy{% #strategy %}

RC scripts allow system administrators to map and start custom services at startup for different run levels. Attackers can establish persistence by adding a malicious binary path or shell commands to `rc.local` or `rc.common`. Upon reboot, the system executes the file contents as root.

## Triage and response{% #triage-and-response %}

1. Review and confirm the changes made to `{{@file.path}}` are a part of normal system administration.
1. If these changes are unauthorized, roll back the host in question to a known good `{{@file.path}}`, or replace the system with a known-good system image.

*Requires Agent version 7.27 or greater.*
