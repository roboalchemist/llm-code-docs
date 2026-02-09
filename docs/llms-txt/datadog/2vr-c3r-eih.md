# Source: https://docs.datadoghq.com/security/default_rules/2vr-c3r-eih.md

---
title: Network scanning utility executed
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Network scanning utility executed
---

# Network scanning utility executed
Classification:attackTactic:[TA0007-discovery](https://attack.mitre.org/tactics/TA0007)Technique:[T1046-network-service-discovery](https://attack.mitre.org/techniques/T1046) 
## What happened{% #what-happened %}

The network scanning utility `{{ @process.comm }}` was executed, potentially for lateral movement.

## Goal{% #goal %}

Detect execution of the `{{ @process.comm }}` network utility.

## Strategy{% #strategy %}

`{{ @process.comm }}` is a network utility commonly used by attackers to understand a victim's network topology and vulnerabilities. After an attacker's initial intrusion into a host (for example, through a web shell exploit, container breakout), they may attempt to use `{{ @process.comm }}` to do reconnaissance. This detection triggers when an execution of `{{ @process.comm }}` is detected on a system. If this is unexpected behavior, it could indicate an attacker attempting to compromise your systems.

## Triage and response{% #triage-and-response %}

1. Determine which user executed `{{ @process.comm }}` and whether this is allowed or expected behavior.
1. If this behavior is unexpected, attempt to contain the compromise (this may be achieved by terminating the workload, depending on the stage of attack) and look for indications of initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the nature of the attack and network tools involved. Investigate the security signals (if present) occurring around the time of the event to establish an attack path.
1. Find and repair the root cause of the exploit.

*Requires Agent version 7.27 or greater*
