# Source: https://docs.datadoghq.com/security/default_rules/def-000-m0e.md

---
title: All Interactive Users Home Directories Must Exist
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > All Interactive Users Home Directories
  Must Exist
---

# All Interactive Users Home Directories Must Exist
 
## Description{% #description %}

Create home directories to all local interactive users that currently do not have a home directory assigned. Use the following commands to create the user home directory assigned in `/etc/passwd`:

```
$ sudo mkdir /home/USER
        
```

## Rationale{% #rationale %}

If a local interactive user has a home directory defined that does not exist, the user may be given access to the / directory as the current working directory upon logon. This could create a Denial of Service because the user would not be able to access their logon configuration files, and it may give them visibility to system files they normally would not be able to access.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

for user in $(awk -F':' '{ if ($3 >= 1000 && $3 != 65534) print $1}' /etc/passwd); do
    mkhomedir_helper $user 0077;
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
  - accounts_user_interactive_home_directory_exists
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Create local_users variable from the getent output
  ansible.builtin.set_fact:
    local_users: '{{ ansible_facts.getent_passwd|dict2items }}'
  tags:
  - accounts_user_interactive_home_directory_exists
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure interactive users have a home directory exists
  ansible.builtin.user:
    name: '{{ item.key }}'
    create_home: true
  loop: '{{ local_users }}'
  when:
  - item.value[2]|int >= 1000
  - item.value[2]|int != 65534
  tags:
  - accounts_user_interactive_home_directory_exists
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
