# Source: https://docs.datadoghq.com/security/default_rules/def-000-dyw.md

---
title: All Interactive User Home Directories Must Be Owned By The Primary User
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > All Interactive User Home Directories
  Must Be Owned By The Primary User
---

# All Interactive User Home Directories Must Be Owned By The Primary User
 
## Description{% #description %}

Change the owner of interactive users home directories to that correct owner. To change the owner of a interactive users home directory, use the following command:

```
$ sudo chown USER /home/USER
        
```

This rule ensures every home directory related to an interactive user is owned by an interactive user. It also ensures that interactive users are owners of one and only one home directory.

## Rationale{% #rationale %}

If a local interactive user does not own their home directory, unauthorized users could access or modify the user's files, and the users may not be able to access their own files.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

awk -F':' '{ if ($3 >= 1000 && $3 != 65534) system("chown -f " $3" "$6) }' /etc/passwd
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Get all local users from /etc/passwd
  ansible.builtin.getent:
    database: passwd
    split: ':'
  tags:
  - file_ownership_home_directories
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Create local_users variable from the getent output
  ansible.builtin.set_fact:
    local_users: '{{ ansible_facts.getent_passwd|dict2items }}'
  tags:
  - file_ownership_home_directories
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Test for existence of home directories to avoid creating them, but only fixing
    ownership
  ansible.builtin.stat:
    path: '{{ item.value[4] }}'
  register: path_exists
  loop: '{{ local_users }}'
  when:
  - item.value[1]|int >= 1000
  - item.value[1]|int != 65534
  tags:
  - file_ownership_home_directories
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure interactive local users are the owners of their respective home directories
  ansible.builtin.file:
    path: '{{ item.0.value[4] }}'
    owner: '{{ item.0.value[1] }}'
  loop: '{{ local_users|zip(path_exists.results)|list }}'
  when: item.1.stat is defined and item.1.stat.exists
  tags:
  - file_ownership_home_directories
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```

## Warning{% #warning %}

Due to OVAL limitation, this rule can report a false negative in a specific situation where two interactive users swap the ownership of their respective home directories.
