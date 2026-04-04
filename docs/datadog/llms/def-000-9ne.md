# Source: https://docs.datadoghq.com/security/default_rules/def-000-9ne.md

---
title: Verify Groupownership of Files in /var/log/apt
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Groupownership of Files in
  /var/log/apt
---

# Verify Groupownership of Files in /var/log/apt

## Description{% #description %}

To properly set the group owner of `/var/log/apt/*`, run the command:

```gdscript3
$ sudo chgrp adm /var/log/apt/*
```

or

```gdscript3
$ sudo chgrp root /var/log/apt/*
```

## Rationale{% #rationale %}

The `/var/log/apt` directory contains information about APT and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if getent group "adm" >/dev/null 2>&1; then
  newgroup="adm"
elif getent group "root" >/dev/null 2>&1; then
  newgroup="root"
fi
if [[ -z ${newgroup} ]]; then
  echo "adm and root is not a defined group on the system"
  exit 1
fi

find -L /var/log/apt/ -maxdepth 1 -type f  ! -group adm ! -group root -regextype posix-extended -regex '.*' -exec chgrp -L $newgroup {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Check that the adm group is defined
  getent:
    database: group
    key: adm
  ignore_errors: true
  when: file_groupownerships_var_log_apt_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_apt
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupownerships_var_log_apt_newgroup variable if adm found
  set_fact:
    file_groupownerships_var_log_apt_newgroup: adm
  when: ansible_facts.getent_group["adm"] is defined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_apt
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Check that the root group is defined
  getent:
    database: group
    key: root
  ignore_errors: true
  when: file_groupownerships_var_log_apt_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_apt
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupownerships_var_log_apt_newgroup variable if root found
  set_fact:
    file_groupownerships_var_log_apt_newgroup: root
  when: ansible_facts.getent_group["root"] is defined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_apt
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /var/log/apt/ file(s) matching .*
  command: find -L /var/log/apt/ -maxdepth 1 -type f  ! -group adm ! -group root -regextype
    posix-extended -regex ".*"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_groupownerships_var_log_apt
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /var/log/apt/ file(s) matching .*
  file:
    path: '{{ item }}'
    group: '{{ file_groupownerships_var_log_apt_newgroup }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_groupownerships_var_log_apt
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
