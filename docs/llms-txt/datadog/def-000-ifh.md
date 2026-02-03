# Source: https://docs.datadoghq.com/security/default_rules/def-000-ifh.md

---
title: Resource provisioned using kubectl in container
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Resource provisioned using kubectl in
  container
---

# Resource provisioned using kubectl in container
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1610-deploy-container](https://attack.mitre.org/techniques/T1610) 
## What happened{% #what-happened %}

A `kubectl` command was used to provision new resources, potentially to establish persistence or create unauthorized workloads.

## Goal{% #goal %}

Detect the use of `kubectl` commands inside a container to provision new resources.

## Strategy{% #strategy %}

This detection triggers when `kubectl` is executed with specific arguments related to provisioning resources, such as creating a namespace and running a pod.

## Triage and response{% #triage-and-response %}

1. Identify the purpose of the container using tags, such as the image and service tags.
1. Determine the resources involved, such as new containers.
1. Initiate the incident response process.
1. Remediate compromised resources and repair the root cause.

*Requires Agent version 7.27 or greater*
