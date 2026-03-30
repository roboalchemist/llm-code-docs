# Source: https://docs.datadoghq.com/security/default_rules/wub-i7c-72x.md

---
title: Unfamiliar process created by web application
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unfamiliar process created by web
  application
---

# Unfamiliar process created by web application
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
## What happened{% #what-happened %}

The web server process executed the command `{{ @process.comm }}`, which may indicate the application is vulnerable to remote code execution (RCE).

## Goal{% #goal %}

Detect shell utilities, HTTP utilities, or shells spawned by a web server.

## Strategy{% #strategy %}

Web shell attacks often involve attackers loading and running malicious files onto a victim machine, creating a backdoor on the compromised system. Attackers use web shells for a variety of purposes, and they can signal the beginning of an intrusion or wider attack. This detection triggers when shell utilities, HTTP utilities, or shells are spawned by a common web server process.

This rule uses the New Value detection method. Datadog learns the historical behavior of a specified field in Agent logs and then creates a signal when unfamiliar values appear.

## Triage and response{% #triage-and-response %}

1. Determine whether or not there is an approved purpose for your web application to execute the process `{{ @process.comm }}`.
1. If this behavior is unexpected, attempt to contain the compromise (this may be achieved by terminating the workload, depending on the stage of attack). Investigate application logs or APM data to look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Find and repair the root cause of the exploit.

## Changelog{% #changelog %}

- 26 September 2024 - Updated rule name and description

*Requires Agent version 7.27 or later*
