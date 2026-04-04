# Source: https://docs.datadoghq.com/security/default_rules/def-000-ui7.md

---
title: Verify Permissions on /var/log/waagent.log(.*) Files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions on
  /var/log/waagent.log(.*) Files
---

# Verify Permissions on /var/log/waagent.log(.*) Files

## Description{% #description %}

To properly set the permissions of `/var/log/waagent.log`, run the command:

```gdscript3
$ sudo chmod 0644 /var/log/waagent.log
```

## Rationale{% #rationale %}

The `/var/log/waagent.log` file contains Azure Linux Guest Agent records events that can be used for troubleshooting and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

find -L /var/log/ -maxdepth 1 -perm /u+xs,g+xws,o+xwt  -type f -regextype posix-extended -regex '.*waagent.log([^\/]+)?$' -exec chmod u-xs,g-xws,o-xwt {} \;
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Find /var/log/ file(s)
  command: find -L /var/log/ -maxdepth 1 -perm /u+xs,g+xws,o+xwt  -type f -regextype
    posix-extended -regex ".*waagent.log([^\/]+)?$"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  tags:
  - configure_strategy
  - file_permissions_var_log_waagent
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set permissions for /var/log/ file(s)
  file:
    path: '{{ item }}'
    mode: u-xs,g-xws,o-xwt
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  tags:
  - configure_strategy
  - file_permissions_var_log_waagent
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
