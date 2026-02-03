# Source: https://docs.datadoghq.com/security/default_rules/def-000-gz7.md

---
title: Verify Group Who Owns gshadow File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Group Who Owns gshadow File
---

# Verify Group Who Owns gshadow File
 
## Description{% #description %}

To properly set the group owner of `/etc/gshadow`, run the command:

```
$ sudo chgrp shadow /etc/gshadow
```

## Rationale{% #rationale %}

The `/etc/gshadow` file contains group password hashes. Protection of this file is critical for system security.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

if getent group "42" >/dev/null 2>&1; then
  newgroup="42"
fi
if [[ -z ${newgroup} ]]; then
  echo "42 is not a defined group on the system"
  exit 1
fi
chgrp $newgroup /etc/gshadow
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_groupowner_etc_gshadow_newgroup variable if represented by gid
  set_fact:
    file_groupowner_etc_gshadow_newgroup: '42'
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - configure_strategy
  - file_groupowner_etc_gshadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/gshadow
  stat:
    path: /etc/gshadow
  register: file_exists
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - configure_strategy
  - file_groupowner_etc_gshadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/gshadow
  file:
    path: /etc/gshadow
    group: '{{ file_groupowner_etc_gshadow_newgroup }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - configure_strategy
  - file_groupowner_etc_gshadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
