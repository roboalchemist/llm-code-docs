# Source: https://docs.datadoghq.com/security/default_rules/def-000-ev0.md

---
title: Ensure PAM Enforces Password Requirements - Enforce for root User
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure PAM Enforces Password
  Requirements - Enforce for root User
---

# Ensure PAM Enforces Password Requirements - Enforce for root User
 
## Description{% #description %}

The pam_pwquality module's `enforce_for_root` parameter controls requirements for enforcing password complexity for the root user. Enable the `enforce_for_root` setting in `/etc/security/pwquality.conf` to require the `root` user to use complex passwords.

## Rationale{% #rationale %}

Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpwquality1' 2>/dev/null | grep -q '^installed$'; then

if [ -e "/etc/security/pwquality.conf" ] ; then
    
    LC_ALL=C sed -i "/^\s*enforce_for_root/Id" "/etc/security/pwquality.conf"
else
    touch "/etc/security/pwquality.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/security/pwquality.conf"

cp "/etc/security/pwquality.conf" "/etc/security/pwquality.conf.bak"
# Insert at the end of the file
printf '%s\n' "enforce_for_root" >> "/etc/security/pwquality.conf"
# Clean up after ourselves.
rm "/etc/security/pwquality.conf.bak"

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
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(a)
  - NIST-800-53-IA-5(4)
  - NIST-800-53-IA-5(c)
  - accounts_password_pam_enforce_root
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure PAM Enforces Password Requirements - Enforce for root User
  lineinfile:
    path: /etc/security/pwquality.conf
    create: true
    regexp: ''
    line: enforce_for_root
    state: present
  when: '"libpwquality1" in ansible_facts.packages'
  tags:
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(a)
  - NIST-800-53-IA-5(4)
  - NIST-800-53-IA-5(c)
  - accounts_password_pam_enforce_root
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
