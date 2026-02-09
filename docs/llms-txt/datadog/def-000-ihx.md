# Source: https://docs.datadoghq.com/security/default_rules/def-000-ihx.md

---
title: Verify Group Who Owns /var/log/localmessages* File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Who Owns
  /var/log/localmessages* File
---

# Verify Group Who Owns /var/log/localmessages* File
 
## Description{% #description %}

To properly set the group owner of `/var/log/localmessages*`, run the command:

```gdscript3
$ sudo chgrp adm /var/log/localmessages*
```

or

```gdscript3
$ sudo chgrp root /var/log/localmessages*
```

## Rationale{% #rationale %}

The `/var/log/localmessages*` file contains log messages from certain boot scripts, including the DHCP client, and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if getent group "adm" >/dev/null 2>&1; then
  newgroup="adm"
elif getent group "root" >/dev/null 2>&1; then
  newgroup="root"
fi
if [[ -z ${newgroup} ]]; then
  echo "adm and root is not a defined group on the system"
  exit 1
fi

find -L /var/log/ -maxdepth 1 -type f  ! -group adm ! -group root -regextype posix-extended -regex '.*localmessages.*' -exec chgrp -L $newgroup {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Check that the adm group is defined
  getent:
    database: group
    key: adm
  ignore_errors: true
  when: file_groupowner_var_log_localmessages_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupowner_var_log_localmessages
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_var_log_localmessages_newgroup variable if adm found
  set_fact:
    file_groupowner_var_log_localmessages_newgroup: adm
  when: ansible_facts.getent_group["adm"] is defined
  tags:
  - configure_strategy
  - file_groupowner_var_log_localmessages
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Check that the root group is defined
  getent:
    database: group
    key: root
  ignore_errors: true
  when: file_groupowner_var_log_localmessages_newgroup is undefined
  tags:
  - configure_strategy
  - file_groupowner_var_log_localmessages
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_var_log_localmessages_newgroup variable if root found
  set_fact:
    file_groupowner_var_log_localmessages_newgroup: root
  when: ansible_facts.getent_group["root"] is defined
  tags:
  - configure_strategy
  - file_groupowner_var_log_localmessages
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /var/log/ file(s) matching .*localmessages.*
  command: find -L /var/log/ -maxdepth 1 -type f  ! -group adm ! -group root -regextype
    posix-extended -regex ".*localmessages.*"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_groupowner_var_log_localmessages
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /var/log/ file(s) matching .*localmessages.*
  file:
    path: '{{ item }}'
    group: '{{ file_groupowner_var_log_localmessages_newgroup }}'
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_groupowner_var_log_localmessages
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
