# Source: https://docs.datadoghq.com/security/default_rules/9el-i95-dnl.md

---
title: A user received an anomalous number of AccessDenied errors
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A user received an anomalous number of
  AccessDenied errors
---

# A user received an anomalous number of AccessDenied errors
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1069-permission-groups-discovery](https://attack.mitre.org/techniques/T1069)
## Goal{% #goal %}

Detect when a user is assessing privileges in AWS through API bruteforcing technique.

## Strategy{% #strategy %}

This rule lets you monitor CloudTrail to detect when the error message of `AccessDenied` is returned on an anomalous number of unique API calls.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@userIdentity.arn}}` should be attempting to use the identified API calls: `{{@evt.name}}`.
   - Use the Cloud SIEM - User Investigation dashboard to assess user activity.
1. Contact the user to see if they intended to make these API calls.
1. If the user did not make the API calls:
   - Rotate the credentials.
   - Investigate to see what API calls might have been made that were successful throughout the rest of the environment.

## Changelog{% #changelog %}

- 17 March 2025 - Updated rule query to exclude `DatadogIntegrationRole`.
