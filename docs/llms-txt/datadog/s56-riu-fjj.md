# Source: https://docs.datadoghq.com/security/default_rules/s56-riu-fjj.md

---
title: Network utility executed with suspicious URI
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Network utility executed with
  suspicious URI
---

# Network utility executed with suspicious URI
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1105-ingress-tool-transfer](https://attack.mitre.org/techniques/T1105)
## What happened{% #what-happened %}

`{{ @process.comm }}` was executed, referencing a file with a file extension that is unusual for a cloud workload.

## Goal{% #goal %}

Detect HTTP requests with patterns that are unusual for a cloud workload.

## Strategy{% #strategy %}

This rule generates a signal when a network utility such as `curl` or `wget` makes a request for a URI with an unusual pattern. The patterns used in this rule appeared in previous compromises of cloud resources. For example, it is unusual for a production workload to download a file with a `.jpg` extension. Threat actors have used this extension to evade detection.

## Triage and response{% #triage-and-response %}

1. Determine the URL being requested using the process tree.
1. Identify other compromised systems by searching logs for requests to this URI or domain.
1. Attempt to contain the compromise (possibly by terminating the workload, depending on the stage of attack). Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.27 or greater.*
