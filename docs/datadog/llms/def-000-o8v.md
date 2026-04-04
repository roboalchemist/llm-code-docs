# Source: https://docs.datadoghq.com/security/default_rules/def-000-o8v.md

---
title: Set Existing Passwords Minimum Age
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set Existing Passwords Minimum Age
---

# Set Existing Passwords Minimum Age

## Description{% #description %}

Configure non-compliant accounts to enforce a 24 hours/1 day minimum password lifetime by running the following command:

```
$ sudo chage -m 1 USER

```

## Rationale{% #rationale %}

Enforcing a minimum password lifetime helps to prevent repeated password changes to defeat the password reuse or history enforcement requirement. If users are allowed to immediately and continually change their password, the password could be repeatedly changed in a short period of time to defeat the organization's policy regarding password reuse.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

var_accounts_minimum_age_login_defs='1'


while IFS= read -r i; do

    chage -m $var_accounts_minimum_age_login_defs $i

done <   <(awk -v var="$var_accounts_minimum_age_login_defs" -F: '(/^[^:]+:[^!*]/ && ($4 < var || $4 == "")) {print $1}' /etc/shadow)
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: XCCDF Value var_accounts_minimum_age_login_defs # promote to variable
  set_fact:
    var_accounts_minimum_age_login_defs: !!str 1
  tags:
    - always

- name: Collect users with not correct minimum time period between password changes
  command: |
    awk -F':' '(/^[^:]+:[^!*]/ && ($4 < {{ var_accounts_minimum_age_login_defs }} || $4 == "")) {print $1}' /etc/shadow
  register: user_names
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(d)
  - NIST-800-53-IA-5(f)
  - accounts_password_set_min_life_existing
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Change the minimum time period between password changes
  command: |
    chage -m {{ var_accounts_minimum_age_login_defs }} {{ item }}
  with_items: '{{ user_names.stdout_lines }}'
  when: user_names.stdout_lines | length > 0
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(d)
  - NIST-800-53-IA-5(f)
  - accounts_password_set_min_life_existing
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
