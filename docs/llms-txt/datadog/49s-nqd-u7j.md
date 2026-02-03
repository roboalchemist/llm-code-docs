# Source: https://docs.datadoghq.com/security/default_rules/49s-nqd-u7j.md

---
title: AWS EC2 new event for EKS Node Group
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AWS EC2 new event for EKS Node Group
---

# AWS EC2 new event for EKS Node Group
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1078-valid-accounts](https://attack.mitre.org/techniques/T1078) 
## Goal{% #goal %}

Detect when an AWS EKS node group makes a new API call.

## Strategy{% #strategy %}

This rule sets a baseline for host activity across an AWS EKS node group, and enables detection of potentially anomalous activity when a node group makes a new API call.

A new API call from a node group can indicate an attacker gaining a foothold within the system and trying API calls not normally associated with this node group.

## Triage and response{% #triage-and-response %}

1. Investigate API activity for the AWS EKS node group to determine if the specific API call is malicious.
1. Review any other security signals for the AWS EKS node group.
1. If the activity is deemed malicious:
   - If possible, isolate the compromised hosts.
   - Determine what other API calls were made by the EKS node group.
   - Begin your organization's incident response process and investigate.
