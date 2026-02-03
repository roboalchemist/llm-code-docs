# Source: https://docs.datadoghq.com/security/default_rules/9fi-ky3-oxl.md

---
title: Package installed in container
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Package installed in container
---

# Package installed in container
Classification:attackTactic:[TA0002-execution](https://attack.mitre.org/tactics/TA0002)Technique:[T1059-command-and-scripting-interpreter](https://attack.mitre.org/techniques/T1059) 
## What happened{% #what-happened %}

`{{ @process.comm }}` installed a package inside a container.

## Goal{% #goal %}

Detect installation of software using a package management utility (`apt` or `yum`) in a container.

## Strategy{% #strategy %}

After an attacker's initial intrusion into a victim's container (for example, through a web shell exploit), they may attempt to install tools and utilities for a variety of malicious purposes. This detection triggers when one of a set of common package management utilities installs a package in a container. Package management in containers is against best practices which highly emphasize immutability. If this is unexpected behavior, it could indicate an attacker attempting to install tools to further compromise your systems.

## Triage and response{% #triage-and-response %}

1. Determine whether or not this is expected behavior.
1. If this behavior is unexpected, attempt to contain the compromise. This may be achieved by terminating the workload, depending on the stage of attack.
1. Look for indications of initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the nature of the attack and the tools involved. Investigate security signals (if present) occurring around the time of the event to establish an attack path.
1. Find and repair the root cause of the exploit.

*Requires Agent version 7.27 or greater*
