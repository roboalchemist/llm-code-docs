# Source: https://docs.datadoghq.com/security/default_rules/6b4-f87-bcd.md

---
title: Kubernetes Service Created with NodePort
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubernetes Service Created with
  NodePort
---

# Kubernetes Service Created with NodePort
Classification:attackTactic:[TA0001-initial-access](https://attack.mitre.org/tactics/TA0001)Technique:[T1190-exploit-public-facing-application](https://attack.mitre.org/techniques/T1190)
## Goal{% #goal %}

Detect when a service's port is attached to the node's IP.

## Strategy{% #strategy %}

This rule monitors when a create (`@http.method:create`) action occurs for a service (`@objectRef.resource:services`) attaching the service's port to the node's IP `@requestObject.spec.type:NodePort`.

Exposing the service's port to the the node's IP allows other hosts on the network namespace to access this service.

## Triage and response{% #triage-and-response %}

Determine if the service needs to expose it's network connection with `NodePort` access.

## Changelog{% #changelog %}

- 7 May 2024 - Updated detection query to include logs from Azure Kubernetes Service.
- 16 July 2024 - Updated detection query to include logs from Google Kubernetes Engine.
