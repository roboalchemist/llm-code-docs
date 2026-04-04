# Source: https://docs.datadoghq.com/security/default_rules/cz4-vmk-ju2.md

---
title: Systemd service modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Systemd service modified
---

# Systemd service modified
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1569-system-services](https://attack.mitre.org/techniques/T1569)
## What happened{% #what-happened %}

The systemd file `{{ @file.path }}` was modified by `{{ @process.comm }}`, potentially to establish persistence.

## Goal{% #goal %}

Detect modifications to system services.

## Strategy{% #strategy %}

Especially in production, systems should be generated based on standard images such as AMIs for Amazon EC2, VM images in Azure, or GCP images. Systemd is the default service manager in many Linux distributions. It manages the lifecycle of background processes and services, and can be used by an attacker to establish persistence in the system. Attackers can do this by injecting code into existing systemd services, or by creating new ones. Systemd services can be started on system boot, and therefore attacker code can persist through system reboots.

## Triage and response{% #triage-and-response %}

1. Check to see what service was modified of created.
1. Identify whether it is a known service, being modified by a known user and/or process.
1. If these changes are not acceptable, roll back the host in question to an acceptable configuration.

*Requires Agent version 7.27 or greater*
