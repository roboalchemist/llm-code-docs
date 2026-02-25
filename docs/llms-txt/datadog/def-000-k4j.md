# Source: https://docs.datadoghq.com/security/default_rules/def-000-k4j.md

---
title: Verify Permissions on SSH Server Public *.pub Key Files
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify Permissions on SSH Server Public
  *.pub Key Files
---

# Verify Permissions on SSH Server Public *.pub Key Files

## Description{% #description %}

To properly set the permissions of `/etc/ssh/*.pub`, run the command:

```
$ sudo chmod 0644 /etc/ssh/*.pub
```

## Rationale{% #rationale %}

If a public host key file is modified by an unauthorized user, the SSH service may be compromised.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

find -L /etc/ssh/ -maxdepth 1 -perm /u+xs,g+xws,o+xwt  -type f -regextype posix-extended -regex '^.*\.pub$' -exec chmod u-xs,g-xws,o-xwt {} \;

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
  - NIST-800-171-3.1.13
  - NIST-800-171-3.13.10
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-2.2.4
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_sshd_pub_key
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Find /etc/ssh/ file(s)
  command: find -L /etc/ssh/ -maxdepth 1 -perm /u+xs,g+xws,o+xwt  -type f -regextype
    posix-extended -regex "^.*\.pub$"
  register: files_found
  changed_when: false
  failed_when: false
  check_mode: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.13
  - NIST-800-171-3.13.10
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-2.2.4
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_sshd_pub_key
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set permissions for /etc/ssh/ file(s)
  file:
    path: '{{ item }}'
    mode: u-xs,g-xws,o-xwt
    state: file
  with_items:
  - '{{ files_found.stdout_lines }}'
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.1.13
  - NIST-800-171-3.13.10
  - NIST-800-53-AC-17(a)
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-2.2.4
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_sshd_pub_key
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```

## Warning{% #warning %}

Remediation is not possible at bootable container build time because SSH host keys are generated post-deployment.
