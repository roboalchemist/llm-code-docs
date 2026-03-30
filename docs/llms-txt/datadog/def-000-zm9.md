# Source: https://docs.datadoghq.com/security/default_rules/def-000-zm9.md

---
title: Container accessed using kubectl in another container
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Container accessed using kubectl in
  another container
---

# Container accessed using kubectl in another container
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1609-container-administration-command](https://attack.mitre.org/techniques/T1609)
## Goal{% #goal %}

Detect the use of `kubectl` inside a container to access another container.

## Strategy{% #strategy %}

This detection triggers when `kubectl` is executed with specific arguments related to accessing containers. These arguments include port forwarding and using `exec` to create a shell.

## Triage and response{% #triage-and-response %}

1. Identify the purpose of the container using tags, such as the image and service tags.
1. Determine the target container using the process arguments.
1. Initiate the incident response process.
1. Remediate compromised resources and repair the root cause.

## What happened{% #what-happened %}

A `kubectl` command was used to access another container, potentially for lateral movement or privilege escalation.

*Requires Agent version 7.27 or greater*
