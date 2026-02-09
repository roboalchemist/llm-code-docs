# Source: https://docs.datadoghq.com/security/default_rules/def-000-c8z.md

---
title: Ensure All User Initialization Files Have Mode 0740 Or Less Permissive
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure All User Initialization Files
  Have Mode 0740 Or Less Permissive
---

# Ensure All User Initialization Files Have Mode 0740 Or Less Permissive
 
## Description{% #description %}

Set the mode of the user initialization files to `0740` with the following command:

```
$ sudo chmod 0740 /home/USER/.INIT_FILE
        
```

## Rationale{% #rationale %}

Local initialization files are used to configure the user's shell environment upon logon. Malicious modification of these files could compromise accounts upon logon.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

var_user_initialization_files_regex='^\.[\w\- ]+$'


readarray -t interactive_users < <(awk -F: '$3>=1000   {print $1}' /etc/passwd)
readarray -t interactive_users_home < <(awk -F: '$3>=1000   {print $6}' /etc/passwd)
readarray -t interactive_users_shell < <(awk -F: '$3>=1000   {print $7}' /etc/passwd)

USERS_IGNORED_REGEX='nobody|nfsnobody'

for (( i=0; i<"${#interactive_users[@]}"; i++ )); do
    if ! grep -qP "$USERS_IGNORED_REGEX" <<< "${interactive_users[$i]}" && \
        [ "${interactive_users_shell[$i]}" != "/sbin/nologin" ]; then
        
        readarray -t init_files < <(find "${interactive_users_home[$i]}" -maxdepth 1 \
            -exec basename {} \; | grep -P "$var_user_initialization_files_regex")
        for file in "${init_files[@]}"; do
            chmod u-s,g-wxs,o= "${interactive_users_home[$i]}/$file"
        done
    fi
done
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: XCCDF Value var_user_initialization_files_regex # promote to variable
  set_fact:
    var_user_initialization_files_regex: !!str ^\.[\w\- ]+$
  tags:
    - always

- name: Ensure All User Initialization Files Have Mode 0740 Or Less Permissive - Gather
    User Info
  ansible.builtin.getent:
    database: passwd
  tags:
  - file_permission_user_init_files
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure All User Initialization Files Have Mode 0740 Or Less Permissive - Find
    Init Files
  ansible.builtin.find:
    paths: '{{ item.value[4] }}'
    pattern: '{{ var_user_initialization_files_regex }}'
    hidden: true
    use_regex: true
  with_dict: '{{ ansible_facts.getent_passwd }}'
  when:
  - item.value[4] != "/sbin/nologin"
  - item.key not in ["nobody", "nfsnobody"]
  - item.value[1] | int >= 1000
  register: found_init_files
  tags:
  - file_permission_user_init_files
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure All User Initialization Files Have Mode 0740 Or Less Permissive - Fix
    Init Files Permissions
  ansible.builtin.file:
    path: '{{ item.1.path }}'
    mode: u-s,g-wxs,o=
  loop: '{{ q(''ansible.builtin.subelements'', found_init_files.results, ''files'',
    {''skip_missing'': True}) }}'
  tags:
  - file_permission_user_init_files
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
