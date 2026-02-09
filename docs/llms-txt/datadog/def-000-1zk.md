# Source: https://docs.datadoghq.com/security/default_rules/def-000-1zk.md

---
title: SSH interesting hostname login notice from Zeek
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SSH interesting hostname login notice
  from Zeek
---

# SSH interesting hostname login notice from Zeek
Classification:attack 
## Goal{% #goal %}

Detect the [SSH interesting hostname login notice](https://docs.zeek.org/en/master/scripts/policy/protocols/ssh/interesting-hostnames.zeek.html).

## Strategy{% #strategy %}

This rule monitors Zeek logs for the notice `SSH::Interesting_Hostname_Login`. The notice is generated if a login originates or responds with a host with a reverse hostname that looks suspicious.

## Triage and response{% #triage-and-response %}

1. Identify the owners of the host that has been accessed.
1. Work with the team to understand if this authentication was expected/legitimate.
1. If it is determined that the activity is malicious:
   - Block the IP address, if it aligns with organization incident response processes.
   - Begin your organization's incident response process and investigate.
