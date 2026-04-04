# Source: https://docs.datadoghq.com/security/default_rules/g78-dht-5cj.md

---
title: Compiler wrote suspicious file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Compiler wrote suspicious file
---

# Compiler wrote suspicious file
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1027-obfuscated-files-or-information](https://attack.mitre.org/techniques/T1027)
## What happened{% #what-happened %}

The process `{{ @process.comm }}` wrote the file `{{ @file.path }}`, which has a suspicious extension or path.

## Goal{% #goal %}

Detect a compiler writing a file with an unusual path or extension.

## Strategy{% #strategy %}

After an initial compromise, attackers may attempt to download additional tools to their victim's infrastructure. In order to make these additional tools difficult to detect or analyze, attackers sometimes deliver their tools as uncompiled code, and then compile their malicious binaries directly on the victim's infrastructure. In containerized environments, the use of compilers is especially suspicious because in production it is a best practice to make containers immutable. The use of a compiler in a production container could indicate an attacker staging tools, or unwanted container configuration drift.

## Triage and response{% #triage-and-response %}

1. Determine whether or not this is expected behavior. For example, did an employee compile a tool inside of a container for an approved reason, or does an approved software compile additional files on startup?
1. If this behavior is unexpected, attempt to contain the compromise. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.27 or greater.*
