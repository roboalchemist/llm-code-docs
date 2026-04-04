# Source: https://docs.datadoghq.com/security/default_rules/def-000-bxh.md

---
title: Generic DNS tunnel detected by Zeek
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Generic DNS tunnel detected by Zeek
---

# Generic DNS tunnel detected by Zeek
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1071-application-layer-protocol](https://attack.mitre.org/techniques/T1071)
## Goal{% #goal %}

Zeek [generic DNS tunnel](https://corelight.com/blog/corelight-sensors-detect-the-chachi-rat) detected.

## Strategy{% #strategy %}

This rule monitors Zeek logs for the generic DNS tunnel detector. The algorithm detects DNS tunnels without requiring use of signatures for every DNS tunneling tool. Since the algorithm measures information transfer, it is capable of detecting non-malicious tunnels that occur all the time. Attackers use DNS tunneling for command and control communications, as it is crucial to network operations and security monitoring visibility may be limited.

## Triage and response{% #triage-and-response %}

1. Assess `{{@dns.question.name}}` domain reputation to determine if domain has been noted as malicious by vendors.
1. Check for other signals from the originating device as a possible indication that the device has been compromised.
1. If it is determined that the activity is malicious:
   - Block the domain, if it aligns with organization incident response processes.
   - Begin your organization's incident response process and investigate.
