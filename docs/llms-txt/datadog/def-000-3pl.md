# Source: https://docs.datadoghq.com/security/default_rules/def-000-3pl.md

---
title: Disable Mounting of freevxfs
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Mounting of freevxfs
---

# Disable Mounting of freevxfs
 
## Description{% #description %}

To configure the system to prevent the `freevxfs` kernel module from being loaded, add the following line to the file `/etc/modprobe.d/freevxfs.conf`:

```
install freevxfs /bin/false
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

if LC_ALL=C grep -q -m 1 "^install freevxfs" /etc/modprobe.d/freevxfs.conf ; then
	
	sed -i 's#^install freevxfs.*#install freevxfs /bin/false#g' /etc/modprobe.d/freevxfs.conf
else
	echo -e "\n# Disable per security requirements" >> /etc/modprobe.d/freevxfs.conf
	echo "install freevxfs /bin/false" >> /etc/modprobe.d/freevxfs.conf
fi

if ! LC_ALL=C grep -q -m 1 "^blacklist freevxfs$" /etc/modprobe.d/freevxfs.conf ; then
	echo "blacklist freevxfs" >> /etc/modprobe.d/freevxfs.conf
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
  - kernel_module_freevxfs_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required

- name: Ensure kernel module 'freevxfs' is disabled
  lineinfile:
    create: true
    dest: /etc/modprobe.d/freevxfs.conf
    regexp: install\s+freevxfs
    line: install freevxfs /bin/false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_freevxfs_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required

- name: Ensure kernel module 'freevxfs' is blacklisted
  lineinfile:
    create: true
    dest: /etc/modprobe.d/freevxfs.conf
    regexp: ^blacklist freevxfs$
    line: blacklist freevxfs
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_freevxfs_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required
```
