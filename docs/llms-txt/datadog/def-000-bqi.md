# Source: https://docs.datadoghq.com/security/default_rules/def-000-bqi.md

---
title: Verify permissions on Message of the Day Banner
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify permissions on Message of the
  Day Banner
---

# Verify permissions on Message of the Day Banner

## Description{% #description %}

To properly set the permissions of `/etc/motd`, run the command:

```
$ sudo chmod 0644 /etc/motd
```

## Rationale{% #rationale %}

Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.

Proper permissions will ensure that only root user can modify the banner.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

chmod u-xs,g-xws,o-xwt /etc/motd
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Test for existence /etc/motd
  stat:
    path: /etc/motd
  register: file_exists
  tags:
  - configure_strategy
  - file_permissions_etc_motd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xws,o-xwt on /etc/motd
  file:
    path: /etc/motd
    mode: u-xs,g-xws,o-xwt
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - configure_strategy
  - file_permissions_etc_motd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
