# Source: https://docs.datadoghq.com/security/default_rules/pzv-32s-1sa.md

---
title: Name Service Switch configuration modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Name Service Switch configuration
  modified
---

# Name Service Switch configuration modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1556-modify-authentication-process](https://attack.mitre.org/techniques/T1556) 
## What happened{% #what-happened %}

The process `{{ @process.comm }}` modified the nsswitch configuration file `{{ @file.path }}`, potentially to manipulate authentication or inject malicious name service information.

## Goal{% #goal %}

Detect modifications to nsswitch.conf.

## Strategy{% #strategy %}

The Name Service Switch (nsswitch) configuration file is used to point system services and other applications to the sources of name-service information. This name-service information includes where the password file is stored, publickey information, and more. An attacker may attempt to modify nsswitch.conf in order to inject attacker-owned information into the authentication process. For instance, the attacker could point to a malicious password file and then login to privileged user accounts.

## Triage and response{% #triage-and-response %}

1. Check to see what changes were made to nsswitch.conf.
1. Check if critical name-service sources were changed, and whether the changes were a part of known system-setup or maintenance.
1. If these changes are unauthorized, roll back the host in question to a known good nsswitch.conf, or replace the system with a known-good system image.

*Requires Agent version 7.27 or greater*
