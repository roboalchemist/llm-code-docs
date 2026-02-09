# Source: https://docs.datadoghq.com/security/default_rules/wnt-129-8hr.md

---
title: SSL certificate tampering
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > SSL certificate tampering
---

# SSL certificate tampering
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1553-subvert-trust-controls](https://attack.mitre.org/techniques/T1553) 
## What happened{% #what-happened %}

`{{ @file.path }}` was created or modified by `{{ @process.comm }}`, potentially to subvert trust.

## Goal{% #goal %}

Detect potential tampering with SSL certificates.

## Strategy{% #strategy %}

SSL certificates, and other forms of trust controls establish trust between systems. Attackers may attempt to subvert trust controls such as SSL certificates in order to trick systems or users into trusting attacker-owned assets such as fake websites, or falsely signed applications.

## Triage and response{% #triage-and-response %}

1. Check whether there were any planned changed to the SSL certificates stores in your infrastructure.
1. If these changes are not acceptable, roll back the host or container in question to a known trustworthy configuration.
1. Investigate security signals (if present) occurring around the time of the event to establish an attack path.
1. Find and repair the root cause of the exploit.

*Requires Agent version 7.27 or greater*
