# Source: https://docs.datadoghq.com/security/default_rules/def-000-jhq.md

---
title: SSH watched country login notice from Zeek
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > SSH watched country login notice from
  Zeek
---

# SSH watched country login notice from Zeek
Classification:attack 
## Goal{% #goal %}

Detect the SSH [watched country login notice](https://docs.zeek.org/en/master/scripts/policy/protocols/ssh/geo-data.zeek.html).

## Strategy{% #strategy %}

This rule monitors Zeek logs for the notice `SSH::Watched_Country_Login`. The notice is generated if an SSH login is seen originating to or from a "watched" country based on the `SSH::watched_countries` variable.

## Triage and response{% #triage-and-response %}

1. Identify the owners of the host that has been accessed.
1. Work with the team to understand if this authentication was expected/legitimate.
1. If it is determined that the activity is malicious:
   - Block the IP address, if it aligns with organization incident response processes.
   - Begin your organization's incident response process and investigate.
