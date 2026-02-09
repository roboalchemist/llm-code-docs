# Source: https://docs.datadoghq.com/security/default_rules/def-000-hb8.md

---
title: Verify /boot/grub/grub.cfg Permissions
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Verify /boot/grub/grub.cfg Permissions
---

# Verify /boot/grub/grub.cfg Permissions
 
## Description{% #description %}

File permissions for `/boot/grub/grub.cfg` should be set to 600. To properly set the permissions of `/boot/grub/grub.cfg`, run the command:

```
$ sudo chmod 600 /boot/grub/grub.cfg
```

## Rationale{% #rationale %}

Proper permissions ensure that only the root user can modify important boot parameters.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( dpkg-query --show --showformat='${db:Status-Status}' 'grub2-common' 2>/dev/null | grep -q '^installed$' && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' ) && [ ! -d /sys/firmware/efi ] && { ! ( [ -f /.dockerenv ] || [ -f /run/.containerenv ] ); }; then

chmod u-xs,g-xwrs,o-xwrt /boot/grub/grub.cfg

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
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_grub2_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Test for existence /boot/grub/grub.cfg
  stat:
    path: /boot/grub/grub.cfg
  register: file_exists
  when:
  - '"/boot/efi" not in ansible_mounts | map(attribute="mount") | list'
  - ( "grub2-common" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  tags:
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_grub2_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure permission u-xs,g-xwrs,o-xwrt on /boot/grub/grub.cfg
  file:
    path: /boot/grub/grub.cfg
    mode: u-xs,g-xwrs,o-xwrt
  when:
  - '"/boot/efi" not in ansible_mounts | map(attribute="mount") | list'
  - ( "grub2-common" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_permissions_grub2_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
