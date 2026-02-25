# Source: https://docs.datadoghq.com/security/default_rules/def-000-bhr.md

---
title: Ensure the Default Umask is Set Correctly in /etc/profile
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure the Default Umask is Set
  Correctly in /etc/profile
---

# Ensure the Default Umask is Set Correctly in /etc/profile

## Description{% #description %}

To ensure the default umask controlled by `/etc/profile` is set properly, add or correct the `umask` setting in `/etc/profile` to read as follows:

```
umask 027

```

Note that `/etc/profile` also reads scrips within `/etc/profile.d` directory. These scripts are also valid files to set umask value. Therefore, they should also be considered during the check and properly remediated, if necessary.

## Rationale{% #rationale %}

The umask value influences the permissions assigned to files when they are created. A misconfigured umask value could result in files with excessive permissions that can be read or written to by unauthorized users.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

var_accounts_user_umask='027'


readarray -t profile_files < <(find /etc/profile.d/ -type f -name '*.sh' -or -name 'sh.local')

for file in "${profile_files[@]}" /etc/profile; do
  grep -qE '^[^#]*umask' "$file" && sed -i -E "s/^(\s*umask\s*)[0-7]+/\1$var_accounts_user_umask/g" "$file"
done

if ! grep -qrE '^[^#]*umask' /etc/profile*; then
  echo "umask $var_accounts_user_umask" >> /etc/profile
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

- name: Ensure the Default Umask is Set Correctly in /etc/profile - Locate Profile
    Configuration Files Where umask Is Defined
  ansible.builtin.find:
    paths:
    - /etc/profile.d
    patterns:
    - sh.local
    - '*.sh'
    contains: ^[\s]*umask\s+\d+
  register: result_profile_d_files
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_profile
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure the Default Umask is Set Correctly in /etc/profile - Replace Existing
    umask Value in Files From /etc/profile.d
  ansible.builtin.replace:
    path: '{{ item.path }}'
    regexp: ^(\s*)umask\s+\d+
    replace: \1umask {{ var_accounts_user_umask }}
  loop: '{{ result_profile_d_files.files }}'
  register: result_umask_replaced_profile_d
  when: result_profile_d_files.matched
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_profile
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure the Default Umask is Set Correctly in /etc/profile - Ensure umask Is
    Set in /etc/profile if Not Already Set Elsewhere
  ansible.builtin.lineinfile:
    create: true
    mode: 420
    path: /etc/profile
    line: umask {{ var_accounts_user_umask }}
  when: not result_profile_d_files.matched
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_profile
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure the Default Umask is Set Correctly in /etc/profile - Ensure umask Value
    For All Existing umask Definition in /etc/profile
  ansible.builtin.replace:
    path: /etc/profile
    regexp: ^(\s*)umask\s+\d+
    replace: \1umask {{ var_accounts_user_umask }}
  register: result_umask_replaced_profile
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - accounts_umask_etc_profile
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
