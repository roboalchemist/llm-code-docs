# Source: https://docs.datadoghq.com/security/default_rules/def-000-7pm.md

---
title: Verify User Who Owns shadow File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify User Who Owns shadow File
---

# Verify User Who Owns shadow File
 
## Description{% #description %}

To properly set the owner of `/etc/shadow`, run the command:

```
$ sudo chown root /etc/shadow 
```

## Rationale{% #rationale %}

The `/etc/shadow` file contains the list of local system accounts and stores password hashes. Protection of this file is critical for system security. Failure to give ownership of this file to root provides the designated owner with access to sensitive information which could weaken the system security posture.

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
chown $newown /etc/shadow
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_owner_etc_shadow_newown variable if represented by uid
  set_fact:
    file_owner_etc_shadow_newown: '0'
  tags:
  - CJIS-5.5.2.2
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_etc_shadow
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
  - file_owner_etc_shadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /etc/shadow
  file:
    path: /etc/shadow
    owner: '{{ file_owner_etc_shadow_newown }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - CJIS-5.5.2.2
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-8.7.c
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_etc_shadow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
