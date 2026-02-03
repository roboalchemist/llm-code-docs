# Source: https://docs.datadoghq.com/security/default_rules/def-000-xav.md

---
title: Verify Group Ownership of System Login Banner
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Ownership of System Login
  Banner
---

# Verify Group Ownership of System Login Banner
 
## Description{% #description %}

To properly set the group owner of `/etc/issue`, run the command:

```
$ sudo chgrp root /etc/issue
```

## Rationale{% #rationale %}

Display of a standardized and approved use notification before granting access to the operating system ensures privacy and security notification verbiage used is consistent with applicable federal laws, Executive Orders, directives, policies, regulations, standards, and guidance.

Proper group ownership will ensure that only root user can modify the banner.

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
chgrp $newgroup /etc/issue
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Set the file_groupowner_etc_issue_newgroup variable if represented by gid
  set_fact:
    file_groupowner_etc_issue_newgroup: '0'
  tags:
  - configure_strategy
  - file_groupowner_etc_issue
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
  - file_groupowner_etc_issue
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/issue
  file:
    path: /etc/issue
    group: '{{ file_groupowner_etc_issue_newgroup }}'
  when: file_exists.stat is defined and file_exists.stat.exists
  tags:
  - configure_strategy
  - file_groupowner_etc_issue
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
