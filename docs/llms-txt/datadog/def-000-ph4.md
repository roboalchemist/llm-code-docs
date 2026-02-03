# Source: https://docs.datadoghq.com/security/default_rules/def-000-ph4.md

---
title: Anomalous number of OCI instances created in multiple availability domains
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous number of OCI instances
  created in multiple availability domains
---

# Anomalous number of OCI instances created in multiple availability domains

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496) 
## Goal{% #goal %}

Detect when an anomalous number of OCI instances are created in multiple availability domains. This could be an indication of cryptomining activity.

## Strategy{% #strategy %}

Monitor Oracle Cloud Audit logs and detect when a single user or service account evokes the `LaunchInstance` API call an anomalous number of times in multiple distinct availability domains.

## Triage and response{% #triage-and-response %}

1. Determine if the user `{{@usr.name}}` and IP address `{{@network.client.ip}}` should be performing the observed event: `{{@evt.name}}`.
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. Otherwise, use the Cloud SIEM - User Investigation dashboard to see if the user `{{@usr.name}}` has taken other actions.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and an investigation.
