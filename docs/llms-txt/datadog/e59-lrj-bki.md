# Source: https://docs.datadoghq.com/security/default_rules/e59-lrj-bki.md

---
title: SSH authorized keys modified
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > SSH authorized keys modified
---

# SSH authorized keys modified
Classification:attackTactic:[TA0005-defense-evasion](https://attack.mitre.org/tactics/TA0005)Technique:[T1098-account-manipulation](https://attack.mitre.org/techniques/T1098)
## What happened{% #what-happened %}

The SSH authorized keys file `{{ @file.path }}` was modified by `{{ @process.comm }}`, potentially to establish persistence.

## Goal{% #goal %}

Detect modifications to authorized SSH keys.

## Strategy{% #strategy %}

SSH is a commonly used key-based authentication mechanism. In this system, the authorized_keys file specifies SSH keys that can be used to authenticate as a specific user on the system. Attacker's may modify the authorized_keys file to authorize attacker-owned SSH keys. This allows the attacker to maintain persistence on a system as a specific user.

## Triage and response{% #triage-and-response %}

1. Check what changes were made to authorized_keys, and under which user.
1. Determine whether any keys were added. If so, determine if the added keys belong to known trusted users.
1. If they keys in question are not acceptable, roll back the host or container in question to a known trusted SSH configuration.

*Requires Agent version 7.27 or greater*
