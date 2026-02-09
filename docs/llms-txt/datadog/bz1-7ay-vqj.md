# Source: https://docs.datadoghq.com/security/default_rules/bz1-7ay-vqj.md

---
title: >-
  A Kubernetes user attempted to perform a high number of actions that were
  denied
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A Kubernetes user attempted to perform
  a high number of actions that were denied
---

# A Kubernetes user attempted to perform a high number of actions that were denied
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1613-container-and-resource-discovery](https://attack.mitre.org/techniques/T1613) 
## Goal{% #goal %}

Identify when a Kubernetes user attempts to perform a high number of actions that are denied in a short amount of time.

## Strategy{% #strategy %}

This rule identifies responses of the API server where the reason for the error is set to `Forbidden`, indicating that an authenticated user attempted to perform an action that they are not explicitly authorized to perform.

The rule flags users who receive permission denied errors on several distinct API endpoints in a short amount of time.

## Triage and response{% #triage-and-response %}

1. Determine if the user: `{{@usr.id}}` is expected to perform the denied actions. If yes, the alert may be due to a misconfigured application or a service account with insufficient privileges.
1. Use the Cloud SIEM `User Investigation` dashboard to review any user actions that may have occurred after the potentially malicious action.

## Changelog{% #changelog %}

- 7 May 2024 - Updated detection query to include logs from Azure Kubernetes Service.
- 15 July 2024 - Updated detection query to include logs from Google Kubernetes Engine.
