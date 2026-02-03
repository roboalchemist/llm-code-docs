# Source: https://docs.datadoghq.com/security/default_rules/mnc-w4f-4pf.md

---
title: Unfamiliar kernel module loaded
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Unfamiliar kernel module loaded
---

# Unfamiliar kernel module loaded
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1547-boot-or-logon-autostart-execution](https://attack.mitre.org/techniques/T1547) 
## What happened{% #what-happened %}

A previously unseen kernel module, `{{ @module.name }}`, was loaded.

## Goal{% #goal %}

Attackers can leverage malicious kernel modules to gain persistence on a system, ensuring their malicious code is executed even after a system reboot. Kernel modules can also help attackers gain elevated permissions and cover their tracks through the use of a rootkit.

Loading a malicious kernel module can be a type of rootkit. Rootkits often create backdoor access and hide evidence of themselves. This includes process, file, and network activity.

## Strategy{% #strategy %}

Kernel modules are loaded from the `/lib/modules` directory in Linux by default, however attackers may attempt to load kernel modules from other locations as well. This detection detects all kernel module loads.

This rule uses the New Value detection method. Datadog will learn the historical behavior of a specified field in Agent logs and then create a signal when unfamiliar values appear.

## Triage and response{% #triage-and-response %}

1. Check the name of the new kernel module created.
1. Check the name of the process loading the kernel module.
1. If the new kernel module is not expected, contain the host or container and roll back to a known good configuration. Initiate the incident response process.
