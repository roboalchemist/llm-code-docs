# Source: https://docs.datadoghq.com/security/default_rules/def-000-jgj.md

---
title: Container breakout attempt using container management socket
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Container breakout attempt using
  container management socket
---

# Container breakout attempt using container management socket
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1613-container-and-resource-discovery](https://attack.mitre.org/techniques/T1613)
## What happened{% #what-happened %}

The process `{{ @process.comm }}` was used to access a container management socket from inside a container, potentially to deploy a new container and escape isolation.

## Goal{% #goal %}

Detect container breakouts that are abusing access to a container management socket, such as `docker.sock`, exposed inside a container. Actors will have access to the socket to deploy misconfigured containers that can be used to break out to the host. Container breakouts remove some or all isolation from a container, enabling an attacker to access the underlying host.

## Strategy{% #strategy %}

Monitor process activity inside containers for executions of `curl` targeting a local socket associated with container management tools such as Docker. A signal is only generated when the request is utilizing the create API action to deploy a new container.

## Triage and response{% #triage-and-response %}

1. Inspect the process arguments to understand the purpose of the command. Adversaries may abuse this access to run privileged containers.
1. If the activity is unexpected, isolate the host to prevent further compromise.
1. Review related signals and management API logs to establish a timeline.
1. Find and repair the root cause.

*Requires Agent version 7.28 or later.*
