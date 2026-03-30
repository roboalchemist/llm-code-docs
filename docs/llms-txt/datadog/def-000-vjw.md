# Source: https://docs.datadoghq.com/security/default_rules/def-000-vjw.md

---
title: Verify Permissions of Files in /var/log/gdm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions of Files in
  /var/log/gdm
---

# Verify Permissions of Files in /var/log/gdm

## Description{% #description %}

To properly set the permissions of `/var/log/gdm/*`, run the command:

```gdscript3
$ sudo chmod 0660 /var/log/gdm/*
```

## Rationale{% #rationale %}

The `/var/log/gdm` directory contains information about the GDM daemon and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

find  /var/log/gdm/  -perm /u+xs,g+xs,o+xwrt  -type f -regextype posix-extended -regex '.*' -exec chmod u-xs,g-xs,o-xwrt {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Find /var/log/gdm/ file(s) recursively
  command: find  /var/log/gdm/  -perm /u+xs,g+xs,o+xwrt  -type f -regextype posix-extended
    -regex ".*"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_permissions_var_log_gdm
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set permissions for /var/log/gdm/ file(s)
  file:
    path: '{{ item }}'
    mode: u-xs,g-xs,o-xwrt
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_permissions_var_log_gdm
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
