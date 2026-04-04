# Source: https://docs.datadoghq.com/security/default_rules/def-000-f5b.md

---
title: Set Existing Passwords Warning Age
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Set Existing Passwords Warning Age
---

# Set Existing Passwords Warning Age

## Description{% #description %}

To configure how many days prior to password expiration that a warning will be issued to users, run the command:

```
$ sudo chage --warndays 7
          USER

```

The DoD requirement is 7, and CIS recommendation is no less than 7 days. This profile requirement is `7`.

## Rationale{% #rationale %}

Providing an advance warning that a password will be expiring gives users time to think of a secure password. Users caught unaware may choose a simple password or write it down where it may be discovered.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

var_accounts_password_warn_age_login_defs='7'


while IFS= read -r i; do
    chage --warndays $var_accounts_password_warn_age_login_defs $i
done <   <(awk -v var="$var_accounts_password_warn_age_login_defs" -F: '(($6 < var || $6 == "") && $2 ~ /^\$/) {print $1}' /etc/shadow)
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: XCCDF Value var_accounts_password_warn_age_login_defs # promote to variable
  set_fact:
    var_accounts_password_warn_age_login_defs: !!str 7
  tags:
    - always

- name: Set Existing Passwords Warning Age - Collect Users With Incorrect Number of
    Days of Warning Before Password Expires
  ansible.builtin.command:
    cmd: awk -F':' '(($6 < {{ var_accounts_password_warn_age_login_defs }} || $6 ==
      "") && $2 ~ /^\$/) {print $1}' /etc/shadow
  register: result_pass_warn_age_user_names
  changed_when: false
  tags:
  - CCE-86913-1
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(d)
  - NIST-800-53-IA-5(f)
  - PCI-DSSv4-8.3.9
  - accounts_password_set_warn_age_existing
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set Existing Passwords Warning Age - Ensure the Number of Days of Warning
    Before Password Expires
  ansible.builtin.command:
    cmd: chage --warndays {{ var_accounts_password_warn_age_login_defs }} {{ item
      }}
  with_items: '{{ result_pass_warn_age_user_names.stdout_lines }}'
  when: result_pass_warn_age_user_names is not skipped and result_pass_warn_age_user_names.stdout_lines
    | length > 0
  tags:
  - CCE-86913-1
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(d)
  - NIST-800-53-IA-5(f)
  - PCI-DSSv4-8.3.9
  - accounts_password_set_warn_age_existing
  - configure_strategy
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
