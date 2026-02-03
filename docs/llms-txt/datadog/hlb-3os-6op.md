# Source: https://docs.datadoghq.com/security/default_rules/hlb-3os-6op.md

---
title: Compiler executed in container
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Compiler executed in container
---

# Compiler executed in container
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1027-obfuscated-files-or-information](https://attack.mitre.org/techniques/T1027) 
## What happened{% #what-happened %}

The compiler process `{{ @process.comm }}` was executed inside a container, which is bad practice outside of build services.

## Goal{% #goal %}

Detect when a compiler (like `clang` or `bcc`) is executed inside of a container.

## Strategy{% #strategy %}

After an initial compromise, attackers may attempt to download additional tools to their victim's infrastructure. In order to make these additional tools difficult to detect or analyze, attackers sometimes deliver their tools as uncompiled code, and then compile their malicious binaries directly on the victim's infrastructure. In containerized environments, the use of compilers is especially suspicious because in production it is best practice to make containers immutable. The use of a compiler in a production container could indicate an attacker staging tools, or unwanted container configuration drift.

## Triage & Response{% #triage--response %}

1. Determine whether or not this is expected behavior. For example, did an employee compile a tool inside of a container for an approved reason, or does an approved software compile additional files on startup?
1. If this behavior is unexpected, attempt to contain the compromise (this may be achieved by terminating the workload, depending on the stage of attack) and look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the nature of the attack and the tools involved. Investigate security signals (if present) occurring around the time of the event to establish an attack path.
1. Find and repair the root cause of the exploit.

*Requires Agent version 7.27 or greater*
