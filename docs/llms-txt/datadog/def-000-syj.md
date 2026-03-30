# Source: https://docs.datadoghq.com/security/default_rules/def-000-syj.md

---
title: Ensure the Default C Shell Umask is Set Correctly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure the Default C Shell Umask is Set
  Correctly
---

# Ensure the Default C Shell Umask is Set Correctly

## Description{% #description %}

To ensure the default umask for users of the C shell is set properly, add or correct the `umask` setting in `/etc/csh.cshrc` to read as follows:

```
umask 027

```

## Rationale{% #rationale %}

The umask value influences the permissions assigned to files when they are created. A misconfigured umask value could result in files with excessive permissions that can be read or written to by unauthorized users.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

var_accounts_user_umask='027'


grep -q "^\s*umask" /etc/csh.cshrc && \
  sed -i -E -e "s/^(\s*umask).*/\1 $var_accounts_user_umask/g" /etc/csh.cshrc
if ! [ $? -eq 0 ]; then
    echo "umask $var_accounts_user_umask" >> /etc/csh.cshrc
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: XCCDF Value var_accounts_user_umask # promote to variable
  set_fact:
    var_accounts_user_umask: !!str 027
  tags:
    - always

- name: Check if umask in /etc/csh.cshrc is already set
  ansible.builtin.lineinfile:
    path: /etc/csh.cshrc
    regexp: ^(\s*)umask\s+.*
    state: absent
  check_mode: true
  changed_when: false
  register: umask_replace
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_csh_cshrc
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Replace user umask in /etc/csh.cshrc
  ansible.builtin.replace:
    path: /etc/csh.cshrc
    regexp: ^(\s*)umask(\s+).*
    replace: \g<1>umask\g<2>{{ var_accounts_user_umask }}
  when: umask_replace.found > 0
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_csh_cshrc
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure the Default umask is Appended Correctly
  ansible.builtin.lineinfile:
    create: true
    path: /etc/csh.cshrc
    line: umask {{ var_accounts_user_umask }}
  when: umask_replace.found == 0
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_csh_cshrc
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
