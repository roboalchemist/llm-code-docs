# Source: https://docs.datadoghq.com/security/default_rules/j21-bxf-prt.md

---
title: Exfiltration attempt via network utility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Exfiltration attempt via network
  utility
---

# Exfiltration attempt via network utility
Classification:attackTactic:[TA0010-exfiltration](https://attack.mitre.org/tactics/TA0010)Technique:[T1048-exfiltration-over-alternative-protocol](https://attack.mitre.org/techniques/T1048) 
## What happened{% #what-happened %}

`{{ @process.comm }}` was executed with arguments indicating data exfiltration.

## Goal{% #goal %}

Detect data exfiltration using a web utility such as `cURL` or `wget`.

## Strategy{% #strategy %}

Some network utilities support arguments for sending file contents in a network request. Attackers use this functionality to exfiltrate data of sensitive files. Multiple files may be packaged into a file archive before being exfiltrated.

## Triage and response{% #triage-and-response %}

1. Inspect the process arguments. Identify the content being sent and the destination URL.
1. Determine if this activity is expected.
1. If the network request is not expected, contain the host or container and roll back to a known good configuration. Initiate the incident response process.
1. Review related signals for other suspicious activity.

*Requires Agent version 7.28 or greater*
