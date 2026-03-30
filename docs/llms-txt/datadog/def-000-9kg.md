# Source: https://docs.datadoghq.com/security/default_rules/def-000-9kg.md

---
title: Verify Group Who Owns /etc/cron.allow file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Group Who Owns /etc/cron.allow
  file
---

# Verify Group Who Owns /etc/cron.allow file

## Description{% #description %}

If `/etc/cron.allow` exists, it must be group-owned by `crontab`. To properly set the group owner of `/etc/cron.allow`, run the command:

```
$ sudo chgrp crontab /etc/cron.allow
```

## Rationale{% #rationale %}

If the owner of the cron.allow file is not set to crontab, the possibility exists for an unauthorized user to view or edit sensitive information.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if getent group "crontab" >/dev/null 2>&1; then
  newgroup="crontab"
fi
if [[ -z ${newgroup} ]]; then
  echo "crontab is not a defined group on the system"
  exit 1
fi
chgrp $newgroup /etc/cron.allow

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
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_cron_allow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Check that the crontab group is defined
  getent:
    database: group
    key: crontab
  ignore_errors: true
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_groupowner_cron_allow_newgroup is undefined
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_cron_allow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_groupowner_cron_allow_newgroup variable if crontab found
  set_fact:
    file_groupowner_cron_allow_newgroup: crontab
  when:
  - '"linux-base" in ansible_facts.packages'
  - ansible_facts.getent_group["crontab"] is defined
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_cron_allow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/cron.allow
  stat:
    path: /etc/cron.allow
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_cron_allow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner on /etc/cron.allow
  file:
    path: /etc/cron.allow
    group: '{{ file_groupowner_cron_allow_newgroup }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_cron_allow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
