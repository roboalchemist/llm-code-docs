# Source: https://docs.datadoghq.com/security/default_rules/kqq-0do-gio.md

---
title: New Kubernetes privileged pod created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > New Kubernetes privileged pod created
---

# New Kubernetes privileged pod created
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1578-modify-cloud-compute-infrastructure](https://attack.mitre.org/techniques/T1578) 
## Goal{% #goal %}

Detect when a privileged pod is created. Privileged pods remove container isolation which allows privileged actions on the host.

## Strategy{% #strategy %}

This rule monitors when a pod (`@objectRef.resource:pods`) is created (`@http.method:create`) and the privileged security context (`@requestObject.spec.containers.securityContext.privileged`) is `true`.

## Triage & Response{% #triage--response %}

Determine if the pod should be privileged.

## Changelog{% #changelog %}

- 7 May 2024 - Updated detection query to include logs from Azure Kubernetes Service.
- 16 July 2024 - Updated detection query to include logs from Google Kubernetes Engine.
