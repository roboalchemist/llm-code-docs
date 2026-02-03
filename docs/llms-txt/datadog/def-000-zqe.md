# Source: https://docs.datadoghq.com/security/default_rules/def-000-zqe.md

---
title: Verify Permissions on Backup passwd File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions on Backup passwd
  File
---

# Verify Permissions on Backup passwd File
 
## Description{% #description %}

To properly set the permissions of `/etc/passwd-`, run the command:

```
$ sudo chmod 0644 /etc/passwd-
```

## Rationale{% #rationale %}

The `/etc/passwd-` file is a backup file of `/etc/passwd`, and as such, it contains information about the users that are configured on the system. Protection of this file is critical for system security.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

chmod u-xs,g-xws,o-xwt /etc/passwd-
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Test for existence /etc/passwd-
  stat:
    path: /etc/passwd-
  register: file_exists
  tags:
  - NIST-800-53-AC-6 (1)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_backup_etc_passwd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xws,o-xwt on /etc/passwd-
  file:
    path: /etc/passwd-
    mode: u-xs,g-xws,o-xwt
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - NIST-800-53-AC-6 (1)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_backup_etc_passwd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
