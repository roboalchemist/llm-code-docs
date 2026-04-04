# Source: https://docs.datadoghq.com/security/default_rules/def-000-dtq.md

---
title: Verify Groupownership of Files in /var/log/gdm
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Groupownership of Files in
  /var/log/gdm
---

# Verify Groupownership of Files in /var/log/gdm

## Description{% #description %}

To properly set the group owner of `/var/log/gdm/*`, run the command:

```gdscript3
$ sudo chgrp gdm /var/log/gdm/*
```

or

```gdscript3
$ sudo chgrp root /var/log/gdm/*
```

## Rationale{% #rationale %}

The `/var/log/gdm` directory contains information about the GDM daemon and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if getent group "gdm" >/dev/null 2>&1; then
  newgroup="gdm"
elif getent group "root" >/dev/null 2>&1; then
  newgroup="root"
fi
if [[ -z ${newgroup} ]]; then
  echo "gdm and root is not a defined group on the system"
  exit 1
fi

find  /var/log/gdm/  -type f  ! -group gdm ! -group root -regextype posix-extended -regex '.*' -exec chgrp -L $newgroup {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Check that the gdm group is defined
  getent:
    database: group
    key: gdm
  ignore_errors: true
  when: file_groupownerships_var_log_gdm_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_gdm
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupownerships_var_log_gdm_newgroup variable if gdm found
  set_fact:
    file_groupownerships_var_log_gdm_newgroup: gdm
  when: ansible_facts.getent_group["gdm"] is defined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_gdm
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Check that the root group is defined
  getent:
    database: group
    key: root
  ignore_errors: true
  when: file_groupownerships_var_log_gdm_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_gdm
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupownerships_var_log_gdm_newgroup variable if root found
  set_fact:
    file_groupownerships_var_log_gdm_newgroup: root
  when: ansible_facts.getent_group["root"] is defined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_gdm
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /var/log/gdm/ file(s) matching .* recursively
  command: find  /var/log/gdm/  -type f  ! -group gdm ! -group root -regextype posix-extended
    -regex ".*"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_groupownerships_var_log_gdm
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /var/log/gdm/ file(s) matching .*
  file:
    path: '{{ item }}'
    group: '{{ file_groupownerships_var_log_gdm_newgroup }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_groupownerships_var_log_gdm
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
