# Source: https://docs.datadoghq.com/security/default_rules/def-000-fyy.md

---
title: Ensure There Are No Accounts With Blank or Null Passwords
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure There Are No Accounts With Blank
  or Null Passwords
---

# Ensure There Are No Accounts With Blank or Null Passwords
 
## Description{% #description %}

Check the "/etc/shadow" file for blank passwords with the following command:

```
$ sudo awk -F: '!$2 {print $1}' /etc/shadow
```

If the command returns any results, this is a finding. Configure all accounts on the system to have a password or lock the account with the following commands: Perform a password reset:

```
$ sudo passwd [username]
```

Lock an account:

```
$ sudo passwd -l [username]
```

## Rationale{% #rationale %}

If an account has an empty password, anyone could log in and run commands with the privileges of that account. Accounts with empty passwords should never be used in operational environments.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'linux-base' 2>/dev/null | grep -q '^installed$'; then

readarray -t users_with_empty_pass < <(sudo awk -F: '!$2 {print $1}' /etc/shadow)

for user_with_empty_pass in "${users_with_empty_pass[@]}"
do
    passwd -l $user_with_empty_pass
done

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
  - DISA-STIG-UBTU-20-010462
  - NIST-800-53-CM-6(b)
  - NIST-800-53-CM-6.1(iv)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.2
  - high_severity
  - low_complexity
  - low_disruption
  - no_empty_passwords_etc_shadow
  - no_reboot_needed
  - restrict_strategy

- name: Collect users with no password
  command: |
    awk -F: '!$2 {print $1}' /etc/shadow
  register: users_nopasswd
  changed_when: false
  when: '"linux-base" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010462
  - NIST-800-53-CM-6(b)
  - NIST-800-53-CM-6.1(iv)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.2
  - high_severity
  - low_complexity
  - low_disruption
  - no_empty_passwords_etc_shadow
  - no_reboot_needed
  - restrict_strategy

- name: Lock users with no password
  command: |
    passwd -l {{ item }}
  with_items: '{{ users_nopasswd.stdout_lines }}'
  when:
  - '"linux-base" in ansible_facts.packages'
  - users_nopasswd is not skipped and users_nopasswd.stdout_lines | length > 0
  tags:
  - DISA-STIG-UBTU-20-010462
  - NIST-800-53-CM-6(b)
  - NIST-800-53-CM-6.1(iv)
  - PCI-DSSv4-2.2
  - PCI-DSSv4-2.2.2
  - high_severity
  - low_complexity
  - low_disruption
  - no_empty_passwords_etc_shadow
  - no_reboot_needed
  - restrict_strategy
```

## Warning{% #warning %}

Note that this rule is not applicable for systems running within a container. Having user with empty password within a container is not considered a risk, because it should not be possible to directly login into a container anyway.
