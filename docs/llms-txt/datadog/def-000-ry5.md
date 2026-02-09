# Source: https://docs.datadoghq.com/security/default_rules/def-000-ry5.md

---
title: Ensure /dev/shm is configured
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Ensure /dev/shm is configured
---

# Ensure /dev/shm is configured
 
## Description{% #description %}

The `/dev/shm` is a traditional shared memory concept. One program will create a memory portion, which other processes (if permitted) can access. If `/dev/shm` is not configured, tmpfs will be mounted to /dev/shm by systemd.

## Rationale{% #rationale %}

Any user can upload and execute files inside the `/dev/shm` similar to the `/tmp` partition. Configuring `/dev/shm` allows an administrator to set the noexec option on the mount, making /dev/shm useless for an attacker to install executable code. It would also prevent an attacker from establishing a hardlink to a system setuid program and wait for it to be updated. Once the program was updated, the hardlink would be broken and the attacker would have his own copy of the program. If the program happened to have a security vulnerability, the attacker could continue to exploit the known flaw.

## Warning{% #warning %}

This rule does not have a remedation. It is expected that this will be managed by systemd and will be a tmpfs partition.
