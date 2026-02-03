# Source: https://docs.datadoghq.com/security/default_rules/def-000-na8.md

---
title: Verify User Who Owns /var/log/cloud-init.log File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify User Who Owns
  /var/log/cloud-init.log File
---

# Verify User Who Owns /var/log/cloud-init.log File
 
## Description{% #description %}

To properly set the owner of `/var/log/cloud-init.log`, run the command:

```gdscript3
$ sudo chown syslog /var/log/cloud-init.log 
```

or

```gdscript3
$ sudo chown root /var/log/cloud-init.log 
```

## Rationale{% #rationale %}

The `/var/log/cloud-init.log` file contains detailed debugging information that helps users troubleshoot cloud-init and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if id "syslog" >/dev/null 2>&1; then
  newown="syslog"
elif id "root" >/dev/null 2>&1; then
  newown="root"
fi
if [[ -z ${newown} ]]; then
  echo "syslog and root is not a defined user on the system"
  exit 1
fi

find -L /var/log/ -maxdepth 1 -type f  ! -user syslog ! -user root -regextype posix-extended -regex '.*cloud-init\.log.*' -exec chown -L $newown {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Check that the syslog user is defined
  getent:
    database: passwd
    key: syslog
  ignore_errors: true
  tags:
  - configure_strategy
  - file_owner_var_log_cloud_init
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_owner_var_log_cloud_init_newown variable if syslog found
  set_fact:
    file_owner_var_log_cloud_init_newown: syslog
  when: ansible_facts.getent_passwd["syslog"] is defined
  tags:
  - configure_strategy
  - file_owner_var_log_cloud_init
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Check that the root user is defined
  getent:
    database: passwd
    key: root
  ignore_errors: true
  when: file_owner_var_log_cloud_init_newown is undefined
  tags:
  - configure_strategy
  - file_owner_var_log_cloud_init
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_owner_var_log_cloud_init_newown variable if root found
  set_fact:
    file_owner_var_log_cloud_init_newown: root
  when: ansible_facts.getent_passwd["root"] is defined
  tags:
  - configure_strategy
  - file_owner_var_log_cloud_init
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /var/log/ file(s) matching .*cloud-init\.log.*
  command: find -L /var/log/ -maxdepth 1 -type f  ! -user syslog ! -user root -regextype
    posix-extended -regex ".*cloud-init\.log.*"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_owner_var_log_cloud_init
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /var/log/ file(s) matching .*cloud-init\.log.*
  file:
    path: '{{ item }}'
    owner: '{{ file_owner_var_log_cloud_init_newown }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_owner_var_log_cloud_init
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
