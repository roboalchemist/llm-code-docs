# Source: https://docs.datadoghq.com/security/default_rules/def-000-yyy.md

---
title: Bitsadmin used to download or execute a file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Bitsadmin used to download or execute a
  file
---

# Bitsadmin used to download or execute a file
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1105-ingress-tool-transfer](https://attack.mitre.org/techniques/T1105) 
## What happened{% #what-happened %}

`{{ @process.executable.name }}` was used to download or execute a file, potentially to download malicious tools.

## Goal{% #goal %}

Detect when bitsadmin is used to download or execute a file.

## Strategy{% #strategy %}

Threat actors are known to utilize tools found natively in a victim's environment to accomplish their objectives. Bitsadmin, a legitimate Windows binary, has been abused by malicious actors in the past to fetch additional tools and payloads, as well as execute malicious content.

## Triage and response{% #triage-and-response %}

1. Identify what is being downloaded or executed, and determine if authorized
1. If it's not authorized, isolate the host from the network.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.50.0 or greater.*
