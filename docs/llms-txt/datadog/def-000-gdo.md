# Source: https://docs.datadoghq.com/security/default_rules/def-000-gdo.md

---
title: Disable Mounting of cramfs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Mounting of cramfs
---

# Disable Mounting of cramfs

## Description{% #description %}

To configure the system to prevent the `cramfs` kernel module from being loaded, add the following line to the file `/etc/modprobe.d/cramfs.conf`:

```
install cramfs /bin/false
```

This effectively prevents usage of this uncommon filesystem. The `cramfs` filesystem type is a compressed read-only Linux filesystem embedded in small footprint systems. A `cramfs` image can be used without having to first decompress the image.

## Rationale{% #rationale %}

Removing support for unneeded filesystem types reduces the local attack surface of the server.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if LC_ALL=C grep -q -m 1 "^install cramfs" /etc/modprobe.d/cramfs.conf ; then

    sed -i 's#^install cramfs.*#install cramfs /bin/false#g' /etc/modprobe.d/cramfs.conf
else
    echo -e "\n# Disable per security requirements" >> /etc/modprobe.d/cramfs.conf
    echo "install cramfs /bin/false" >> /etc/modprobe.d/cramfs.conf
fi

if ! LC_ALL=C grep -q -m 1 "^blacklist cramfs$" /etc/modprobe.d/cramfs.conf ; then
    echo "blacklist cramfs" >> /etc/modprobe.d/cramfs.conf
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
  - kernel_module_cramfs_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required

- name: Ensure kernel module 'cramfs' is disabled
  lineinfile:
    create: true
    dest: /etc/modprobe.d/cramfs.conf
    regexp: install\s+cramfs
    line: install cramfs /bin/false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_cramfs_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required

- name: Ensure kernel module 'cramfs' is blacklisted
  lineinfile:
    create: true
    dest: /etc/modprobe.d/cramfs.conf
    regexp: ^blacklist cramfs$
    line: blacklist cramfs
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_cramfs_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required
```
