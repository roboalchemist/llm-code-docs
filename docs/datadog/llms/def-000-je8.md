# Source: https://docs.datadoghq.com/security/default_rules/def-000-je8.md

---
title: Verify /boot/grub/grub.cfg User Ownership
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Verify /boot/grub/grub.cfg User
  Ownership
---

# Verify /boot/grub/grub.cfg User Ownership

## Description{% #description %}

The file `/boot/grub/grub.cfg` should be owned by the `root` user to prevent destruction or modification of the file. To properly set the owner of `/boot/grub/grub.cfg`, run the command:

```
$ sudo chown root /boot/grub/grub.cfg
```

## Rationale{% #rationale %}

Only root should be able to modify important boot parameters.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if ( dpkg-query --show --showformat='${db:Status-Status}' 'grub2-common' 2>/dev/null | grep -q '^installed$' && dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$' ) && [ ! -d /sys/firmware/efi ] && { ! ( [ -f /.dockerenv ] || [ -f /run/.containerenv ] ); }; then

if id "0" >/dev/null 2>&1; then
  newown="0"
fi
if [[ -z ${newown} ]]; then
  echo "0 is not a defined user on the system"
  exit 1
fi
chown $newown /boot/grub/grub.cfg

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
  - CJIS-5.5.2.2
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-7.1
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_grub2_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Set the file_owner_grub2_cfg_newown variable if represented by uid
  set_fact:
    file_owner_grub2_cfg_newown: '0'
  when:
  - '"/boot/efi" not in ansible_mounts | map(attribute="mount") | list'
  - ( "grub2-common" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  tags:
  - CJIS-5.5.2.2
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-7.1
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_grub2_cfg
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
  - CJIS-5.5.2.2
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-7.1
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_grub2_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed

- name: Ensure owner on /boot/grub/grub.cfg
  file:
    path: /boot/grub/grub.cfg
    owner: '{{ file_owner_grub2_cfg_newown }}'
  when:
  - '"/boot/efi" not in ansible_mounts | map(attribute="mount") | list'
  - ( "grub2-common" in ansible_facts.packages and "linux-base" in ansible_facts.packages
    )
  - not ( ansible_virtualization_type in ["docker", "lxc", "openvz", "podman", "container"]
    )
  - file_exists.stat is defined and file_exists.stat.exists
  tags:
  - CJIS-5.5.2.2
  - NIST-800-171-3.4.5
  - NIST-800-53-AC-6(1)
  - NIST-800-53-CM-6(a)
  - PCI-DSS-Req-7.1
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.6
  - configure_strategy
  - file_owner_grub2_cfg
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
```
