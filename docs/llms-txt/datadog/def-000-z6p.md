# Source: https://docs.datadoghq.com/security/default_rules/def-000-z6p.md

---
title: Kubernetes service account token created in container
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Kubernetes service account token
  created in container
---

# Kubernetes service account token created in container
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1609-container-administration-command](https://attack.mitre.org/techniques/T1609)
## What happened{% #what-happened %}

A `kubectl` command was used to create a new service account token, potentially to establish persistence or escalate privileges.

## Goal{% #goal %}

Detect the use of `kubectl` commands inside a container to create a new service account token.

## Strategy{% #strategy %}

This detection triggers when `kubectl` is executed with specific arguments related to creating a new service account token.

## Triage and response{% #triage-and-response %}

1. Identify the purpose and scope of the service account.
1. Confirm if the service account token being created is authorized.
1. Determine the resources involved, such as new containers.
1. Initiate the incident response process.
1. Remediate compromised resources and repair the root cause.

*Requires Agent version 7.27 or greater*
