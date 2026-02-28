# Source: https://docs.datadoghq.com/security/default_rules/def-000-gix.md

---
title: Verify /boot/grub2/user.cfg Permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify /boot/grub2/user.cfg Permissions
---

# Verify /boot/grub2/user.cfg Permissions

## Description{% #description %}

File permissions for `/boot/grub2/user.cfg` should be set to 600. To properly set the permissions of `/boot/grub2/user.cfg`, run the command:

```
$ sudo chmod 600 /boot/grub2/user.cfg
```

## Rationale{% #rationale %}

Proper permissions ensure that only the root user can read or modify important boot parameters.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if [ ! -d /sys/firmware/efi ] && rpm --quiet -q grub2-common && { [ ! -f /.dockerenv ] && [ ! -f /run/.containerenv ]; }; then

chmod u-xs,g-xwrs,o-xwrt /boot/grub2/user.cfg

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
  - CCE-86023-9
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_user_cfg
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
  - CCE-86023-9
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_user_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xwrs,o-xwrt on /boot/grub2/user.cfg
  file:
    path: /boot/grub2/user.cfg
    mode: u-xs,g-xwrs,o-xwrt
  when:
  - '"/boot/efi" not in ansible_mounts | map(attribute="mount") | list'
  - '"grub2-common" in ansible_facts.packages'
  - ansible_virtualization_type not in ["docker", "lxc", "openvz", "podman", "container"]
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - CCE-86023-9
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_user_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
