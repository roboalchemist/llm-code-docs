# Source: https://docs.datadoghq.com/security/default_rules/iuc-a05-y6b.md

---
title: Interactive shell spawned in container
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Interactive shell spawned in container
---

# Interactive shell spawned in container
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1609-container-administration-command](https://attack.mitre.org/techniques/T1609) 
## What happened{% #what-happened %}

The process `{{ @process.comm }}` was executed with the interactive (`-i`) flag in a container

## Goal{% #goal %}

Detect the execution of a shell with the interactive flag (`-i`) in a container.

## Strategy{% #strategy %}

After an attacker's initial intrusion into a victim container (for example, through a web shell exploit), they may attempt to escalate privileges, break out of the container, or exfiltrate secrets by running interative shell utilities inside of the container. This detection triggers when execution of one of a set of common Linux shell utilities (like `bash` or `sh`) is detected in a container with the interactive flag (`-i`). If this is unexpected behavior, it could indicate an attacker attempting to run arbitrary commands inside of your containers and potentially break out onto the host.

## Triage & Response{% #triage--response %}

1. Inspect the command line arguments of the shell process execution to determine if the shell was run with the `-i` flag.
1. If this behavior is unexpected, attempt to contain the compromise (possibly by terminating the workload, depending on the stage of attack) and look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the nature of the attack and utilities involved. Investigate security signals (if present) occurring around the time of the event to establish an attack path.
1. Find and repair the root cause of the exploit.
