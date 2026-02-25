# Source: https://docs.datadoghq.com/security/default_rules/sc8-pjc-tut.md

---
title: Local account password modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Local account password modified
---

# Local account password modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## What happened{% #what-happened %}

`{{ @process.comm }}` changed a local account password.

## Goal{% #goal %}

Detect use of the `passwd` or `chpasswd` commands to change account passwords.

## Strategy{% #strategy %}

The `passwd` operating system command is used to change user account passwords. The `chpasswd` command does this in bulk. If this is unexpected behavior, it could indicate an attacker attempting to compromise your host machine and achieve persistence. This detection is triggered when execution of the `passwd` or `chpasswd` command is detected.

## Triage and response{% #triage-and-response %}

1. Determine which user executed the command and whether or not this is allowed or expected behavior.
1. If this behavior is unexpected, attempt to contain the compromise (this may be achieved by terminating the workload, depending on the stage of attack) and look for indications of initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Investigate security signals (if present) occurring around the time of the event to establish an attack path.
1. Find and repair the root cause of the exploit.

*Requires Agent version 7.27 or greater*
