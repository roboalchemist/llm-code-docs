# Source: https://docs.datadoghq.com/security/default_rules/q2g-reo-fw1.md

---
title: A Kubernetes user was assigned cluster administrator permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A Kubernetes user was assigned cluster
  administrator permissions
---

# A Kubernetes user was assigned cluster administrator permissions
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098) 
## Goal{% #goal %}

Identify when a Kubernetes user is assigned cluster-level administrative permissions.

## Strategy{% #strategy %}

This rule monitors when a `ClusterRoleBinding` object is created to bind a Kubernetes user to the `cluster-admin` [default cluster-wide role](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles). This effectively grants the referenced user with full administrator permissions over all the Kubernetes cluster.

## Triage and response{% #triage-and-response %}

1. Determine if the Kubernetes user referenced in `@requestObject.subjects` is expected to have been granted administrator permissions on the cluster
1. Determine if the actor (`@usr.id`) is authorized to assign administrator permissions
1. Use the Cloud SIEM `User Investigation` dashboard to review any user actions that may have occurred after the potentially malicious action.

## Changelog{% #changelog %}

- 20 September 2022 - Updated tags.
- 7 May 2024 - Updated detection query to include logs from Azure Kubernetes Service.
- 15 July 2024 - Updated detection query to include logs from Google Kubernetes Engine.
