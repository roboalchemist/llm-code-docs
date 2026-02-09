# Source: https://docs.datadoghq.com/security/default_rules/def-000-8ke.md

---
title: User Initialization Files Must Not Run World-Writable Programs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > User Initialization Files Must Not Run
  World-Writable Programs
---

# User Initialization Files Must Not Run World-Writable Programs
 
## Description{% #description %}

Set the mode on files being executed by the user initialization files with the following command:

```
$ sudo chmod o-w FILE
        
```

## Rationale{% #rationale %}

If user start-up files execute world-writable programs, especially in unprotected directories, they could be maliciously modified to destroy user files or otherwise compromise the system at the user level. If the system is compromised at the user level, it is easier to elevate privileges to eventually compromise the system at the root and network level.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

readarray -t world_writable_files < <(find / -xdev -type f -perm -0002 2> /dev/null)
readarray -t interactive_home_dirs < <(awk -F':' '{ if ($3 >= 1000 && $3 != 65534) print $6 }' /etc/passwd)

for world_writable in "${world_writable_files[@]}"; do
    for homedir in "${interactive_home_dirs[@]}"; do
        if grep -q -d skip "$world_writable" "$homedir"/.*; then
            chmod o-w $world_writable
            break
        fi
    done
done
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: User Initialization Files Must Not Run World-Writable Programs - Initialize
    variables
  set_fact:
    home_user_dirs: []
    world_writable_files: []
  tags:
  - accounts_user_dot_no_world_writable_programs
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: User Initialization Files Must Not Run World-Writable Programs - Get user's
    home dir list
  ansible.builtin.getent:
    database: passwd
  register: passwd_database
  tags:
  - accounts_user_dot_no_world_writable_programs
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: User Initialization Files Must Not Run World-Writable Programs - Fill home_user_dirs
  set_fact:
    home_user_dirs: '{{ home_user_dirs + [item.data[4]] }}'
  when: item.data[4] is defined and item.data[2]|int >= 1000 and item.data[2]|int
    != 65534
  with_items: '{{ passwd_database.ansible_facts.getent_passwd | dict2items(key_name=''user'',
    value_name=''data'')}}'
  tags:
  - accounts_user_dot_no_world_writable_programs
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: User Initialization Files Must Not Run World-Writable Programs - Get world
    writable files
  ansible.builtin.shell: |
    find / -xdev -type f -perm -0002 2> /dev/null
  register: world_writable_files
  tags:
  - accounts_user_dot_no_world_writable_programs
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: User Initialization Files Must Not Run World-Writable Programs - Find referenced_files
    in init files
  ansible.builtin.find:
    paths: '{{ home_user_dirs }}'
    contains: '{{ item }}'
    hidden: true
    read_whole_file: true
    recurse: true
  with_items: '{{ world_writable_files.stdout_lines }}'
  register: referenced_files
  tags:
  - accounts_user_dot_no_world_writable_programs
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: User Initialization Files Must Not Run World-Writable Programs - Remove world
    writable permissions
  ansible.builtin.file:
    path: '{{ item.item }}'
    mode: o-w
  when: item.matched > 0
  with_items: '{{ referenced_files.results }}'
  tags:
  - accounts_user_dot_no_world_writable_programs
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
