# Source: https://docs.datadoghq.com/security/default_rules/def-000-3pb.md

---
title: Verify Group Who Owns Backup group File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Group Who Owns Backup group File
---

# Verify Group Who Owns Backup group File

## Description{% #description %}

To properly set the group owner of `/etc/group-`, run the command:

```
$ sudo chgrp root /etc/group-
```

## Rationale{% #rationale %}

The `/etc/group-` file is a backup file of `/etc/group`, and as such, it contains information regarding groups that are configured on the system. Protection of this file is important for system security.

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
chgrp $newgroup /etc/group-
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_groupowner_backup_etc_group_newgroup variable if represented
    by gid
  set_fact:
    file_groupowner_backup_etc_group_newgroup: '0'
  tags:
  - NIST-800-53-AC-6 (1)
  - PCI-DSS-Req-8.7
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_backup_etc_group
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/group-
  stat:
    path: /etc/group-
  register: file_exists
  tags:
  - NIST-800-53-AC-6 (1)
  - PCI-DSS-Req-8.7
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_backup_etc_group
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/group-
  file:
    path: /etc/group-
    group: '{{ file_groupowner_backup_etc_group_newgroup }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - NIST-800-53-AC-6 (1)
  - PCI-DSS-Req-8.7
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_backup_etc_group
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
