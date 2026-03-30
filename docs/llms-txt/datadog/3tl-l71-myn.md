# Source: https://docs.datadoghq.com/security/default_rules/3tl-l71-myn.md

---
title: DNS lookup for paste service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > DNS lookup for paste service
---

# DNS lookup for paste service
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1105-ingress-tool-transfer](https://attack.mitre.org/techniques/T1105)
## What happened{% #what-happened %}

`{{ @process.comm }}` made a DNS lookup for the domain `{{ @dns.question.name }}`, potentially to download malicious tools or to exfiltrate data.

## Goal{% #goal %}

Paste sites such as pastebin.com can be used by attackers to host malicious scripts, configuration files, and other text data. The files are then downloaded to the host using a network utility such as `wget` or `curl`. These sites may also be used to exfiltrate data.

## Strategy{% #strategy %}

Detect when a process performs a DNS lookup for a paste site.

## Triage and response{% #triage-and-response %}

1. Check if the application `{{@process.executable.name}}` is expected to make connections to `{{@dns.question.name}}`.
1. If the DNS lookup is unexpected, contain the host or container and roll back to a known good configuration.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.36 or greater*
