# Source: https://docs.datadoghq.com/security/default_rules/def-000-tz6.md

---
title: Anomalous number of Google Cloud Compute GPU virtual machines created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Anomalous number of Google Cloud
  Compute GPU virtual machines created
---

# Anomalous number of Google Cloud Compute GPU virtual machines created
Classification:attackTactic:[TA0040-impact](https://attack.mitre.org/tactics/TA0040)Technique:[T1496-resource-hijacking](https://attack.mitre.org/techniques/T1496) 
## Goal{% #goal %}

Detect when an attempt to create a GPU-based virtual machine (VM) instance in Google Compute Engine occurs.

## Strategy{% #strategy %}

This rule monitors Google Cloud Audit Logs to determine when an attempt to create an anomalous number of GPU-based VM instances in Google Compute Engine has occurred. An attacker who has already gained initial access may try to create GPU-based VM instances with goal mining cryptocurrency.

## Triage and response{% #triage-and-response %}

1. Reach out to the user or owner of the service account to determine if this action is legitimate.
1. If the action is legitimate, consider including the user in a suppression list. See this article on [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. Otherwise, use the Cloud SIEM - User Investigation dashboard to see if the user `{{@usr.id}}` has taken other actions.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and an investigation.

## Changelog{% #changelog %}

- 23 September 2025 - Updated query to exclude `GCP Managed Service Accounts`.
