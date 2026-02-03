# Source: https://docs.datadoghq.com/security/default_rules/6ph-8a1-ul5.md

---
title: Container management utility in container
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Container management utility in
  container
---

# Container management utility in container
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1609-container-administration-command](https://attack.mitre.org/techniques/T1609) 
## What happened{% #what-happened %}

`{{ @process.comm }}` was executed inside a container, which could be used for enumeration or lateral movement.

## Goal{% #goal %}

Detect execution of a container management utility (for example, `kubectl` or `docker`) in a container.

## Strategy{% #strategy %}

After an attacker's initial intrusion into a victim container (for example, through a web shell exploit), they may attempt to enumerate other pods or containers, escalate privileges, or exfiltrate secrets by running container management orchestration utilities. This detection triggers when execution of one of a set of common container management utilities (like `kubectl` or `docker`) executes with specific process arguments detected in a container. If this is unexpected behavior, it could indicate an attacker attempting to compromise your pods, containers, and hosts.

## Triage and response{% #triage-and-response %}

1. Determine whether or not this is expected behavior.
1. If this behavior is unexpected, attempt to contain the compromise (this may be achieved by terminating the workload, depending on the stage of attack) and look for indications of initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the nature of the attack and utilities involved. Investigate security signals (if present) occurring around the time of the event to establish an attack path.
1. Find and repair the root cause of the exploit.

*Requires version 7.27 or higher*
