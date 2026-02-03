# Source: https://docs.datadoghq.com/security/default_rules/def-000-dvy.md

---
title: Verify Permissions on /etc/at.allow file
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions on /etc/at.allow
  file
---

# Verify Permissions on /etc/at.allow file
 
## Description{% #description %}

If `/etc/at.allow` exists, it must have permissions `0640` or more restrictive. To properly set the permissions of `/etc/at.allow`, run the command:

```
$ sudo chmod 0640 /etc/at.allow
```

## Rationale{% #rationale %}

If the permissions of the at.allow file are not set to 0640 or more restrictive, the possibility exists for an unauthorized user to view or edit sensitive information.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

chmod u-xs,g-xws,o-xwrt /etc/at.allow

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
  - file_permissions_at_allow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /etc/at.allow
  stat:
    path: /etc/at.allow
  register: file_exists
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_at_allow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xws,o-xwrt on /etc/at.allow
  file:
    path: /etc/at.allow
    mode: u-xs,g-xws,o-xwrt
  when:
  - '"linux-base" in ansible_facts.packages'
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_at_allow
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
