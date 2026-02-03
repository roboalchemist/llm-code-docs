# Source: https://docs.datadoghq.com/security/default_rules/eix-qdn-n68.md

---
title: DNS lookup for IP lookup service
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > DNS lookup for IP lookup service
---

# DNS lookup for IP lookup service
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1016-system-network-configuration-discovery](https://attack.mitre.org/techniques/T1016) 
## What happened{% #what-happened %}

A DNS lookup was made for the domain `{{ @dns.question.name }}`, which is used to discover the public IP of the host.

## Goal{% #goal %}

IP check services return the public IP of the client. They are used legitimately for configuration purposes when utilizing infrastructure as code. They can be abused by attackers to determine the organization they have compromised.

## Strategy{% #strategy %}

Detect when a DNS lookup is done for a domain belonging to an IP check service.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@process.executable.name}}` is expected to make a connection to `{{@dns.question.name}}`.
1. If the DNS lookup is unexpected, contain the host or container and roll back to a known good configuration.
1. Start incident response and determine the initial entry point.

*Requires Agent version 7.36 or greater*
