# Source: https://docs.datadoghq.com/security/default_rules/def-000-do8.md

---
title: Verify Permissions on Backup group File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Permissions on Backup group File
---

# Verify Permissions on Backup group File

## Description{% #description %}

To properly set the permissions of `/etc/group-`, run the command:

```
$ sudo chmod 0644 /etc/group-
```

## Rationale{% #rationale %}

The `/etc/group-` file is a backup file of `/etc/group`, and as such, it contains information regarding groups that are configured on the system. Protection of this file is important for system security.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

chmod u-xs,g-xws,o-xwt /etc/group-
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Test for existence /etc/group-
  stat:
    path: /etc/group-
  register: file_exists
  tags:
  - NIST-800-53-AC-6 (1)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_backup_etc_group
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xws,o-xwt on /etc/group-
  file:
    path: /etc/group-
    mode: u-xs,g-xws,o-xwt
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - NIST-800-53-AC-6 (1)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_backup_etc_group
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
