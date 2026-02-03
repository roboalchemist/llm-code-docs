# Source: https://docs.datadoghq.com/security/default_rules/def-000-nul.md

---
title: Post compromise shell detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Post compromise shell detected
---

# Post compromise shell detected
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190) 
## What happened{% #what-happened %}

The process `{{ @process.comm }}` was executed with arguments indicating a post compromise shell being created for remote access.

## Goal{% #goal %}

Detect attempts to create an interactive shell from common web or application processes.

## Strategy{% #strategy %}

Many applications (for example, certain databases, web servers, and search engines) are hosted by binaries that run on the host. Attackers may take advantage of flaws in programs built with these applications (for example, SQL injection on a database running as a Java process).

This detection triggers when a process spawns common shell utilities, HTTP utilities, or shells with arguments that are known to be used to establish shells on the targeted asset. If this is unexpected behavior, it could indicate an attacker is attempting to compromise your host.

## Triage and response{% #triage-and-response %}

1. Determine the nature and purpose of the process.
1. Determine whether there is an approved purpose for the process to execute shells and utilities.
1. If this behavior is unexpected, attempt to contain the compromise (this may be achieved by terminating the workload, depending on the stage of attack). Investigate application logs or APM data to look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Find and repair the root cause of the exploit.
