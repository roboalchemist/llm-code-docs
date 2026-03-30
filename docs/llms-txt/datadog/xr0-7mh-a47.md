# Source: https://docs.datadoghq.com/security/default_rules/xr0-7mh-a47.md

---
title: User created interactively
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > User created interactively
---

# User created interactively
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1136-create-account](https://attack.mitre.org/techniques/T1136)
## What happened{% #what-happened %}

A new user was created in an interactive session using `{{ @process.comm }}`.

## Goal{% #goal %}

Detect the creation of a new user on the system using an interactive session.

## Strategy{% #strategy %}

Attacker's may add local accounts to systems that they have compromised to maintain access to those systems. If an attacker has gained a sufficient level of access (like admin privileges) on a system, they can make a new user for themselves. In production systems, users should be created in the base image of the system (for example, the AMI or other VM image), or they should be created programmatically by configuration management tools. The creation of a new user by an interactive (human) session is suspicious.

## Triage & Response{% #triage--response %}

1. Determine whether the creation of a new user is expected behavior.
1. If this behavior is unexpected, attempt to contain the compromise (possibly by terminating the workload, depending on the stage of attack), and look for indications of the initial compromise. Follow your organization's internal processes for investigating and remediating compromised systems.
1. Determine the scope of the attack. Investigate whether or not multiple systems had this user added around the same time, and whether the systems impacted follow a pattern. For example, if a user was added to multiple systems, do they share the same workload or base image? What other activity occurred directly before or after the user was added?

*Requires Agent version 7.27 or greater*
