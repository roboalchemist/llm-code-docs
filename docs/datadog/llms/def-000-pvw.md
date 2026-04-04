# Source: https://docs.datadoghq.com/security/default_rules/def-000-pvw.md

---
title: Verify User Who Owns /var/log/(b|w)tmp(.*|-*) File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify User Who Owns
  /var/log/(b|w)tmp(.*|-*) File
---

# Verify User Who Owns /var/log/(b|w)tmp(.*|-*) File

## Description{% #description %}

To properly set the owner of `/var/log/(b|w)tmp(.*|-*)`, run the command:

```gdscript3
$ sudo chown root /var/log/(b|w)tmp(.*|-*)
```

## Rationale{% #rationale %}

The `/var/log/(b|w)tmp(.*|-*)` file contains logs of reports the most recent login of all users and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if id "0" >/dev/null 2>&1; then
  newown="0"
fi
if [[ -z ${newown} ]]; then
  echo "0 is not a defined user on the system"
  exit 1
fi

find -L /var/log/ -maxdepth 1 -type f  ! -user 0 -regextype posix-extended -regex '.*(b|w)tmp((\.|-)[^\/]+)?$' -exec chown -L $newown {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_owner_var_log_wbtmp_newown variable if represented by uid
  set_fact:
    file_owner_var_log_wbtmp_newown: '0'
  tags:
  - configure_strategy
  - file_owner_var_log_wbtmp
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /var/log/ file(s) matching .*(b|w)tmp((\.|-)[^\/]+)?$
  command: find -L /var/log/ -maxdepth 1 -type f  ! -user 0 -regextype posix-extended
    -regex ".*(b|w)tmp((\.|-)[^\/]+)?$"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_owner_var_log_wbtmp
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /var/log/ file(s) matching .*(b|w)tmp((\.|-)[^\/]+)?$
  file:
    path: '{{ item }}'
    owner: '{{ file_owner_var_log_wbtmp_newown }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_owner_var_log_wbtmp
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
