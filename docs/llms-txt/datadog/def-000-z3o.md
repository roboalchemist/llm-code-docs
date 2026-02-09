# Source: https://docs.datadoghq.com/security/default_rules/def-000-z3o.md

---
title: Disable Modprobe Loading of USB Storage Driver
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Disable Modprobe Loading of USB Storage
  Driver
---

# Disable Modprobe Loading of USB Storage Driver
 
## Description{% #description %}

To prevent USB storage devices from being used, configure the kernel module loading system to prevent automatic loading of the USB storage driver. To configure the system to prevent the `usb-storage` kernel module from being loaded, add the following line to the file `/etc/modprobe.d/usb-storage.conf`:

```
install usb-storage /bin/false
```

This will prevent the `modprobe` program from loading the `usb-storage` module, but will not prevent an administrator (or another program) from using the `insmod` program to load the module manually.

## Rationale{% #rationale %}

USB storage devices such as thumb drives can be used to introduce malicious software.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if LC_ALL=C grep -q -m 1 "^install usb-storage" /etc/modprobe.d/usb-storage.conf ; then
	
	sed -i 's#^install usb-storage.*#install usb-storage /bin/false#g' /etc/modprobe.d/usb-storage.conf
else
	echo -e "\n# Disable per security requirements" >> /etc/modprobe.d/usb-storage.conf
	echo "install usb-storage /bin/false" >> /etc/modprobe.d/usb-storage.conf
fi

if ! LC_ALL=C grep -q -m 1 "^blacklist usb-storage$" /etc/modprobe.d/usb-storage.conf ; then
	echo "blacklist usb-storage" >> /etc/modprobe.d/usb-storage.conf
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
  - DISA-STIG-UBTU-20-010461
  - NIST-800-171-3.1.21
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - PCI-DSSv4-3.4
  - PCI-DSSv4-3.4.2
  - disable_strategy
  - kernel_module_usb-storage_disabled
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required

- name: Ensure kernel module 'usb-storage' is disabled
  lineinfile:
    create: true
    dest: /etc/modprobe.d/usb-storage.conf
    regexp: install\s+usb-storage
    line: install usb-storage /bin/false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010461
  - NIST-800-171-3.1.21
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - PCI-DSSv4-3.4
  - PCI-DSSv4-3.4.2
  - disable_strategy
  - kernel_module_usb-storage_disabled
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required

- name: Ensure kernel module 'usb-storage' is blacklisted
  lineinfile:
    create: true
    dest: /etc/modprobe.d/usb-storage.conf
    regexp: ^blacklist usb-storage$
    line: blacklist usb-storage
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010461
  - NIST-800-171-3.1.21
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - NIST-800-53-MP-7
  - PCI-DSSv4-3.4
  - PCI-DSSv4-3.4.2
  - disable_strategy
  - kernel_module_usb-storage_disabled
  - low_complexity
  - medium_disruption
  - medium_severity
  - reboot_required
```
