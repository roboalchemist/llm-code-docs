# Source: https://docs.datadoghq.com/security/default_rules/wpm-g1s-8yx.md

---
title: A new Kubernetes admission controller was created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > A new Kubernetes admission controller
  was created
---

# A new Kubernetes admission controller was created
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1578-modify-cloud-compute-infrastructure](https://attack.mitre.org/techniques/T1578) 
## Goal{% #goal %}

Identify when a new Kubernetes [admission controller](https://kubernetes.io/docs/reference/access-authn-authz/admission-controllers/) is created in the cluster.

Admission controllers can intercept all incoming requests to the API server. An attacker can use them to establish persistence or to access sensitive data (such as secrets) sent to the API server.

## Strategy{% #strategy %}

This rule identifies when a `MutatingWebhookConfiguration` or `ValidatingWebhookConfiguration` is created.

## Triage and response{% #triage-and-response %}

1. Determine if the admission controller being created is expected.
1. Determine if the user: `{{@usr.id}}` should be creating the admission controller.
1. Use the Cloud SIEM `User Investigation` dashboard to review user actions that occurred after the potentially malicious action.

## Changelog{% #changelog %}

- 20 September 2022 - Updated tags.
- 7 May 2024 - Updated detection query to include logs from Azure Kubernetes Service.
- 15 July 2024 - Updated detection query to include logs from Google Kubernetes Engine.
