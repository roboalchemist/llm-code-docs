# Source: https://docs.datadoghq.com/security/default_rules/def-000-zyz.md

---
title: Certutil used to transmit or decode a file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Certutil used to transmit or decode a
  file
---

# Certutil used to transmit or decode a file
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1105-ingress-tool-transfer](https://attack.mitre.org/techniques/T1105) 
## What happened{% #what-happened %}

The command `{{ @process.executable.name }}` was executed, potentially to download malicious tools.

## Goal{% #goal %}

Detect when certutil is used to download a file or decode content.

## Strategy{% #strategy %}

Threat actors are known to utilize tools found natively in a victim's environment to accomplish their objectives. Certutil, a legitimate Windows binary, has been abused by malicious actors in the past to fetch additional tools and payloads, as well as decode obfuscated payloads to avoid detection.

## Triage and response{% #triage-and-response %}

1. Identify what is being downloaded or decoded.
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.50.0 or greater.*
