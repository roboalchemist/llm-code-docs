# Source: https://docs.datadoghq.com/security/default_rules/def-000-zxh.md

---
title: Anomalous number of instances with high GPU created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous number of instances with high
  GPU created
---

# Anomalous number of instances with high GPU created

{% alert level="danger" %}
This rule is part of a beta feature. To learn more, [contact Support](https://docs.datadoghq.com/help/).
{% /alert %}
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496) 
## Goal{% #goal %}

Detect when an attempt to create a high GPU-based virtual machine (VM) instance in OCI occurs.

## Strategy{% #strategy %}

This rule monitors OCI Audit Logs to determine when an attempt to create an anomalous number of high GPU-based VM instances in Google Compute Engine has occurred. An attacker who has already gained initial access may try to create GPU-based VM instances with goal mining cryptocurrency.

## Triage and response{% #triage-and-response %}

1. Determine if `{{@usr.name}}` should be creating the VM instances.
1. If the action is legitimate, consider including the user in a suppression list. See this article on [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and an investigation.
