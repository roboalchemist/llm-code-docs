# Source: https://docs.datadoghq.com/security/default_rules/def-000-xgb.md

---
title: Verify /boot/grub2/user.cfg User Ownership
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify /boot/grub2/user.cfg User
  Ownership
---

# Verify /boot/grub2/user.cfg User Ownership
 
## Description{% #description %}

The file `/boot/grub2/user.cfg` should be owned by the `root` user to prevent reading or modification of the file. To properly set the owner of `/boot/grub2/user.cfg`, run the command:

```
$ sudo chown root /boot/grub2/user.cfg 
```

## Rationale{% #rationale %}

Only root should be able to modify important boot parameters. Also, non-root users who read the boot parameters may be able to identify weaknesses in security upon boot and be able to exploit them.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -d /sys/firmware/efi ] && rpm --quiet -q grub2-common && { [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; }; then

chown 0 /boot/grub2/user.cfg

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
  - CCE-86014-8
  - CJIS-5.5.2.2
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-7.1
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_user_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /boot/grub2/user.cfg
  stat:
    path: /boot/grub2/user.cfg
  register: file_exists
  when:
  - '"/boot/efi" not in ansible_mounts | map(attribute="mount") | list'
  - '"grub2-common" in ansible_facts.packages'
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  tags:
  - CCE-86014-8
  - CJIS-5.5.2.2
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-7.1
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_user_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner 0 on /boot/grub2/user.cfg
  file:
    path: /boot/grub2/user.cfg
    owner: '0'
  when:
  - '"/boot/efi" not in ansible_mounts | map(attribute="mount") | list'
  - '"grub2-common" in ansible_facts.packages'
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - CCE-86014-8
  - CJIS-5.5.2.2
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-7.1
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_user_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
