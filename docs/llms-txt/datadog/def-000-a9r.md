# Source: https://docs.datadoghq.com/security/default_rules/def-000-a9r.md

---
title: Verify Permissions on Backup shadow File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions on Backup shadow
  File
---

# Verify Permissions on Backup shadow File
 
## Description{% #description %}

To properly set the permissions of `/etc/shadow-`, run the command:

```
$ sudo chmod 0640 /etc/shadow-
```

## Rationale{% #rationale %}

The `/etc/shadow-` file is a backup file of `/etc/shadow`, and as such, it contains the list of local system accounts and password hashes. Protection of this file is critical for system security.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

chmod u-xs,g-xws,o-xwrt /etc/shadow-
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Test for existence /etc/shadow-
  stat:
    path: /etc/shadow-
  register: file_exists
  tags:
  - NIST-800-53-AC-6 (1)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_backup_etc_shadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xws,o-xwrt on /etc/shadow-
  file:
    path: /etc/shadow-
    mode: u-xs,g-xws,o-xwrt
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - NIST-800-53-AC-6 (1)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_backup_etc_shadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
