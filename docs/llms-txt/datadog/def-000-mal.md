# Source: https://docs.datadoghq.com/security/default_rules/def-000-mal.md

---
title: Hash of known malware detected
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Hash of known malware detected
---

# Hash of known malware detected
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1059-command-and-scripting-interpreter](https://attack.mitre.org/techniques/T1059) 
## What happened{% #what-happened %}

The file `{{ @file.path }}` was identified as malware based on its hash.

## Goal{% #goal %}

Detect malicious files observed in threat intelligence feeds.

## Strategy{% #strategy %}

Hashes are collected and compared to a database of known malicious files. In some cases fuzzy hashing is used to match files similar to known malware.

For more details see [our blog post](https://www.datadoghq.com/blog/cloud-security-malware-detection/).

## Triage & Response{% #triage--response %}

1. Verify the file `{{ @file.path }}` is unexpected and does not have a business purpose.
1. Pause or isolate the affected container.
1. Review related signals and relevant logs to identify additional malicious activity.
1. Follow your organization's internal processes for investigating and remediating compromised systems.

*Requires Agent version 7.49 or later*
