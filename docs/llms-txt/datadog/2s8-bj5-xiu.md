# Source: https://docs.datadoghq.com/security/default_rules/2s8-bj5-xiu.md

---
title: Network utility executed in container
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Network utility executed in container
---

# Network utility executed in container
Classification:attackTactic:[TA0011-command-and-control](https://attack.mitre.org/tactics/TA0011)Technique:[T1105-ingress-tool-transfer](https://attack.mitre.org/techniques/T1105)
## What happened{% #what-happened %}

The process `{{ @process.comm }}` was executed, potentially to download additional tools.

## Goal{% #goal %}

Detect execution of a network utility executed from a suspicious location in a container.

## Strategy{% #strategy %}

After an attacker's initial intrusion into a victim container (for example, through a web shell exploit), they may attempt to use network utilities for a variety of malicious purposes (for example, reconnaissance or data exfiltration). This detection triggers when execution of one of a set of network utilities (for example, `nslookup`, `netcat`) is detected in a container. Different utilities may serve different purposes in an attack; for example, DNS tools like `nslookup` could be involved in a DNS data exfiltration attack, and `netcat` could indicate a backdoor and data exfiltration. If this is unexpected behavior, it could indicate an attacker attempting to compromise your containers and host.

These utilities executed by a file located in `/tmp` or another writeable directory could indicate a malicious script attempting to perform actions on the host. These actions may include downloading additional tools or exfiltrating data.

## Triage and response{% #triage-and-response %}

1. Determine whether or not this is expected behavior.
1. Review the ancestors for unexpected processes or files executed.
1. If this behavior is unexpected, attempt to contain the compromise (this may be achieved by terminating the workload, depending on the stage of attack) and look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the nature of the attack and network tools involved. Investigate security signals (if present) occurring around the time of the event to establish an attack path and signals from other tools. For example, if a DNS exfiltration attack is suspected, examine DNS traffic and servers if available.
1. Find and repair the root cause of the exploit.

*Requires Agent version 7.34 or greater*
