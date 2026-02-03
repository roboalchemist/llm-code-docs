# Source: https://docs.datadoghq.com/security/default_rules/def-000-p6y.md

---
title: GitHub private repository changed to public visibility
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > GitHub private repository changed to
  public visibility
---

# GitHub private repository changed to public visibility

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0009-collection](https://attack.mitre.org/tactics/TA0009)Technique:[T1213-data-from-information-repositories](https://attack.mitre.org/techniques/T1213) 
## Goal{% #goal %}

Detect when a GitHub repository visibility is changed to public.

## Strategy{% #strategy %}

This rule monitors GitHub audit logs for when a GitHub repository that was previously private gets moved to public visibility. Private repositories typically contain intellectual property, sensitive architecture, or other important data. Private repositories should be made public only with approval from the organization.

## Triage and response{% #triage-and-response %}

1. Determine if the change taken by `{{@github.actor}}` is authorized.
1. If the change was not authorized or was unexpected, begin your organization's incident response process and investigate.

- 3 January 2025 - update detection rule severity from High to Medium.
