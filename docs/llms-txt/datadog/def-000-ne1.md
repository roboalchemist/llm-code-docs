# Source: https://docs.datadoghq.com/security/default_rules/def-000-ne1.md

---
title: Verify Ownership of Files in /var/log/gdm3
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Ownership of Files in
  /var/log/gdm3
---

# Verify Ownership of Files in /var/log/gdm3
 
## Description{% #description %}

To properly set the owner of `/var/log/gdm3/*`, run the command:

```gdscript3
$ sudo chown root /var/log/gdm3/* 
```

## Rationale{% #rationale %}

The `/var/log/gdm3` directory contains information about the GDM daemon and should only be accessed by authorized personnel.

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

find  /var/log/gdm3/  -type f  ! -user 0 -regextype posix-extended -regex '.*' -exec chown -L $newown {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_ownerships_var_log_gdm3_newown variable if represented by uid
  set_fact:
    file_ownerships_var_log_gdm3_newown: '0'
  tags:
  - configure_strategy
  - file_ownerships_var_log_gdm3
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /var/log/gdm3/ file(s) matching .* recursively
  command: find  /var/log/gdm3/  -type f  ! -user 0 -regextype posix-extended -regex
    ".*"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_ownerships_var_log_gdm3
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /var/log/gdm3/ file(s) matching .*
  file:
    path: '{{ item }}'
    owner: '{{ file_ownerships_var_log_gdm3_newown }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_ownerships_var_log_gdm3
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
