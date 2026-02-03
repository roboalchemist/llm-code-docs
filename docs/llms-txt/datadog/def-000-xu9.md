# Source: https://docs.datadoghq.com/security/default_rules/def-000-xu9.md

---
title: SSH login by password guesser from Zeek
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > SSH login by password guesser from Zeek
---

# SSH login by password guesser from Zeek
Classification:attackTactic:[TA0006-credential-access](https://attack.mitre.org/tactics/TA0006)Technique:[T1110-brute-force](https://attack.mitre.org/techniques/T1110) 
## Goal{% #goal %}

Detect the [SSH login by password guesser notice](https://docs.zeek.org/en/master/scripts/policy/protocols/ssh/detect-bruteforcing.zeek.html).

## Strategy{% #strategy %}

This rule monitors Zeek logs for the notice `SSH::Login_By_Password_Guesser`. The notice is generated if a successful login attempt is detected for a host that has been previously identified as a "password guesser".

## Triage and response{% #triage-and-response %}

1. Identify the owners of the host that has been accessed.
1. Work with the team to understand if this authentication was expected/legitimate.
1. If it is determined that the activity is malicious:
   - Block the IP address, if it aligns with organization incident response processes.
   - Begin your organization's incident response process and investigate.
