# Source: https://docs.datadoghq.com/security/default_rules/vw5-94j-nr5.md

---
title: Pwnkit privilege escalation attempt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Pwnkit privilege escalation attempt
---

# Pwnkit privilege escalation attempt
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1068-exploitation-for-privilege-escalation](https://attack.mitre.org/techniques/T1068) 
## What happened{% #what-happened %}

`{{ @process.comm }}` was executed with the `SHELL` or `PATH` environment variables, indicating exploitation of the vulnerability `CVE-2021-4034`.

## Goal{% #goal %}

Detect exploitation of `CVE-2021-4034` dubbed PwnKit.

## Strategy{% #strategy %}

PwnKit is a local privilege escalation vulnerability originally found by [Qualys](https://blog.qualys.com/vulnerabilities-threat-research/2022/01/25/pwnkit-local-privilege-escalation-vulnerability-discovered-in-polkits-pkexec-cve-2021-4034). It affects PolicyKit's `pkexec` program, which is a SUID-root program installed by default on many Linux distributions. This detection triggers whenever `pkexec` is executed by a non-root process with the `SHELL` and `PATH` variables set.

## Triage and response{% #triage-and-response %}

1. Determine the purpose of the process executing `pkexec`.
1. Look for any suspicious actions or commands being executed after the `pkexec` execution.
1. If this behavior is unexpected, it could indicate a malicious actor has access to the host and is attempting to increase privileges for post exploitation actions. Investigate application logs or APM data to look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Ensure to update the PolicyKit package to its latest version to mitigate the vulnerability. If updating is not feasible, remove the SUID bit that is set by default on `pkexec` with the following command: `sudo chmod -s \$(which pkexec)`.

*Requires Agent version 7.27 or greater*
