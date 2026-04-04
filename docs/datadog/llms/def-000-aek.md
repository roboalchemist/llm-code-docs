# Source: https://docs.datadoghq.com/security/default_rules/def-000-aek.md

---
title: Verify User Who Owns passwd File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify User Who Owns passwd File
---

# Verify User Who Owns passwd File

## Description{% #description %}

To properly set the owner of `/etc/passwd`, run the command:

```
$ sudo chown root /etc/passwd
```

## Rationale{% #rationale %}

The `/etc/passwd` file contains information about the users that are configured on the system. Protection of this file is critical for system security.

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
chown $newown /etc/passwd
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_owner_etc_passwd_newown variable if represented by uid
  set_fact:
    file_owner_etc_passwd_newown: '0'
  tags:
  - CJIS-5.5.2.2
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_etc_passwd
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
  - file_owner_etc_passwd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /etc/passwd
  file:
    path: /etc/passwd
    owner: '{{ file_owner_etc_passwd_newown }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - CJIS-5.5.2.2
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_etc_passwd
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
