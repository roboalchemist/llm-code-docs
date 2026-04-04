# Source: https://docs.datadoghq.com/security/default_rules/def-000-4dh.md

---
title: Verify User Who Owns /etc/security/opasswd.old File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify User Who Owns
  /etc/security/opasswd.old File
---

# Verify User Who Owns /etc/security/opasswd.old File

## Description{% #description %}

To properly set the owner of `/etc/security/opasswd.old`, run the command:

```
$ sudo chown root /etc/security/opasswd.old
```

## Rationale{% #rationale %}

The `/etc/security/opasswd.old` file stores backups of old passwords to prevent password reuse. Protection of this file is critical for system security.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if id "0" >/dev/null 2>&1; then
  newown="0"
fi
if [[ -z ${newown} ]]; then
  echo "0 is not a defined user on the system"
  exit 1
fi
chown $newown /etc/security/opasswd.old
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_owner_etc_security_opasswd_old_newown variable if represented
    by uid
  set_fact:
    file_owner_etc_security_opasswd_old_newown: '0'
  tags:
  - configure_strategy
  - file_owner_etc_security_opasswd_old
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/security/opasswd.old
  stat:
    path: /etc/security/opasswd.old
  register: file_exists
  tags:
  - configure_strategy
  - file_owner_etc_security_opasswd_old
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /etc/security/opasswd.old
  file:
    path: /etc/security/opasswd.old
    owner: '{{ file_owner_etc_security_opasswd_old_newown }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - configure_strategy
  - file_owner_etc_security_opasswd_old
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
