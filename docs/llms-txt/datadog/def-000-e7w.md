# Source: https://docs.datadoghq.com/security/default_rules/def-000-e7w.md

---
title: Verify Group Who Owns passwd File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Group Who Owns passwd File
---

# Verify Group Who Owns passwd File
 
## Description{% #description %}

To properly set the group owner of `/etc/passwd`, run the command:

```
$ sudo chgrp root /etc/passwd
```

## Rationale{% #rationale %}

The `/etc/passwd` file contains information about the users that are configured on the system. Protection of this file is critical for system security.

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
chgrp $newgroup /etc/passwd
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_groupowner_etc_passwd_newgroup variable if represented by gid
  set_fact:
    file_groupowner_etc_passwd_newgroup: '0'
  tags:
  - CJIS-5.5.2.2
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_etc_passwd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/passwd
  stat:
    path: /etc/passwd
  register: file_exists
  tags:
  - CJIS-5.5.2.2
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_etc_passwd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/passwd
  file:
    path: /etc/passwd
    group: '{{ file_groupowner_etc_passwd_newgroup }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - CJIS-5.5.2.2
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_etc_passwd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
