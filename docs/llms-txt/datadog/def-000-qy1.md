# Source: https://docs.datadoghq.com/security/default_rules/def-000-qy1.md

---
title: Verify Permissions on /etc/cron.allow file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions on /etc/cron.allow
  file
---

# Verify Permissions on /etc/cron.allow file
 
## Description{% #description %}

If `/etc/cron.allow` exists, it must have permissions `0640` or more restrictive. To properly set the permissions of `/etc/cron.allow`, run the command:

```
$ sudo chmod 0640 /etc/cron.allow
```

## Rationale{% #rationale %}

If the permissions of the cron.allow file are not set to 0640 or more restrictive, the possibility exists for an unauthorized user to view or edit sensitive information.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

chmod u-xs,g-xws,o-xwrt /etc/cron.allow

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```zed
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_cron_allow
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
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_cron_allow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xws,o-xwrt on /etc/cron.allow
  file:
    path: /etc/cron.allow
    mode: u-xs,g-xws,o-xwrt
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_cron_allow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
