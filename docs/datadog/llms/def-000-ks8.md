# Source: https://docs.datadoghq.com/security/default_rules/def-000-ks8.md

---
title: Ensure PAM Enforces Password Requirements - Enforcing
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure PAM Enforces Password
  Requirements - Enforcing
---

# Ensure PAM Enforces Password Requirements - Enforcing

## Description{% #description %}

Verify that the operating system uses "pwquality" to enforce the password complexity rules. Verify the pwquality module is being enforced by operating system by running the following command:

```

$ grep -i enforcing /etc/security/pwquality.conf
enforcing = 1
```

If the value of "enforcing" is not "1" or the line is commented out, this is a finding.

## Rationale{% #rationale %}

Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks. Using enforcing=1 ensures "pwquality" enforces complex password construction configuration and has the ability to limit brute-force attacks on the system.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpwquality1' 2>/dev/null | grep -q '^installed$'; then

if [ -e "/etc/security/pwquality.conf" ] ; then

    LC_ALL=C sed -i "/^\s*enforcing = 1/Id" "/etc/security/pwquality.conf"
else
    touch "/etc/security/pwquality.conf"
fi
# make sure file has newline at the end
sed -i -e '$a\' "/etc/security/pwquality.conf"

cp "/etc/security/pwquality.conf" "/etc/security/pwquality.conf.bak"
# Insert at the end of the file
printf '%s\n' "enforcing = 1" >> "/etc/security/pwquality.conf"
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
  - DISA-STIG-UBTU-20-010057
  - accounts_password_pam_enforcing
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure PAM Enforces Password Requirements - Enforcing
  lineinfile:
    path: /etc/security/pwquality.conf
    create: true
    regexp: ''
    line: enforcing = 1
    state: present
  when: '"libpwquality1" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010057
  - accounts_password_pam_enforcing
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
