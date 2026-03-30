# Source: https://docs.datadoghq.com/security/default_rules/66d-nnk-onm.md

---
title: Anomalous S3 bucket activity from user ARN
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous S3 bucket activity from user
  ARN
---

# Anomalous S3 bucket activity from user ARN
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1530-data-from-cloud-storage](https://attack.mitre.org/techniques/T1530)
## Goal{% #goal %}

Detect when an AWS user performs S3 bucket write activities they do not usually perform.

## Strategy{% #strategy %}

Monitor cloudtrail logs for S3 Data Plane events (`@eventCategory:Data`) to detect when an AWS User (`@userIdentity.arn`) is detected performing anomalous S3 Write `(@evt.name:(Abort* OR Create* OR Delete* OR Initiate* OR Put* OR Replicate* OR Update*))` API calls.

## Triage and response{% #triage-and-response %}

1. Determine if user: `{{@userIdentity.arn}}` should be performing the: `{{@evt.name}}` API calls.
   - Use the Cloud SIEM - User Investigation dashboard to assess user activity.
1. If not, investigate the user: `{{@userIdentity.arn}}` for indicators of account compromise and rotate credentials as necessary.

## Changelog{% #changelog %}

27 October 2022 - Updated tags.
