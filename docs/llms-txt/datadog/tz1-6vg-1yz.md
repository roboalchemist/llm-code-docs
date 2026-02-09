# Source: https://docs.datadoghq.com/security/default_rules/tz1-6vg-1yz.md

---
title: System authentication files modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > System authentication files modified
---

# System authentication files modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## What happened{% #what-happened %}

The PAM configuration file `{{ @file.path }}` was modified by the process `{{ @process.comm }}`, potentially to manipulate authentication procedures.

## Goal{% #goal %}

Detect modifications to `pam.d` directory.

## Strategy{% #strategy %}

Linux Pluggable Authentication Modules (PAM) provide authentication for applications and services. Authentication modules in the PAM system are setup and configured under the `/etc/pam.d/` directory. An attacker may attempt to modify or add an authentication module in PAM in order to bypass the authentication process, or reveal system credentials.

## Triage and response{% #triage-and-response %}

1. Identify if the changes to the path `{{@file.path}}` were part of known system setup or mainenance.
1. If these changes were unauthorized, roll back the host in question to a known good PAM configuration, or replace the system with a known-good system image.

*Required Agent version 7.27 or higher*
