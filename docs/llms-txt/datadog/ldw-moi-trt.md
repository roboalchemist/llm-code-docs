# Source: https://docs.datadoghq.com/security/default_rules/ldw-moi-trt.md

---
title: Database process spawned shell
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Database process spawned shell
---

# Database process spawned shell
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
## What happened{% #what-happened %}

The process `{{ @process.comm }}` was executed by a database process (for example, MySQL, PostgreSQL, or MongoDB), potentially by using an exploit.

## Goal{% #goal %}

Detect common shell utilities, HTTP utilities, or shells spawned by a database process (for example, MySQL, PostgreSQL, or MongoDB).

## Strategy{% #strategy %}

Attacks on databases often take advantage of oversights in I/O sanitization and validation to run attacker statements and commands. For example, these attacks could take the form of database query injection, which can signal the beginning of an intrusion and wider attack, by establishing a web shell or exfiltrating data. This detection triggers when common shell utilities, HTTP utilities, or shells are spawned by one of a set of database processes (e.g., MySQL, MongoDB, PostgreSQL). This is atypical behavior for a database. If this is unexpected behavior, it could indicate an attacker attempting to compromise your database or host machine.

## Triage and response{% #triage-and-response %}

1. Determine whether or not there is an approved purpose for your database to execute shells and utilities.
1. If this behavior is unexpected, attempt to contain the compromise (this may be achieved by terminating the workload, depending on the stage of attack). Investigate application logs or APM data to look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Find and repair the root cause of the exploit.

*Requires Agent version 7.27 or greater*
