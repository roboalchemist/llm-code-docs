# Source: https://docs.datadoghq.com/security/default_rules/1bw-akj-fk7.md

---
title: Log4Shell Scanning Detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Log4Shell Scanning Detected
---

# Log4Shell Scanning Detected
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
## Goal{% #goal %}

Detect when a Log4j scanning attempt occurs in your environment.

## Strategy{% #strategy %}

Regex search on logs to find specific payloads indicative of Log4j scanning.

## Triage and response{% #triage-and-response %}

1. Investigate if the host is running a vulnerable version of the Log4j Java library
1. Use the [Log4j Investigation Dashboard](https://app.datadoghq.com/dash/integration/cloud_security_platform_log4shell_investigator) to conduct impact analysis
1. Explore what other services the attacker hit in the last day - Linked to investigation query
1. Explore Java logs associated with the attacker - linked to investigation query
