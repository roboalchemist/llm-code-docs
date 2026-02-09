# Source: https://docs.datadoghq.com/security/default_rules/9fq-2av-prp.md

---
title: AWS Detective Graph deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS Detective Graph deleted
---

# AWS Detective Graph deleted
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detect when a user deletes an Amazon Detective behavior graph.

## Strategy{% #strategy %}

This rule lets you monitor this CloudTrail API call to detect if a user has deleted an Amazon Detective behavior graph:

- [DeleteGraph](https://docs.aws.amazon.com/detective/latest/APIReference/API_DeleteGraph.html)

## Triage and response{% #triage-and-response %}

1. Determine if the behavior graph should have been deleted.
1. Determine which user ({{@userIdentity.arn}}) in your organization deleted the behavior graph.
1. If the user did not make the API call:
   - Rotate the credentials.
   - Investigate if the same credentials made other unauthorized API calls.

## Changelog{% #changelog %}

- 1 April 2022 - Updated rule and signal message.
- 18 November 2022 - Updated severity.
