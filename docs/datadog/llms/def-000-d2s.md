# Source: https://docs.datadoghq.com/security/default_rules/def-000-d2s.md

---
title: Verify Permissions on cron.monthly
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify Permissions on cron.monthly
---

# Verify Permissions on cron.monthly

## Description{% #description %}

To properly set the permissions of `/etc/cron.monthly`, run the command:

```
$ sudo chmod 0700 /etc/cron.monthly
```

## Rationale{% #rationale %}

Service configuration files enable or disable features of their respective services that if configured incorrectly can lead to insecure and vulnerable configurations. Therefore, service configuration files should have the correct access rights to prevent unauthorized changes.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

find -H /etc/cron.monthly/ -maxdepth 1 -perm /u+s,g+xwrs,o+xwrt -type d -exec chmod u-s,g-xwrs,o-xwrt {} \;

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```go
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_cron_monthly
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /etc/cron.monthly/ file(s)
  command: 'find -L /etc/cron.monthly/ -maxdepth 1 -perm /u+s,g+xwrs,o+xwrt  -type
    d '
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_cron_monthly
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set permissions for /etc/cron.monthly/ file(s)
  file:
    path: '{{ item }}'
    mode: u-s,g-xwrs,o-xwrt
    state: directory
  with_items:
  - '{{ files_found.stdout_lines }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_cron_monthly
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
