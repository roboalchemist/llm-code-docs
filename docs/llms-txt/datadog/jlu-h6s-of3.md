# Source: https://docs.datadoghq.com/security/default_rules/jlu-h6s-of3.md

---
title: Anomalous number of S3 buckets accessed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Anomalous number of S3 buckets accessed
---

# Anomalous number of S3 buckets accessed
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1619-cloud-storage-object-discovery](https://attack.mitre.org/techniques/T1619)
## Goal{% #goal %}

Detect when an AWS assumed role accesses S3 buckets that they do not usually access.

## Strategy{% #strategy %}

Monitor cloudtrail logs to identify when a `@userIdentity.assumed_role` makes an anomalous amount of `GetObject` calls to a unique number of S3 buckets (`@requestParameters.bucketName`).

## Triage and response{% #triage-and-response %}

Determine if the user using the assumed role: {{@userIdentity.assumed_role}} should be accessing a bunch of random buckets.

- Here is a list of buckets that were accessed (up to 10): {{@requestParameters.bucketName}}

## Changelog{% #changelog %}

- 30 March 2022 - Updated query and signal message.
- 17 October 2022 - Updated tags.
- 11 January 2023 - Updated severity.
