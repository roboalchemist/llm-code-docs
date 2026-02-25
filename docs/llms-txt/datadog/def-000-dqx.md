# Source: https://docs.datadoghq.com/security/default_rules/def-000-dqx.md

---
title: Sudoers policy file modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Sudoers policy file modified
---

# Sudoers policy file modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1548-abuse-elevation-control-mechanism](https://attack.mitre.org/techniques/T1548)
## What happened{% #what-happened %}

The `sudoers` policy `{{ @file.path }}` was modified by `{{ @process.comm }}`, potentially to escalate privileges.

## Goal{% #goal %}

Detect modifications to `/etc/sudoers` policy file.

## Strategy{% #strategy %}

Sudo allows users to perform commands from terminals with delegated authority to give certain users (or groups of users) the ability to run some (or all) commands as root. The sudoers policy file, `/etc/sudoers`, describes which users can run commands with root level privileges using sudo. Adversaries may attempt to edit the sudoers policy file to execute commands as other users or to spawn processes with higher privileges.

## Triage and response{% #triage-and-response %}

1. Identify if the changes to the path `{{@file.path}}` were part of known system setup or maintenance.
1. If these changes were unauthorized, roll back the host in question to a known good sudoers policy file, or replace the system with a known good system image.

*Requires Agent version 7.27 or greater.*
