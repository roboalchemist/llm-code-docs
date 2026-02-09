# Source: https://docs.datadoghq.com/security/default_rules/def-000-ouv.md

---
title: Possible brute force attempted against user
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Possible brute force attempted against
  user
---

# Possible brute force attempted against user

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when a user attempts to access the OCI console an anomalous amount of times.

## Strategy{% #strategy %}

This rule monitors OCI to detect the `404` error message.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@user.name}}` should be attempting to use the identified API calls: `{{@evt.name}}`.
1. Contact the user to see if they intended to make these API calls.
1. If the user did not make the API calls:
   - Rotate the credentials.
   - Investigate which unauthorized API calls might have succeeded throughout the rest of the environment.
