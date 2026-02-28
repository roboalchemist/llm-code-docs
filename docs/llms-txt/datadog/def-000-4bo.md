# Source: https://docs.datadoghq.com/security/default_rules/def-000-4bo.md

---
title: Verify Ownership of Files in /var/log/sssd
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Ownership of Files in
  /var/log/sssd
---

# Verify Ownership of Files in /var/log/sssd

## Description{% #description %}

To properly set the owner of `/var/log/sssd/*`, run the command:

```gdscript3
$ sudo chown sssd /var/log/sssd/*
```

or

```gdscript3
$ sudo chown root /var/log/sssd/*
```

## Rationale{% #rationale %}

The `/var/log/sssd` directory contains debug logs for the System Security Services Daemon (SSSD) and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if id "sssd" >/dev/null 2>&1; then
  newown="sssd"
elif id "root" >/dev/null 2>&1; then
  newown="root"
fi
if [[ -z ${newown} ]]; then
  echo "sssd and root is not a defined user on the system"
  exit 1
fi

find  /var/log/sssd/  -type f  ! -user sssd ! -user root -regextype posix-extended -regex '.*' -exec chown -L $newown {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Check that the sssd user is defined
  getent:
    database: passwd
    key: sssd
  ignore_errors: true
  tags:
  - configure_strategy
  - file_ownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_ownerships_var_log_sssd_newown variable if sssd found
  set_fact:
    file_ownerships_var_log_sssd_newown: sssd
  when: ansible_facts.getent_passwd["sssd"] is defined
  tags:
  - configure_strategy
  - file_ownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Check that the root user is defined
  getent:
    database: passwd
    key: root
  ignore_errors: true
  when: file_ownerships_var_log_sssd_newown is undefined
  tags:
  - configure_strategy
  - file_ownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_ownerships_var_log_sssd_newown variable if root found
  set_fact:
    file_ownerships_var_log_sssd_newown: root
  when: ansible_facts.getent_passwd["root"] is defined
  tags:
  - configure_strategy
  - file_ownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /var/log/sssd/ file(s) matching .* recursively
  command: find  /var/log/sssd/  -type f  ! -user sssd ! -user root -regextype posix-extended
    -regex ".*"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_ownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /var/log/sssd/ file(s) matching .*
  file:
    path: '{{ item }}'
    owner: '{{ file_ownerships_var_log_sssd_newown }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_ownerships_var_log_sssd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
