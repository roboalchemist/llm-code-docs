# Source: https://docs.datadoghq.com/security/default_rules/def-000-jkv.md

---
title: Verify Group Who Owns /var/log/syslog File
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Who Owns /var/log/syslog
  File
---

# Verify Group Who Owns /var/log/syslog File
 
## Description{% #description %}

To properly set the group owner of `/var/log/syslog`, run the command:

```gdscript3
$ sudo chgrp adm /var/log/syslog
```

## Rationale{% #rationale %}

The `/var/log/syslog` file contains logs of error messages in the system and should only be accessed by authorized personnel.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'rsyslog' 2>/dev/null | grep -q '^installed$'; then

if getent group "4" >/dev/null 2>&1; then
  newgroup="4"
fi
if [[ -z ${newgroup} ]]; then
  echo "4 is not a defined group on the system"
  exit 1
fi
chgrp $newgroup /var/log/syslog

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
  - DISA-STIG-UBTU-20-010420
  - configure_strategy
  - file_groupowner_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_var_log_syslog_newgroup variable if represented by
    gid
  set_fact:
    file_groupowner_var_log_syslog_newgroup: '4'
  when: '"rsyslog" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010420
  - configure_strategy
  - file_groupowner_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /var/log/syslog
  stat:
    path: /var/log/syslog
  register: file_exists
  when: '"rsyslog" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010420
  - configure_strategy
  - file_groupowner_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /var/log/syslog
  file:
    path: /var/log/syslog
    group: '{{ file_groupowner_var_log_syslog_newgroup }}'
  when:
  - '"rsyslog" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010420
  - configure_strategy
  - file_groupowner_var_log_syslog
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
