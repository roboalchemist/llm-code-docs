# Source: https://docs.datadoghq.com/security/default_rules/def-000-yfb.md

---
title: Anomalous number of AWS Lambda functions deleted
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous number of AWS Lambda
  functions deleted
---

# Anomalous number of AWS Lambda functions deleted
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1485-data-destruction](https://attack.mitre.org/techniques/T1485) 
## Goal{% #goal %}

Detects anomalous deletion of AWS Lambda functions. This rule identifies when a user or role deletes an unusual number of Lambda functions within a short time period.

## Strategy{% #strategy %}

This rule monitors AWS CloudTrail logs for `DeleteFunction20150331` events. The detection uses anomaly detection to establish a baseline of normal deletion patterns over a 24-hour learning period and identifies deviations from this baseline. Lambda functions often contain critical business logic and their deletion can disrupt services or remove security controls.

## Triage & Response{% #triage--response %}

1. Review the `@userIdentity.arn` to identify the account or role that performed the deletions.
1. Check the `@requestParameters.functionName` to determine which specific Lambda functions were deleted.
1. Verify if the deleted functions were part of a planned decommissioning or migration effort.
1. Examine the CloudTrail logs for additional suspicious activity from the same identity around the time of the deletions.
1. Review AWS CloudWatch logs for the deleted functions to check for any unusual activity prior to deletion.
1. Check if the identity has the necessary permissions to perform these deletions through IAM policies.
1. Restore the deleted functions from backups if available and implement stricter access controls for Lambda function deletion.
