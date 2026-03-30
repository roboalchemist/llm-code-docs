# Source: https://docs.datadoghq.com/security/default_rules/a9f-f61-a6c.md

---
title: New Kubernetes Namespace Created
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > New Kubernetes Namespace Created
---

# New Kubernetes Namespace Created
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1578-modify-cloud-compute-infrastructure](https://attack.mitre.org/techniques/T1578)
## Goal{% #goal %}

Detect when a user is creating a Kubernetes namespace.

## Strategy{% #strategy %}

This rule monitors when a `create` action occurs for the Kubernetes namespace (`@objectRef.resource:namespaces`) to detect when a user is creating a new Kubernetes namespace.

## Triage and response{% #triage-and-response %}

Determine if the user should be creating this new namespace.

## Changelog{% #changelog %}

- 7 May 2024 - Updated detection query to include logs from Azure Kubernetes Service.
- 16 July 2024 - Updated detection query to include logs from Google Kubernetes Engine.
