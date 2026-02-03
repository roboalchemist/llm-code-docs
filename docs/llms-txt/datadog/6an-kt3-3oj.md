# Source: https://docs.datadoghq.com/security/default_rules/6an-kt3-3oj.md

---
title: AppArmor profile modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > AppArmor profile modified
---

# AppArmor profile modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1562-impair-defenses](https://attack.mitre.org/techniques/T1562) 
## What happened{% #what-happened %}

The command `{{ @process.comm }}` was used to modify AppArmor profiles, potentially disabling security tools.

## Goal{% #goal %}

Detect modification of AppArmor profiles using an interactive session.

## Strategy{% #strategy %}

After an initial intrusion, attackers may attempt to disable security tools to avoid possible detection of their offensive tools and activities. [AppArmor](https://wiki.ubuntu.com/AppArmor) is a Linux Security Module (LSM) feature that confines programs to a limited set of resources. Disabling AppArmor could help an attacker run disallowed tools and gain access to resources that are otherwise blocked. This detection looks for commands that disable or modify AppArmor during interactive sessions, which is highly irregular in production environments.

## Triage & Response{% #triage--response %}

1. Determine whether or not this is expected behavior.
1. If this behavior is unexpected, attempt to contain the compromise (possibly by terminating the workload, depending on the stage of attack) and look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the nature of the attack and utilities involved. Investigate security signals (if present) occurring around the time of the event to establish an attack path.
1. Find and repair the root cause of the exploit.

*Requires Agent version 7.27 or greater*
