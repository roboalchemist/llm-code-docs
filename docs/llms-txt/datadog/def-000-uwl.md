# Source: https://docs.datadoghq.com/security/default_rules/def-000-uwl.md

---
title: Ensure PAM Enforces Password Requirements - Minimum Special Characters
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > OOTB Rules > Ensure PAM Enforces Password
  Requirements - Minimum Special Characters
---

# Ensure PAM Enforces Password Requirements - Minimum Special Characters

## Description{% #description %}

The pam_pwquality module's `ocredit=` parameter controls requirements for usage of special (or "other") characters in a password. When set to a negative number, any password will be required to contain that many special characters. When set to a positive number, pam_pwquality will grant +1 additional length credit for each special character. Modify the `ocredit` setting in `/etc/security/pwquality.conf` to equal -1 to require use of a special character in passwords.

## Rationale{% #rationale %}

Use of a complex password helps to increase the time and resources required to compromise the password. Password complexity, or strength, is a measure of the effectiveness of a password in resisting attempts at guessing and brute-force attacks.

Password complexity is one factor of several that determines how long it takes to crack a password. The more complex the password, the greater the number of possible combinations that need to be tested before the password is compromised. Requiring a minimum number of special characters makes password guessing attacks more difficult by ensuring a larger search space.

## Remediation{% #remediation %}

### Shell script{% #shell-script %}

The following script can be run on the host to remediate the issue.

```bash
#!/bin/bash

# Remediation is applicable only in certain platforms
if dpkg-query --show --showformat='${db:Status-Status}' 'libpwquality1' 2>/dev/null | grep -q '^installed$'; then

var_password_pam_ocredit='-1'








# Strip any search characters in the key arg so that the key can be replaced without
# adding any search characters to the config file.
stripped_key=$(sed 's/[\^=\$,;+]*//g' <<< "^ocredit")

# shellcheck disable=SC2059
printf -v formatted_output "%s = %s" "$stripped_key" "$var_password_pam_ocredit"

# If the key exists, change it. Otherwise, add it to the config_file.
# We search for the key string followed by a word boundary (matched by \>),
# so if we search for 'setting', 'setting2' won't match.
if LC_ALL=C grep -q -m 1 -i -e "^ocredit\\>" "/etc/security/pwquality.conf"; then
    escaped_formatted_output=$(sed -e 's|/|\\/|g' <<< "$formatted_output")
    LC_ALL=C sed -i --follow-symlinks "s/^ocredit\\>.*/$escaped_formatted_output/gi" "/etc/security/pwquality.conf"
else
    if [[ -s "/etc/security/pwquality.conf" ]] && [[ -n "$(tail -c 1 -- "/etc/security/pwquality.conf" || true)" ]]; then
        LC_ALL=C sed -i --follow-symlinks '$a'\\ "/etc/security/pwquality.conf"
    fi
    printf '%s\n' "$formatted_output" >> "/etc/security/pwquality.conf"
fi

else
    >&2 echo 'Remediation is not applicable, nothing was done'
fi
```

### Ansible playbook{% #ansible-playbook %}

The following playbook can be run with Ansible to remediate the issue.

```gdscript3
- name: Gather the package facts
  package_facts:
    manager: auto
  tags:
  - DISA-STIG-UBTU-20-010055
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(a)
  - NIST-800-53-IA-5(4)
  - NIST-800-53-IA-5(c)
  - accounts_password_pam_ocredit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
- name: XCCDF Value var_password_pam_ocredit # promote to variable
  set_fact:
    var_password_pam_ocredit: !!str -1
  tags:
    - always

- name: Ensure PAM Enforces Password Requirements - Minimum Special Characters - Check
    if system relies on pam-auth-update tool
  ansible.builtin.stat:
    path: /usr/sbin/pam-auth-update
  register: result_pam_auth_update_present
  when: '"libpwquality1" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010055
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(a)
  - NIST-800-53-IA-5(4)
  - NIST-800-53-IA-5(c)
  - accounts_password_pam_ocredit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure PAM Enforces Password Requirements - Minimum Special Characters - Remediation
    where pam-auth-update tool is present
  block:

  - name: Check if /usr/share/pam-configs/cac_pwquality exists
    stat:
      path: /usr/share/pam-configs/cac_pwquality
    register: pwquality_file_stat

  - name: Put the content into /usr/share/pam-configs/cac_pwquality if it does not
      exist
    copy:
      dest: /usr/share/pam-configs/cac_pwquality
      content: |
        Name: Pwquality password strength checking
        Default: yes
        Priority: 1024
        Conflicts: cracklib
        Password-Type: Primary
        Password:
          requisite           pam_pwquality.so retry=3
      force: true
    when: not pwquality_file_stat.stat.exists

  - name: Ensure PAM Enforces Password Requirements - Minimum Special Characters -
      Ensure pam-auth-update profile changes are applied
    ansible.builtin.command:
      cmd: pam-auth-update --enable cac_pwquality
  when:
  - '"libpwquality1" in ansible_facts.packages'
  - result_pam_auth_update_present.stat.exists
  tags:
  - DISA-STIG-UBTU-20-010055
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(a)
  - NIST-800-53-IA-5(4)
  - NIST-800-53-IA-5(c)
  - accounts_password_pam_ocredit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy

- name: Ensure PAM Enforces Password Requirements - Minimum Special Characters - Ensure
    PAM variable ocredit is set accordingly
  ansible.builtin.lineinfile:
    create: true
    dest: /etc/security/pwquality.conf
    regexp: ^#?\s*ocredit
    line: ocredit = {{ var_password_pam_ocredit }}
  when: '"libpwquality1" in ansible_facts.packages'
  tags:
  - DISA-STIG-UBTU-20-010055
  - NIST-800-53-CM-6(a)
  - NIST-800-53-IA-5(1)(a)
  - NIST-800-53-IA-5(4)
  - NIST-800-53-IA-5(c)
  - accounts_password_pam_ocredit
  - low_complexity
  - low_disruption
  - medium_severity
  - no_reboot_needed
  - restrict_strategy
```
