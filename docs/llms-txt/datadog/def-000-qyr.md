# Source: https://docs.datadoghq.com/security/default_rules/def-000-qyr.md

---
title: Verify Group Who Owns /var/log/auth.log File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Who Owns /var/log/auth.log
  File
---

# Verify Group Who Owns /var/log/auth.log File

## Description{% #description %}

To properly set the group owner of `/var/log/auth.log`, run the command:

```gdscript3
$ sudo chgrp adm /var/log/auth.log
```

or

```gdscript3
$ sudo chgrp root /var/log/auth.log
```

## Rationale{% #rationale %}

The `/var/log/auth.log` file contains records information about user login attempts and authentication processes and should only be accessed by authorized personnel.

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
chgrp $newgroup /var/log/auth.log
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Check that the adm group is defined
  getent:
    database: group
    key: adm
  ignore_errors: true
  when: file_groupowner_var_log_auth_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupowner_var_log_auth
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_var_log_auth_newgroup variable if adm found
  set_fact:
    file_groupowner_var_log_auth_newgroup: adm
  when: ansible_facts.getent_group["adm"] is defined
  tags:
  - configure_strategy
  - file_groupowner_var_log_auth
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Check that the root group is defined
  getent:
    database: group
    key: root
  ignore_errors: true
  when: file_groupowner_var_log_auth_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupowner_var_log_auth
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_var_log_auth_newgroup variable if root found
  set_fact:
    file_groupowner_var_log_auth_newgroup: root
  when: ansible_facts.getent_group["root"] is defined
  tags:
  - configure_strategy
  - file_groupowner_var_log_auth
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /var/log/auth.log
  stat:
    path: /var/log/auth.log
  register: file_exists
  tags:
  - configure_strategy
  - file_groupowner_var_log_auth
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /var/log/auth.log
  file:
    path: /var/log/auth.log
    group: '{{ file_groupowner_var_log_auth_newgroup }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - configure_strategy
  - file_groupowner_var_log_auth
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
