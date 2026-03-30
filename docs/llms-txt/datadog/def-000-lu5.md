# Source: https://docs.datadoghq.com/security/default_rules/def-000-lu5.md

---
title: Verify Permissions on /var/log/secure File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions on /var/log/secure
  File
---

# Verify Permissions on /var/log/secure File

## Description{% #description %}

To properly set the permissions of `/var/log/secure`, run the command:

```gdscript3
$ sudo chmod 0640 /var/log/secure
```

## Rationale{% #rationale %}

The `/var/log/secure` file contains information related to authentication and authorization privileges and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

chmod u-xs,g-xws,o-xwrt /var/log/secure
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Test for existence /var/log/secure
  stat:
    path: /var/log/secure
  register: file_exists
  tags:
  - configure_strategy
  - file_permissions_var_log_secure
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xws,o-xwrt on /var/log/secure
  file:
    path: /var/log/secure
    mode: u-xs,g-xws,o-xwrt
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - configure_strategy
  - file_permissions_var_log_secure
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
