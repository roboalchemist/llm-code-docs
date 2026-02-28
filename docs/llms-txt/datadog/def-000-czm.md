# Source: https://docs.datadoghq.com/security/default_rules/def-000-czm.md

---
title: Looney Tunables (CVE-2023-4911) exploited for privilege escalation
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Looney Tunables (CVE-2023-4911)
  exploited for privilege escalation
---

# Looney Tunables (CVE-2023-4911) exploited for privilege escalation
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1068-exploitation-for-privilege-escalation](https://attack.mitre.org/techniques/T1068)
## What happened{% #what-happened %}

The process `{{ @process.comm }}` executed in a fashion indicating exploitation of the privilege escalation vulnerability `CVE-2023-4911`.

## Goal{% #goal %}

Detect exploitation of CVE-2023-4911, a buffer overflow in GNU C.

## Strategy{% #strategy %}

This vulnerability exists in GNU C Library's dynamic loader `ld.so` while processing the `GLIBC_TUNABLES` environment variable. A local attacker could launch a SUID binary with a maliciously crafted `GLIBC_TUNABLES` value to execute code with elevated permissions. This detection monitors SUID binary executions and alerts when the `GLIBC_TUNABLES` environment variable is provided.

## Triage and response{% #triage-and-response %}

1. Inspect the executing process and the `@process.envs` field to determine if this is expected activity.
1. Review the process tree and related signals to establish a timeline and determine where the activity originated from.
1. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Find and repair the root cause of the exploit.

*Requires Agent version 7.27 or later.*
