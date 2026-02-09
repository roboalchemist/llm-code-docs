# Source: https://docs.datadoghq.com/security/default_rules/def-000-lrr.md

---
title: Verify Group Who Owns SSH Server config file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Who Owns SSH Server config
  file
---

# Verify Group Who Owns SSH Server config file
 
## Description{% #description %}

To properly set the group owner of `/etc/ssh/sshd_config`, run the command:

```
$ sudo chgrp root /etc/ssh/sshd_config
```

## Rationale{% #rationale %}

Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations. Therefore, service configuration files should be owned by the correct group to prevent unauthorized changes.

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
chgrp $newgroup /etc/ssh/sshd_config

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
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - configure_strategy
  - file_groupowner_sshd_config
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_sshd_config_newgroup variable if represented by gid
  set_fact:
    file_groupowner_sshd_config_newgroup: '0'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - configure_strategy
  - file_groupowner_sshd_config
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/ssh/sshd_config
  stat:
    path: /etc/ssh/sshd_config
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - configure_strategy
  - file_groupowner_sshd_config
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/ssh/sshd_config
  file:
    path: /etc/ssh/sshd_config
    group: '{{ file_groupowner_sshd_config_newgroup }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - configure_strategy
  - file_groupowner_sshd_config
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
