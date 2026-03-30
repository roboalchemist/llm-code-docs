# Source: https://docs.datadoghq.com/security/default_rules/def-000-zph.md

---
title: Verify Group Who Owns shadow File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Group Who Owns shadow File
---

# Verify Group Who Owns shadow File

## Description{% #description %}

To properly set the group owner of `/etc/shadow`, run the command:

```
$ sudo chgrp shadow /etc/shadow
```

## Rationale{% #rationale %}

The `/etc/shadow` file stores password hashes. Protection of this file is critical for system security.

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
chgrp $newgroup /etc/shadow
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_groupowner_etc_shadow_newgroup variable if represented by gid
  set_fact:
    file_groupowner_etc_shadow_newgroup: '42'
  tags:
  - CJIS-5.5.2.2
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_etc_shadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/shadow
  stat:
    path: /etc/shadow
  register: file_exists
  tags:
  - CJIS-5.5.2.2
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_etc_shadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/shadow
  file:
    path: /etc/shadow
    group: '{{ file_groupowner_etc_shadow_newgroup }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - CJIS-5.5.2.2
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_etc_shadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
