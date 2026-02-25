# Source: https://docs.datadoghq.com/security/default_rules/def-000-z1m.md

---
title: Verify User Who Owns /var/log/syslog File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify User Who Owns /var/log/syslog
  File
---

# Verify User Who Owns /var/log/syslog File

## Description{% #description %}

To properly set the owner of `/var/log/syslog`, run the command:

```gdscript3
$ sudo chown syslog /var/log/syslog
```

## Rationale{% #rationale %}

The `/var/log/syslog` file contains logs of error messages in the system and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - DISA-STIG-UBTU-20-010421
  - configure_strategy
  - file_owner_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Check that the syslog user is defined
  getent:
    database: passwd
    key: syslog
  ignore_errors: true
  when: '"rsyslog" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010421
  - configure_strategy
  - file_owner_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_owner_var_log_syslog_newown variable if syslog found
  set_fact:
    file_owner_var_log_syslog_newown: syslog
  when:
  - '"rsyslog" in ansible_facts.packages'
  - ansible_facts.getent_passwd["syslog"] is defined
  tags:
  - DISA-STIG-UBTU-20-010421
  - configure_strategy
  - file_owner_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /var/log/syslog
  stat:
    path: /var/log/syslog
  register: file_exists
  when: '"rsyslog" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010421
  - configure_strategy
  - file_owner_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /var/log/syslog
  file:
    path: /var/log/syslog
    owner: '{{ file_owner_var_log_syslog_newown }}'
  when:
  - '"rsyslog" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010421
  - configure_strategy
  - file_owner_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
