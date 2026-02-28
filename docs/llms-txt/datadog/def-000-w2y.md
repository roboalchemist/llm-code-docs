# Source: https://docs.datadoghq.com/security/default_rules/def-000-w2y.md

---
title: Verify Permissions on /etc/security/opasswd.old File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions on
  /etc/security/opasswd.old File
---

# Verify Permissions on /etc/security/opasswd.old File

## Description{% #description %}

To properly set the permissions of `/etc/security/opasswd.old`, run the command:

```
$ sudo chmod 0600 /etc/security/opasswd.old
```

## Rationale{% #rationale %}

The `/etc/security/opasswd.old` file stores backups of old passwords to prevent password reuse. Protection of this file is critical for system security.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

chmod u-xs,g-xwrs,o-xwrt /etc/security/opasswd.old
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Test for existence /etc/security/opasswd.old
  stat:
    path: /etc/security/opasswd.old
  register: file_exists
  tags:
  - configure_strategy
  - file_permissions_etc_security_opasswd_old
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xwrs,o-xwrt on /etc/security/opasswd.old
  file:
    path: /etc/security/opasswd.old
    mode: u-xs,g-xwrs,o-xwrt
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - configure_strategy
  - file_permissions_etc_security_opasswd_old
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
