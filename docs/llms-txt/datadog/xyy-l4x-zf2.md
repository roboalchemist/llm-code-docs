# Source: https://docs.datadoghq.com/security/default_rules/xyy-l4x-zf2.md

---
title: Google Compute Engine project metadata SSH key added or modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Google Compute Engine project metadata
  SSH key added or modified
---

# Google Compute Engine project metadata SSH key added or modified
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when an attempt to add or modify a SSH key to GCE project metadata occurs.

## Strategy{% #strategy %}

This rule monitors Google Cloud Audit Logs to determine when an attempt to add or modify a SSH key in the GCE project metadata has occurred. A malicious actor who has already gained initial access may try to preserve access or laterally move to other GCE instances by adding their SSH key to the project metadata.

**Notes:**

- This rule triggers with a `Medium` severity when this activity originates from an anonymizing proxy.

## Triage and response{% #triage-and-response %}

1. Reach out to the user or owner of the service account to determine if this action is legitimate.
1. If the action is legitimate, consider including the IP address or ASN in a suppression list. See this article on [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. Otherwise, use the Cloud SIEM - IP Investigation dashboard to see if the IP address: `{{@network.client.ip}}` has taken other actions.
1. If the results of the triage indicate that a malicious actor has taken the action, begin your company's Incident Response process and investigate.

## Changelog{% #changelog %}

- 9 February 2023 - Updated rule title and triage and response section.
- 25 September 2024 - Updated query to replace attribute `@threat_intel.results.category:anonymizer`.
