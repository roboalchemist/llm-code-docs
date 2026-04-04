# Source: https://docs.datadoghq.com/security/default_rules/def-000-p8z.md

---
title: GitHub unknown user cloned private repository
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub unknown user cloned private
  repository
---

# GitHub unknown user cloned private repository

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213)
## Goal{% #goal %}

Detect when a unknown actor clones a Github repository.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a repository clone occurs but the actor field is null.

## Triage and response{% #triage-and-response %}

1. Determine if the clone action was taken by IP address associated with the activity is from a known corporate device.
1. If the clone action cannot be attributed to an internal user, then begin your organization's incident response process and investigate.
