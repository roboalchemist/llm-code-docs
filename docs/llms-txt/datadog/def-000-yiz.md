# Source: https://docs.datadoghq.com/security/default_rules/def-000-yiz.md

---
title: Disable Mounting of udf
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Mounting of udf
---

# Disable Mounting of udf
 
## Description{% #description %}

To configure the system to prevent the `udf` kernel module from being loaded, add the following line to the file `/etc/modprobe.d/udf.conf`:

```
install udf /bin/false
```

This effectively prevents usage of this uncommon filesystem. The `udf` filesystem type is the universal disk format used to implement the ISO/IEC 13346 and ECMA-167 specifications. This is an open vendor filesystem type for data storage on a broad range of media. This filesystem type is neccessary to support writing DVDs and newer optical disc formats.

## Rationale{% #rationale %}

Removing support for unneeded filesystem types reduces the local attack surface of the system.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

if LC_ALL=C grep -q -m 1 "^install udf" /etc/modprobe.d/udf.conf ; then
	
	sed -i 's#^install udf.*#install udf /bin/false#g' /etc/modprobe.d/udf.conf
else
	echo -e "\n# Disable per security requirements" >> /etc/modprobe.d/udf.conf
	echo "install udf /bin/false" >> /etc/modprobe.d/udf.conf
fi

if ! LC_ALL=C grep -q -m 1 "^blacklist udf$" /etc/modprobe.d/udf.conf ; then
	echo "blacklist udf" >> /etc/modprobe.d/udf.conf
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
  - kernel_module_udf_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required

- name: Ensure kernel module 'udf' is disabled
  lineinfile:
    create: true
    dest: /etc/modprobe.d/udf.conf
    regexp: install\s+udf
    line: install udf /bin/false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_udf_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required

- name: Ensure kernel module 'udf' is blacklisted
  lineinfile:
    create: true
    dest: /etc/modprobe.d/udf.conf
    regexp: ^blacklist udf$
    line: blacklist udf
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - NIST-800-171-3.4.6
  - NIST-800-53-CM-6(a)
  - NIST-800-53-CM-7(a)
  - NIST-800-53-CM-7(b)
  - disable_strategy
  - kernel_module_udf_disabled
  - low_complexity
  - low_severity
  - medium_disruption
  - reboot_required
```
