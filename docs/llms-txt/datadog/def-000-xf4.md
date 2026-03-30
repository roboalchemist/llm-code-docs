# Source: https://docs.datadoghq.com/security/default_rules/def-000-xf4.md

---
title: Verify Group Who Owns /etc/shells File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Group Who Owns /etc/shells File
---

# Verify Group Who Owns /etc/shells File

## Description{% #description %}

To properly set the group owner of `/etc/shells`, run the command:

```
$ sudo chgrp root /etc/shells
```

## Rationale{% #rationale %}

The `/etc/shells` file contains the list of full pathnames to shells on the system. Since this file is used by many system programs this file should be protected.

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
chgrp $newgroup /etc/shells
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_groupowner_etc_shells_newgroup variable if represented by gid
  set_fact:
    file_groupowner_etc_shells_newgroup: '0'
  tags:
  - NIST-800-53-AC-3
  - NIST-800-53-MP-2
  - configure_strategy
  - file_groupowner_etc_shells
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/shells
  stat:
    path: /etc/shells
  register: file_exists
  tags:
  - NIST-800-53-AC-3
  - NIST-800-53-MP-2
  - configure_strategy
  - file_groupowner_etc_shells
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/shells
  file:
    path: /etc/shells
    group: '{{ file_groupowner_etc_shells_newgroup }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - NIST-800-53-AC-3
  - NIST-800-53-MP-2
  - configure_strategy
  - file_groupowner_etc_shells
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
