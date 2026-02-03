# Source: https://docs.datadoghq.com/security/default_rules/1y1-elh-nph.md

---
title: AWS Kinesis Firehose stream destination modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > AWS Kinesis Firehose stream destination
  modified
---

# AWS Kinesis Firehose stream destination modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## Goal{% #goal %}

Detects when an AWS Kinesis Firehose Destination is modified.

## Strategy{% #strategy %}

The rule monitors AWS Kinesis Firehose logs `@eventSource:firehose.amazonaws.com` and detects when the `@evt.name` is `UpdateDestination`.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` is expected to perform the `{{@evt.name}}` API call on the account: `{{@userIdentity.accountId}}`.
1. If the API call was not made by the user, rotate the user credentials and investigate what other APIs were successfully accessed.
   - Rotate the credentials.
   - Investigate if the same credentials made other unauthorized API calls.
