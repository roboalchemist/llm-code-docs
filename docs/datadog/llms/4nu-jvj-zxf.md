# Source: https://docs.datadoghq.com/security/default_rules/4nu-jvj-zxf.md

---
title: Kernel module directory modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Kernel module directory modified
---

# Kernel module directory modified
Classification:attackTactic:[TA0003-persistence](https://attack.mitre.org/tactics/TA0003)Technique:[T1547-boot-or-logon-autostart-execution](https://attack.mitre.org/techniques/T1547)
## What happened{% #what-happened %}

The process `{{ @process.comm }}` modified the kernel module file `{{ @file.path }}`, potentially to establish persistence or gain elevated privileges.

## Goal{% #goal %}

Kernel modules can be used to automatically execute code when a host starts up. Attackers sometimes use kernel modules to gain persistence on a particular host, ensuring that their code is executed even after a system reboot. Kernel modules can also help attackers gain elevated permissions on a system.

Loading a malicious kernel module is a type of rootkit. Rootkits often create backdoor access and hide evidence of themselves. This includes process, file, and network activity.

## Strategy{% #strategy %}

Kernel modules are loaded from the `/lib/modules` directory in Linux. This detection watches for all new files created under that directory.

## Triage and response{% #triage-and-response %}

1. Check the name of the new kernel module created.
1. Check which user or process created the module.
1. If the new kernel module is not expected, contain the host or container and roll back to a known good configuration. Initiate the incident response process.

*Requires Agent version 7.27 or greater*
