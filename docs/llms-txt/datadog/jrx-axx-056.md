# Source: https://docs.datadoghq.com/security/default_rules/jrx-axx-056.md

---
title: Unfamiliar kernel module loaded from memory
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Unfamiliar kernel module loaded from
  memory
---

# Unfamiliar kernel module loaded from memory
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1547-boot-or-logon-autostart-execution](https://attack.mitre.org/techniques/T1547) 
## What happened{% #what-happened %}

The kernel module `{{ @module.name }}` was loaded from memory, which may be installation of a rootkit.

## Goal{% #goal %}

Kernel modules can be used to automatically execute code when a host starts up. Attackers sometimes use kernel modules to gain persistence on a particular host, ensuring that their code is executed even after a system reboot. Kernel modules can also help attackers gain elevated permissions on a system.

Loading a malicious kernel module is a type of rootkit. Rootkits often create backdoor access and hide evidence of themselves. This includes process, file, and network activity.

## Strategy{% #strategy %}

Kernel modules are loaded from the `/lib/modules` directory in Linux by default. In an attempt to thwart forensics, attackers sometimes attempt to load malicious kernel modules from memory so as not to leave artifacts on disk. This detection watches for all new kernel modules being loaded directly from memory.

## Triage and response{% #triage-and-response %}

1. Check the name of the new kernel module created.
1. If the new kernel module is not expected, contain the host or container and roll back to a known good configuration. Initiate the incident response process.

*Requires Agent version 7.35 or greater*
