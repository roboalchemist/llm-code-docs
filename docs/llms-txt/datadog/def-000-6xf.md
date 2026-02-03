# Source: https://docs.datadoghq.com/security/default_rules/def-000-6xf.md

---
title: Verify Group Who Owns /etc/at.deny file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Group Who Owns /etc/at.deny file
---

# Verify Group Who Owns /etc/at.deny file
 
## Description{% #description %}

If `/etc/at.deny` exists, it must be group-owned by `root`. To properly set the group owner of `/etc/at.deny`, run the command:

```
$ sudo chgrp root /etc/at.deny
```

## Rationale{% #rationale %}

If the owner of the at.deny file is not set to root, the possibility exists for an unauthorized user to view or edit sensitive information.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if getent group "0" >/dev/null 2>&1; then
  newgroup="0"
fi
if [[ -z ${newgroup} ]]; then
  echo "0 is not a defined group on the system"
  exit 1
fi
chgrp $newgroup /etc/at.deny

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - configure_strategy
  - file_groupowner_at_deny
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_at_deny_newgroup variable if represented by gid
  set_fact:
    file_groupowner_at_deny_newgroup: '0'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - configure_strategy
  - file_groupowner_at_deny
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/at.deny
  stat:
    path: /etc/at.deny
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - configure_strategy
  - file_groupowner_at_deny
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/at.deny
  file:
    path: /etc/at.deny
    group: '{{ file_groupowner_at_deny_newgroup }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - configure_strategy
  - file_groupowner_at_deny
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
