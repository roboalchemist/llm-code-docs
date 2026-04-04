# Source: https://docs.datadoghq.com/security/default_rules/p1b-13u-xtn.md

---
title: Runc binary modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Runc binary modified
---

# Runc binary modified
Classification:attackTactic:[TA0004-privilege-escalation](https://attack.mitre.org/tactics/TA0004)Technique:[T1611-escape-to-host](https://attack.mitre.org/techniques/T1611)
## What happened{% #what-happened %}

The `runc` binary `{{ @file.path }}` was modified by `{{ @process.comm }}`, which could be an attempt to exploit the container escape vulnerability `CVE-2019-5736`.

## Goal{% #goal %}

Detect modifications to the `runc` binary outside of the normal package management lifecycle.

## Strategy{% #strategy %}

[CVE-2019-5736](https://nvd.nist.gov/vuln/detail/CVE-2019-5736), a vulnerability in `runc` through version 1.0-rc6 could allow attackers to overwrite the host `runc` binary, which allows the attacker to effectively escape a running container, and gain root access on the underlying host. Any modifications to `runc` (outside of standard package management upgrades) could be exploiting this vulnerability to gain root access to the system.

## Triage & Response{% #triage--response %}

1. Check to see which user or process changed the `runc` binary.
1. If these changes are not acceptable, roll back contain the host in question to an acceptable configuration.
1. Update `runc` to a version above 1.0-rc6 (or Docker 18.09.2 and above).
1. Determine the nature of the attack and utilities involved. Investigate security signals (if present) occurring around the time of the event to establish an attack path.

*Requires Agent version 7.27 or greater*
