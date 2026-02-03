# Source: https://docs.datadoghq.com/security/default_rules/def-000-pz7.md

---
title: Verify Group Who Owns /etc/security/opasswd File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Who Owns
  /etc/security/opasswd File
---

# Verify Group Who Owns /etc/security/opasswd File
 
## Description{% #description %}

To properly set the group owner of `/etc/security/opasswd`, run the command:

```
$ sudo chgrp root /etc/security/opasswd
```

## Rationale{% #rationale %}

The `/etc/security/opasswd` file stores old passwords to prevent password reuse. Protection of this file is critical for system security.

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
chgrp $newgroup /etc/security/opasswd
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_groupowner_etc_security_opasswd_newgroup variable if represented
    by gid
  set_fact:
    file_groupowner_etc_security_opasswd_newgroup: '0'
  tags:
  - configure_strategy
  - file_groupowner_etc_security_opasswd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/security/opasswd
  stat:
    path: /etc/security/opasswd
  register: file_exists
  tags:
  - configure_strategy
  - file_groupowner_etc_security_opasswd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/security/opasswd
  file:
    path: /etc/security/opasswd
    group: '{{ file_groupowner_etc_security_opasswd_newgroup }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - configure_strategy
  - file_groupowner_etc_security_opasswd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
