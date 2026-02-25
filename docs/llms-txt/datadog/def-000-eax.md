# Source: https://docs.datadoghq.com/security/default_rules/def-000-eax.md

---
title: >-
  Cisco Secure Email Threat Defense unusual spike found for the high severity
  verdict techniques
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Cisco Secure Email Threat Defense
  unusual spike found for the high severity verdict techniques
---

# Cisco Secure Email Threat Defense unusual spike found for the high severity verdict techniques

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1566-phishing](https://attack.mitre.org/techniques/T1566)
## Goal{% #goal %}

Detects emails when there are unusual spikes in high-severity verdict techniques that helps to analyze the techniques that cause the threats in email.

## Strategy{% #strategy %}

This rule monitors emails to detect unusual spikes in high-severity verdict techniques.

## Triage and response{% #triage-and-response %}

1. Investigate high-severity technique - `{{@verdict.techniques.type}}` using which threat emails has been detected.
1. Assess the potential impact of these threat emails on systems, data, operations, and overall security posture.
1. Take prevention steps to reduce threats emails sent with similar techniques.
