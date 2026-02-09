# Source: https://docs.datadoghq.com/security/default_rules/def-000-ieo.md

---
title: Verify Permissions on /var/log/syslog File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions on /var/log/syslog
  File
---

# Verify Permissions on /var/log/syslog File
 
## Description{% #description %}

To properly set the permissions of `/var/log/syslog`, run the command:

```gdscript3
$ sudo chmod 0640 /var/log/syslog
```

## Rationale{% #rationale %}

The `/var/log/syslog` file contains logs of error messages in the system and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

chmod u-xs,g-xws,o-xwrt /var/log/syslog
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Test for existence /var/log/syslog
  stat:
    path: /var/log/syslog
  register: file_exists
  tags:
  - DISA-STIG-UBTU-20-010422
  - configure_strategy
  - file_permissions_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xws,o-xwrt on /var/log/syslog
  file:
    path: /var/log/syslog
    mode: u-xs,g-xws,o-xwrt
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010422
  - configure_strategy
  - file_permissions_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
