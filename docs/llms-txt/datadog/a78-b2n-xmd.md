# Source: https://docs.datadoghq.com/security/default_rules/a78-b2n-xmd.md

---
title: Cron job modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Cron job modified
---

# Cron job modified
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1053-scheduled-task-or-job](https://attack.mitre.org/techniques/T1053)
## What happened{% #what-happened %}

The cron file `{{ @file.path }}` was created or modified, potentially for persistence.

## Goal{% #goal %}

Detect the creation or modification of new cron jobs on a system.

## Strategy{% #strategy %}

Cron is a task scheduling system that runs tasks on a time-based schedule. Attackers can use cron jobs to gain persistence on a system, or even to run malicious code at system-boot. Cron jobs can also be used for remote code execution, or to run a process under a different user-context.

## Triage and response{% #triage-and-response %}

1. Check to see which cron task was created or modified.
1. Check whether the cron task was created or modified by a known user or process.
1. If these changes are not acceptable, roll back the host or container in question to an acceptable configuration.

*Requires Agent version 7.27 or greater*
