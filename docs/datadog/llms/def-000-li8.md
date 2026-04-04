# Source: https://docs.datadoghq.com/security/default_rules/def-000-li8.md

---
title: Disable Mounting of hfs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Mounting of hfs
---

# Disable Mounting of hfs

## Description{% #description %}

To configure the system to prevent the `hfs` kernel module from being loaded, add the following line to the file `/etc/modprobe.d/hfs.conf`:

```
install hfs /bin/false
```

This effectively prevents usage of this uncommon filesystem.

## Rationale{% #rationale %}

Linux kernel modules which implement filesystems that are not needed by the local system should be disabled.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if LC_ALL=C grep -q -m 1 "^install hfs" /etc/modprobe.d/hfs.conf ; then

    sed -i 's#^install hfs.*#install hfs /bin/false#g' /etc/modprobe.d/hfs.conf
else
    echo -e "\n# Disable per security requirements" >> /etc/modprobe.d/hfs.conf
    echo "install hfs /bin/false" >> /etc/modprobe.d/hfs.conf
fi

if ! LC_ALL=C grep -q -m 1 "^blacklist hfs$" /etc/modprobe.d/hfs.conf ; then
    echo "blacklist hfs" >> /etc/modprobe.d/hfs.conf
fi

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
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_hfs_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required

- name: Ensure kernel module 'hfs' is disabled
  lineinfile:
    create: true
    dest: /etc/modprobe.d/hfs.conf
    regexp: install\s+hfs
    line: install hfs /bin/false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_hfs_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required

- name: Ensure kernel module 'hfs' is blacklisted
  lineinfile:
    create: true
    dest: /etc/modprobe.d/hfs.conf
    regexp: ^blacklist hfs$
    line: blacklist hfs
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_hfs_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required
```
