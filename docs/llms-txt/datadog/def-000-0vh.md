# Source: https://docs.datadoghq.com/security/default_rules/def-000-0vh.md

---
title: Verify Permissions on /var/log/wtmp(.*) Files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions on /var/log/wtmp(.*)
  Files
---

# Verify Permissions on /var/log/wtmp(.*) Files
 
## Description{% #description %}

To properly set the permissions of `/var/log/(b|w)tmp(.*|-*)`, run the command:

```gdscript3
$ sudo chmod 0664 /var/log/(b|w)tmp(.*|-*)
```

## Rationale{% #rationale %}

The `/var/log/(b|w)tmp(.*|-*)` files contains logs of reports the most recent login of all users and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

find -L /var/log/ -maxdepth 1 -perm /u+xs,g+xs,o+xwt  -type f -regextype posix-extended -regex '.*(b|w)tmp((\.|-)[^\/]+)?$' -exec chmod u-xs,g-xs,o-xwt {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Find /var/log/ file(s)
  command: find -L /var/log/ -maxdepth 1 -perm /u+xs,g+xs,o+xwt  -type f -regextype
    posix-extended -regex ".*(b|w)tmp((\.|-)[^\/]+)?$"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_permissions_var_log_wbtmp
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set permissions for /var/log/ file(s)
  file:
    path: '{{ item }}'
    mode: u-xs,g-xs,o-xwt
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_permissions_var_log_wbtmp
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
