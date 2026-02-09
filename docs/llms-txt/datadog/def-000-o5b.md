# Source: https://docs.datadoghq.com/security/default_rules/def-000-o5b.md

---
title: Domain added to Google Workspace allowlisted domains
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Domain added to Google Workspace
  allowlisted domains
---

# Domain added to Google Workspace allowlisted domains
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Detect when a domain is added to Google Workspace's allowlisted domains.

## Strategy{% #strategy %}

This rule monitors Google Workspace logs to determine when a domain was added to Google Workspace's allowlisted domains. An attacker may add a trusted domain to reduce the level of security controls to allow for the exfiltration or collection of data.

## Triage and response{% #triage-and-response %}

1. Reach out to the user or owner of the service account to determine if this action is legitimate.
1. If the action is legitimate, consider including the user in a suppression list. See [Best practices for creating detection rules with Datadog Cloud SIEM](https://www.datadoghq.com/blog/writing-datadog-security-detection-rules/#fine-tune-security-signals-to-reduce-noise) for more information.
1. Otherwise, use the Cloud SIEM - User Investigation dashboard to see if the user: `{{@usr.email}}` has taken other actions.
1. If the results of the triage indicate that an attacker has taken the action, begin your company's incident response process and an investigation.
