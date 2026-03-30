# Source: https://docs.datadoghq.com/security/default_rules/def-000-vp9.md

---
title: Verify Group Who Owns /var/log/*.journal(~) File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Who Owns
  /var/log/*.journal(~) File
---

# Verify Group Who Owns /var/log/*.journal(~) File

## Description{% #description %}

To properly set the group owner of `/var/log/*.journal(~)`, run the command:

```gdscript3
$ sudo chgrp systemd-journal /var/log/*.journal(~)
```

or

```gdscript3
$ sudo chgrp root /var/log/*.journal(~)
```

## Rationale{% #rationale %}

The `/var/log/*.journal(~)` files are system logs managed by the "systemd" service.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if getent group "systemd-journal" >/dev/null 2>&1; then
  newgroup="systemd-journal"
elif getent group "root" >/dev/null 2>&1; then
  newgroup="root"
fi
if [[ -z ${newgroup} ]]; then
  echo "systemd-journal and root is not a defined group on the system"
  exit 1
fi

find  /var/log/  -type f  ! -group systemd-journal ! -group root -regextype posix-extended -regex '.*\.journal[~]?' -exec chgrp -L $newgroup {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Check that the systemd-journal group is defined
  getent:
    database: group
    key: systemd-journal
  ignore_errors: true
  when: file_groupowner_var_log_journal_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupowner_var_log_journal
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_var_log_journal_newgroup variable if systemd-journal
    found
  set_fact:
    file_groupowner_var_log_journal_newgroup: systemd-journal
  when: ansible_facts.getent_group["systemd-journal"] is defined
  tags:
  - configure_strategy
  - file_groupowner_var_log_journal
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Check that the root group is defined
  getent:
    database: group
    key: root
  ignore_errors: true
  when: file_groupowner_var_log_journal_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupowner_var_log_journal
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_var_log_journal_newgroup variable if root found
  set_fact:
    file_groupowner_var_log_journal_newgroup: root
  when: ansible_facts.getent_group["root"] is defined
  tags:
  - configure_strategy
  - file_groupowner_var_log_journal
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /var/log/ file(s) matching .*\.journal[~]? recursively
  command: find  /var/log/  -type f  ! -group systemd-journal ! -group root -regextype
    posix-extended -regex ".*\.journal[~]?"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_groupowner_var_log_journal
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /var/log/ file(s) matching .*\.journal[~]?
  file:
    path: '{{ item }}'
    group: '{{ file_groupowner_var_log_journal_newgroup }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_groupowner_var_log_journal
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
