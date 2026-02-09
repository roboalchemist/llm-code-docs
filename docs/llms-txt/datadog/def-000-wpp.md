# Source: https://docs.datadoghq.com/security/default_rules/def-000-wpp.md

---
title: Disable Core Dumps for All Users
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Datadog Security > OOTB Rules > Disable Core Dumps for All Users
---

# Disable Core Dumps for All Users
 
## Description{% #description %}

To disable core dumps for all users, add the following line to `/etc/security/limits.conf`, or to a file within the `/etc/security/limits.d/` directory:

```
*     hard   core    0
```

## Rationale{% #rationale %}

A core dump includes a memory image taken at the time the operating system terminates an application. The memory image could contain sensitive data and is generally useful only for developers trying to debug problems.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpam-runtime' 2>/dev/null | grep -q '^installed$'; then

SECURITY_LIMITS_FILE="/etc/security/limits.conf"

if grep -qE '^\s*\*\s+hard\s+core' $SECURITY_LIMITS_FILE; then
        sed -ri 's/(hard\s+core\s+)[[:digit:]]+/\1 0/' $SECURITY_LIMITS_FILE
else
        echo "*     hard   core    0" >> $SECURITY_LIMITS_FILE
fi

if ls /etc/security/limits.d/*.conf > /dev/null; then
        sed -ri '/^\s*\*\s+hard\s+core/d' /etc/security/limits.d/*.conf
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
  - NIST-800-53-CM-6
  - NIST-800-53-SC-7(10)
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_users_coredumps
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Disable core dumps with limits
  lineinfile:
    dest: /etc/security/limits.conf
    regexp: ^[^#].*core
    line: '*        hard       core      0'
    create: true
  when: '"libpam-runtime" in ansible_facts.packages'
  tags:
  - NIST-800-53-CM-6
  - NIST-800-53-SC-7(10)
  - PCI-DSSv4-3.3
  - PCI-DSSv4-3.3.1
  - PCI-DSSv4-3.3.1.1
  - disable_users_coredumps
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
