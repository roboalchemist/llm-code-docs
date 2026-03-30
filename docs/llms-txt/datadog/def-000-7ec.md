# Source: https://docs.datadoghq.com/security/default_rules/def-000-7ec.md

---
title: Verify Grouponwership of Files in /var/log/sssd
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Grouponwership of Files in
  /var/log/sssd
---

# Verify Grouponwership of Files in /var/log/sssd

## Description{% #description %}

To properly set the group owner of `/var/log/sssd/*`, run the command:

```gdscript3
$ sudo chgrp sssd /var/log/sssd/*
```

or

```gdscript3
$ sudo chgrp root /var/log/sssd/*
```

## Rationale{% #rationale %}

The `/var/log/sssd` directory contains debug logs for the System Security Services Daemon (SSSD) and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if getent group "sssd" >/dev/null 2>&1; then
  newgroup="sssd"
elif getent group "root" >/dev/null 2>&1; then
  newgroup="root"
fi
if [[ -z ${newgroup} ]]; then
  echo "sssd and root is not a defined group on the system"
  exit 1
fi

find  /var/log/sssd/  -type f  ! -group sssd ! -group root -regextype posix-extended -regex '.*' -exec chgrp -L $newgroup {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Check that the sssd group is defined
  getent:
    database: group
    key: sssd
  ignore_errors: true
  when: file_groupownerships_var_log_sssd_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupownerships_var_log_sssd_newgroup variable if sssd found
  set_fact:
    file_groupownerships_var_log_sssd_newgroup: sssd
  when: ansible_facts.getent_group["sssd"] is defined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Check that the root group is defined
  getent:
    database: group
    key: root
  ignore_errors: true
  when: file_groupownerships_var_log_sssd_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupownerships_var_log_sssd_newgroup variable if root found
  set_fact:
    file_groupownerships_var_log_sssd_newgroup: root
  when: ansible_facts.getent_group["root"] is defined
  tags:
  - configure_strategy
  - file_groupownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /var/log/sssd/ file(s) matching .* recursively
  command: find  /var/log/sssd/  -type f  ! -group sssd ! -group root -regextype posix-extended
    -regex ".*"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_groupownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /var/log/sssd/ file(s) matching .*
  file:
    path: '{{ item }}'
    group: '{{ file_groupownerships_var_log_sssd_newgroup }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_groupownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
