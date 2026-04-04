# Source: https://docs.datadoghq.com/security/default_rules/def-000-5jf.md

---
title: Disable Mounting of hfsplus
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Mounting of hfsplus
---

# Disable Mounting of hfsplus

## Description{% #description %}

To configure the system to prevent the `hfsplus` kernel module from being loaded, add the following line to the file `/etc/modprobe.d/hfsplus.conf`:

```
install hfsplus /bin/false
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

if LC_ALL=C grep -q -m 1 "^install hfsplus" /etc/modprobe.d/hfsplus.conf ; then

    sed -i 's#^install hfsplus.*#install hfsplus /bin/false#g' /etc/modprobe.d/hfsplus.conf
else
    echo -e "\n# Disable per security requirements" >> /etc/modprobe.d/hfsplus.conf
    echo "install hfsplus /bin/false" >> /etc/modprobe.d/hfsplus.conf
fi

if ! LC_ALL=C grep -q -m 1 "^blacklist hfsplus$" /etc/modprobe.d/hfsplus.conf ; then
    echo "blacklist hfsplus" >> /etc/modprobe.d/hfsplus.conf
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
  - kernel_module_hfsplus_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required

- name: Ensure kernel module 'hfsplus' is disabled
  lineinfile:
    create: true
    dest: /etc/modprobe.d/hfsplus.conf
    regexp: install\s+hfsplus
    line: install hfsplus /bin/false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_hfsplus_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required

- name: Ensure kernel module 'hfsplus' is blacklisted
  lineinfile:
    create: true
    dest: /etc/modprobe.d/hfsplus.conf
    regexp: ^blacklist hfsplus$
    line: blacklist hfsplus
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_hfsplus_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required
```
