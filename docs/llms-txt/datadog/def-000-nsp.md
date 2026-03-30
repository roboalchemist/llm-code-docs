# Source: https://docs.datadoghq.com/security/default_rules/def-000-nsp.md

---
title: Ensure users' .netrc Files are not group or world accessible
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure users' .netrc Files are not
  group or world accessible
---

# Ensure users' .netrc Files are not group or world accessible

## Description{% #description %}

While the system administrator can establish secure permissions for users' .netrc files, the users can easily override these. This rule ensures every .netrc file or directory under the home directory related to an interactive user is not group or world accessible

## Rationale{% #rationale %}

.netrc files may contain unencrypted passwords that may be used to attack other systems. Note: While the complete removal of .netrc files is recommended, if any are required on the system, secure permissions must be applied.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

for user in $(awk -F':' '{ if ($3 >= 1000 && $3 != 65534) print $1 }' /etc/passwd); do
    home_dir=$(getent passwd "$user" | cut -d: -f6)
    find "${home_dir}/.netrc" -exec chmod 0600 {} \;
done
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Get all local users from /etc/passwd
  ansible.builtin.getent:
    database: passwd
    split: ':'
  tags:
  - CCE-89524-3
  - accounts_users_netrc_file_permissions
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Create local_users variable from the getent output
  ansible.builtin.set_fact:
    local_users: '{{ ansible_facts.getent_passwd|dict2items }}'
  tags:
  - CCE-89524-3
  - accounts_users_netrc_file_permissions
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Test for existence of .netrc file in home directories to avoid creating them,
    but only fixing permissions
  ansible.builtin.stat:
    path: '{{ item.value[4] }}/.netrc'
  register: path_exists
  loop: '{{ local_users }}'
  when:
  - item.value[1]|int >= 1000
  - item.value[1]|int != 65534
  tags:
  - CCE-89524-3
  - accounts_users_netrc_file_permissions
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure group and world cannot access respective .netrc files
  ansible.builtin.file:
    path: '{{ item.item.value[4] }}/.netrc'
    mode: '0600'
    state: file
  loop: '{{ path_exists.results }}'
  when: item.stat is defined and item.stat.exists
  tags:
  - CCE-89524-3
  - accounts_users_netrc_file_permissions
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
