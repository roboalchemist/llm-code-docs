# Source: https://docs.datadoghq.com/security/default_rules/def-000-f5g.md

---
title: Verify Group Who Owns /etc/security/opasswd.old File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Who Owns
  /etc/security/opasswd.old File
---

# Verify Group Who Owns /etc/security/opasswd.old File
 
## Description{% #description %}

To properly set the group owner of `/etc/security/opasswd.old`, run the command:

```
$ sudo chgrp root /etc/security/opasswd.old
```

## Rationale{% #rationale %}

The `/etc/security/opasswd.old` file stores backups of old passwords to prevent password reuse. Protection of this file is critical for system security.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if getent group "0" >/dev/null 2>&1; then
  newgroup="0"
fi
if [[ -z ${newgroup} ]]; then
  echo "0 is not a defined group on the system"
  exit 1
fi
chgrp $newgroup /etc/security/opasswd.old
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_groupowner_etc_security_opasswd_old_newgroup variable if represented
    by gid
  set_fact:
    file_groupowner_etc_security_opasswd_old_newgroup: '0'
  tags:
  - configure_strategy
  - file_groupowner_etc_security_opasswd_old
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
  - file_groupowner_etc_security_opasswd_old
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/security/opasswd.old
  file:
    path: /etc/security/opasswd.old
    group: '{{ file_groupowner_etc_security_opasswd_old_newgroup }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - configure_strategy
  - file_groupowner_etc_security_opasswd_old
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
