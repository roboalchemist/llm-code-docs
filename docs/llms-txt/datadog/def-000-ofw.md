# Source: https://docs.datadoghq.com/security/default_rules/def-000-ofw.md

---
title: Set Password Hashing Algorithm in /etc/libuser.conf
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Set Password Hashing Algorithm in
  /etc/libuser.conf
---

# Set Password Hashing Algorithm in /etc/libuser.conf
 
## Description{% #description %}

In `/etc/libuser.conf`, add or correct the following line in its `[defaults]` section to ensure the system will use the SHA-512 algorithm for password hashing:

```
crypt_style = sha512
```

## Rationale{% #rationale %}

Passwords need to be protected at all times, and encryption is the standard method for protecting passwords. If passwords are not encrypted, they can be plainly read (i.e., clear text) and easily compromised. Passwords that are encrypted with a weak algorithm are no more protected than if they are kepy in plain text.

This setting ensures user and group account administration utilities are configured to store only encrypted representations of passwords. Additionally, the `crypt_style` configuration option ensures the use of a strong hashing algorithm that makes password cracking attacks more difficult.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if rpm --quiet -q libuser; then

LIBUSER_CONF="/etc/libuser.conf"
CRYPT_STYLE_REGEX='[[:space:]]*\[defaults](.*(\n)+)+?[[:space:]]*crypt_style[[:space:]]*'

# Try find crypt_style in [defaults] section. If it is here, then change algorithm to sha512.
# If it isn't here, then add it to [defaults] section.
if grep -qzosP $CRYPT_STYLE_REGEX $LIBUSER_CONF ; then
        sed -i "s/\(crypt_style[[:space:]]*=[[:space:]]*\).*/\1sha512/g" $LIBUSER_CONF
elif grep -qs "\[defaults]" $LIBUSER_CONF ; then
        sed -i "/[[:space:]]*\[defaults]/a crypt_style = sha512" $LIBUSER_CONF
else
        echo -e "[defaults]\ncrypt_style = sha512" >> $LIBUSER_CONF
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
  - CCE-82038-1
  - CJIS-5.6.2.2
  - DISA-STIG-RHEL-07-010220
  - NIST-800-171-3.13.11
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(c)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.1
  - PCI-DSSv4-8.3.2
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_password_hashing_algorithm_libuserconf

- name: Set Password Hashing Algorithm in /etc/libuser.conf
  lineinfile:
    dest: /etc/libuser.conf
    insertafter: ^\s*\[defaults]
    regexp: ^#?crypt_style
    line: crypt_style = sha512
    state: present
    create: true
  when: '"libuser" in ansible_facts.packages'
  tags:
  - CCE-82038-1
  - CJIS-5.6.2.2
  - DISA-STIG-RHEL-07-010220
  - NIST-800-171-3.13.11
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(c)
  - NIST-800-53-IA-5(c)
  - PCI-DSS-Req-8.2.1
  - PCI-DSSv4-8.3.2
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
  - set_password_hashing_algorithm_libuserconf
```
