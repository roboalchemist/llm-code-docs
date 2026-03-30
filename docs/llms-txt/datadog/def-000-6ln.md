# Source: https://docs.datadoghq.com/security/default_rules/def-000-6ln.md

---
title: Verify /boot/grub2/grub.cfg Group Ownership
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify /boot/grub2/grub.cfg Group
  Ownership
---

# Verify /boot/grub2/grub.cfg Group Ownership

## Description{% #description %}

The file `/boot/grub2/grub.cfg` should be group-owned by the `root` group to prevent destruction or modification of the file. To properly set the group owner of `/boot/grub2/grub.cfg`, run the command:

```
$ sudo chgrp root /boot/grub2/grub.cfg
```

## Rationale{% #rationale %}

The `root` group is a highly-privileged group. Furthermore, the group-owner of this file should not have any access privileges anyway.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -d /sys/firmware/efi ] && rpm --quiet -q grub2-common && { [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; }; then

chgrp 0 /boot/grub2/grub.cfg

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
  - CCE-82023-3
  - CJIS-5.5.2.2
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-7.1
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_grub2_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /boot/grub2/grub.cfg
  stat:
    path: /boot/grub2/grub.cfg
  register: file_exists
  when:
  - '"/boot/efi" not in ansible_mounts | map(attribute="mount") | list'
  - '"grub2-common" in ansible_facts.packages'
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-82023-3
  - CJIS-5.5.2.2
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-7.1
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_grub2_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure group owner 0 on /boot/grub2/grub.cfg
  file:
    path: /boot/grub2/grub.cfg
    group: '0'
  when:
  - '"/boot/efi" not in ansible_mounts | map(attribute="mount") | list'
  - '"grub2-common" in ansible_facts.packages'
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - CCE-82023-3
  - CJIS-5.5.2.2
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-7.1
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_groupowner_grub2_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
