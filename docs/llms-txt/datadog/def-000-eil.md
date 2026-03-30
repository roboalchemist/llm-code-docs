# Source: https://docs.datadoghq.com/security/default_rules/def-000-eil.md

---
title: Verify ownership of System Login Banner
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify ownership of System Login Banner
---

# Verify ownership of System Login Banner

## Description{% #description %}

To properly set the owner of `/etc/issue`, run the command:

```
$ sudo chown root /etc/issue
```

## Rationale{% #rationale %}

Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.

Proper ownership will ensure that only root user can modify the banner.

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
chown $newown /etc/issue
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_owner_etc_issue_newown variable if represented by uid
  set_fact:
    file_owner_etc_issue_newown: '0'
  tags:
  - configure_strategy
  - file_owner_etc_issue
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/issue
  stat:
    path: /etc/issue
  register: file_exists
  tags:
  - configure_strategy
  - file_owner_etc_issue
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /etc/issue
  file:
    path: /etc/issue
    owner: '{{ file_owner_etc_issue_newown }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - configure_strategy
  - file_owner_etc_issue
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
