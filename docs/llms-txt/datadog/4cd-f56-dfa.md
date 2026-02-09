# Source: https://docs.datadoghq.com/security/default_rules/4cd-f56-dfa.md

---
title: AWS S3 Public Access Block removed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS S3 Public Access Block removed
---

# AWS S3 Public Access Block removed
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562)Framework:pciControl:7.2.1 
## Goal{% #goal %}

Detect when the S3 Public Access Block configuration has been removed

## Strategy{% #strategy %}

This rule lets you monitor this CloudTrail API call to detect if an attacker is deleting the S3 Public Access Block configuration:

- [DeleteAccountPublicAccessBlock](https://docs.aws.amazon.com/cli/latest/reference/s3api/delete-public-access-block.html)

## Triage and response{% #triage-and-response %}

1. Determine who the user was who made this API call.
1. Contact the user and inform them of best practices of enabling Public Access Block on S3 buckets.
1. Re-enable Public Access Block on the S3 bucket.

More details on S3 Public Block Public Access can be found [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/access-control-block-public-access.html).

## Changelog{% #changelog %}

- 18 March 2022 - Updated severity and query.
- 31 October 2022 - Updated severity.
