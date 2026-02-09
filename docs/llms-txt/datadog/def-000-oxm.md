# Source: https://docs.datadoghq.com/security/default_rules/def-000-oxm.md

---
title: Sensitive namespace modified using kubectl
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Sensitive namespace modified using
  kubectl
---

# Sensitive namespace modified using kubectl
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1609-container-administration-command](https://attack.mitre.org/techniques/T1609) 
## Goal{% #goal %}

Detect the use of `kubectl` inside a container to modify the ConfigMap of a sensitive namespace.

## Strategy{% #strategy %}

This detection triggers when `kubectl` is executed with specific arguments related to modifying the ConfigMap of a sensitive namespace.

## Triage and response{% #triage-and-response %}

1. Identify the purpose of the configuration being applied, and determine if it is authorized.
1. If it is not authorized, identify and revoke the credential used to authenticate to the Kubernetes API.
1. Initiate the incident response process.
1. Remediate compromised resources and repair the root cause.

## What happened{% #what-happened %}

A `kubectl` command was used to modify a ConfigMap in a sensitive namespace, potentially to alter cluster configuration or inject malicious settings.

*Requires Agent version 7.27 or greater*
